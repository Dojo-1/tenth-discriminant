#!/usr/bin/env python3
"""Phase306-D: bridge Worldlet moving frames to ACTUAL D203 full source.

NO invented points and NO changes to 100x100 field Gram or class-number bound.
Uses original Phase304 source routine as oracle and separate exact omega ring.
"""
from pathlib import Path
import sys

import numpy as np

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "research" / "phase304"))
import highjet_d203_original as pilot  # noqa: E402

from arithmetic_fabric import (actual_d203_points,  # noqa: E402
                               exact_original_jet_rows, trace_gram,
                               gram_covariance, transpose, mmul, mod_matrix,
                               det, eye, Cage, transport_functor)

D = 203
MOD = 5**3
ROWS = (0, 2, 4)  # original (r,s)=(0,0),(1,0),(2,0)
U = ((1, 2, 0), (0, 1, -1), (0, 0, 1))


def main():
    pilot.guard()  # SHA-gate frozen Phase304 source-probe dependencies
    rho, R, S, J, old = pilot.params(D)
    assert (rho, R, S, J) == (24, 50, 2, 2)
    q = pilot.qmax(rho)
    assert len(q) == 263 and len(old) == 127
    # Pilot original source, FULL 100x1052 evaluation at 5^3 precision.
    original = pilot.evaluate_original_jets(q, R, S, J, MOD)
    assert original.shape == (100, 1052)
    selected = np.asarray(original[list(ROWS), :], dtype=np.int64)

    # Our independent exact omega multiplication and ORDINARY j0/j1 jets
    # on the SAME original 263 points. No basis coercion or source change.
    reconstructed = exact_original_jet_rows(q, degrees=(0, 1, 2),
                                             jets=J, d=D)
    assert (len(reconstructed), len(reconstructed[0])) == (3, 1052)
    assert mod_matrix(reconstructed, MOD) == tuple(
        tuple(int(x) for x in row) for row in selected)
    assert mod_matrix(reconstructed, 5) == tuple(
        tuple(int(x) % 5 for x in row) for row in selected)

    # Independently reconstruct original trace pairing at all observations.
    ours = trace_gram(reconstructed, D)
    from_pilot = pilot.original_trace_gram(selected, len(q), J, MOD)
    assert mod_matrix(ours, MOD) == tuple(
        tuple(int(x) for x in row) for row in from_pilot)
    assert det(ours) > 0

    # Noncommuting integral moving frame, exact source lattice covariance.
    moved, expected, before, after = gram_covariance(U, reconstructed)
    assert moved == expected and before == after and before > 0
    assert transpose(mmul(U, reconstructed)) == mmul(
        transpose(reconstructed), transpose(U))

    # The field, prime, precision and source are *types*, not lost labels.
    cage = Cage(D, 5, 3, "Phase304.D203.full263.original-j0j1")
    fwd, modular_conjugate = transport_functor(U, reconstructed, cage)
    assert fwd == modular_conjugate
    assert fwd == mod_matrix(mmul(U, reconstructed), MOD)

    # Hostile controls: a different field chart and a missing ordinary jet
    # must NEVER be accepted as a replay of this frozen original source.
    wrong_d = exact_original_jet_rows(q, degrees=(0, 1, 2),
                                      jets=J, d=187)
    assert mod_matrix(wrong_d, MOD) != mod_matrix(reconstructed, MOD)
    wrong_j = exact_original_jet_rows(q, degrees=(0, 1, 2),
                                      jets=1, d=D)
    assert len(wrong_j[0]) != len(reconstructed[0])

    print("PASS PHASE306D_ACTUAL_D203_SOURCE", {
        "field_d": D, "maximal_order_points": len(q),
        "all_original_rows": R*S, "selected_original_row_indices": ROWS,
        "original_ordinary_jets": J, "selected_raw_coordinate_checks": 3*1052,
        "exact_trace_gram_cells": 9, "precision": MOD,
        "integral_covariance": True, "determinant_invariant": True,
        "full_100row_source_not_replaced": True,
        "same_original_rho_R_S_J": True,
        "negative_field_chart_rejected": True,
        "negative_missing_j1_rejected": True,
        "no_new_discriminant_bound": True
    })


if __name__ == "__main__":
    main()
