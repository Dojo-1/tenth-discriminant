#!/usr/bin/env python3
"""Phase294: exact 40-dimensional boundary jet module of original Q383.

Pre-registered at 820ceb61 BEFORE code and CI. This is ONLY the RAW
original 725-row Gram support defect modulo 5. Never promote its rank
to a primitive pairing valuation or to an actual-field theorem.
"""
from collections import Counter
from pathlib import Path
import subprocess
import sys

ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/"research"/"phase206"))
from source_probe import params,gram,mul,fall,rank_mod

P=5
D=583
R,S,J=145,5,5
FROZEN={
    "research/phase206/source_probe.py":
        "3f954b59d9f86b06ad53667c869b5b24f2e6c7f6",
    "research/phase204/ordinary_jet_filtration.py":
        "dd8b00547ec09a5d9baec15ad34c9ee3e6e4f6b8",
    "research/phase293/moment_transport_remainder.py":
        "a114b5b7744ed67254caa98ef91c7f11d016d80a",
}
ORIGINAL_LABELS=((0,0),(1,0),(2,0),(1,1),(4,0),(4,1))
REPS=((2,1),(2,2),(3,1),(3,2))

def guard():
    for path,sha in FROZEN.items():
        current=subprocess.check_output(
            ["git","rev-parse","HEAD:"+path],cwd=ROOT,text=True
        ).strip()
        assert current==sha,("original helper drift",path,current,sha)

def measure(Q,alpha):
    return Counter((x%P,(alpha*y)%P) for x,y in Q)

def difference_measure(a,b):
    return Counter({x:a[x]-b[x] for x in a.keys()|b.keys()
                    if a[x]!=b[x]})

def signed_support(Q):
    before=measure(Q,1)
    after=measure(Q,2)
    difference=difference_measure(after,before)
    assert sum(difference.values())==0
    mass=sum(abs(t) for t in difference.values())//2
    assert mass==104
    assert len(difference)==20
    for x in range(P):
        expected=11 if x in (2,3) else 10
        for y in (1,2,3,4):
            sign=1 if y in (2,3) else -1
            assert difference[x,y]==sign*expected
            assert difference[x,y]==difference[x,(-y)%P]
            assert difference[x,y]==difference[(-x)%P,(-y)%P]
        assert difference[x,0]==0
    active={(x,y):d%P for (x,y),d in difference.items() if d%P}
    assert len(active)==8
    assert set(active)=={(x,y) for x in (2,3) for y in (1,2,3,4)}
    assert len({min((x,y),(x,(-y)%P))
                for x,y in active})==4
    assert tuple(sorted(REPS))==tuple(sorted(
        {min((x,y),(x,(-y)%P)) for x,y in active}))
    assert measure(Q,-2)==after
    return difference,active,mass

def powers(z,lim):
    out=[(1,0)]
    for k in range(lim):
        out.append(mul(out[-1],z,D,P))
    return out

def residue_eval_matrix():
    """ALL original 725 rows, 4 Frobenius orbits x 5 j x 2 channels."""
    cache={}
    for q in REPS:
        a,b=q
        z=(a%P,b%P)
        w=(a%P,(-b)%P)
        zz=powers(z,R-1)
        ww=powers(w,S-1)
        assert zz[P]==w,("Frobenius z^5=conjugate z failed",q)
        cache[q]=(zz,ww)
    E=[]
    for r in range(R):
        for s in range(S):
            row=[]
            for q in REPS:
                zz,ww=cache[q]
                for j in range(J):
                    if j>r:
                        row.extend((0,0))
                    else:
                        u,v=mul(zz[r-j],ww[s],D,P)
                        coef=fall(r,j)%P
                        row.extend(((coef*u)%P,(coef*v)%P))
            assert len(row)==40
            E.append(row)
    assert len(E)==R*S
    return E

def signed_metric(active):
    """Original B=diag(2,2D), both conjugates -> 4*delta*diag(1,D)."""
    weights=[]
    for x,y in REPS:
        delta=active[x,y]
        assert delta%P in (1,P-1)
        for j in range(J):
            weights.extend(((4*delta)%P,(4*delta*D)%P))
    assert len(weights)==40 and all(v%P for v in weights)
    return weights

def factor_gram(E,W,idx):
    return [[sum(E[i][k]*W[k]*E[j][k] for k in range(40))%P
             for j in idx] for i in idx]

def same_mod(A,B):
    return all((int(u)-int(v))%P==0
        for row1,row2 in zip(A,B) for u,v in zip(row1,row2))

def moment_oracle(E,W,Q):
    labels=ORIGINAL_LABELS
    idx=[r*S+s for r,s in labels]
    calculated=factor_gram(E,W,idx)
    old=gram(D,Q,J,labels)
    moved=gram(D,[(x,2*y) for x,y in Q],J,labels)
    other=gram(587,Q,J,labels)
    delta1=[[u-v for u,v in zip(a,b)] for a,b in zip(moved,old)]
    delta2=[[u-v for u,v in zip(a,b)] for a,b in zip(other,old)]
    assert same_mod(calculated,delta1) and same_mod(calculated,delta2)
    assert rank_mod(calculated,P)==5
    # A second, hostile high-r comparison catches source coverage gaps.
    high=((0,0),(39,0),(70,1),(144,4))
    ids=[r*S+s for r,s in high]
    finite=factor_gram(E,W,ids)
    a=gram(587,Q,J,high)
    b=gram(D,Q,J,high)
    assert same_mod(finite,[[u-v for u,v in zip(x,y)]
                            for x,y in zip(a,b)])
    return {"original_phase293_six_row_defect_rank":5,
            "independent_exact_Gram_oracle_rows":len(labels)+len(high),
            "independent_original_jets_all_orders":J}

