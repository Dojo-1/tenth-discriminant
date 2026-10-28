# Change the queue, retain every check

The new passive polynomial/jet theorem passed local checks and every
mathematical step in PR39's external run. GitHub nevertheless cancelled
the overall job at25minutes. [Exact preserved receipt](PR39_CI_LIMIT_RECEIPT.md).
PR39 remains draft/unmerged; the cancelled run is not green CI.

The old two-worker queue put the assembly family last. Phase112 instead
starts families with larger declared timeouts first, stable on ties.
Every command, control, timeout and failure rule stays the same; results
still appear in the original declaration order. There are still TWO workers.
This changes scheduling, not the mathematics or its resource allowance.

All six inherited synthetic tests are unchanged. Two additions check
submission/reporting order and a deterministic queue model. In that model,
starting the long final job earlier reduces12time units to9. A deliberately
misleading timeout proxy reverses the comparison:9becomes12. These are
synthetic units, not measured Lean speedups or a completion guarantee.

The sole local run passed all eight tests. [Exact evidence](PHASE112_VERIFICATION.md).
No Lean theorem, control family or workflow was rerun locally.
The next publication needs its OWN single pinned CI on the new final head,
with the unchanged25minute limit; source/tree/security and full terminal
logs must pass before the existing user-authorized merge. A new failure
must be preserved too. Independent human review remains open.

The arithmetic/geometry research question remains [compatible transport](PASSIVE_TRANSPORT_CURRENT.md).
No cutoff improvement or full classification follows from queue scheduling.
