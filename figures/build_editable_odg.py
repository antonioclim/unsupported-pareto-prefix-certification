#!/usr/bin/env python3
"""Convert the supplied analytic SVGs to individual native OpenDocument shapes.

No SVG/image object is embedded. Text runs stay editable; paths, markers,
axes and bands are separate native shapes. Uses Python stdlib, lxml, Pillow
and the local DejaVu Sans fonts; LibreOffice performs the FODG-to-ODG save.
The reference SVGs and exact scientific values are inputs, never modified.
"""
from __future__ import annotations
import argparse, collections, hashlib, json, math, re, shutil, subprocess, tempfile
from pathlib import Path
from lxml import etree as E
from PIL import ImageFont

NS = {
 'office':'urn:oasis:names:tc:opendocument:xmlns:office:1.0',
 'style':'urn:oasis:names:tc:opendocument:xmlns:style:1.0',
 'text':'urn:oasis:names:tc:opendocument:xmlns:text:1.0',
 'draw':'urn:oasis:names:tc:opendocument:xmlns:drawing:1.0',
 'fo':'urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0',
 'svg':'urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0',
 'dc':'http://purl.org/dc/elements/1.1/',
 'meta':'urn:oasis:names:tc:opendocument:xmlns:meta:1.0',
 'xlink':'http://www.w3.org/1999/xlink',
 'xml':'http://www.w3.org/XML/1998/namespace'}
SVG='http://www.w3.org/2000/svg'
I=(1.,0.,0.,1.,0.,0.)
NUM=r'[-+]?(?:\d*\.\d+|\d+\.?\d*)(?:[eE][-+]?\d+)?'

def q(tag):
 a,b=tag.split(':');return '{'+NS[a]+'}'+b

def el(parent,tag,attrs=None,text=None):
 n=E.SubElement(parent,q(tag),{q(k):str(v) for k,v in (attrs or {}).items()})
 if text is not None:n.text=text
 return n

def cm(pt):return f'{float(pt)*2.54/72:.8f}cm'
def stroke_cm(pt):
 # LibreOffice stores stroke widths in 0.01 mm increments. Round upward so
 # a nominal 1 pt stroke cannot become 0.99211 pt in the native PDF export.
 return f'{math.ceil(float(pt)*2.54/72*1000-1e-9)/1000:.3f}cm'
def num(v):return f'{v:.7f}'.rstrip('0').rstrip('.') or '0'
def multiply(a,b):
 A,B,C,D,Ee,F=a;g,h,i,j,k,l=b
 return (A*g+C*h,B*g+D*h,A*i+C*j,B*i+D*j,A*k+C*l+Ee,B*k+D*l+F)
def point(m,x,y):return(m[0]*x+m[2]*y+m[4],m[1]*x+m[3]*y+m[5])
def matrix(s):
 m=I
 for typ,vals in re.findall(r'(\w+)\(([^)]*)\)',s or ''):
  z=list(map(float,re.findall(NUM,vals)))
  if typ=='translate':t=(1,0,0,1,z[0],z[1] if len(z)>1 else 0)
  elif typ=='scale':t=(z[0],0,0,z[-1],0,0)
  elif typ=='matrix':t=tuple(z)
  elif typ=='rotate':
   a=math.radians(z[0]);t=(math.cos(a),math.sin(a),-math.sin(a),math.cos(a),0,0)
   if len(z)==3:t=multiply(multiply((1,0,0,1,z[1],z[2]),t),(1,0,0,1,-z[1],-z[2]))
  else:raise ValueError('Unhandled transform '+typ)
  m=multiply(m,t)
 return m

def style(node,parent=None):
 d=dict(parent or {})
 for k in ['fill','stroke','stroke-width','stroke-opacity','opacity','font-size','font-weight','font-style','font-family','text-anchor']:
  if node.get(k) is not None:d[k]=node.get(k)
 for part in node.get('style','').split(';'):
  if ':' in part:
   k,v=part.split(':',1);d[k.strip()]=v.strip()
 return d

