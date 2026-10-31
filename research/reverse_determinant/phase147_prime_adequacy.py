#!/usr/bin/env python3
"""Phase147: exact p-local support minima of ORIGINAL ordinary-Z integer jets.

Finite input: rho=5, R=8, S=J=4, D=13,17,18,19,21,23,24,25.
The p-local adequacy theorem is elementary; no field-bound implication.
"""
from __future__ import annotations
from itertools import combinations
from math import comb, log
from sympy import Matrix, ZZ, eye
from sympy.matrices.normalforms import hermite_normal_form, smith_normal_form
from phase144_verifier import FULL as REPO_D19, evaluation as REPO_E19

R,S,J,RHO=8,4,4,5
N=R*S
MASK=(1<<N)-1
WITNESSES={
 13:[(-4,0),(-1,0),(-1,1),(0,1),(1,-1),(2,0),(5,0)],
 17:[(-3,0),(-1,0),(-1,1),(0,1),(1,1),(2,0),(2,1),(4,0)],
 18:[(-2,0),(-2,1),(-1,-1),(0,1),(1,-1),(2,-1),(5,0)],
 19:[(-2,-1),(-1,-1),(-1,0),(0,-1),(0,0),(1,-1)],
 21:[(-3,0),(-2,0),(-1,0),(0,0),(0,1),(1,1),(2,-1)],
 23:[(-4,0),(-3,0),(-1,-1),(-1,0),(0,0),(0,1),(1,0),(1,1),(4,0)],
 24:[(-2,0),(-1,1),(0,0),(0,1),(1,-1),(2,0)],
 25:[(-3,0),(-2,0),(-1,0),(0,-1),(0,0),(1,0),(2,0),(3,0),(4,0)],
}
LOWER={
 13:(177100,2592,0,0),
 17:(116280,9720,0,0),
 18:(54264,4560,0,0),
 19:(20349,0,0,0),
 21:(54264,1296,0,0),
 23:(24310,224,0,0),
 24:(6188,56,0,0),
 25:(1287,48,20,0),
}

def qellipse(d):
 return sorted((x,y) for x in range(-RHO,RHO+1) for y in range(-RHO,RHO+1)
               if x*x+d*y*y<=RHO*RHO)
def mul(a,b,d):return (a[0]*b[0]-d*a[1]*b[1],a[0]*b[1]+a[1]*b[0])
def pwr(a,n,d):
 v=(1,0)
 for _ in range(n):v=mul(v,a,d)
 return v
def falling(r,j):
 z=1
 for k in range(j):z*=r-k
 return z

def original_eval(Q,d):
 """Independent parameterized integer-pair expansion; compare at D=19."""
 columns=[]
 for x,y in Q:
  zp=[pwr((x,y),k,d) for k in range(R)]
  wp=[pwr((x,-y),k,d) for k in range(S)]
  for j in range(J):
   re=[]; im=[]
   for r in range(R):
    for s in range(S):
     a,b=mul(zp[r-j],wp[s],d) if j<=r else (0,0)
     f=falling(r,j) if j<=r else 0
     re.append(f*a); im.append(f*b)
   columns.extend([re,im])
 return Matrix(N,len(columns),lambda i,k:columns[k][i])

def dabs(X):return abs(int(X.det(method='domain-ge')))
def lnint(n):
 assert n>0
 s=str(n); k=min(len(s),16)
 return log(int(s[:k]))+(len(s)-k)*log(10)
