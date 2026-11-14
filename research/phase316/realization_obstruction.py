#!/usr/bin/env python3
"""Phase316-C: first exact GLOBAL realization obstruction, n=164.

Synthetic wild gauge tags preserve full ideal convolution, local norm
mod125, conjugation and original suborder conductor2 selection; they
are nevertheless not ray tags of actual integer solutions to
x²+163y²=164. The exact norm164 fibre in the native original order
contains only (±1,±1), i.e. 2omega and 2baromega modulo units +/-1.

This identifies a precise missing arithmetical *global section*
condition, NOT a new field and NOT a uniform Gram determinant bound.
"""
from collections import Counter,defaultdict
from math import gcd
from pathlib import Path
import sys

import numpy as np

ROOT=Path(__file__).resolve().parents[2]
for folder in ("phase206","phase311","phase312","phase313",
               "phase314","phase315","phase316"):
    sys.path.insert(0,str(ROOT/"research"/folder))
from wild_log125 import signed_ray125_tag,exhaustive_lift_table,norm,is_unit
from wild_gauge import antisymmetric_valuation,shifted_ray_tag
from conductor250_original_mod25 import (
    original_integer_source_oracle,gram_from_unit_rays_and_nonunit_lifts,
    unit_and_nonunit_counts
)
from ray_to_original_gram import embed_integer_pair_to_omega

D=163
MOD=25
TOP=125


def signed_ideal_spectra_for_original_source(Qint):
    actual=defaultdict(Counter)
    synthetic=defaultdict(Counter)
    seen=set(Qint)
    recorded={}
    for z in Qint:
        if z==(0,0):
            continue
        neg=(-z[0],-z[1])
        assert neg in seen
        if z>neg:
            continue
        x,y=z
        n=x*x+D*y*y
        omega=embed_integer_pair_to_omega(z)
        if not is_unit(omega,D):
            continue
        a=signed_ray125_tag(omega,D)
        b=shifted_ray_tag(omega)
        assert a==signed_ray125_tag((-omega[0],-omega[1]),D)
        assert b==shifted_ray_tag((-omega[0],-omega[1]))
        actual[n][a]+=1
        synthetic[n][b]+=1
        recorded[z]=(n,a,b,antisymmetric_valuation(omega))
    return actual,synthetic,recorded


def flatten_counts(spectra):
    counts=Counter()
    for n,C in spectra.items():
        counts.update(C)
    return counts


def gram_for_unit_histogram(C,lookup):
    return gram_from_unit_rays_and_nonunit_lifts(C,Counter(),lookup)


def first_global_realization_obstruction():
    Qint,Qomega,Gnative,source=original_integer_source_oracle()
    assert len(Qint)==109
    actual,synthetic,recorded=signed_ideal_spectra_for_original_source(Qint)
    unit,nonunit=unit_and_nonunit_counts(Qomega)
    assert flatten_counts(actual)==unit
    assert sum(nonunit.values())==9
    changed_norms=sorted(
        n for n in set(actual)|set(synthetic)
        if actual[n]!=synthetic[n])
    assert changed_norms and changed_norms[0]==164,(
        "first actual integer-order norm obstruction not 164",changed_norms)

    # A completely independent exact equation solver:
    # y²<=164/163<2, hence y∈{-1,0,1}; for y=0,164 is
    # nonsquare; for y=±1, x²=1.
    fibre=[
        (x,y) for y in range(-1,2) for x in range(-13,14)
        if x*x+D*y*y==164
    ]
    assert set(fibre)=={(-1,-1),(-1,1),(1,-1),(1,1)}
    source_fibre=[z for z in Qint if z[0]*z[0]+D*z[1]*z[1]==164]
    assert set(source_fibre)==set(fibre)

    expected_real_tags={
        signed_ray125_tag(embed_integer_pair_to_omega(z),D)
        for z in fibre
    }
    assert len(expected_real_tags)==2
    assert set(actual[164])==expected_real_tags
    assert sum(actual[164].values())==2
    assert sum(synthetic[164].values())==2
    assert set(synthetic[164]).isdisjoint(expected_real_tags),(
        "synthetic norm164 class accidentally realized by a global generator")

    # Every synthetic local class HAS a residue representative modulo125
    # with EXACTLY the right local norm, and a compatible even-coordinate
    # lift modulo2 because 125 is odd. Nonetheless no actual original
    # integral norm164 solution gives that ray class.
    lookup,meta=exhaustive_lift_table(D)
    unrealizable=[]
    for tag in sorted(synthetic[164]):
        z125=lookup[tag]
        assert norm(z125,D,TOP)==164%TOP
        # Choose an integer lift congruent to z125 mod125 and divisible
        # by2 in BOTH omega coordinates, enforcing inert2 suborder gate.
        z250=tuple(x+125*(x%2) for x in z125)
        assert all(x%2==0 for x in z250)
        assert norm(z250,D,TOP)==164%TOP
        assert signed_ray125_tag(z250,D)==tag
        assert tag not in expected_real_tags
        unrealizable.append({
            "signed_tame_class":tag[0],
            "second_wild_log":tag[1],
            "local_residue_mod125":z125,
            "conductor2_even_coordinate_integral_lift":z250,
            "local_norm_mod125":norm(z125,D,TOP),
            "actual_exact_norm164_integer_generator_exists":False,
        })
    assert len(unrealizable)==2

    native_recon=gram_from_unit_rays_and_nonunit_lifts(unit,nonunit,lookup)
    assert np.array_equal(native_recon,Gnative)
    changed_unit=flatten_counts(synthetic)
    Gsynthetic=gram_from_unit_rays_and_nonunit_lifts(changed_unit,nonunit,lookup)
    assert np.array_equal(Gsynthetic%5,Gnative%5)
    delta=(Gsynthetic-Gnative)%MOD
    G164_actual=gram_for_unit_histogram(actual[164],lookup)
    G164_twisted=gram_for_unit_histogram(synthetic[164],lookup)
    delta164=(G164_twisted-G164_actual)%MOD
    remainder=(delta-delta164)%MOD
    if changed_norms==[164]:
        assert not np.any(remainder)
    changed=np.argwhere(delta)
    assert len(changed)==363
    a,b=changed[0]
    assert (int(a),int(b),int(delta[a,b]))==(0,26,15)
    return {
        "D":D,
        "native_integer_order_Q":len(Qint),
        "all_changed_selected_original_signed_ray_norm_shells":changed_norms,
        "first_changed_exact_norm":changed_norms[0],
        "exact_original_norm164_integer_solutions":sorted(fibre),
        "signed_actual_ideals_norm164":sum(actual[164].values()),
        "signed_synthetic_ideals_norm164":sum(synthetic[164].values()),
        "all_synthetic_norm164_tags_OUTSIDE_actual_exact_fibre":True,
        "synthetic_norm164_rays_locally_realizable_at_conductor250":unrealizable,
        "same_original_primitive_G_mod5":True,
        "changed_primitive_Gram_cells_mod25":int(len(changed)),
        "changed_Gram_entry_first":[int(a),int(b),int(delta[a,b])],
        "all_Gram_changes_explained_by_norm164_fibre_only":
            not np.any(remainder),
        "other_original_norm_shells_changed_if_any":
            [n for n in changed_norms if n!=164],
        "global_realization_obstruction_not_deduced_from_local_norm_only":True,
        "no_new_field_or_cutoff_claim":True,
    }


def main():
    print("PHASE316_FIRST_EXACT_GLOBAL_RAY_REALIZATION_OBSTRUCTION_PASS",
          first_global_realization_obstruction(),flush=True)


if __name__=="__main__":
    main()