class Converter:
 def __init__(self,svgfile):
  self.input=svgfile;self.fig=svgfile.stem;self.source=E.parse(str(svgfile));self.ids={n.get('id'):n for n in self.source.iter() if n.get('id')}
  self.doc=E.Element(q('office:document'),nsmap={k:v for k,v in NS.items() if k!='xml'},attrib={q('office:version'):'1.3',q('office:mimetype'):'application/vnd.oasis.opendocument.graphics'})
  meta=el(self.doc,'office:meta');el(meta,'dc:title',text=self.fig+' — native editable analytic figure');el(meta,'dc:creator',text='Antonio Clim');el(meta,'dc:description',text=('Exact prefix-acquisition illustration from Supplement S1.6; no empirical data.' if self.fig=='Fig1' else 'Analytic theorem illustration; individual native editable text and vector shapes. '+('P44 sharp candidate-census limit 12/11 and unrestricted randomised bounds 23/22 to 12/11.' if self.fig=='Fig3' else 'Scientific values unchanged from the P37 baseline; renumbered in P41.')));el(meta,'meta:generator',text='build_editable_odg.py (native OpenDocument conversion)')
  self.styles=el(self.doc,'office:styles');self.auto=el(self.doc,'office:automatic-styles')
  lp=el(self.auto,'style:page-layout',{'style:name':'PageLayout'})
  el(lp,'style:page-layout-properties',{'fo:page-width':cm(360),'fo:page-height':cm(432),'fo:margin-top':'0cm','fo:margin-bottom':'0cm','fo:margin-left':'0cm','fo:margin-right':'0cm','style:print-orientation':'portrait'})
  dp=el(self.auto,'style:style',{'style:name':'PageStyle','style:family':'drawing-page'});el(dp,'style:drawing-page-properties',{'draw:fill':'solid','draw:fill-color':'#ffffff','draw:background-size':'full'})
  master=el(self.doc,'office:master-styles');el(master,'style:master-page',{'style:name':'Default','style:page-layout-name':'PageLayout','draw:style-name':'PageStyle'})
  body=el(self.doc,'office:body');drawing=el(body,'office:drawing')
  layers=el(master,'draw:layer-set')
  for name in ['Figure content','Editable labels','Analytic marks']:
   el(layers,'draw:layer',{'draw:name':name})
  self.page=el(drawing,'draw:page',{'draw:name':self.fig,'draw:master-page-name':'Default','draw:style-name':'PageStyle'})
  self.cache={};self.dashes={};self.count=collections.Counter();self.objects=[];self.counter=0;self.skipped=[]
  # A native adjustable diagonal hatch. Parallel lines are 8/sqrt(2) pt apart.
  el(self.styles,'draw:hatch',{'draw:name':'Exact_regime_hatch','draw:display-name':'Exact regime diagonal hatch','draw:style':'single','draw:color':'#8b9aaa','draw:distance':cm(8/math.sqrt(2)),'draw:rotation':'450'})

 def graphic_style(self,s,text=False):
  props={}
  if text:
   props={'draw:fill':'none','draw:stroke':'none','draw:auto-grow-height':'false','draw:auto-grow-width':'false','draw:textarea-vertical-align':'top','fo:wrap-option':'no-wrap'}
   for a in ['left','right','top','bottom']:props['fo:padding-'+a]='0cm'
  else:
   fill=s.get('fill','#000000');stroke=s.get('stroke','none')
   props['draw:fill']='none' if fill=='none' else ('hatch' if fill.startswith('url') else 'solid')
   if fill.startswith('url'):props.update({'draw:fill-hatch-name':'Exact_regime_hatch','draw:fill-hatch-solid':'true','draw:fill-color':'#d9e5f2'})
   elif fill!='none':props['draw:fill-color']=fill
   props['draw:stroke']='none' if stroke=='none' else 'solid'
   if stroke!='none':props.update({'svg:stroke-color':stroke,'svg:stroke-width':stroke_cm(float(s.get('stroke-width','1'))),'draw:stroke-linejoin':s.get('stroke-linejoin','round'),'svg:stroke-linecap':{'square':'square','round':'round','butt':'butt'}.get(s.get('stroke-linecap','butt'),'butt')})
   # LibreOffice respects these standard OpenDocument opacity properties.
   if s.get('opacity'):props['draw:opacity']=num(float(s['opacity'])*100)+'%'
   if s.get('stroke-opacity'):props['svg:stroke-opacity']=num(float(s['stroke-opacity'])*100)+'%'
   if s.get('stroke-dasharray') and stroke!='none':
    dash=tuple(map(float,s['stroke-dasharray'].split(',')))
    if dash not in self.dashes:
     name='Dash'+str(len(self.dashes)+1);self.dashes[dash]=name
     el(self.styles,'draw:stroke-dash',{'draw:name':name,'draw:style':'rect','draw:dots1':'1','draw:dots1-length':cm(dash[0]),'draw:distance':cm(dash[1])})
    props['draw:stroke']='dash';props['draw:stroke-dash']=self.dashes[dash]
  key=json.dumps(props,sort_keys=True)
  if key not in self.cache:
   name='gr'+str(len(self.cache)+1);self.cache[key]=name
   st=el(self.auto,'style:style',{'style:name':name,'style:family':'graphic'});el(st,'style:graphic-properties',props)
  return self.cache[key]

 def paragraph_style(self,s):
  fs=float(s.get('font-size','9px').replace('px','').replace('pt',''))
  props={'fo:font-family':'DejaVu Sans','fo:font-size':num(fs)+'pt','fo:color':s.get('fill','#000000'),'fo:font-weight':s.get('font-weight','normal'),'fo:font-style':'italic' if s.get('font-style') in ('italic','oblique') else 'normal','style:font-size-asian':num(fs)+'pt','style:font-size-complex':num(fs)+'pt'}
  key='p'+json.dumps(props,sort_keys=True)
  if key not in self.cache:
   name='p'+str(len(self.cache)+1);self.cache[key]=name
   st=el(self.auto,'style:style',{'style:name':name,'style:family':'paragraph'})
   el(st,'style:paragraph-properties',{'fo:margin-left':'0cm','fo:margin-right':'0cm','fo:margin-top':'0cm','fo:margin-bottom':'0cm','fo:text-indent':'0cm','fo:text-align':'start','fo:line-height':'100%','fo:keep-together':'always'})
   el(st,'style:text-properties',props)
  return self.cache[key],fs

 def named(self,kind,source_id,**extra):
  self.counter+=1;name=f'{self.fig}_{self.counter:04d}_{source_id}_{kind}'
  self.count[kind]+=1;self.objects.append({'name':name,'kind':kind,'source_id':source_id,**extra})
  return name

 def path(self,node,parent,m,s,sid):
  tokens=re.findall(r'[A-Za-z]|'+NUM,node.get('d',''));cmds=[];points=[];i=0
  while i<len(tokens):
   cmd=tokens[i];i+=1
   if cmd in ['z','Z']:cmds.append(('Z',[]));continue
   if cmd not in ['M','L','C','Q']:raise ValueError('Unsupported path command '+cmd)
   n={'M':2,'L':2,'C':6,'Q':4}[cmd];coords=[]
   for j in range(0,n,2):
    p=point(m,float(tokens[i+j]),float(tokens[i+j+1]));coords.extend(p);points.append(p)
   i+=n;cmds.append((cmd,coords))
  if not points:return
  xmin=min(p[0] for p in points);xmax=max(p[0] for p in points);ymin=min(p[1] for p in points);ymax=max(p[1] for p in points)
  # Empty rectangles in the original plot have no area and no stroke.
  if (xmax-xmin<1e-9 or ymax-ymin<1e-9) and s.get('stroke','none')=='none':
   self.skipped.append({'source_id':sid,'reason':'zero-area, no-stroke original path'});return
  # Expand hatch into separate editable lines, matching the source's 1 pt
  # stroke. ODF's built-in hatch has no controllable line-width property.
  if s.get('fill','').startswith('url'):
   if any(c not in ('M','L','Z') for c,_ in cmds):raise ValueError('Hatched path is not a polygon')
   group=el(parent,'draw:g',{'draw:name':sid+'_editable_hatched_band'});self.count['group']+=1
   base=dict(s);base['fill']='#d9e5f2';base['stroke']='none'
   self.path(node,group,m,base,sid+'_fill')
   # Global SVG hatch lines have x+y = 8*k (pt). A half-point inset
   # keeps 1 pt diagonal strokes inside the filled rectangle boundary.
   inset=.5/math.sqrt(2);xl,xr=xmin+inset,xmax-inset;yt,yb=ymin+inset,ymax-inset
   hs=self.graphic_style({'fill':'none','stroke':'#8b9aaa','stroke-width':'1','stroke-linecap':'butt'})
   for k in range(math.ceil((xl+yt)/8),math.floor((xr+yb)/8)+1):
    c=8*k;pts=[]
    for xx,yy in [(xl,c-xl),(xr,c-xr),(c-yt,yt),(c-yb,yb)]:
     if xl-1e-7<=xx<=xr+1e-7 and yt-1e-7<=yy<=yb+1e-7 and not any(abs(xx-a)+abs(yy-b)<1e-7 for a,b in pts):pts.append((xx,yy))
    if len(pts)==2:
     el(group,'draw:line',{'draw:name':self.named('hatch_line',sid),'draw:style-name':hs,'draw:layer':'Analytic marks','svg:x1':cm(pts[0][0]),'svg:y1':cm(pts[0][1]),'svg:x2':cm(pts[1][0]),'svg:y2':cm(pts[1][1])})
   border=dict(s);border['fill']='none'
   self.path(node,group,m,border,sid+'_border')
   return
  sty=self.graphic_style(s)
  if len(cmds)>=2 and cmds[0][0]=='M' and all(c=='L' for c,_ in cmds[1:]) and (len(cmds)==2 or xmax-xmin<1e-9 or ymax-ymin<1e-9):
   attrs={'draw:name':self.named('line',sid),'draw:style-name':sty,'draw:layer':'Analytic marks','svg:x1':cm(cmds[0][1][0]),'svg:y1':cm(cmds[0][1][1]),'svg:x2':cm(cmds[-1][1][0]),'svg:y2':cm(cmds[-1][1][1])};el(parent,'draw:line',attrs);return
  # Native paths use a local bounding box, so one marker can be moved/resized.
  w=max(xmax-xmin,.01);h=max(ymax-ymin,.01)
  path=[]
  for cmd,coords in cmds:
   local=[(v-(xmin if j%2==0 else ymin))*100 for j,v in enumerate(coords)]
   path.append(cmd+(' '+' '.join(num(v) for v in local) if local else ''))
  el(parent,'draw:path',{'draw:name':self.named('path',sid),'draw:style-name':sty,'draw:layer':'Analytic marks','svg:x':cm(xmin),'svg:y':cm(ymin),'svg:width':cm(w),'svg:height':cm(h),'svg:viewBox':'0 0 '+num(w*100)+' '+num(h*100),'svg:d':' '.join(path)})

 def text_run(self,parent,content,x,y,m,s,sid):
  if not content:return
  ps,fs=self.paragraph_style(s)
  fontfile='DejaVuSans'+('-BoldOblique' if s.get('font-weight') in ('bold','700','800','900') and s.get('font-style') in ('oblique','italic') else '-Bold' if s.get('font-weight') in ('bold','700','800','900') else '-Oblique' if s.get('font-style') in ('oblique','italic') else '')+'.ttf'
  candidates=[Path(__file__).resolve().parent/'fonts'/fontfile, Path('/usr/share/fonts/truetype/dejavu')/fontfile,Path('/usr/local/share/fonts')/fontfile]
  fp=next((p for p in candidates if p.exists()),None)
  if fp is None:raise FileNotFoundError(fontfile+' is required for stable text placement')
  font=ImageFont.truetype(str(fp),round(fs*100))
  width=font.getlength(content)/100
  anchor=s.get('text-anchor','start');shift={'start':0,'middle':width/2,'end':width}.get(anchor,0)
  # LO 26.8 calibration: baseline is approximately 0.932 * font size below
  # a zero-padding frame. Native editable text is intentionally not outlined.
  localx=x-shift;localy=y-.932*fs
  tx,ty=point(m,localx,localy);angle=math.atan2(m[1],m[0])
  attrs={'draw:name':self.named('text',sid,text=content,font_pt=fs),'draw:style-name':self.graphic_style({},text=True),'draw:layer':'Editable labels','svg:width':cm(width+1.0),'svg:height':cm(fs*1.35)}
  if abs(angle)<1e-9:attrs.update({'svg:x':cm(tx),'svg:y':cm(ty)})
  else:
   # ODF angles are anticlockwise; SVG's y-down coordinates are clockwise.
   attrs['draw:transform']='rotate('+num(-angle)+') translate('+cm(tx)+' '+cm(ty)+')'
  frame=el(parent,'draw:frame',attrs);box=el(frame,'draw:text-box');p=el(box,'text:p',{'text:style-name':ps})
  # Explicit text:s elements preserve repeated/leading spaces in mathtext runs.
  chunks=re.split('( +)',content);last=None
  for chunk in chunks:
   if not chunk:continue
   if chunk.startswith(' '):last=el(p,'text:s',{'text:c':str(len(chunk))})
   elif last is None:p.text=(p.text or '')+chunk
   else:last.tail=(last.tail or '')+chunk

 def visit(self,node,parent,m=I,inherited=None,sid='figure'):
  tag=E.QName(node).localname
  if tag in ['defs','metadata','style','clipPath','pattern','title','desc']:return
  s=style(node,inherited);m=multiply(m,matrix(node.get('transform')));sid=node.get('id',sid)
  if tag in ['svg','g']:
   dest=parent
   if tag=='g':
    dest=el(parent,'draw:g',{'draw:name':sid});self.count['group']+=1
   for child in node:
    if isinstance(child.tag,str):self.visit(child,dest,m,s,sid)
   if dest is not parent and len(dest)==0:parent.remove(dest);self.count['group']-=1
  elif tag=='path':self.path(node,parent,m,s,sid)
  elif tag=='use':
   ref=node.get('{http://www.w3.org/1999/xlink}href') or node.get('href');target=self.ids[ref.lstrip('#')]
   um=multiply(m,(1,0,0,1,float(node.get('x','0')),float(node.get('y','0'))))
   # Referenced path presentation attributes provide defaults; use overrides them.
   ts=style(target);ts.update(s)
   self.path(target,parent,um,ts,sid)
  elif tag=='text':
   x=float(node.get('x','0'));y=float(node.get('y','0'))
   if len(node):
    group=el(parent,'draw:g',{'draw:name':sid+'_editable_math_runs'});self.count['group']+=1
    if node.text and node.text.strip():self.text_run(group,node.text,x,y,m,s,sid)
    for child in node:
     if E.QName(child).localname!='tspan':raise ValueError('Unhandled text child')
     text=''.join(child.itertext());ts=style(child,s)
     # Matplotlib sometimes gives each glyph a position in one tspan.
     xs=list(map(float,re.findall(NUM,child.get('x',str(x)))));ys=list(map(float,re.findall(NUM,child.get('y',str(y)))))
     if len(xs)==1:self.text_run(group,text,xs[0],ys[0],m,ts,sid)
     elif len(xs)==len(text):
      for j,c in enumerate(text):self.text_run(group,c,xs[j],ys[j] if len(ys)>1 else ys[0],m,ts,sid)
     else:raise ValueError('Unequal glyph x positions')
   else:self.text_run(parent,node.text or '',x,y,m,s,sid)
  else:raise ValueError('Unhandled SVG element '+tag)

 def save(self,out):
  self.visit(self.source.getroot(),self.page)
  # Collapse redundant one-child groups but retain all semantic source groups.
  out.write_bytes(E.tostring(self.doc,xml_declaration=True,encoding='UTF-8',pretty_print=True))
  return {'revision':'P44','figure':self.fig,'source_svg_sha256':hashlib.sha256(self.input.read_bytes()).hexdigest(),'native_counts':dict(self.count),'objects':self.objects,'skipped_invisible_original_paths':self.skipped,'embedded_images':0,'canvas_points':[360,432],'all_text_native_editable':True,'conversion_notes':['Native ODF paths/lines; separate shape for each original marker.','Native editable text frames, including separately editable math glyph runs grouped by source label.','Separate native 1 pt hatch lines for exact-regime bands; each line can be edited.','Native dash and opacity styles; no raster/image/SVG embedding.','P44: native stroke widths rounded upward to 0.01 mm to preserve the minimum nominal width.','Minor font metric, hatch endpoint, antialiasing and stroke placement differences may occur across office versions.']}


