#!/usr/bin/env python3
"""Rebuild manuscript Figures 2 and 3 from exact constants.

No stored image, external archive or network input is read.  Matplotlib is an
optional presentation dependency; the scientific check suite remains stdlib.
Figure 1 has a separate exact prefix generator. This module never writes Fig1.
"""
from __future__ import annotations
import argparse
from datetime import datetime, timezone
from fractions import Fraction as F
from hashlib import sha256
import json
from math import sqrt
from pathlib import Path
import platform
import sys

CAPTIONS = {
  "Fig2": "Analytically established acquisition regimes on diagonal bands. Each separate column represents one integer archive length N; no values between columns are implied. The completion width satisfies 0<d<=1. For K=3, the zero-overhead and first-supercritical regions include their upper boundaries and hold for arbitrary fixed positive row prices and nonnegative common setup. The marked five-row triangular case has unit-price, zero-setup ratios 71/67 and 15/14. For K>=3 at unit prices and zero setup, 0<dN<=1 gives the exact unbounded-domain formula; outside this range the general comparison provides bounds. At d=0 the positive class is empty and no acquisition ratio is assigned.",
  "Fig3": "A fixed alphabet and the cost of requiring complete candidate observation. (A) The raw symbols are (0,0), (1,0) and (1,1). The displayed mean vectors of the two hard worlds use N=12 and q=3. Diamonds and squares mark candidates, coloured circles mark left rivals, and the shared right rival is (1,0); the two lines join the rivals. (B) Lower and upper bounds for accumulation points of the optimal acquisition ratios as integer N grows, on the continuous triangle with K=3, unit row prices and zero setup. The middle row restricts policies to full candidate observation before TRUE on every positive archive and has the exact asymptotic limit 12/11. The unrestricted randomised interval is [23/22,12/11], of width 1/22. These are analytic results, not confidence intervals or measured performance. Convergence and the exact asymptotic constants for unrestricted policies remain open."
}

def exact_values():
    rows=[]
    for n in range(1,17):
        zero=F(1) if n==1 else min(F(1),F(2,n-1))
        first=F(1) if n==1 else min(F(1),F(3,n-1))
        rows.append({'N':n,'zero_overhead_upper':str(zero),
                     'first_supercritical_upper':str(first),'general_exact_upper':str(F(1,n))})
    worlds={
      'U':{'A':['3/4','1/4'],'L':['5/12','5/12'],'R':['1','0']},
      'V':{'A':['5/6','1/4'],'L':['1/2','1/2'],'R':['1','0']}
    }
    return {
      'schema':'sicomp-analytic-figures-p44-v1',
      'revision':'P44',
      'scope':'Analytic theorem illustrations, not empirical observations',
      'Fig2':{
        'model':'T_d={(c,f):0<=f<=c<=1,c-f<=d}',
        'domain':{'N':'positive integers','d':'0<d<=1','displayed_N':list(range(1,17))},
        'd_zero':'excluded: positive archive class is empty',
        'K3':{'zero_overhead':'d*(N-1)<=2','first_supercritical':'2<d*(N-1)<=3','prices':'arbitrary fixed positive row prices; common setup permitted'},
        'general_K':{'K':'K>=3','equality':'0<d*N<=1','prices':'unit row prices; zero setup'},
        'boundaries':rows,
        'finite_marker':{'N':5,'d':'1','randomised':'71/67','deterministic':'15/14','prices':'unit row prices; zero setup'}},
      'Fig3':{
        'alphabet':[['0','0'],['1','0'],['1','1']], 'N':12,'q':3,
        'worlds':worlds,
        'candidate_vertical_gap_above_rival_chord':{'U':'1/14','V':'1/12'},
        'bounds_scope':{'domain':'continuous triangle T_1','K':3,'row_prices':'unit','setup':'0','meaning':'exact limit for randomised candidate-census policies; bounds on liminf and limsup for unrestricted policies, whose convergence is not proved'},
        'bounds':[
          {'policy_class':'randomised unrestricted','lower':'23/22','upper':'12/11'},
          {'policy_class':'randomised candidate complete before TRUE on every positive archive','lower':'12/11','upper':'12/11'},
          {'policy_class':'deterministic unrestricted','lower':'12/11','upper_expression':'3/(4*sqrt(2)-3)','upper_decimal_display':f'{3/(4*sqrt(2)-3):.6f}'}],
        'candidate_complete_bound_gap':'0',
        'candidate_census_asymptotic_limit':'12/11',
        'unrestricted_randomised_bound_gap':'1/22',
        'conditional_partial_candidate_probability':'At least 1/2 asymptotically on the specified hard family IF a valid policy sequence approaches the known lower bound 23/22',
        'exact_global_limits':{'randomised_candidate_census':'12/11','randomised_unrestricted':'open','deterministic_unrestricted':'open'}},
      'captions':CAPTIONS,
      'proof_locations':{
        'Fig2':'Main diagonal-band geometry and priced-transition results; finite five-row case in Supplementary Materials',
        'Fig3':'Main fixed-alphabet hard family, candidate-census lower bound and sharp two-branch triangle policy; Supplement algebraic verification'},
      'display_contract':{'width_inches':5.0,'height_inches':6.0,'minimum_declared_font_pt':8.5,'minimum_essential_stroke_pt':1.0,
                          'discrete_N':'separate columns, never interpolated','PDF':'vector paths and embedded text fonts','SVG':'vector paths and text','PNG_dpi':360}}

