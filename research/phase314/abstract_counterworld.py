#!/usr/bin/env python3
"""Phase314-C: restricted ABSTRACT counterworld to an invalid inference.

Two ray-spectrum assignments on the four shells {1,9,49,441} have
identical ACTUAL D163 zeroth ideal counts (1 each) and satisfy every
coprime convolution law INTERNAL to those four shells. Keep correct
conductor2 and signed tame classes. Perturb a single WILD coordinate
at norm9, then transport it multiplicatively to norm441; quadratic
moments and original Gram contributions change.

The mutated spectra are ABSTRACT monoid representations, not a real
Q(sqrt(-163)) ray-class distribution. Actual element arithmetic at 3
fixes the true delta(3); the alternate assignment violates that extra
number-field datum. Thus only the implication from "zeroth ideal counts
and coprime shell convolution" to "forced wild quadratic moments" fails;
this does NOT disprove richer class-number-one+arithmetic constraints.
"""
from collections import Counter

from pathlib import Path
import sys
import numpy as np

ROOT=Path(__file__).resolve().parents[2]
for p in ("phase312","phase313","phase314"):
    sys.path.insert(0,str(ROOT/"research"/p))
from conductor2_order_gate import ray50_tag,ray50_product
from norm_shell_bridge import all_ideal_count_at_norm
from truncated_ray_convolution import direct_jet50,moment_convolution50
from wild_quadratic_gram import direct_unit_Gram

D=163
NORM_SHELLS=(1,9,49,441)


def abstract_counterworld():
    actual={
        1:ray50_tag((1,0)),
        9:ray50_tag((3,0)),
        49:ray50_tag((7,0)),
        441:ray50_tag((21,0)),
    }
    assert ray50_product(actual[9],actual[49])==actual[441]
    assert all(all_ideal_count_at_norm(D,n)==1 for n in NORM_SHELLS)
    pert=dict(actual)
    r2,(c,(x,y))=pert[9]
    pert[9]=(r2,(c,((x+1)%5,y)))
    pert[441]=ray50_product(pert[9],pert[49])
    assert pert[9]!=actual[9] and pert[441]!=actual[441]
    assert pert[9][0]==actual[9][0]
    assert pert[9][1][0]==actual[9][1][0]

    results=[]
    for name,world in (("real_element_tags",actual),
                       ("ABSTRACT_changed_wild_only",pert)):
        spectra={n:Counter({world[n]:1}) for n in NORM_SHELLS}
        jets={n:direct_jet50(spectra[n]) for n in NORM_SHELLS}
        for n in NORM_SHELLS:
            assert sum(spectra[n].values())==all_ideal_count_at_norm(D,n)
            assert moment_convolution50(jets[1],jets[n])==jets[n]
        assert moment_convolution50(jets[9],jets[49])==jets[441]
        results.append({
            "model":name,
            "correct_zeroth_ideal_counts_for_each_frozen_shell":True,
            "all_coprime_convolution_relations_internal_to_four_shells":True,
            "norm9_wild":world[9][1][1],
            "norm441_wild":world[441][1][1],
        })
    c=actual[9][1][0]
    one=direct_unit_Gram(D,c,actual[9][1][1])
    two=direct_unit_Gram(D,c,pert[9][1][1])
    assert one.shape==two.shape==(40,40)
    diff=(two-one)%5
    assert np.any(diff),(
        "two abstract ray worlds differ but original source Gram blind to shift")
    i,j=np.argwhere(diff)[0]
    return {
        "D":D,"frozen_formal_shell_norms":NORM_SHELLS,
        "two_models":results,
        "both_preserve_conductor2_and_tame_residues":True,
        "both_preserve_actual_zeroth_ideal_counts_ON_THE_FOUR_SHELLS":True,
        "full_coprime_convolution_constraints_for_all_other_shells_NOT_claimed":True,
        "different_wild_second_jet_or_first_jet":True,
        "different_original_primitive_Gram_entry":{
            "row_i":int(i),"row_j":int(j),
            "difference_mod5":int(diff[i,j])
        },
        "alternate_wild_assignments_not_realizable_as_actual_D163_elements":True,
        "conv_plus_totals_alone_cannot_force_a_wild_Gram_value":True,
        "extra_number_field_residue_reciprocity_constraints_still_required":True,
        "does_not_refute_uniform_h1_discriminant_theorem":True,
    }


def main():
    print("PHASE314_ABSTRACT_WILD_CONVOLUTION_COUNTERWORLD_PASS",
          abstract_counterworld(),flush=True)


if __name__=="__main__":
    main()
