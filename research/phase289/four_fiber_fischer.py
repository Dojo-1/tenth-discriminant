#!/usr/bin/env python3
"""Phase289: original-source four-fiber Noether/Fischer strengthening.

Preregistered at c78213e BEFORE the executable source was authored.
This certifies a finite Archimedean improvement OVER prior disjoint pair
blocks, not a new p-adic factor or production-wide discriminant bound.
"""
from fractions import Fraction as F
from math import log
from pathlib import Path
import subprocess
import sys

HERE=Path(__file__).resolve()
ROOT=HERE.parents[2]
for sub in ("phase206","phase204"):
    sys.path.insert(0,str(HERE.parents[1]/sub))
from source_probe import params,gram,det,fibers
from ordinary_jet_filtration import jet

HASHES={
 "research/phase206/source_probe.py":"3f954b59d9f86b06ad53667c869b5b24f2e6c7f6",
 "research/phase204/ordinary_jet_filtration.py":"dd8b00547ec09a5d9baec15ad34c9ee3e6e4f6b8",
}
CASES={
 283:{"params":(31,70,2,2,169),"pairs":35,"four":17,
      "left_pairs":1,"singles":1},
 403:{"params":(40,100,4,4,219),"pairs":51,"four":25,
      "left_pairs":1,"singles":1},
}


def source_guard():
    for path,expected in HASHES.items():
        actual=subprocess.check_output(
            ["git","rev-parse","HEAD:"+path],cwd=ROOT,text=True
        ).strip()
        assert actual==expected,("changed original source",path,actual,expected)


def partition(R,S):
    """Exactly Phase206 parity consecutive pairs, then two-pair coarsening."""
    universe=list(range(1-S,R))
    baseline=[]
    new=[]
    for h in (0,1):
        ds=[d for d in universe if d%2==h]
        pairs=[ds[i:i+2] for i in range(0,len(ds),2)]
        baseline.extend(pairs)
        i=0
        while i<len(pairs):
            if (i+1<len(pairs)
                and len(pairs[i])==2 and len(pairs[i+1])==2):
                new.append(pairs[i]+pairs[i+1])
                i+=2
            else:
                new.append(pairs[i])
                i+=1
    assert sorted(d for group in baseline for d in group)==universe
    assert sorted(d for group in new for d in group)==universe
    assert all(len(g) in (1,2,4) for g in new)
    assert all(all(d%2==g[0]%2 for d in g) for g in new)
    flat=[(r,s) for group in new for d in group for r,s in fibers(R,S,d)]
    assert sorted(flat)==[(r,s) for r in range(R) for s in range(S)]
    # The pair multiset, including a singleton, must be the old fixed matching.
    phase206_old=[]
    for h in (0,1):
        ds=[d for d in universe if d%2==h]
        phase206_old.extend([ds[i:i+2] for i in range(0,len(ds),2)])
    assert baseline==phase206_old
    return baseline,new


def submatrix(G,ii,jj=None):
    if jj is None: jj=ii
    return [[G[i][j] for j in jj] for i in ii]


def matmul(A,B):
    assert A and B and len(A[0])==len(B)
    cols=list(zip(*B))
    return [[sum((a*b for a,b in zip(row,col)),F(0))
             for col in cols] for row in A]


def transpose(A):
    return [list(x) for x in zip(*A)]


def eye(n):
    return [[F(i==j) for j in range(n)] for i in range(n)]


def block(A,B,C,D):
    return [a+b for a,b in zip(A,B)]+[a+b for a,b in zip(C,D)]


def inv_fraction(A):
    n=len(A)
    V=[[F(z) for z in A[i]]+eye(n)[i] for i in range(n)]
    for k in range(n):
        pivot=next((i for i in range(k,n) if V[i][k]),None)
        assert pivot is not None,("singular pair Gram",k)
        V[k],V[pivot]=V[pivot],V[k]
        denom=V[k][k]
        V[k]=[x/denom for x in V[k]]
        for i in range(n):
            if i==k:continue
            c=V[i][k]
            if c:
                V[i]=[x-c*y for x,y in zip(V[i],V[k])]
    inv=[row[n:] for row in V]
    assert matmul(A,inv)==eye(n)
    return inv


