# Phase107: arbitrary even-field transport closes

Preregistered at b7e03e3634f6e2bf31ab3708cae94d2d0880ecd0, against
38d799e38145d6676f89d8aaa638bd8ae94c1ffc. Separate local branch
codex/even-field-transport. [Human proof](ALL_FIELD_TWO_CLASS_GUIDE.md).

The complete standalone target passed on its FIRST invocation:
100.7739366 seconds, exit0, no resource stop; observed peak working set
3,339,501,568 bytes, below the registered 8192 MB per-process threshold.
The time cap was600s, cumulative cap1200s. No repair, probe or replay.
All nine public statements/four control expectations are the first source;
no new definitions. Namespace audit:11logical/11theorems/0runtime, only
propext,Classical.choice,Quot.sound.

| Fresh root | Reached declarations | Excluded inputs |
| --- | ---: | ---: |
| arbitrary_even_discriminant_bound | 60,578 | 60 |
| arbitrary_discriminant_bound | 60,689 | 37 |
| classNumber_gt_two_of_large_discriminant | 60,694 | 37 |

The even branch excludes all58roots from Phase104 plus two coordinate
bridge/counterexample roots. The combined statements exclude all35h1/
classification/finite-answer roots from Phase88 plus those same two roots.
They legitimately reuse the existing odd h<=2 bound in the odd branch;
we do not claim independence from that explicitly used result.

Executed from lean:
`lake env lean -j 1 ../research/ender_radius_bridge/Phase107EvenFieldTwoClass.lean`.
The [manifest](PHASE107_RESULTS.json) and [four raw artifacts](PHASE107_RAW.zip)
retain exact source/stdout/stderr/result. Verify saved evidence without
running Lean: `python research/ender_radius_bridge/verify_phase107_results.py`.
Production/root/tools/pins/CI and earlier protocols/evidence remain frozen.
No library integration, new full-library audit or external CI here.

The actual all-parity conclusion is δ<2^52 under actual h<=2, with odd
δ<2^50. The 50-billion h1 bound is unchanged. This is no full classification.
[PR37's distinct CI stop](PR37_CI_LIMIT_RECEIPT.md) remains cancelled and
unmerged; its final PASS log text is not a successful CI job completion.
No rerun, increased resource limit or workflow modification was made.
