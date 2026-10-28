# Finish every check with bounded concurrency

The previous CI run reached its25-minute job limit. It built and audited
the library, and printed the final control PASS message, but GitHub
cancelled the job. That is a cancelled run, not a green check.
[The complete stopped record](PR37_CI_LIMIT_RECEIPT.md) remains preserved.

The controller ran eight additional control families one after another.
Those families share the prebuilt library but not their temporary files.
Two are exact arithmetic in memory; the six Lean families create separate
temporary directories and read the compiled library. A nested multiplicity
arithmetic check is also pure. Their mathematical cases do not change.

The new scheduler runs at most two families at once. It retains all eight
commands, their timeouts, good/bad cases and rejection rules. Captured
stdout/stderr is reported in declaration order. Nonzero exits, timeouts,
launch errors and invalid job lists prevent the final all-controls PASS.
The initial matched pairs and proof-audit probes remain unchanged.

Six small SYNTHETIC tests passed on their first run: the concurrency cap,
complete output/coverage, nonzero failure, timeout with partial output,
launch failure and invalid-list rejection. They invoke small Python
programs or mocks, not Lean. They are not a proof check or a CI pass.
[Exact local evidence](PHASE109_VERIFICATION.md).

The repo is public. GitHub's [current runner reference](https://docs.github.com/en/actions/reference/runners/github-hosted-runners)
lists4CPU/16GB for public ubuntu24.04 jobs. A two-family attempt is
plausible given observed roughly3.3GB individual Lean working sets, but
this is not a guarantee about concurrent peak memory or measured speedup.
The workflow,25-minute limit and per-family timeouts are unchanged.

The publication target also contains the new actual-field theorem through
Phase108. This is a separately registered source/architecture; stopped
PR37 at38d799e is not rerun or rehabilitated. The
[publication PR](https://github.com/Dojo-1/tenth-discriminant/pulls?q=head%3Acodex%2Fcontrol-schedule-publication)
records the actual final source, CI and merge receipts. No gate is treated
as passing until the entire new job completes successfully.
