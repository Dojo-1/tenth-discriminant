#!/usr/bin/env python3
"""T7 exact, preregistered: original D19 ordinary-jet Gram, R=4 S=J=4.

Checks 3 universal Frobenius kernel vectors and one independent
residue-balanced horizontal-fiber vector at radius6. No substitute Gram,
floating point, external numerical packages or uniform discriminant claims.
"""
import json
from pathlib import Path
import sys

src=Path(__file__).resolve().parents[1]/"plural_moving_frames"
sys.path.insert(0,str(src))
from original_source_small_pilot import ordinary_jet,ellipse,determinant,D
from source_kernel_certificate import rref, outside_kernel

R,S,J,p=4,4,4,3
n=R*S


def gram_parameterized(Q):
    rows=[(r,s) for r in range(R) for s in range(S)]
    out=[[0]*n for _ in range(n)]
    for point in Q:
        for j in range(J):
            v=[ordinary_jet(point,r,s,j) for r,s in rows]
            for i in range(n):
                for h in range(i,n):
                    out[i][h]+=2*(v[i][0]*v[h][0]+D*v[i][1]*v[h][1])
    for i in range(n):
        for h in range(i):
            out[i][h]=out[h][i]
    return out


def unit_row(r,s):
    u=[0]*n
    u[r*S+s]=1
    return u


def test_T7():
    assert D==19
    u=[]
    for s in range(3):
        w=unit_row(3,s)
        w[s+1]=2
        u.append(w)
    v=unit_row(3,2)
    v[1]=2
    assert v!=u[2]
    vectors=u+[v]
    _,pivots=rref(vectors,p)
    assert len(pivots)==4, ("independence",pivots)
    Q6=ellipse(6)
    Q7=ellipse(7)
    assert len(Q6)==31 and len(Q7)==37
    G6=gram_parameterized(Q6)
    G7=gram_parameterized(Q7)
    # T8: compare, for diagnosis only, to the original Gram restricted to
    # y=0 observations. This is not an alternate production determinant.
    Axis6=gram_parameterized([point for point in Q6 if point[1]==0])
    Axis7=gram_parameterized([point for point in Q7 if point[1]==0])
    assert all((G6[i][j]-Axis6[i][j])%p==0
               for i in range(n) for j in range(n))
    assert G6[0][0]-Axis6[0][0]==36
    assert G7[0][0]-Axis7[0][0]==44
    assert (G7[0][0]-Axis7[0][0])%p==2
    _,axis6piv=rref(Axis6,p)
    assert len(axis6piv)==9
    assert determinant(G6)>0 and determinant(G7)>0
    for name,G in (("rho6",G6),("rho7",G7)):
        for s,w in enumerate(u):
            assert outside_kernel(G,w,p)==[0]*n, (name,s)
    assert outside_kernel(G6,v,p)==[0]*n
    g7v=outside_kernel(G7,v,p)
    assert g7v[1]==2
    _,piv6=rref(G6,p)
    _,piv7=rref(G7,p)
    assert len(piv6)<=12, len(piv6)
    assert len(piv7)<=13, len(piv7)
    return {
        "parameter":{"D":D,"R":R,"S":S,"J":J,"p":p},
        "support_counts":{"rho6":len(Q6),"rho7":len(Q7)},
        "universal_Frobenius_vectors":u,
        "extra_residue_fiber_vector":v,
        "independent_kernel_vectors_rho6":4,
        "rank_mod3":{"rho6":len(piv6),"rho7":len(piv7)},
        "rho7_extra_vector_component_0_1":g7v[1],
        "real_determinants_positive":True,
        "T8": {"mod3_full_equals_axis_at_radius6":True,
               "rank_mod3_axis_radius6":len(axis6piv),
               "entry_0_0_nonreal_delta": {"radius6":36,"radius7":44},
               "mod3_full_differs_from_axis_at_radius7":True}
    }


if __name__=="__main__":
    print(json.dumps(test_T7(),indent=2))
    print("ROUND201_T7_EXTENDED_SOURCE_PASS")
