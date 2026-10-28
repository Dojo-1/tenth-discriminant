# Phase112: schedule long control families before the tail

Register before controller edits or synthetic execution. Base source:
`b66b5f8a86df9cf515ccdab57dca529b006eeb01`, tree
`f24d8dcf9058438892aa97c1dd20ff43179f42fa`.
Phase111's sole CI run40753057286 is CANCELLED at25m. Preserve its
complete raw receipt and PR39 draft/unmerged state. Never rerun that cycle
or transfer its passing steps into an overall-success claim.

## Fixed operational hypothesis

The existing two-worker FIFO controller queues the assembly family last.
A STATIC priority derived only from the eight already declared timeouts
may reduce this tail: dispatch larger-timeout jobs first, stable on ties.
This is a different executor policy, not a mathematical proof change.
Declared timeout is only a scheduling proxy; it is not measured duration.
No empirical speedup or guaranteed future CI completion is assumed.

Retain exactly TWO workers, the same eight children and nested controls,
commands, cwd, byte diagnostics, per-child timeouts, validation/failure
semantics, initial matched-pair/audit probes and final all-controls gate.
Only submission order may change. Capture all futures, but emit every
result in ORIGINAL declaration order. Nonzero, timeout, launch error,
empty/duplicate/nonpositive jobs still reject; never short-circuit away a
registered child. No new CPU/memory quota, dropped controls, looser gate,
changed toolchain, raised25m workflow limit or mathematical premise.

Allowed implementation: lean/control_schedule.py dispatch ordering and
lean/control_schedule_tests.py additions. Preserve all six existing tests
byte-for-byte. Add exactly TWO synthetic tests: static dispatch/tie order
with original diagnostic order, and a deterministic two-worker queue model
where a long final task exposes a FIFO tail. The model is NOT a wall-clock
benchmark or evidence of actual Lean/CI speedup.

## One bounded validation

One invocation of `python control_schedule_tests.py` from lean, all EIGHT
tests,120s and8192MB per owned process. Preserve controller/test snapshots,
stdout,stderr and result, including failure. No repairs/repeats/probes
following any failure or resource stop. Do NOT run Lean or any old family
locally. Peak RSS may be UNOBSERVED if the short process exits between
samples; never invent zero usage.

A saved verifier must compare the exact eight old call tuples/timeouts,
the unchanged driver and initial/final gates, two-worker bound, sorted
submission versus original reporting order, all six inherited test bodies,
first-run budget/result and raw hashes. All tracked base files except the
two named implementation files and current reader documents stay frozen.
Verify frozen files against the base Git tree, not by weakening an old
root-fixed verifier. This includes every Lean source/root, tool, workflow,
pin, previous protocol/result/verifier/review/certificate and failed record.
Reader exceptions: README.md,STATUS.md,lean/FORMALIZATION.md,
TAO_OBJECTIVES_CURRENT.md,TAO_REPLY_BRIEF.md, and the two current guides
PASSIVE_TRANSPORT_CURRENT.md/VERIFICATION_CURRENT.md in this directory.

After local acceptance and compact reader/evidence updates, publish ONE
new final-source draft PR with the new executor policy and unchanged
mathematics. Run ONE unchanged pinned25m CI; no head changes, second
dispatch, retry, raised limits or merge after a resource stop. Inspect full
terminal logs, all eight families, audit/source/security and tested tree
before the existing user-authorized merge, only if overall CI SUCCESS.
PR39's cancelled run stays cancelled even if ancestry is merged later.
No new reviewer or Tao post. No new cutoff/classification/hardness claim.

The mathematical next candidate remains the larger angular-weight radial
block bound, which requires its OWN preregistration before any attempt.
