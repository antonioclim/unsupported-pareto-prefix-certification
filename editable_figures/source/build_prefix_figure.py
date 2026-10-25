#!/usr/bin/env python3
"""New exact explanatory figure; uses the retained native ODF converter class.
Own source: BSD-3-Clause; covered figure: CC BY 4.0. Integrated as Figure 1 in P41; P37 unchanged.
"""
from pathlib import Path
from fractions import Fraction as F
import json,hashlib,subprocess,shutil,tempfile
from xml.sax.saxutils import escape
from build_editable_odg import Converter,q
import argparse
p=argparse.ArgumentParser(description=__doc__);p.add_argument('--output-dir',type=Path,required=True);args=p.parse_args()
ROOT=args.output_dir.resolve();ROOT.mkdir(parents=True,exist_ok=True)
W,H=360,432
els=[]
def txt(x,y,s,size=9,bold=False,anchor='start'):
 els.append(f'<text x="{x}" y="{y}" font-family="DejaVu Sans" font-size="{size}" font-weight="{"bold" if bold else "normal"}" text-anchor="{anchor}" fill="#000000">{escape(s)}</text>')
def path(d,fill='none',stroke='#333333',sw=1.1):els.append(f'<path d="{d}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>')
def rect(x,y,w,h,fill='white',stroke='#333333'):path(f'M {x} {y} L {x+w} {y} L {x+w} {y+h} L {x} {y+h} Z',fill,stroke)
def line(x1,y1,x2,y2):path(f'M {x1} {y1} L {x2} {y2}')
# 5 inch width; all labels >=8.5 pt; nominal strokes 1.1 pt. Shape labels stay editable in ODG.
txt(12,17,'(a) Same observations; different cheapest certificates',10,True)
txt(12,33,'Shared prefix b = (2, 3, 1): six paid records',9)
xs=[61,153,245];ys=[63,96,129]
for i,s in enumerate(['Record 1','Record 2','Record 3']):txt(xs[i]+42,49,s,8.5,True,'middle')
rows=[['(3/8, 7/8)','(3/8, 7/8)','unread'],['(0, 1)','(0, 1)','(0, 7/8)'],['(7/8, 0)','unread','unread']]
for g,label in enumerate(['A','L','R']):
 txt(35,ys[g]+17,label,10,True,'middle')
 for j,value in enumerate(rows[g]):
  observed=(g==0 and j<2) or g==1 or(g==2 and j==0)
  rect(xs[j],ys[g],84,25,'#e0e6eb' if observed else '#ffffff')
  txt(xs[j]+42,ys[g]+16,value,8.5,False,'middle')
# hidden state table, retrospective only, not supplied to policy
txt(12,174,'Two compatible archives (hidden from the policy)',9,True)
for x,s in [(12,'World'),(67,'A record 3'),(158,'R records 2, 3'),(285,'Minimum b')]:txt(x,190,s,8.5,True)
line(12,197,348,197)
for yy,vals in [(211,['I','(0, 0)','(5/8, 0), (3/8, 0)','(2, 3, 3)']),(229,['II','(0, 1)','(5/8, 0), (1, 1)','(3, 3, 1)'])]:
 for x,s in zip([12,67,158,285],vals):txt(x,yy,s,8.5)
txt(12,250,'(b) Buying the wrong tail adds avoidable observations',10,True)
# costs from routes after shared prefix, total includes base6
txt(12,267,'Next acquisition route',8.5,True)
txt(249,267,'World I',8.5,True,'middle');txt(315,267,'World II',8.5,True,'middle')
line(12,274,348,274)
for yy,label,a,b in [(290,'Candidate tail first',9,7),(310,'Right tail first (records 2 and 3)',8,9),(334,'Cheapest realised prefix C*',8,7)]:
 txt(12,yy,label,8.5,yy==334);txt(249,yy,str(a),9,yy==334,'middle');txt(315,yy,str(b),9,yy==334,'middle')
line(12,318,348,318)
rect(12,350,336,47,'#eef1f4')
txt(180,367,'Mix the two routes with probabilities 16/23 and 7/23',8.5,False,'middle')
txt(180,385,'Expected cost / C* = 25/23 in both worlds',9,True,'middle')
txt(12,416,'All costs count whole records. World labels are retrospective.',8.5)
svg='<svg xmlns="http://www.w3.org/2000/svg" width="360pt" height="432pt" viewBox="0 0 360 432">'+''.join(els)+'</svg>'
sp=ROOT/'Fig1.svg';sp.write_text(svg)
c=Converter(sp);inv=c.save(ROOT/'Fig1_Editable.fodg')
inv['conversion_notes']=['Native editable text frames and separate vector paths. No raster or SVG image object embedded.','5 inch wide. Minimum label font 8.5pt, nominal lines 1.1pt.','World I equals archive A and world II equals archive D in Supplement S1.6.']
(ROOT/'Fig1_Object_Inventory.json').write_text(json.dumps(inv,ensure_ascii=False,indent=2)+'\n')
qmix=F(16,23)
assert (qmix*9+(1-qmix)*8)/8==F(25,23)
assert (qmix*7+(1-qmix)*9)/7==F(25,23)
record={'revision':'P44','status':'PASS','scope':'Exact arithmetic for the displayed route mixture. TRUE-prefix minima are separately verified by the P40 demonstrator and analytically in Supplement S1.6. This script alone is not an independent certificate optimiser.','prob_candidate_first':str(qmix),'expected_costs':{'I':str(qmix*9+(1-qmix)*8),'II':str(qmix*7+(1-qmix)*9)},'minimum_costs':{'I':8,'II':7},'common_prefix':[2,3,1],'rows_paid_common':6,'displayed_ratio':'25/23','script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'native_images':0}
(ROOT/'Fig1_Exact_Values.json').write_text(json.dumps(record,indent=2)+'\n')
(ROOT/'Fig1_Caption.txt').write_text('Fig1. A six-record prefix is shared by two positive archives, I and II, corresponding to A and D in Supplement S1.6. Observed records are shaded; world labels and unread values are shown retrospectively and are unavailable to the acquisition policy. In I the unique minimum TRUE prefix leaves the candidate incomplete, whereas in II it leaves the right rival incomplete. Continuing from the common prefix, candidate-tail-first and right-tail-first routes have total costs (9,7) and (8,9). Mixing them with probabilities 16/23 and 7/23 balances their ratios at 25/23 on this pair. The global upper bound requires the full policy of Supplement S1.6; this two-world illustration alone is not a global optimality proof. The public domain permits independent [0,1]^2 completions; the displayed pair is not a two-world promise. All coordinates are exact, rows are disclosed in fixed order, prices are unit and setup is zero.\n')
print('Created SVG and native editable FODG; exact displayed arithmetic PASS.')
