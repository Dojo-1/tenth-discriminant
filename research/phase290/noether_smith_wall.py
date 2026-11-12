#!/usr/bin/env python3
"""Phase290: source-exact Noether/Smith wall and p-local countermodels.

Preregistered at 0a3303a, BEFORE this implementation. Finite six-row
original D563 principal test, NOT the full 700-row determinant or a
class-number field theorem. Standard library only.
"""
from itertools import combinations
from math import gcd
from pathlib import Path
import subprocess, sys

ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/"research"/"phase206"))
sys.path.insert(0,str(ROOT/"research"/"phase204"))
from source_probe import params,gram,det,rank_mod
from ordinary_jet_filtration import jet

D=563
LABELS=((0,0),(1,0),(2,0),(1,1),(4,0),(4,1))
PRIMES=(2,3,5,7,563)
FROZEN={
 "research/phase206/source_probe.py":"3f954b59d9f86b06ad53667c869b5b24f2e6c7f6",
 "research/phase204/ordinary_jet_filtration.py":"dd8b00547ec09a5d9baec15ad34c9ee3e6e4f6b8",
}

def guard():
    for path,sha in FROZEN.items():
        got=subprocess.check_output(["git","rev-parse","HEAD:"+path],
                                    cwd=ROOT,text=True).strip()
        assert got==sha,("source drift",path,got,sha)

def eye(n):
    return [[int(i==j) for j in range(n)] for i in range(n)]

def zeros(n,m):
    return [[0]*m for _ in range(n)]

def tr(A):
    return [list(x) for x in zip(*A)]

def mm(A,B):
    assert len(A[0])==len(B)
    cols=list(zip(*B))
    return [[sum(a*b for a,b in zip(row,col)) for col in cols] for row in A]

def plus(A,B):
    return [[a+b for a,b in zip(x,y)] for x,y in zip(A,B)]

def neg(A):
    return [[-x for x in row] for row in A]

def diag(a):
    return [[v if i==j else 0 for j in range(len(a))] for i,v in enumerate(a)]

def block(A,B,C,D0):
    assert len(A)==len(B) and len(C)==len(D0)
    return [a+b for a,b in zip(A,B)]+[c+d for c,d in zip(C,D0)]

def eval_ordinary(Q,J):
    E=[]
    for r,s in LABELS:
        E.append([w for j in range(J) for z in Q
                  for w in jet(D,r,s,j,z)])
    W=[v for _j in range(J) for _z in Q for v in (2,2*D)]
    assert all(len(row)==len(W) for row in E)
    return E,W

def gram_direct(E,W):
    return mm([[a*b for a,b in zip(row,W)] for row in E],tr(E))

def v_p(n,p):
    assert n>0
    count=0
    while n%p==0:
        count+=1;n//=p
    return count