def fraction_det(A):
    M=[[F(x) for x in row] for row in A]
    n=len(M)
    value=F(1)
    for k in range(n):
        piv=next((i for i in range(k,n) if M[i][k]),None)
        if piv is None:return F(0)
        if piv!=k:
            M[k],M[piv]=M[piv],M[k]
            value=-value
        d=M[k][k]
        value*=d
        for i in range(k+1,n):
            c=M[i][k]/d
            if c:
                M[i][k:]=[x-c*y for x,y in zip(M[i][k:],M[k][k:])]
    return value


def jet_pair_entry(D,Q,J,a,b):
    """Independent ordinary-jet and original trace-metric entry."""
    s=0
    for j in range(J):
        for z in Q:
            v=jet(D,*a,j,z)
            w=jet(D,*b,j,z)
            s+=2*(v[0]*w[0]+D*v[1]*w[1])
    return s


def moving_shear_control(G,a,b):
    """Exact rational moving frame from two old 2-fiber blocks to a quartet."""
    total=a+b
    A=submatrix(G,list(range(a)))
    B=submatrix(G,list(range(a,total)))
    C=submatrix(G,list(range(a)),list(range(a,total)))
    Ai=inv_fraction(A)
    D=matmul(transpose(C),Ai)
    Z=[[F(0)]*a for _ in range(b)]
    assert len(D)==b and len(D[0])==a
    CTC=matmul(D,C)
    S=[[F(B[i][j])-CTC[i][j] for j in range(b)] for i in range(b)]
    assert fraction_det(S)>0
    assert fraction_det(A)*fraction_det(S)==det(G)
    eye_a=eye(a)
    eye_b=eye(b)
    for t in (F(0),F(1,2),F(1)):
        low=[[-t*d for d in row] for row in D]
        H=block(eye_a,[[F(0)]*b for _ in range(a)],low,eye_b)
        moved=matmul(matmul(H,G),transpose(H))
        want=block(
          A,[[(F(1)-t)*v for v in row] for row in C],
          [[(F(1)-t)*v for v in row] for row in transpose(C)],
          [[F(B[i][j])-t*(2-t)*CTC[i][j] for j in range(b)] for i in range(b)]
        )
        assert moved==want,("moving source-congruence mismatch",t)
        assert fraction_det(moved)==det(G)
        if t==1:
            assert all(moved[i][j]==0 for i in range(a) for j in range(a,total))
            assert submatrix(moved,list(range(a,total)))==S
    # Explicit wrong-sign control: adding the cross term never gives Schur.
    wrong=[[F(B[i][j])+CTC[i][j] for j in range(b)] for i in range(b)]
    assert wrong!=S if any(v!=0 for row in C for v in row) else wrong==S
    return True


def witness_and_gain(D,Q,J,labels,a,b,G):
    A=submatrix(G,list(range(a)))
    B=submatrix(G,list(range(a,a+b)))
    da,db,dq=det(A),det(B),det(G)
    assert da>0 and db>0 and dq>0,("not positive original Gram",D,labels)
    pairprod=da*db
    assert pairprod>=dq,("Fischer violation",D,labels)
    C=submatrix(G,list(range(a)),list(range(a,a+b)))
    witnesses=[(i,j,C[i][j]) for i in range(a) for j in range(b) if C[i][j]]
    if not witnesses:
        assert pairprod==dq,("nonzero correlation without cross",D,labels)
        return 0,False,F(0),0.,False
    i,j,c=witnesses[0]
    u=G[i][i]
    v=G[a+j][a+j]
    assert u>0 and v>0 and 0<c*c<u*v
    assert dq*u*v<=pairprod*(u*v-c*c),("canonical correlation lower failed",D,labels)
    independent=jet_pair_entry(D,Q,J,labels[i],labels[a+j])
    assert independent==c,("second exact ordinary-jet oracle disagrees",D,labels)
    assert pairprod>dq
    # Exact conservative K such that 2^K*dq < da*db.
    k=max(0,pairprod.bit_length()-dq.bit_length()-1)
    while k>0 and (dq<<k)>=pairprod:
        k-=1
    while (dq<<(k+1))<pairprod:
        k+=1
    assert (dq<<k)<pairprod
    assert (dq<<(k+1))>=pairprod
    q=F(c*c,u*v)
    assert 0<q<1
    # Floating-point log gain is an illustration only; all certificates above
    # use exact integer or Fraction inequalities.
    approx=log(pairprod)-log(dq)
    assert approx>=-1e-7
    return k,True,q,approx,True


