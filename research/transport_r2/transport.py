"""Exact affine transport; optional geometry selects eviction, never truth.

The global transport identity is derived in README, not yet proved in Lean.
No production file is edited. Requires SymPy 1.14.0 for the admission oracle.
"""
from __future__ import annotations
from collections import OrderedDict
from dataclasses import dataclass
from fractions import Fraction as Q
from math import acosh, comb, sqrt, tanh
from time import perf_counter
import hashlib
import importlib.util
import json
from pathlib import Path
import sympy as sp

Z, W = sp.symbols('Z W')
POINTS = tuple(map(Q, (0, 1, -1, 2, -2, 3, -3)))
SOURCE_BLOB = '0c4ccb8f2dab99a5317f80345eae7920390fcbc0'

def require(ok: bool, message: str) -> None:
    if not ok:
        raise ValueError(message)

@dataclass(frozen=True)
class Poly:
    terms: tuple[tuple[int, int, Q], ...]
    def __post_init__(self):
        require(all(type(r) is int and type(s) is int and r >= 0 and s >= 0
                    and isinstance(c, Q) and c != 0 for r, s, c in self.terms),
                'invalid polynomial terms')
        require(tuple(sorted(self.terms)) == self.terms and
                len({(r,s) for r,s,c in self.terms}) == len(self.terms),
                'polynomial must be canonical sparse data')
    @classmethod
    def make(cls, terms):
        d = {}
        for r,s,c in terms:
            require(type(r) is int and type(s) is int and r >= 0 and s >= 0, 'negative exponent')
            require(isinstance(c,(int,Q)) and not isinstance(c,bool), 'exact rational coefficient required')
            d[r,s] = d.get((r,s), Q(0)) + Q(c)
        return cls(tuple((r,s,c) for (r,s),c in sorted(d.items()) if c))
    @property
    def degrees(self):
        return (max((r for r,s,c in self.terms), default=0),
                max((s for r,s,c in self.terms), default=0))
    def coeff(self, r, s):
        return next((c for i,j,c in self.terms if (i,j)==(r,s)), Q(0))
    def payload(self):
        return [[r,s,str(c)] for r,s,c in self.terms]
    def key(self):
        return ('QQ', 'ordinary', self.degrees, self.terms)
    def digest(self):
        return hashlib.sha256(json.dumps(self.payload()).encode()).hexdigest()
    def expr(self):
        return sum((sp.Rational(c.numerator,c.denominator)*Z**r*W**s
                    for r,s,c in self.terms), sp.S.Zero)
    def specialize(self,t):
        a,_ = self.degrees
        return [sum((c*Q(t)**s for r,s,c in self.terms if r==i),Q(0))
                for i in range(a+1)]

@dataclass(frozen=True)
class Frame:
    scale: Q = Q(1)
    u: Q = Q(1)
    h: Q = Q(0)
    v: Q = Q(1)
    b: Q = Q(0)
    def __post_init__(self):
        require(all(isinstance(x,Q) for x in (self.scale,self.u,self.h,self.v,self.b)),
                'frame coefficients must be exact rationals')
        require(self.scale != 0 and self.u != 0 and self.v != 0, 'noninvertible frame')
    def apply(self, p: Poly) -> Poly:
        return Poly.make((i,j,c*self.scale*comb(r,i)*self.u**i*self.h**(r-i)*
                          comb(s,j)*self.v**j*self.b**(s-j))
                         for r,s,c in p.terms for i in range(r+1) for j in range(s+1))
    def then(self, other: Frame) -> Frame:
        # other.apply(self.apply(F)): substitution order is explicit.
        return Frame(self.scale*other.scale,self.u*other.u,self.h+self.u*other.h,
                     self.v*other.v,self.b+self.v*other.b)
    def inverse(self) -> Frame:
        return Frame(1/self.scale,1/self.u,-self.h/self.u,1/self.v,-self.b/self.v)
    def factor(self,a: int) -> Q:
        require(a >= 1, 'positive exact Z-degree required')
        return self.scale**(2*a-1)*self.u**(a*a)
    def map_point(self,t: Q) -> Q:
        return (t-self.b)/self.v
    def payload(self):
        return [str(x) for x in (self.scale,self.u,self.h,self.v,self.b)]