def hermite_certificate(E,W):
    # Polynomials Z^0,...,Z^39 are all ORIGINAL rows with s=0.
    ids=[r*S for r in range(40)]
    square=[E[i] for i in ids]
    assert rank_mod(square,P)==40
    H=factor_gram(E,W,ids)
    assert rank_mod(H,P)==40
    # Four DISTINCT irreducible quadratic Frobenius minimal
    # polynomials, each jet ideal to exponent5: CRT degree40.
    quadratics=[]
    residues={x*x%P for x in range(P)}
    for x,y in REPS:
        c=(-2*x)%P
        d=(x*x+D*y*y)%P
        discr=(c*c-4*d)%P
        assert discr not in residues
        quadratics.append((c,d))
    assert len(set(quadratics))==4
    assert 4*2*J==40 and J==P
    ev=[i for i in ids if ((i//S)+(i%S))%2==0]
    od=[i for i in ids if ((i//S)+(i%S))%2==1]
    assert len(ev)==len(od)==20
    HE=factor_gram(E,W,ev)
    HO=factor_gram(E,W,od)
    HC=[[H[ids.index(i)][ids.index(j)] for j in od] for i in ev]
    assert all(v==0 for row in HC for v in row)
    assert rank_mod(HE,P)==rank_mod(HO,P)==20
    even=[E[r*S+s] for r in range(R) for s in range(S)
          if (r+s)%2==0]
    odd=[E[r*S+s] for r in range(R) for s in range(S)
         if (r+s)%2==1]
    assert rank_mod(E,P)==40
    assert rank_mod(even,P)==20 and rank_mod(odd,P)==20
    return {"full_original_725_raw_Gram_defect_rank_mod5":40,
            "original_even_raw_defect_rank":20,
            "original_odd_raw_defect_rank":20,
            "first40_original_Z_rows_Hermite_minor_is_unit":True,
            "four_distinct_irreducible_quadratics_mod5":quadratics,
            "Frobenius_orbit_count":4,
            "original_jets_per_orbit":J,
            "no_cross_parity_Gram_defect":True}

def hostile_controls(Q):
    # No moving frame = no signed boundary.
    assert not difference_measure(measure(Q,1),measure(Q,1))
    # Phi and -Phi have equal transported multiplicities by the
    # original conjugation-invariant point source.
    assert measure(Q,2)==measure(Q,-2)
    # Equal transverse widths make the residue-support measure invariant.
    rect=[(x,y) for y in range(-2,3) for x in range(-21,22)]
    assert len(rect)==215
    assert not difference_measure(measure(rect,2),measure(rect,1))
    # One Frobenius conjugate pair, one jet (J1), Z^0,Z^1:
    # the metric 4 diag(1,D) is invertible and evaluation rank2.
    q=(1,1)
    toy=[[1,0],[q[0]%P,q[1]%P]]
    assert rank_mod(toy,P)==2
    toyH=[[
        sum(toy[i][k]*w*toy[j][k] for k,w in
            enumerate((4%P,(4*D)%P)))%P
        for j in range(2)] for i in range(2)]
    assert rank_mod(toyH,P)==2
    assert rank_mod(toy[:1],P)==1
    # Ordinary derivative orders j >= p are zero in characteristic p:
    # our Hermite rank lemma explicitly assumes J<=p.
    assert all(fall(r,P)%P==0 for r in range(P,60))
    # Raw congruence modp can be lost after an index-p division:
    # 5==10 mod5, but 5/5=1 vs 10/5=2 mod5.
    assert 5%P==10%P and (5//P)%P!=(10//P)%P
    return {"alpha_identity_no_boundary":True,
            "alpha_sign_conjugation_control":True,
            "equal_width_rectangle_no_boundary":True,
            "single_orbit_J1_trace_pairing_rank2":True,
            "ordinary_jets_J_gt_p_not_allowed":True,
            "raw_modp_does_not_transport_through_division_by_p":True}

def main():
    guard()
    rho,R0,S0,J0,Q=params(D)
    rho2,R2,S2,J2,Q2=params(587)
    assert (rho,R0,S0,J0,len(Q))==(53,R,S,J,383)
    assert (rho2,R2,S2,J2,len(Q2))==(53,146,5,5,383)
    assert Q==Q2
    delta,active,mass=signed_support(Q)
    E=residue_eval_matrix()
    W=signed_metric(active)
    hermite=hermite_certificate(E,W)
    old=moment_oracle(E,W,Q)
    controls=hostile_controls(Q)
    print("PHASE294_RESIDUE_BOUNDARY_MODULE",{
        "source_full_original_D583_rows":R*S,
        "source_original_D587_first725_DIAGNOSTIC":True,
        "source_original_Q_points":len(Q),
        "source_modulus":P,"ordinary_J":J,
        "integer_residue_support_transport_mass":mass,
        "integer_signed_residue_counts":sorted(
            [[x,y,weight] for (x,y),weight in delta.items()]),
        "active_nonzero_signed_residue_count_mod5":len(active),
        "transverse_frobenius_orbits":[list(q) for q in REPS],
        "original_trace_B583_residue_metric_units":True,
        "carrier_dim_over_F5":len(W),
        "rank_and_parity":hermite,
        "independent_source_oracles":old,
        "hostile_matched_controls":controls,
        "raw_support_defect_is_NOT_primitive_Gram_valuation":True,
        "no_uniform_D_class_one_or_discriminant_cutoff_claim":True,
    },flush=True)
    print("PASS Phase294 signed four-orbit Frobenius jet boundary rank40",flush=True)

if __name__=="__main__":
    main()
