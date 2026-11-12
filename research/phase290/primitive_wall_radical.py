#!/usr/bin/env python3
"""Phase290-B: separate modular radical lift and exact wall determinant polynomial.

Preregistered AFTER Phase290-A results at d9421fe, BEFORE this script.
The chosen six original D563 rows, jets, metric and wall never change.
"""
from itertools import permutations
from noether_smith_wall import (
    D, LABELS, guard, params, gram, det, eval_ordinary,
    gram_direct, plus, v_p
)

def rref(A,b,p):
    n=len(A)
    M=[[v%p for v in A[i]]+[b[i]%p] for i in range(n)]
    pivots=[]
    rank=0
    for col in range(n):
        pivot=next((i for i in range(rank,n) if M[i][col]),None)
        if pivot is None:
            continue
        M[rank],M[pivot]=M[pivot],M[rank]
        t=pow(M[rank][col],-1,p)
        M[rank]=[(t*v)%p for v in M[rank]]
        for i in range(n):
            if i!=rank and M[i][col]:
                c=M[i][col]
                M[i]=[(x-c*y)%p for x,y in zip(M[i],M[rank])]
        pivots.append(col)
        rank+=1
        if rank==n:
            break
    consistent=not any(
        all(M[i][j]==0 for j in range(n)) and M[i][-1]!=0
        for i in range(n)
    )
    return M,pivots,consistent

def solve(A,b,p):
    M,pivots,okay=rref(A,b,p)
    if not okay:return None
    sol=[0]*len(A)
    for row,col in enumerate(pivots):
        sol[col]=M[row][-1]
    assert all(sum(A[i][j]*sol[j] for j in range(len(A)))%p==b[i]%p
               for i in range(len(A)))
    return sol

def primitive_kernel(A,p):
    M,pivots,okay=rref(A,[0]*len(A),p)
    assert okay and len(pivots)==len(A)-1
    free=[j for j in range(len(A)) if j not in pivots]
    assert len(free)==1
    v=[0]*len(A);v[free[0]]=1
    for row,col in enumerate(pivots):
        v[col]=(-M[row][free[0]])%p
    assert any(v) and all(sum(a*b for a,b in zip(row,v))%p==0 for row in A)
    return v

def multiply(A,v):
    return [sum(a*b for a,b in zip(row,v)) for row in A]

def test_lifts(A,p):
    v=primitive_kernel(A,p)
    parity=[(-1)**(r+s) for r,s in LABELS]
    support={parity[i] for i,x in enumerate(v) if x%p}
    assert len(support)==1
    outcomes=[]
    for k in (1,2):
        Gv=multiply(A,v)
        denom=p**k
        assert all(x%denom==0 for x in Gv),("input not a kernel at depth",p,k)
        rhs=[(-x//denom)%p for x in Gv]
        w=solve(A,rhs,p)
        if w is None:
            left_obstruction=sum(a*b for a,b in zip(primitive_kernel(A,p),rhs))%p
            assert left_obstruction!=0,("missing left-radical obstruction",p,k)
            outcomes.append({"from_power":k,"lift_exists":False,
                             "left_radical_obstruction_mod_p":left_obstruction})
            break
        v=[x+denom*y for x,y in zip(v,w)]
        assert all(x%(denom*p)==0 for x in multiply(A,v))
        outcomes.append({"from_power":k,"lift_exists":True})
    if p==5:
        assert [x["lift_exists"] for x in outcomes]==[True,False]
    elif p==7:
        assert [x["lift_exists"] for x in outcomes]==[False]
    else:
        raise AssertionError("unsupported frozen radical prime")
    return {"initial_primitive_kernel":primitive_kernel(A,p),
            "kernel_parity":next(iter(support)),
            "lifts":outcomes}

def det_poly(A,B):
    """Leibniz expansion in Z[t], independent of numeric determinant calls."""
    n=len(A);assert n==len(B)==6
    out=[0]*(n+1)
    for perm in permutations(range(n)):
        inversions=sum(perm[i]>perm[j] for i in range(n) for j in range(i+1,n))
        sign=-1 if inversions%2 else 1
        row=[1]
        for i,j in enumerate(perm):
            new=[0]*(len(row)+1)
            for k,a in enumerate(row):
                new[k]+=a*A[i][j]
                new[k+1]+=a*B[i][j]
            row=new
        for k,a in enumerate(row):
            out[k]+=sign*a
    return out

def evaluate(coeff,t):
    val=0
    for c in coeff[::-1]:
        val=val*t+c
    return val

def derivative(coeff,t):
    return sum(k*coeff[k]*(t**(k-1)) for k in range(1,len(coeff)))

def main():
    guard()
    rho,R,S,J,Q=params(D)
    assert (rho,R,S,J,len(Q))==(51,140,5,5,359)
    inner=[z for z in Q if abs(z[1])<=1]
    extra=[z for z in Q if abs(z[1])==2]
    assert len(inner)==285 and len(extra)==74
    G0=gram(D,inner,J,LABELS)
    G1=gram(D,Q,J,LABELS)
    Delta=gram(D,extra,J,LABELS)
    assert plus(G0,Delta)==G1
    assert G0==gram_direct(*eval_ordinary(inner,J))
    assert G1==gram_direct(*eval_ordinary(Q,J))
    for p in (5,7):
        assert len(rref(G0,[0]*6,p)[1])==6
        assert len(rref(G1,[0]*6,p)[1])==5
    assert v_p(det(G1),5)==2
    assert v_p(det(G1),7)==1

    depths={str(p):test_lifts(G1,p) for p in (5,7)}
    coeff=det_poly(G0,Delta)
    assert len(coeff)==7
    assert evaluate(coeff,0)==det(G0)
    assert evaluate(coeff,1)==det(G1)
    for t in (2,-1):
        actual=[[G0[i][j]+t*Delta[i][j] for j in range(6)]
                for i in range(6)]
        assert evaluate(coeff,t)==det(actual)
    parity=[(-1)**(r+s) for r,s in LABELS]
    assert all(A[i][j]==0
       for A in (G0,Delta) for i in range(6) for j in range(6)
       if parity[i]!=parity[j])

    roots={}
    for p in (3,5,7):
        rootdata=[(t,derivative(coeff,t)%p)
                  for t in range(p) if evaluate(coeff,t)%p==0]
        roots[str(p)]=rootdata
    assert any(t==1 for t,_ in roots["5"])
    assert any(t==1 for t,_ in roots["7"])
    assert all(t!=0 for t,_ in roots["5"])
    assert all(t!=0 for t,_ in roots["7"])

    print("PHASE290B_PRIMITIVE_RADICAL",{
      "D":D,"source_Q_inner":len(inner),"source_Q_full":len(Q),
      "rows_checked":6,"ordinary_jet_orders":list(range(J)),
      "modular_depth_lifting":depths,
      "determinant_wall_polynomial_degree":next((k for k in range(6,-1,-1) if coeff[k]),0),
      "formal_wall_parameter_roots_and_derivatives_mod_p":roots,
      "polynomial_direct_det_controls":[-1,0,1,2],
      "same_original_gram_and_no_prime_double_counting":True,
      "not_continuous_integer_gauge_or_new_field_bound":True
    },flush=True)
    print("PASS Phase290-B prime-local radical depth and exact determinant wall polynomial",flush=True)

if __name__=="__main__":
    main()