def canonicalize(p: Poly):
    """Exact section for scalar/two-translation orbits with nonzero corner.
    Returns (representative, representative-to-input frame, supported).
    It is deliberately not a general affine-equivalence solver.
    """
    a,b = p.degrees
    require(a >= 1, 'positive exact Z-degree required')
    c = p.coeff(a,b)
    if not c:
        return p, Frame(), False
    h = -p.coeff(a-1,b)/(a*c)
    shift = -p.coeff(a,b-1)/(b*c) if b else Q(0)
    normalizer = Frame(1/c,Q(1),h,Q(1),shift)
    return normalizer.apply(p), normalizer.inverse(), True

def load_production(path: str):
    data = Path(path).read_bytes()
    sha = hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()
    require(sha == SOURCE_BLOB, 'frozen production source drift')
    spec = importlib.util.spec_from_file_location('frozen_multiplicity', path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod

def matrix_value(p: Poly,t: Q,production) -> Q:
    a,_ = p.degrees
    require(a >= 1, 'positive exact Z-degree required')
    return Q(production.det(production.fixed_sylvester(p.specialize(t),a)))

def oracle_value(p: Poly,t: Q) -> Q:
    """Independent column construction via symbolic differentiation, fixed size."""
    a,_ = p.degrees
    require(a >= 1, 'positive exact Z-degree required')
    n = 2*a-1
    f = p.expr().subs(W,sp.Rational(t.numerator,t.denominator))
    g = sp.diff(f,Z)
    cols = [sp.Poly(Z**j*f,Z) for j in range(a-1)]
    cols += [sp.Poly(Z**j*g,Z) for j in range(a)]
    mat = sp.Matrix(n,n,lambda i,j: cols[j].nth(i))
    val = mat.det(method='domain-ge')
    return Q(int(sp.numer(val)),int(sp.denom(val)))

@dataclass(frozen=True)
class Record:
    source: Poly
    degree: int
    samples: tuple[tuple[Q,Q], ...]
    field: str = 'QQ'
    derivative: str = 'ordinary'
    def validate(self):
        require(self.field=='QQ' and self.derivative=='ordinary', 'incompatible record regime')
        require(self.degree==self.source.degrees[0] and self.degree>=1, 'wrong global degree')
        require(bool(self.samples) and len(self.samples)<=len(POINTS), 'empty/oversized record')
        require(all(isinstance(t,Q) and isinstance(d,Q) for t,d in self.samples), 'inexact samples')
        require(len({t for t,d in self.samples})==len(self.samples), 'duplicate probes')
        require(all(d==0 for t,d in self.samples[:-1]), 'record continues after success')
    def payload(self):
        return {'source':self.source.payload(),'degree':self.degree,
                'samples':[[str(t),str(d)] for t,d in self.samples],
                'field':self.field,'derivative':self.derivative}

def admit(record: Record) -> int:
    record.validate()
    for t,d in record.samples:
        require(oracle_value(record.source,t)==d, 'forged source value')
    return len(record.samples)

def transport(record: Record,target: Poly,frame: Frame):
    """Conditional on admission of the root; no fuzzy or distance input allowed."""
    record.validate()
    require(frame.apply(record.source)==target, 'incorrect transport identity')
    require(target.degrees[0]==record.degree, 'changed global degree')
    return tuple((frame.map_point(t),frame.factor(record.degree)*d) for t,d in record.samples)

def ball_feature(p: Poly):
    a,b = p.degrees
    v = (a/4,b/3,tanh(float(p.coeff(0,0))/4))
    norm = sqrt(sum(x*x for x in v))
    return tuple(x/(1+norm) for x in v)

def distance(x,y,hyperbolic=False):
    d2 = sum((a-b)**2 for a,b in zip(x,y))
    if not hyperbolic:
        return sqrt(d2)
    nx,ny = sum(a*a for a in x),sum(b*b for b in y)
    require(nx<1 and ny<1, 'outside Poincare chart')
    return acosh(max(1.0,1+2*d2/((1-nx)*(1-ny))))

POLICIES = ('direct','raw_lru','canonical_lru','euclidean','hyperbolic',
            'euclidean_slow','hyperbolic_slow','canonical_unbounded')

class Runner:
    def __init__(self,policy,production,capacity=4):
        require(policy in POLICIES,'unknown policy')
        require(type(capacity) is int and capacity>0,'positive cache capacity required')
        self.policy,self.production,self.capacity=policy,production,capacity
        self.cache=OrderedDict()
        self.context=None
        self.regime=None
        self.counts=dict(production_calls=0,admission_calls=0,hits=0,misses=0,
                         nonzero=0,unresolved=0,hard_resets=0,max_entries=0,max_bytes=0)
        self.times={k:0.0 for k in ('normalization','routing','solving','admission','transport','total')}
    def run(self,p: Poly):
        started=perf_counter(); t=perf_counter()
        normal,to_target,supported=canonicalize(p)
        self.times['normalization']+=perf_counter()-t
        use_canonical=self.policy not in ('direct','raw_lru')
        source=normal if use_canonical else p
        frame=to_target if use_canonical else Frame()
        key=source.key()
        t=perf_counter()
        if self.policy in ('euclidean','hyperbolic','euclidean_slow','hyperbolic_slow'):
            feature=ball_feature(normal)
            if self.context is None or self.regime != p.degrees:
                self.context=feature; self.regime=p.degrees
                self.counts['hard_resets']+=1
            else:
                eta=0.25 if self.policy.endswith('_slow') else 1.0
                self.context=tuple((1-eta)*a+eta*b for a,b in zip(self.context,feature))
        record=self.cache.get(key) if self.policy!='direct' else None
        self.times['routing']+=perf_counter()-t
        if record is not None:
            self.counts['hits']+=1; self.cache.move_to_end(key)
        else:
            self.counts['misses']+=1; samples=[]; t=perf_counter()
            points=POINTS if use_canonical else tuple(to_target.map_point(x) for x in POINTS)
            for point in points:
                d=matrix_value(source,point,self.production)
                self.counts['production_calls']+=1; samples.append((point,d))
                if d: break
            record=Record(source,source.degrees[0],tuple(samples))
            self.times['solving']+=perf_counter()-t
            t=perf_counter(); self.counts['admission_calls']+=admit(record)
            self.times['admission']+=perf_counter()-t
            if self.policy!='direct':
                t=perf_counter()
                if self.policy!='canonical_unbounded' and len(self.cache)>=self.capacity:
                    if self.policy in ('raw_lru','canonical_lru'):
                        self.cache.popitem(last=False)
                    else:
                        hyper=self.policy.startswith('hyperbolic')
                        victim=max(self.cache,key=lambda k: distance(ball_feature(self.cache[k].source),self.context,hyper))
                        del self.cache[victim]
                self.cache[key]=record
                self.times['routing']+=perf_counter()-t
        t=perf_counter(); samples=transport(record,p,frame)
        self.times['transport']+=perf_counter()-t
        self.times['total']+=perf_counter()-started
        self.counts['nonzero' if samples[-1][1] else 'unresolved']+=1
        self.counts['max_entries']=max(self.counts['max_entries'],len(self.cache))
        byte_count=sum(len(json.dumps(r.payload()).encode()) for r in self.cache.values())
        self.counts['max_bytes']=max(self.counts['max_bytes'],byte_count)
        return {'target':p.digest(),'source':source.digest(),'supported':supported,
                'frame':frame.payload(),'samples':[[str(t),str(d)] for t,d in samples],
                'nonzero':bool(samples[-1][1])}