def smith_by_all_minors(G):
    n=len(G)
    assert n==6 and all(len(row)==n for row in G)
    d=[1]
    for k in range(1,n+1):
        g=0
        for ii in combinations(range(n),k):
            for jj in combinations(range(n),k):
                g=gcd(g,abs(det([[G[i][j] for j in jj] for i in ii])))
        assert g and g%d[-1]==0
        d.append(g)
    s=[d[i+1]//d[i] for i in range(n)]
    assert all(s[i+1]%s[i]==0 for i in range(n-1))
    p=1
    for x in s:p*=x
    assert p==det(G)>0
    return s

def inversion(Q,J):
    index={z:i for i,z in enumerate(Q)}
    assert len(index)==len(Q)
    assert all((-x,-y) in index for x,y in Q)
    perm=[];signs=[]
    for j in range(J):
        for x,y in Q:
            other=index[-x,-y]
            for channel in (0,1):
                perm.append(2*(j*len(Q)+other)+channel)
                signs.append((-1)**j)
    assert all(perm[perm[k]]==k and signs[perm[k]]==signs[k]
               for k in range(len(perm)))
    return perm,signs

def symmetry(E,W,Q,J):
    perm,signs=inversion(Q,J)
    P=[(-1)**(r+s) for r,s in LABELS]
    for i,row in enumerate(E):
        for k in range(len(W)):
            assert P[i]*row[k]==signs[k]*row[perm[k]]
            assert W[k]==W[perm[k]]
    G=gram_direct(E,W)
    assert all(G[i][j]==P[i]*P[j]*G[i][j]
               for i in range(len(P)) for j in range(len(P)))
    return P,perm,signs

def small_integral_wall(Gminus,J):
    orbit=[(0,-2),(0,2)]
    C,W=eval_ordinary(orbit,J)
    n=len(LABELS);m=len(W)
    assert (n,m)==(6,20)
    B=diag(W)
    CB=[[a*b for a,b in zip(row,W)] for row in C]
    Gplus=plus(Gminus,mm(CB,tr(C)))
    Wall=block(Gminus,CB,tr(CB),neg(B))
    U=block(eye(n),neg(C),zeros(m,n),eye(m))
    V=block(eye(n),C,zeros(m,n),eye(m))
    Direct=block(Gplus,zeros(n,m),zeros(m,n),neg(B))
    assert mm(U,V)==eye(n+m)
    assert mm(V,U)==eye(n+m)
    assert mm(mm(U,Direct),tr(U))==Wall
    assert mm(mm(V,Wall),tr(V))==Direct
    for p in PRIMES:
        assert rank_mod(Wall,p)==rank_mod(Direct,p)
    parity,perm,sign=symmetry(C,W,orbit,J)
    T=zeros(m,m)
    for k in range(m):T[perm[k]][k]=sign[k]
    assert mm(T,T)==eye(m) and tr(T)==T
    S=block(diag(parity),zeros(n,m),zeros(m,n),T)
    assert mm(S,S)==eye(n+m)
    assert mm(mm(S,Wall),tr(S))==Wall
    assert mm(mm(S,U),tr(S))==U
    assert mm(mm(S,Direct),tr(S))==Direct
    return {"size":n+m,"added_orbit_points":2,
            "metric_v2":sum(v_p(w,2) for w in W),
            "metric_v563":sum(v_p(w,563) for w in W),
            "unimodular_congruence_and_symmetry":True}

def hostile_controls():
    # Each 1 x m evaluation row consists only of ones; coker E=0.
    # Every observation has the SAME permitted positive trace weight 2.
    a_old,a_new=2,2+2+2
    b_old,b_new=2+2+2,2+2+2+2
    assert v_p(a_old,3)==0 and v_p(a_new,3)==1
    assert v_p(b_old,3)==1 and v_p(b_new,3)==0
    swap=[[0,1],[1,0]]
    eig=[[1,1],[1,-1]]
    assert mm(swap,eig)==[[1,-1],[1,1]]
    assert det(eig)==-2 and det(eig)%2==0
    return True

def main():
    guard()
    rho,R,S,J,Q=params(D)
    assert (rho,R,S,J,len(Q))==(51,140,5,5,359)
    inner=[z for z in Q if abs(z[1])<=1]
    outer=[z for z in Q if abs(z[1])==2]
    assert len(inner)==285 and len(outer)==74
    assert set(inner).isdisjoint(outer)
    assert set(inner)|set(outer)==set(Q)
    assert all((-x,-y) in set(outer) for x,y in outer)
    assert len(inner)>2*(R-1)+(S-1)

    Em,Wm=eval_ordinary(inner,J)
    Ed,Wd=eval_ordinary(outer,J)
    Ep,Wp=eval_ordinary(Q,J)
    assert len(Ep[0])==len(Em[0])+len(Ed[0])
    for i in range(len(LABELS)):
        assert sorted(Em[i]+Ed[i])==sorted(Ep[i])
    Gm,Gd,Gp=(gram_direct(E,W) for E,W in
              ((Em,Wm),(Ed,Wd),(Ep,Wp)))
    assert Gm==gram(D,inner,J,LABELS)
    assert Gd==gram(D,outer,J,LABELS)
    assert Gp==gram(D,Q,J,LABELS)
    assert plus(Gm,Gd)==Gp
    assert det(Gp)>=det(Gm)>0
    for E,W,q in ((Em,Wm,inner),(Ed,Wd,outer),(Ep,Wp,Q)):
        symmetry(E,W,q,J)
    source_rank={}
    for p in PRIMES:
        old,new=rank_mod(Em,p),rank_mod(Ep,p)
        assert old<=new<=6
        source_rank[str(p)]=[old,new]
    old_smith=smith_by_all_minors(Gm)
    new_smith=smith_by_all_minors(Gp)
    local={}
    for p in PRIMES:
        old=[v_p(x,p) for x in old_smith]
        new=[v_p(x,p) for x in new_smith]
        assert sum(old)==v_p(det(Gm),p)
        assert sum(new)==v_p(det(Gp),p)
        local[str(p)]={"old":old,"new":new,
                       "total_change":sum(new)-sum(old)}
    assert all(z in outer for z in ((0,-2),(0,2)))
    wall=small_integral_wall(Gm,J)
    assert hostile_controls()
    print("PHASE290_NOETHER_SMITH_WALL",{
        "D":D,"rho":rho,"original_source_rows_unchanged":R*S,
        "principal_gram_rows_tested":[list(z) for z in LABELS],
        "ordinary_Z_jet_orders":list(range(J)),
        "Q_inner":len(inner),"Q_added":len(outer),"Q_original":len(Q),
        "original_trace_metric":"2,2D",
        "source_rank_Fp_inner_and_original":source_rank,
        "six_by_six_Smith_invariant_exponents":local,
        "direct_vs_mixed_moment_gram_exact":True,
        "original_gram_wall_difference_exact":True,
        "wall_presentation":wall,
        "p3_gram_valuation_can_rise_or_fall_under_positive_addition":True,
        "p2_signed_eigenbasis_not_unimodular":True,
        "no_700_row_smith_or_field_theorem_claim":True,
    },flush=True)
    print("PASS Phase290 exact Noether Smith wall certificate",flush=True)

if __name__=="__main__":
    main()
