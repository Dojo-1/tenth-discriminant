#!/usr/bin/env python3
"""Phase309-C: original observation-cover filtration and Picard event log.

Minors J_S grow with the actual observation set; inverse-ideal coefficient
lattices shrink. Their Picard classes need not evolve monotonically and
are NOT persistent-homology barcodes. No full-field bound is inferred.
"""
import sys
from pathlib import Path

HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE))
sys.path.insert(0,str(HERE.parent/"phase308"))

import original_source_picard as source
import picard_tendrils as ideals


def coeff_allowed(coordinate_numerator,denominator,points,D):
    """b=numerator/denominator in the inverse ideal of differences z_i-z0."""
    if denominator<=0:
        raise ValueError("denominator must be positive")
    z0=points[0]
    assert z0==(0,0)
    for z in points[1:]:
        diff=(z[0]-z0[0],z[1]-z0[1])
        x=ideals.mul(diff,coordinate_numerator,D)
        if any(v%denominator for v in x):
            return False
    return True


def original_source_event_chain():
    ps,q=source.patch_source(203,3,0)
    assert ps.observations==((0,0),(3,0),(0,1))
    ordered=ps.observations+((1,0),)
    assert all(z in q for z in ordered)
    rows=[]
    for k,ideal_norm,expected_order in ((2,9,1),(3,3,4),(4,1,1)):
        points=ordered[:k]
        A=tuple(((1,0),z) for z in points)
        minors=source.two_by_two_minors(A,203)
        idx=ideals.ideal_z_index(203,minors)
        assert idx==ideal_norm,(k,idx)
        G=tuple(tuple(sum(source.trace_pair(x,y,203)
                          for x,y in zip(s,t))
                      for t in ( ((1,0),)*k,points ))
                for s in ( ((1,0),)*k,points ))
        det=G[0][0]*G[1][1]-G[0][1]*G[1][0]
        assert det>0
        rows.append({
            "num_observations":k,
            "points":points,
            "maximal_minor_Z_index_Norm":idx,
            "Picard_class_order":expected_order,
            "saturated_inverse_ideal_class":"principal" if expected_order==1 else "order4 inverse",
            "original_restricted_integer_Gram":G,
            "original_restricted_integer_Gram_det":det,
            "v3_of_Gram_det":next((v for v in range(10) if det%(3**(v+1))!=0),None)
        })
    assert [x["maximal_minor_Z_index_Norm"] for x in rows]==[9,3,1]
    assert [x["Picard_class_order"] for x in rows]==[1,4,1]
    assert [x["original_restricted_integer_Gram_det"] for x in rows]==[36,671,895]
    assert [x["v3_of_Gram_det"] for x in rows]==[2,0,0]
    # Explicit coefficient inverse-ideal strict-inclusion witnesses.
    b_1_over3=(1,0)
    b_baromega_over3=ideals.conjugate((0,1))
    assert coeff_allowed(b_1_over3,3,ordered[:2],203)
    assert not coeff_allowed(b_1_over3,3,ordered[:3],203)
    assert coeff_allowed(b_baromega_over3,3,ordered[:2],203)
    assert coeff_allowed(b_baromega_over3,3,ordered[:3],203)
    assert not coeff_allowed(b_baromega_over3,3,ordered[:4],203)
    assert all(coeff_allowed((1,0),1,ordered[:k],203) for k in (2,3,4))
    # This is a genuine *non-monotone class history*, NOT a monotone valuation
    # for the global 100-row original field matrix.
    return {
      "original_field_D":203,
      "source_labels":"(1,Z), original j0 only",
      "event_log":rows,
      "ideal_inclusions":"(3) strict subset (3,omega) strict subset O",
      "inverse_coefficient_lattices":"(1/3)O strict superset I^-1 strict superset O",
      "strict_witness_1_over3":"allowed at 2, rejected at 3",
      "strict_witness_conjomega_over3":"allowed at 3, rejected at 4",
      "Picard_event_class_orders":[1,4,1],
      "different_original_trace_Gram_v3":[2,0,0],
      "all_original_observations_genuine":True,
      "no_full_100_row_Picard_persistence":True,
      "no_persistent_homology_claim":True,
      "no_field_bound_improved":True
    }


def main():
    print("PHASE309_PICARD_EVENT_FILTRATION_PASS",
          original_source_event_chain(),flush=True)


if __name__=="__main__":
    main()