def verify_semantics(v):
    def dominates(x,y):return all(a<=b for a,b in zip(x,y)) and x!=y
    for row in v['Fig2']['boundaries']:
        n=row['N'];z=F(row['zero_overhead_upper']);s=F(row['first_supercritical_upper'])
        assert 0<z<=s<=1
        assert z*(n-1)<=2
        if z<1:assert z*(n-1)==2
        if s>z:assert s*(n-1)==3
        assert F(row['general_exact_upper'])*n==1
        # Direct classification on and just above each strict threshold.
        if n>3:
            d=F(2,n-1);assert d*(n-1)==2
            assert (d+F(1,1000*n))*(n-1)>2
        if n>4:
            d=F(3,n-1);assert d*(n-1)==3
            assert (d+F(1,1000*n))*(n-1)>3
    for name,w in v['Fig3']['worlds'].items():
        a,l,r=(tuple(map(F,w[k])) for k in ['A','L','R'])
        assert not dominates(l,a) and not dominates(r,a)
        chord=l[1]+(r[1]-l[1])*(a[0]-l[0])/(r[0]-l[0])
        assert a[1]-chord==F(v['Fig3']['candidate_vertical_gap_above_rival_chord'][name])>0
        # Independent support test by intersecting alpha intervals for (alpha,1-alpha).
        lo,hi=F(0),F(1)
        for p in (l,r):
            b=p[1]-a[1];c=p[0]-a[0]-b
            if c>0:lo=max(lo,-b/c)
            elif c<0:hi=min(hi,-b/c)
            else:assert b>=0
        assert lo>hi
    assert F(12,11)-F(12,11)==F(v['Fig3']['candidate_complete_bound_gap'])
    assert F(12,11)-F(23,22)==F(v['Fig3']['unrestricted_randomised_bound_gap'])
    assert 12-11*F(23,22)==F(1,2)
    return {'status':'PASS','integer_N_boundaries':16,'worlds_checked':2,
            'method':'exact Fractions for thresholds, domination, chord gaps and support intervals; analytic radical converted only for plotting',
            'scope':'checks displayed semantics, not universal theorem proofs'}

