#!/usr/bin/env python3
"""Change one native text object and one line style in a temporary copy.
Save it as ODG, reopen it as FODG, and verify both edits survive. No PDF is
created. The supplied finished figures are never modified.
"""

# Assertion-based verification must not run with its checks disabled.
if not __debug__:
    raise SystemExit("Run without Python optimisation (-O or -OO).")

import argparse,copy,json,subprocess,tempfile
from pathlib import Path
from lxml import etree as E
NS={'draw':'urn:oasis:names:tc:opendocument:xmlns:drawing:1.0','style':'urn:oasis:names:tc:opendocument:xmlns:style:1.0','text':'urn:oasis:names:tc:opendocument:xmlns:text:1.0','svg':'urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0','office':'urn:oasis:names:tc:opendocument:xmlns:office:1.0'}
def q(x):a,b=x.split(':');return '{'+NS[a]+'}'+b
p=argparse.ArgumentParser(description=__doc__);p.add_argument('--kit-root',type=Path,default=Path(__file__).resolve().parents[1]);p.add_argument('--soffice',default='soffice');a=p.parse_args();root=a.kit_root.resolve()
results=[]
for figure in ['Fig1','Fig2','Fig3']:
 with tempfile.TemporaryDirectory(prefix='sicomp_odg_edit_probe_') as d:
  d=Path(d);src=d/'input';saved=d/'saved';reopened=d/'reopened'
  for x in [src,saved,reopened]:x.mkdir()
  r=E.parse(str(root/'fodg'/f'{figure}_Editable.fodg'));line=r.find('.//draw:line',NS);line_name=line.get(q('draw:name'))
  style_name=line.get(q('draw:style-name'));st=r.find('.//style:style[@style:name="'+style_name+'"]',NS);new=copy.deepcopy(st);new.set(q('style:name'),'EditProbeMagenta');new.find('style:graphic-properties',NS).set(q('svg:stroke-color'),'#ff00ff');st.getparent().append(new);line.set(q('draw:style-name'),'EditProbeMagenta')
  frame=next(x for x in r.findall('.//draw:frame',NS) if x.find('draw:text-box/text:p',NS) is not None)
  para=frame.find('draw:text-box/text:p',NS)
  for child in list(para):para.remove(child)
  para.text='EDIT_PROBE';frame_name=frame.get(q('draw:name'));r.write(str(src/'probe.fodg'),encoding='UTF-8',xml_declaration=True)
  for inputpath,out,fmt in [(src/'probe.fodg',saved,'odg'),(saved/'probe.odg',reopened,'fodg')]:
   subprocess.run([a.soffice,'-env:UserInstallation='+(d/'lo-profile').as_uri(),'--headless','--convert-to',fmt,'--outdir',str(out),str(inputpath)],check=True,capture_output=True,text=True)
  out=E.parse(str(reopened/'probe.fodg'));actual=out.find('.//draw:frame[@draw:name="'+frame_name+'"]',NS);assert actual is not None
  assert 'EDIT_PROBE' in ''.join(actual.itertext())
  ln=out.find('.//draw:line[@draw:name="'+line_name+'"]',NS);style_name=ln.get(q('draw:style-name'));st=out.find('.//style:style[@style:name="'+style_name+'"]',NS)
  assert st.find('style:graphic-properties',NS).get(q('svg:stroke-color'))=='#ff00ff'
  result={'figure':figure,'status':'PASS','native_text_edited_and_reopened':frame_name,'native_line_colour_edited_and_reopened':line_name,'method':'Temporary FODG edit -> LibreOffice ODG save -> LibreOffice FODG reopen; checked native object identity and changed values.','finished_figures_modified':False,'new_pdfs_created':0,'limit':'Programmatic native-object edit; desktop GUI interaction was not exercised.'}
  results.append(result)
result={'status':'PASS','revision':'P44','figures':results,'GUI_interaction_executed':False}
(root/'verification/Edit_Roundtrip_Probe.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
