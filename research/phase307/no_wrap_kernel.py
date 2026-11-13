#!/usr/bin/env python3
"""Phase307-G: universal no-wrap regime for Frobenius-Hermite first-level weight.

Plain Fp polynomial arithmetic on the ORIGINAL rectangular monomial labels.
This is source algebra, NOT a uniform class-number-one field theorem.
"""
from pathlib import Path
import sys

ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/"research"/"phase305"))
from frobenius_hermite_rank import kernel_census, valuation_weight, monomial_remainders


def rank_modp(rows,p):
    pivots={}
    for raw in rows:
        x=[int(v)%p for v in raw]
        for col in sorted(pivots):
            v=x[col]
            if v:
                row=pivots[col]
                for t in range(col,len(x)):
                    x[t]=(x[t]-v*row[t])%p
        k=next((i for i,v in enumerate(x) if v),None)
        if k is not None:
            inv=pow(x[k],-1,p)
            pivots[k]=[v*inv%p for v in x]
    return len(pivots)


def no_wrap_certificate(R,S,p):
    if not (R>0 and S>0 and p>=2):
        raise ValueError("positive rectangle and p>=2 needed")
    j=min(S,p)  # ordinary derivatives, j>=p vanish mod p
    degree=p*p*j
    maxexp=R-1+p*(S-1)
    applicable=maxexp<degree
    row_labels={(r+p*s) for r in range(R) for s in range(S)}
    raw_rank=len(row_labels)
    w=valuation_weight(R,S,p)
    theoretical_h=(S-1)*max(R-p,0)
    expected_independent_rank=R*S-theoretical_h
    assert raw_rank==expected_independent_rank,(
        "monomial interval count identity failed",R,S,p)
    data={
        "R":R,"S":S,"p":p,"effective_ordinary_J":j,
        "quotient_degree":degree,"source_max_degree":maxexp,
        "no_wrap_applicable":applicable,"raw_monomial_span_rank":raw_rank,
        "existing_valuationWeight":w
    }
    if applicable:
        exact=kernel_census(R,S,S,p)
        assert exact["image_rank"]==raw_rank
        assert exact["kernel_dimension"]==theoretical_h
        assert theoretical_h<=w
        data.update({
            "proved_interval_kernel":theoretical_h,
            "exact_modular_kernel":exact["kernel_dimension"],
            "first_level_gain_not_positive":True
        })
    return data


def first_crossing_p5_s2():
    p,S=5,2
    left=no_wrap_certificate(45,S,p)
    right=no_wrap_certificate(46,S,p)
    assert left["no_wrap_applicable"] and not right["no_wrap_applicable"]
    assert left["source_max_degree"]==49
    assert right["source_max_degree"]==50
    assert right["quotient_degree"]==50
    # Independent second row-reduction, not a string copy of rank output.
    def independent_quotient_rank(R):
        maxexp=R-1+p*(S-1)
        vec=monomial_remainders(p,S,maxexp)
        return rank_modp((vec[r+p*s] for r in range(R) for s in range(S)),p)
    lrank=independent_quotient_rank(45)
    rrank=independent_quotient_rank(46)
    assert (lrank,rrank)==(50,50)
    assert kernel_census(45,2,2,5)["kernel_dimension"]==40
    assert kernel_census(46,2,2,5)["kernel_dimension"]==42
    assert (valuation_weight(45,2,5),valuation_weight(46,2,5))==(40,41)
    return {
      "p":5,"S_J":2,
      "no_wrap_last_R":45,"first_wrap_R":46,
      "R45_first_level_h_vs_existing_w":[40,40],
      "R46_first_level_h_vs_existing_w":[42,41],
      "R46_exact_positive_first_level_gain":1,
      "monomial_remainder_rank_same_before_after":[lrank,rrank],
      "this_is_an_abstract_rectangle_not_native_R_for_D203":True,
      "no_uniform_class_one_bound":True
    }


def main():
    controls=[
        (30,2,11),
        (30,3,7),
        (5,2,3),
        (45,2,5),
        (7,3,11),
        (55,2,17),
        (35,4,13),
    ]
    out=[no_wrap_certificate(*t) for t in controls]
    assert all(x["no_wrap_applicable"] and x["first_level_gain_not_positive"]
               for x in out),out
    boundary=first_crossing_p5_s2()
    print("PHASE307_NO_WRAP_KERNEL_THEOREM_CONTROLS_PASS",{
       "no_wrap_parameter_controls":out,
       "sharp_first_wrapping_boundary":boundary,
       "method":"independent monomial interval count and modular quotient ranks",
       "scope":"source level only, not a new field bound"
    },flush=True)


if __name__=="__main__":
    main()