def draw_fig1(plt,v):
    from matplotlib.patches import Patch
    fig,axes=plt.subplots(2,1,figsize=(5,6))
    fig.subplots_adjust(left=.115,right=.98,bottom=.16,top=.91,hspace=.70)
    green='#dbe9d5';blue='#d9e5f2';grey='#f0f0f0';edge='#30383f'
    ns=[r['N'] for r in v['Fig2']['boundaries']]
    z=[float(F(r['zero_overhead_upper'])) for r in v['Fig2']['boundaries']]
    b=[float(F(r['first_supercritical_upper'])) for r in v['Fig2']['boundaries']]
    q=[float(F(r['general_exact_upper'])) for r in v['Fig2']['boundaries']]
    ax=axes[0]
    ax.bar(ns,z,width=.74,color=green,edgecolor='none',zorder=2)
    nonempty=[i for i in range(len(ns)) if b[i]>z[i]]
    ax.bar([ns[i] for i in nonempty],[b[i]-z[i] for i in nonempty],bottom=[z[i] for i in nonempty],width=.74,color=blue,edgecolor='#8b9aaa',linewidth=1.0,hatch='///',zorder=2)
    ax.bar(ns,[1-i for i in b],bottom=b,width=.74,color=grey,edgecolor='none',zorder=1)
    ax.plot(ns,z,'o',color='#355332',ms=3,zorder=3)
    ax.plot([ns[i] for i in nonempty],[b[i] for i in nonempty],'s',color='#315b7a',ms=3,zorder=3)
    ax.set_title(r'A  Three configurations ($K=3$)',loc='left',pad=8,fontweight='bold',fontsize=10)
    ax.plot(5,1,'D',mfc='white',mec='#242424',ms=5,zorder=5,clip_on=False)
    ax.annotate('$N=5$, $d=1$\n$71/67$ randomised\n$15/14$ deterministic',
                xy=(5,1),xytext=(8.7,.80),fontsize=8.5,ha='left',va='top',
                bbox={'facecolor':'white','edgecolor':'none','pad':2},
                arrowprops={'arrowstyle':'-','color':edge,'linewidth':1.0},zorder=8)
    ax.legend(handles=[Patch(facecolor=green,label=r'Ratio 1: $d(N-1)\leq2$'),
                       Patch(facecolor=blue,edgecolor='#8b9aaa',hatch='///',label=r'Exact two-terminal regime: $2<d(N-1)\leq3$'),
                       Patch(facecolor=grey,label='Remaining regime: bounds; exact value open in general')],
              loc='upper left',bbox_to_anchor=(-.02,-.24),frameon=False,fontsize=8.5,
              borderaxespad=0,handlelength=1.8,labelspacing=.25)
    ax=axes[1]
    ax.bar(ns,q,width=.74,color=blue,edgecolor='#8b9aaa',linewidth=1.0,hatch='///',zorder=2)
    ax.bar(ns,[1-i for i in q],bottom=q,width=.74,color=grey,edgecolor='none',zorder=1)
    ax.plot(ns,q,'s',color='#315b7a',ms=3,zorder=3)
    ax.set_title(r'B  General catalogue ($K\geq3$)',loc='left',pad=8,fontweight='bold',fontsize=10)
    ax.text(9,.74,'General lower and upper bounds',ha='center',va='center',fontsize=9,
            bbox={'facecolor':'white','edgecolor':'none','pad':2})
    fig.text(.115,.075,r'Hatched region: exact formula for $0<dN\leq1$',
             ha='left',va='bottom',fontsize=9)
    for ax in axes:
        ax.set(xlim=(.45,16.55),ylim=(-.025,1.055),ylabel='Band width $d$')
        ax.set_xticks([1,2,3,4,5,6,8,10,12,14,16]);ax.set_xticks(ns,minor=True)
        ax.tick_params(axis='x',labelsize=8.5,length=2);ax.tick_params(axis='x',which='minor',length=1.5)
        ax.set_yticks([0,.25,.5,.75,1]);ax.set_yticklabels(['0','.25','.50','.75','1'])
        ax.tick_params(axis='y',labelsize=8.5)
        ax.spines[['top','right']].set_visible(False)
        ax.axhline(0,color='#333333',lw=1.0,ls=':',zorder=4)
        ax.scatter(ns,[0]*len(ns),marker='o',s=10,facecolors='white',edgecolors='#333333',linewidths=1.0,zorder=6)
        ax.grid(axis='y',alpha=.14,zorder=0)
    axes[1].set_xlabel('Rows per configuration $N$ (integer)',labelpad=4)
    fig.text(.115,.035,r'$d=0$ is excluded: no positive archives.',fontsize=9,ha='left')
    return fig

