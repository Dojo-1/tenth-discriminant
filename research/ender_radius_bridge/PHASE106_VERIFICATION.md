# Phase106: compatible charts and shifts join the library

The accepted Phase105 mathematics is now a production module:
[CoordinateTranslation.lean](../../lean/TenthDiscriminant/CoordinateTranslation.lean).
All 29 public theorem statements and proofs, five complete definitions,
four controls and printed reports are exact after five dependency imports.
The 68-root checker is relocated unchanged apart from diagnostic names.
One root import makes the bridge available to the whole library.
No standalone proof replay, mathematical repair or cutoff change occurred.

Preregistration `725e00f5725aeeeee542bfd93d526cd8545dd9f2`;
accepted base `aaeab39ac01f8e6b692f4e848c2648eeaa3cce00`.

| Check | Exact command from lean | Seconds | Result |
| --- | --- | --- | --- |
| Module | `lake build TenthDiscriminant.CoordinateTranslation` | 32.2865581 | PASS first invocation |
| Full library | `lake build` | 18.7997817 | PASS first invocation |
| Fresh closures | `lake env lean -j 1 ../research/ender_radius_bridge/Phase106InputCheck.lean` | 19.433218 | PASS first invocation |
| Whole axiom audit | `lake env lean -j 1 Audit.lean` | 28.7409321 | PASS first invocation |

Each process stayed below its registered time and 8192 MB memory caps.
Fresh closures remain 37,660 / 17,619 / 12,095 and exclude all 68 forbidden
inputs. Whole audit: 5,350 logical declarations, 4,554 theorems, 17,015
runtime-only auxiliaries excluded; only the three permitted axioms.
`python lean/verify_sources.py` also passed all 250 endpoint identities;
this checks correspondence, not Arb margins. The inherited trailing blank
line at module EOF is preserved for exact accepted-body correspondence.

[Manifest](PHASE106_RESULTS.json) and [25 raw artifacts](PHASE106_RAW.zip)
retain all four invocations and the source-check transcript. Verify saved
evidence without rerunning Lean:
`python research/ender_radius_bridge/verify_phase106_results.py`.
The older Phase105 failures and protocol remain frozen.

[Human mathematics](COORDINATE_TRANSLATION_GUIDE.md): chart norms commute;
shifts preserve metric, counts, divisor and guarded positivity, while the
original trace-Gram determinant can change from 24 to 60. This integration
lowers no cutoff and supplies no independent human review. External pinned
CI and publication must be recorded against their own final source head;
PR36's earlier passing checks are not transferred here.