def main():
 p=argparse.ArgumentParser(description=__doc__);p.add_argument('--kit-root',type=Path,default=Path(__file__).resolve().parents[1]);p.add_argument('--soffice',default=shutil.which('soffice'));p.add_argument('--convert',action='store_true',help='save ODG and reopen it to export a verification PDF');a=p.parse_args();root=a.kit_root.resolve()
 for d in ['fodg','odg','native_exports','verification']:(root/d).mkdir(parents=True,exist_ok=True)
 inventories=[]
 for name in ['Fig1','Fig2','Fig3']:
  c=Converter(root/'reference_exports'/f'{name}.svg');inventories.append(c.save(root/'fodg'/f'{name}_Editable.fodg'))
 (root/'verification'/'Object_Inventory.json').write_text(json.dumps(inventories,ensure_ascii=False,indent=2)+'\n')
 if a.convert:
  if not a.soffice:raise SystemExit('LibreOffice soffice is required with --convert')
  with tempfile.TemporaryDirectory(prefix='sicomp_editable_figure_build_') as profile:
   for name in ['Fig1','Fig2','Fig3']:
    for inp,outdir,fmt in [(root/'fodg'/f'{name}_Editable.fodg',root/'odg','odg'),(root/'odg'/f'{name}_Editable.odg',root/'native_exports','pdf:draw_pdf_Export')]:
     subprocess.run([a.soffice,'-env:UserInstallation='+Path(profile).resolve().as_uri(),'--headless','--convert-to',fmt,'--outdir',str(outdir),str(inp)],check=True)
 print('Created native editable figures; see verification/Object_Inventory.json')
if __name__=='__main__':main()
