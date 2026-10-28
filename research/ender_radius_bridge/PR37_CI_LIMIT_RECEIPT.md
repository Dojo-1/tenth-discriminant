# PR37: preserve the CI timeout without relabelling it

[PR37](https://github.com/Dojo-1/tenth-discriminant/pull/37) remains draft
and unmerged at source38d799e38145d6676f89d8aaa638bd8ae94c1ffc.
[Pinned run40707296487](https://github.com/Dojo-1/tenth-discriminant/actions/runs/40707296487),
job122882737948, completed CANCELLED. The explicit annotation says:
"The job has exceeded the maximum execution time of 25m0s".

Source correspondence, full build and whole dependency audit completed
successfully. The log reports5350logical/4554theorems/17015runtime.
The final negative-control PASS marker appears at14:59:46.377UTC, followed
by cancellation at14:59:46.407UTC. The control step and overall job do not
have successful completion status. Same-head CodeQL122883088584 and
security analyses122882732420/122882732279 passed.

The [raw evidence archive](PR37_CI_LIMIT_EVIDENCE.zip) preserves the entire
downloaded log and run/job/annotation metadata; [hashes](PR37_CI_LIMIT_RECEIPT.json).
Log SHA256:492621373e6622cb711272f9e1ce4780cd8ad2bd38c20fdfa73fdaabf4320fa7.
All four LOCAL Phase106 checks passed first time. This does not turn the
cancelled external run green. The PR body also carries this terminal receipt.
No CI rerun, limit increase, changed workflow, weakened check or merge.
User merge authorization persists; the successful publication gate is unresolved.
Phase107 is a separate mathematical target, not a retry of this CI run.
