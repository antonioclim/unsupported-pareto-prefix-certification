import json,re,time,math
from pathlib import Path
from fractions import Fraction as F
start=time.monotonic()
class Poly:
    names=['g','z','w','v','t','G','V','x','delta']
    Z=(0,)*len(names)
    def __init__(self, obj=0):
        if isinstance(obj,Poly): self.c=obj.c.copy()
        elif isinstance(obj,dict): self.c={k:F(v) for k,v in obj.items() if v}
        else: self.c={} if not obj else {self.Z:F(obj)}
    @classmethod
    def variable(cls,name):
        e=list(cls.Z); e[cls.names.index(name)]=1
        return cls({tuple(e):F(1)})
    def __add__(self,b):
        b=Poly(b);c=self.c.copy()
        for k,v in b.c.items():c[k]=c.get(k,F(0))+v
        return Poly(c)
    __radd__=__add__
    def __neg__(self):return Poly({k:-v for k,v in self.c.items()})
    def __sub__(self,b):return self+-Poly(b)
    def __rsub__(self,b):return Poly(b)+-self
    def __mul__(self,b):
        b=Poly(b);c={}
        for ka,va in self.c.items():
            for kb,vb in b.c.items():
                k=tuple(a+b for a,b in zip(ka,kb));c[k]=c.get(k,F(0))+va*vb
        return Poly(c)
    __rmul__=__mul__
    def __pow__(self,n):
        r=Poly(1)
        for _ in range(n):r=r*self
        return r
    def __truediv__(self,b):return self*F(1,b)
    def __eq__(self,b):return self.c==Poly(b).c
    def __hash__(self):return hash(tuple(sorted(self.c.items())))
    def __repr__(self):return repr(self.c)
    def index(self):
        assert len(self.c)==1
        e,co=next(iter(self.c.items()));assert sum(e)==1 and co==1
        return e.index(1)
    def subs(self,mapping,val=None):
        if val is not None:mapping={mapping:val}
        mapped={k.index():Poly(v)for k,v in mapping.items()}
        vars=[mapped.get(i,Poly({tuple(1 if j==i else 0 for j in range(len(self.names))):F(1)}))for i in range(len(self.names))]
        powers={(i,0):Poly(1)for i in range(len(self.names))}
        r=Poly()
        for a,co in self.c.items():
            part=Poly(co)
            for i,n in enumerate(a):
                if n:
                    if (i,n)not in powers:powers[(i,n)]=vars[i]**n
                    part=part*powers[(i,n)]
            r=r+part
        return r
    def degree(self,var):return max((k[var.index()]for k in self.c),default=0)
    def terms(self,vars):
        idx=[v.index()for v in vars]
        assert all(all(not e[j]for j in range(len(self.names))if j not in idx)for e in self.c)
        return [(tuple(e[j]for j in idx),co)for e,co in self.c.items()]