def case(D):
    rho,R,S,J,Q=params(D)
    expected=CASES[D]
    assert (rho,R,S,J,len(Q))==expected["params"]
    assert len(Q)>2*(R-1)+(S-1)
    qset=set(Q)
    assert all((-x,-y) in qset for x,y in Q)
    baseline,groups=partition(R,S)
    assert sum(len(g)==2 for g in baseline)==expected["pairs"]
    assert sum(len(g)==4 for g in groups)==expected["four"]
    assert sum(len(g)==2 for g in groups)==expected["left_pairs"]
    assert sum(len(g)==1 for g in groups)==expected["singles"]

    # The central Noether odd block cross is exactly zero.
    Z=gram(D,Q,J,[(0,0),(1,0)])
    assert Z[0][1]==0
    assert jet_pair_entry(D,Q,J,(0,0),(1,0))==0

    ktotal=0
    strict=0
    sumq=F(0)
    loggain=0.
    used=0
    gauge=False
    blockrows=[]
    worst=0.
    for fib in groups:
        labels=[(r,s) for d in fib for r,s in fibers(R,S,d)]
        assert labels
        used+=len(labels)
        blockrows.append(len(labels))
        if len(fib)==4:
            a=sum(len(fibers(R,S,d)) for d in fib[:2])
            b=sum(len(fibers(R,S,d)) for d in fib[2:])
            G=gram(D,Q,J,labels)
            ki,yes,q,lg,_=witness_and_gain(D,Q,J,labels,a,b,G)
            ktotal+=ki
            strict+=int(yes)
            sumq+=q
            loggain+=lg
            worst=max(worst,lg)
            if yes and not gauge:
                moving_shear_control(G,a,b)
                gauge=True
        else:
            # Prior Phase206 leftover pair/singleton remains unchanged.
            sub=gram(D,Q,J,labels)
            assert det(sub)>0
    assert used==R*S
    assert gauge
    assert strict>0 and ktotal>0,("no new fixed quartet upper saving",D,strict,ktotal)
    assert loggain>0
    print("PHASE289_FOUR_FIBER_FISCHER",{
      "D":D,"rho":rho,"R":R,"S":S,"J":J,"Q":len(Q),
      "original_full_rows_covered":used,
      "parity_adjacent_old_pairs":expected["pairs"],
      "fixed_four_fiber_blocks":expected["four"],
      "strict_four_block_corrections":strict,
      "unchanged_leftover_two_fiber":expected["left_pairs"],
      "unchanged_leftover_single":expected["singles"],
      "largest_quartet_rows":max(blockrows),
      "total_exact_dyadic_log2_gain_lower":ktotal,
      "conservative_log_gain_bound":"K*ln(2)",
      "approx_extra_log_gain_not_a_certificate":round(loggain,9),
      "approx_extra_normalized":round(loggain/(R*R*S),10),
      "exact_fraction_correlation_witness_sum_positive":sumq>0,
      "exact_rational_moving_schur_frame":True,
      "no_local_Smith_or_field_bound_claim":True,
    },flush=True)
    return ktotal


def main():
    source_guard()
    K283=case(283)
    K403=case(403)
    assert K283>=1 and K403>=1
    print("PHASE289_FINITE_D403_NESTED_LOWER",{
      "prior_radial_to_pair_dyadic_log_gain_at_least":251,
      "new_pair_to_four_dyadic_log_gain_at_least":K403,
      "combined_radial_to_four_dyadic_log_gain_at_least":251+K403,
      "no_pair_gain_counted_twice":True,
      "finite_original_source_not_a_uniform_D_theorem":True
    },flush=True)
    print("PASS Phase289 exact original-source parity quartet Fischer upper",flush=True)


if __name__=="__main__":
    main()