def F2_blocks(C):
 return [[sum((int(C[i,8*q+j])&1)<<i for i in range(N)) for j in range(8)]
         for q in range(C.cols//8)]
def F3_blocks(C):
 out=[]
 for q in range(C.cols//8):
  part=[]
  for j in range(8):
   o=t=0
   for i in range(N):
    v=int(C[i,8*q+j])%3
    if v==1:o|=1<<i
    if v==2:t|=1<<i
   part.append((o,t))
  out.append(part)
 return out

def rank2(B,sel):
 base=[0]*N;k=0
 for q in sel:
  for v in B[q]:
   while v:
    i=v.bit_length()-1
    if base[i]:v^=base[i]
    else:base[i]=v;k+=1;break
 return k

def add3(a1,a2,b1,b2):
 a0=MASK^(a1|a2);b0=MASK^(b1|b2)
 return ((a0&b1)|(a1&b0)|(a2&b2),(a0&b2)|(a2&b0)|(a1&b1))
def rank3(B,sel):
 base=[(0,0)]*N;k=0
 for q in sel:
  for o,t in B[q]:
   while o or t:
    i=(o|t).bit_length()-1
    po,pt=base[i]
    if po or pt:
     o,t=add3(o,t,pt,po) if o&(1<<i) else add3(o,t,po,pt)
    else:
     base[i]=(o,t) if o&(1<<i) else (t,o)
     k+=1;break
 return k

def rankprime(C,sel,p):
 basis={}
 for q in sel:
  for j in range(8):
   v=[int(C[i,8*q+j])%p for i in range(N)]
   for i in range(N-1,-1,-1):
    if not v[i]:continue
    if i in basis:
     b=basis[i];mul=v[i]
     v=[(a-mul*x)%p for a,x in zip(v,b)]
    else:
     inv=pow(v[i],-1,p)
     basis[i]=[(inv*x)%p for x in v]
     break
   if len(basis)==N:return N
 return len(basis)

def odd_minor_bound(C):
 """A nonzero square column minor mod 2, hence a valid exact modular HNF bound."""
 base=[0]*N;which=[]
 for j in range(C.cols):
  v=sum((int(C[i,j])&1)<<i for i in range(N))
  while v:
   i=v.bit_length()-1
   if base[i]:v^=base[i]
   else:base[i]=v;which.append(j);break
  if len(which)==N:break
 assert len(which)==N
 bound=dabs(C[:,which])
 assert bound>0 and bound%2==1
 return bound

def full_image_certificate(C):
 C=C.applyfunc(int)
 return hermite_normal_form(C,D=odd_minor_bound(C))==eye(N)

def gram_det(E,d):
 metric=Matrix.diag(*([2,2*d]*(E.cols//2)))
 G=E*metric*E.T
 return dabs(G),sum(lnint(int(G[i,i])) for i in range(N))

def local_failure_control(d,H,Q):
 if d!=21:return
 witness=[(-2,0),(-1,-1),(-1,0),(0,0),(0,1),(1,1),(5,0)]
 C=(H.inv()*original_eval(witness,d)).applyfunc(int)
 blocks=list(range(len(witness)))
 assert all(rankprime(C,blocks,p)==N for p in (2,3,5))
 assert rankprime(C,blocks,7)==28
 bound=odd_minor_bound(C)
 sub=hermite_normal_form(C,D=bound)
 assert dabs(sub)==7**4
 sn=smith_normal_form(sub,domain=ZZ)
 nonunit=[abs(int(sn[i,i])) for i in range(N) if abs(int(sn[i,i]))!=1]
 assert nonunit==[7,7,7,7]
 print('CONTROL D21: mod2/3/5 all full, but index=7^4; mod7 rank=28',flush=True)

def main():
 assert qellipse(19)==REPO_D19
 assert original_eval(REPO_D19,19)==REPO_E19(REPO_D19)
 axis=original_eval([(x,0) for x in range(-4,4)],19)
 real_minor=axis[:,[8*t+2*j for t in range(8) for j in range(J)]]
 real_bound=dabs(real_minor)
 assert real_bound>0
 print('PASS: original Phase140 ordinary-Z jets reproduced; real-line square witness valid',flush=True)
 for d,qs in WITNESSES.items():
  Q=qellipse(d);E=original_eval(Q,d)
  H=hermite_normal_form(E,D=real_bound)
  C=(H.inv()*E).applyfunc(int)
  assert all(v.q==1 for v in H.inv()*E)
  B2=F2_blocks(C); B3=F3_blocks(C)
  kmin=len(qs); lower_k=kmin-1
  n2=n23=n235=0
  for inds in combinations(range(len(Q)),lower_k):
   if rank2(B2,inds)<N:continue
   n2+=1
   if rank3(B3,inds)<N:continue
   n23+=1
   if rankprime(C,inds,5)<N:continue
   n235+=1
  got=(comb(len(Q),lower_k),n2,n23,n235)
  assert got==LOWER[d],(d,got,LOWER[d])
  assert n235==0
  assert all(q in Q for q in qs)
  Es=original_eval(qs,d)
  Cs=(H.inv()*Es).applyfunc(int)
  assert full_image_certificate(Cs)
  assert rank2(F2_blocks(Cs),range(kmin))==N
  assert rank3(F3_blocks(Cs),range(kmin))==N
  full_det,full_had=gram_det(E,d)
  sub_det,sub_had=gram_det(Es,d)
  assert full_det>=sub_det>0 and full_had>=lnint(full_det)
  assert sub_had>=lnint(sub_det)
  print('D=',d,'full_points=',len(Q),'minimum=',kmin,'lower_exhausted=',got,
        'logdet_full=',f'{lnint(full_det):.8f}',
        'logdet_min=',f'{lnint(sub_det):.8f}',
        'log_hadamard_min=',f'{sub_had:.8f}',flush=True)
  local_failure_control(d,H,Q)
 print('PHASE147_PASS: 8 exact minimum supports; 2/3/5 modular exclusions; 7-primary counterworld',flush=True)

if __name__=='__main__':main()
