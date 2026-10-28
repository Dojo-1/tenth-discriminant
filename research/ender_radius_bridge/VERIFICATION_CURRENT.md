# Read verification by source version

The local library through108 proves the actual imaginary-quadratic-field
class-number-at-most-two discriminant bound below2^52, sharper below2^50
when odd. [Human proof](ALL_FIELD_BOUND_CURRENT.md) · [Exact integration](PHASE108_VERIFICATION.md).
All four first local checks passed; the whole audit covers5361logical
and4565theorem declarations, with197reachable modules.

Phase109 changes control-family scheduling only. All eight mathematical
control files/timeouts and initial probes are preserved. Six synthetic
scheduler tests passed; these are a different evidence class from Lean.
[Scheduling explanation](CONTROL_SCHEDULING_GUIDE.md).

External status is recorded against the final head in the
[publication PR](https://github.com/Dojo-1/tenth-discriminant/pulls?q=head%3Acodex%2Fcontrol-schedule-publication)
and [branch CI](https://github.com/Dojo-1/tenth-discriminant/actions/workflows/lean.yml?query=branch%3Acodex%2Fcontrol-schedule-publication).
Those receipts identify source/run/tree and merge status; a cancelled run
is not a successful completion. [PR37's earlier timeout](PR37_CI_LIMIT_RECEIPT.md)
remains preserved. A later successful run does not change that old result.
Independent human semantic review, Mathlib acceptance and optimality remain
open. The h1 cutoff stays50billion; no full classification is announced.
