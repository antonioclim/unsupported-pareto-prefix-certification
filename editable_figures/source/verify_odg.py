#!/usr/bin/env python3
"""Check native ODG objects, editable texts, rendered glyphs and page geometry.
The supplied PDF must have been exported by reopening the corresponding ODG.
This checks the artefacts; it is not a proof of the mathematical theorems.
"""

# Assertion-based verification must not run with its checks disabled.
if not __debug__:
    raise SystemExit("Run without Python optimisation (-O or -OO).")

import argparse, collections, hashlib, json, re, subprocess, sys
from datetime import datetime, timezone
from pathlib import Path
from zipfile import ZipFile
from lxml import etree as E
import fitz
from PIL import Image
D='urn:oasis:names:tc:opendocument:xmlns:drawing:1.0'
T='urn:oasis:names:tc:opendocument:xmlns:text:1.0'
S='urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0'

def decode(n):
 result=n.text or ''
 for c in n:
  tag=E.QName(c).localname
  result+=(' '*int(c.get('{'+T+'}c','1')) if tag=='s' else '\t' if tag=='tab' else '\n' if tag=='line-break' else decode(c))+(c.tail or '')
 return result

def numcm(v):
 assert v.endswith('cm'),v
 return float(v[:-2])*72/2.54

def main():
 p=argparse.ArgumentParser(description=__doc__);p.add_argument('--kit-root',type=Path,default=Path(__file__).resolve().parents[1]);p.add_argument('--render-previews',action='store_true');a=p.parse_args();root=a.kit_root.resolve()
 inventory=json.loads((root/'verification/Object_Inventory.json').read_text());report=[]
 for fig in ['Fig1','Fig2','Fig3']:
  with ZipFile(root/'odg'/f'{fig}_Editable.odg') as z:
   r=E.fromstring(z.read('content.xml'));sxml=E.fromstring(z.read('styles.xml'));names=z.namelist()
  counts=collections.Counter(E.QName(n).localname for n in r.iter())
  assert all(counts[k]==0 for k in ['image','object','object-ole','binary-data'])
  assert not [x for x in names if x.startswith('Pictures/')]
  nodes={n.get('{'+D+'}name'):n for n in r.iter() if n.get('{'+D+'}name')}
  generated=next(x for x in inventory if x['figure']==fig)
  frames=[x for x in generated['objects'] if x['kind']=='text']
  for item in frames:
   actual=nodes[item['name']];assert E.QName(actual).localname=='frame'
   text=''.join(decode(x) for x in actual.findall('.//{'+T+'}p'))
   assert text==item['text'],(item['name'],repr(text),repr(item['text']))
  assert len(frames)==counts['text-box']
  fodg=E.parse(str(root/'fodg'/f'{fig}_Editable.fodg'))
  geom=[]
  for n in fodg.iter():
   if E.QName(n).localname not in ['line','path']:continue
   actual=nodes[n.get('{'+D+'}name')]
   for key in ['x','y','width','height','x1','x2','y1','y2']:
    kval='{'+S+'}'+key
    if n.get(kval) and actual.get(kval):geom.append(abs(numcm(n.get(kval))-numcm(actual.get(kval))))
  assert max(geom)<.04,(fig,max(geom))
  doc=fitz.open(root/'native_exports'/f'{fig}_Editable.pdf');assert len(doc)==1;p0=doc[0]
  assert tuple(p0.rect)==(0.,0.,360.,432.) and not p0.get_images()
  svg=E.parse(str(root/'reference_exports'/f'{fig}.svg'))
  expected=''.join(''.join(x.itertext()) for x in svg.findall('.//{http://www.w3.org/2000/svg}text'))
  norm=lambda s:collections.Counter(c for c in s if not c.isspace())
  assert norm(expected)==norm(p0.get_text())
  stroked=[d for d in p0.get_drawings() if d['type'] in ('s','fs')]
  minimum_stroke=min(d['width'] for d in stroked)
  assert minimum_stroke>=1.0,(fig,minimum_stroke)
  spans=[s for b in p0.get_text('dict')['blocks'] if 'lines' in b for l in b['lines'] for s in l['spans']]
  assert min(s['size'] for s in spans)>=8.49
  outside=[s['text'] for s in spans if s['bbox'][0]<-.1 or s['bbox'][1]<-.1 or s['bbox'][2]>360.1 or s['bbox'][3]>432.1]
  assert not outside,outside
  if fig=='Fig3':
   headings=['A  Fixed alphabet and two hard worlds','B  Asymptotic bounds on acquisition ratios']
   for heading in headings:assert any(s['text']==heading for s in spans),heading+' wrapped or changed'
   # Both legend line samples are 18 pt long and must end before label x=243.576.
   for sid in ['line2d_10','line2d_11']:
    lines=[n for name,n in nodes.items() if sid+'_line' in name and E.QName(n).localname=='line']
    assert len(lines)==1
    end=numcm(lines[0].get('{'+S+'}x2'));assert abs(end-236.376)<.04
  if a.render_previews:p0.get_pixmap(matrix=fitz.Matrix(5,5)).save(root/'native_exports'/f'{fig}_Editable.png')
  report.append({'figure':fig,'status':'PASS','canvas_inches':[5,6],'native_text_boxes':counts['text-box'],'native_vector_shapes':sum(counts[k] for k in ['path','polygon','polyline','line']),'native_vector_counts':{k:counts[k] for k in ['line','path','polygon','polyline']},'named_groups':counts['g'],'images_objects_ole_binary_data':0,'pictures_assets':0,'thumbnail_note':'An application preview thumbnail may exist; no image is placed on the drawing page.','exact_editable_text_runs_preserved':len(frames),'nonwhitespace_rendered_glyphs_preserved':sum(norm(expected).values()),'maximum_roundtrip_geometry_coordinate_error_pt':max(geom),'minimum_exported_stroke_pt':minimum_stroke,'minimum_exported_font_pt':min(s['size'] for s in spans),'text_spans_outside_page':len(outside),'pdf_images':0,'odg_sha256':hashlib.sha256((root/'odg'/f'{fig}_Editable.odg').read_bytes()).hexdigest(),'pdf_sha256':hashlib.sha256((root/'native_exports'/f'{fig}_Editable.pdf').read_bytes()).hexdigest()})
 result={'schema':'sicomp-native-odg-verification-p44-v1','revision':'P44','finished_at_utc':datetime.now(timezone.utc).isoformat(),'status':'PASS','figures':report,'scope':['Native XML structure and original editable text run equality after LibreOffice ODG roundtrip.','No images, OLE or embedded graphic objects on the page.','One 5×6 in PDF page per figure, exported by reopening the ODG.','All stroked native PDF paths meet the 1 pt minimum at the final 5 inch width.','Rendered non-whitespace glyph inventory equals the input SVG; PDF text lies inside the page.','All native path/line bounding coordinates retained within 0.04 pt after office unit quantisation.','Fig3 headings remain single-line; both legend sample lines end at the intended point.'],'limits':['No claim of pixel-identical rendering across LibreOffice versions or platforms.','The original SVG and PDF differ slightly in multiline text metrics; ODG follows SVG positions.','Glyph inventory and bounds do not alone prove absence of every possible visual overlap: all three final figures were also visually inspected.','Desktop mouse/keyboard editing was not exercised; editability is established by native objects, editable text and the separate edit-and-reopen probe.','These checks validate figure representation and arithmetic inputs, not the manuscript theorems.']}
 (root/'verification/Native_ODG_Verification.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n');print(json.dumps(result,ensure_ascii=False,indent=2))
if __name__=='__main__':main()