def draw_fig2(plt,v):
    from matplotlib.lines import Line2D
    fig=plt.figure(figsize=(5,6))
    fig.text(.02,.965,'A  Fixed alphabet and two hard worlds',fontsize=10,fontweight='bold')
    ax=fig.add_axes([.12,.61,.43,.32]);note=fig.add_axes([.61,.63,.37,.28]);note.axis('off')
    colours={'U':'#216b89','V':'#a96219'};markers={'U':'D','V':'s'}
    ax.fill([0,1,1],[0,0,1],color='#f3f4f5',zorder=0)
    ax.plot([0,1,1,0],[0,0,1,0],color='#9ba4ab',lw=1.0)
    symbols=v['Fig3']['alphabet']
    ax.scatter([float(F(p[0])) for p in symbols],[float(F(p[1])) for p in symbols],
               s=28,c='#222b31',zorder=5)
    for name,w in v['Fig3']['worlds'].items():
        a,l,r=(tuple(float(F(t)) for t in w[k]) for k in ['A','L','R'])
        ax.plot([l[0],r[0]],[l[1],r[1]],color=colours[name],lw=1.1,ls='-' if name=='U' else '--')
        ax.scatter(*l,s=26,color=colours[name],marker='o',zorder=6)
        ax.scatter(*a,s=32,color=colours[name],marker=markers[name],zorder=7)
        ax.annotate(name,a,xytext=(-10,8) if name=='U' else (7,7),textcoords='offset points',fontsize=9,color='#000000')
    for x,y,txt,dx,dy in [(0,0,'(0,0)',.025,.055),(1,0,'(1,0)',-.24,.055),(1,1,'(1,1)',-.26,-.10)]:
        ax.text(x+dx,y+dy,txt,fontsize=8.5)
    ax.set(xlim=(-.035,1.035),ylim=(-.035,1.035),xlabel='Mean first objective',ylabel='Mean second objective')
    ax.set_xticks([0,.5,1]);ax.set_yticks([0,.5,1]);ax.set_aspect('equal')
    note.text(0,1,'$N=12$, $q=3$\n\nBlack dots: symbols\nColoured circles: L\nDiamonds/squares: A\nShared R = (1,0)',fontsize=8.5,va='top',linespacing=1.35)
    note.legend(handles=[Line2D([0],[0],color=colours['U'],marker='D',lw=1.1,label='World U'),
                         Line2D([0],[0],color=colours['V'],marker='s',ls='--',lw=1.1,label='World V')],
                loc='lower left',bbox_to_anchor=(-.07,.05),frameon=False,fontsize=9,handlelength=2)
    fig.text(.02,.51,'B  Asymptotic bounds on acquisition ratios',fontsize=10,fontweight='bold')
    ax=fig.add_axes([.31,.16,.66,.30])
    lo=[F(23,22),F(12,11),F(12,11)];hi=[F(12,11),F(12,11),3/(4*sqrt(2)-3)]
    labels=['Randomised\nunrestricted','Randomised\ncandidate-census','Deterministic\nunrestricted']
    ys=[2,1,0];cols=['#216b89','#5c3f7b','#a96219']
    for i,y in enumerate(ys):
        l,h=float(lo[i]),float(hi[i])
        if i == 1:
            ax.plot(l,y,linestyle='none',marker='D',ms=5,mew=1.3,color=cols[i],zorder=4)
        else:
            ax.plot([l,h],[y,y],color=cols[i],lw=7,alpha=.20,solid_capstyle='butt',zorder=2)
            ax.plot([l,h],[y,y],color=cols[i],lw=1.3,zorder=3)
            ax.plot([l,h],[y,y],linestyle='none',marker='|',ms=9,mew=1.3,color=cols[i],zorder=4)
        ax.text(-.045,y,labels[i],transform=ax.get_yaxis_transform(),ha='right',va='center',fontsize=8.5)
    ax.text(float(lo[0]),2.20,'23/22',ha='center',fontsize=9)
    ax.text(float(hi[0]),2.20,'12/11',ha='center',fontsize=9)
    ax.text((float(lo[0])+float(hi[0]))/2,1.68,'Gap = 1/22',ha='center',fontsize=8.5)
    ax.annotate('Exact limit: 12/11',xy=(float(lo[1]),1),xytext=(1.015,.90),
                ha='left',va='center',fontsize=8.5,linespacing=1.25,
                arrowprops={'arrowstyle':'-','color':cols[1],'linewidth':1.0},
                bbox={'facecolor':'white','edgecolor':'none','pad':1.5})
    ax.text(float(lo[2])-.002,.19,'12/11',ha='right',fontsize=9)
    ax.text(1.147,.19,'3/(4√2 − 3)',ha='right',fontsize=9)
    ax.set(xlim=(.998,1.153),ylim=(-.43,2.48),xlabel='Cost / cheapest realised certificate',yticks=[])
    ax.set_xticks([1,1.05,1.10,1.15]);ax.set_xticklabels(['1.00','1.05','1.10','1.15'])
    ax.axvline(1,color='#727272',lw=1.0,ls=':');ax.grid(axis='x',alpha=.16)
    ax.spines['left'].set_visible(False)
    fig.text(.02,.052,'Continuous triangle; $K=3$; unit prices; zero setup.\nFor unrestricted policies, convergence remains open.',
             fontsize=8.5,ha='left',linespacing=1.35)
    return fig

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--output-dir',type=Path,default=Path(__file__).resolve().parent/'generated')
    args=p.parse_args();out=args.output_dir.resolve();out.mkdir(parents=True,exist_ok=True)
    values=exact_values();semantic=verify_semantics(values)
    (out/'Theorem_Figures_Exact_Values.json').write_text(json.dumps(values,ensure_ascii=False,indent=2)+'\n')
    (out/'Theorem_Figures_Captions.txt').write_text('\n\n'.join(k+'. '+v for k,v in CAPTIONS.items())+'\n')
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    matplotlib.rcParams.update({'font.family':'DejaVu Sans','font.size':9,
        'axes.linewidth':1.0,'grid.linewidth':1.0,'patch.linewidth':1.0,'hatch.linewidth':1.0,
        'xtick.major.width':1.0,'ytick.major.width':1.0,'xtick.minor.width':1.0,'ytick.minor.width':1.0,
        'axes.titlesize':10,'axes.labelsize':9,'xtick.labelsize':8.5,'ytick.labelsize':8.5,
        'svg.fonttype':'none','svg.hashsalt':'sicomp-p33-analytic-figures-v1',
        'pdf.fonttype':42,'ps.fonttype':42,'axes.spines.top':False,'axes.spines.right':False})
    exports=[];font_records=[]
    for name,fn in [('Fig2',draw_fig1),('Fig3',draw_fig2)]:
        fig=fn(plt,values);fig.canvas.draw()
        from matplotlib.text import Text
        visible=[t for t in fig.findobj(Text) if t.get_visible() and t.get_text()]
        font_records.append({'figure':name,'minimum_font_pt':min(t.get_fontsize() for t in visible),'canvas_inches':list(fig.get_size_inches()),'visible_text_items':len(visible)})
        for ext in ['pdf','svg','png']:
            target=out/f'{name}.{ext}'
            kw={'facecolor':'white'}
            if ext=='png':kw.update(dpi=360,metadata={'Software':'Matplotlib '+matplotlib.__version__})
            if ext=='svg':kw['metadata']={'Date':'2026-10-24','Creator':'make_figures.py; exact analytic constants'}
            if ext=='pdf':kw['metadata']={'Title':name+' - analytic acquisition regimes','Author':'Antonio Clim','Creator':'make_figures.py','CreationDate':datetime(2026,10,24,tzinfo=timezone.utc),'ModDate':datetime(2026,10,24,tzinfo=timezone.utc)}
            fig.savefig(target,**kw)
            exports.append({'file':target.name,'bytes':target.stat().st_size,'sha256':sha256(target.read_bytes()).hexdigest()})
        plt.close(fig)
    report={'schema':'sicomp-theorem-figure-build-p44-v1','revision':'P44','finished_at_utc':datetime.now(timezone.utc).isoformat(),'release_metadata_date':'2026-10-24','status':'PASS','semantic_checks':semantic,'exports':exports,'font_records':font_records,
            'script_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),
            'values_sha256':sha256((out/'Theorem_Figures_Exact_Values.json').read_bytes()).hexdigest(),
            'environment':{'python':platform.python_version(),'matplotlib':matplotlib.__version__,'platform':platform.platform()},
            'reads_old_images':False,'network_calls':False,'new_measurements':False,
            'scope':'generation and checks of figure semantics only; proofs remain analytic',
            'final_insertion_requirement':'Insert at 5 inch width or greater, without a smaller height limit; smallest configured text is 8.5 pt at 5 inches.'}
    assert all(x['minimum_font_pt']>=8.5 for x in font_records)
    (out/'Theorem_Figures_Build_Record.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({'status':report['status'],'output_dir':str(out),'files':[x['file'] for x in exports],'font_records':font_records},indent=2))
if __name__=='__main__':main()
