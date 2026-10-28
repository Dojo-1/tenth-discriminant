# Phase109: bounded independent-control scheduling and new-source publication

Base0b004e0eff68806ce485e3d3ee8598af6c873bc7. Register before scheduler or
controller edits/tests/new CI. New target includes the actual arbitrary-field
h<=2 theorem integrated108, absent from stopped PR37 source38d799e.
PR37 CI40707296487 stays CANCELLED/draft/unmerged; no retry at that head,
limit increase or relabelled green run. Preserve its full evidence archive.

Scope: add a small control_schedule.py helper using at most2workers for
ONLY the eight existing final child families in negative_controls.py.
Keep all eight child scripts AND nested multiplicity_exact_controls.py
byte-exact. Preserve their executable/arguments/cwd, order of reported
outputs, timeouts120/120/120/120/240/360/240/360 and every positive/negative
case and rejection rule. Keep the initial pairs/probes byte-exact except
one scheduler import and one new pure-scheduler self-test call. The final
all-controls PASS stays after successful return from ALL eight families.
No success if any nonzero exit, timeout, launch error or invalid/empty/
duplicate job list. Diagnostics and partial timeout output must survive.
No mathematical source, pinned workflow, toolchain or resource-limit edit.

Static independence audit: exact Gram/jet uniqueness/nested exact
multiplicity are pure in-memory arithmetic; the other six families use
separate tempfile.TemporaryDirectory and invoke read-only lake env lean
on their own temporary files. The prebuilt common .olean/configuration is
read-only during this stage. No family writes into the production tree.
Public repo verified private=false. Current official GitHub documentation
lists ubuntu24.04 public runner4CPU/16GB; two recently observed roughly
3.3GB Lean working sets make max2 a bounded plausible attempt, not a
memory guarantee or measured speedup. Source https://docs.github.com/en/actions/reference/runners/github-hosted-runners .

Add six SYNTHETIC tests (no Lean, not a mathematical verification):
max2 actual overlapping workers and all8jobs; real small child processes
preserve all8outputs/UTF8stdout/stderr/order; nonzero exit rejects;
intentional short synthetic timeout rejects and retains partial output;
launchOSError rejects; invalid empty/duplicate/nonpositive-timeout lists
reject. Expectations fixed at first suite run, max3suite invocations120s
(each outer) with at most2 plumbing fixes. Stop unexpected resource stop;
preserve every run/result. The deliberate synthetic timeout is an expected
negative test, not a real Lean/CI resource stop. Do not run inherited Lean
controls locally as a retry. Verify exact original child list/timeouts,
unchanged controller prefix and all child bytes, immutable math/root/pins/
workflow, raw local logs and prior files with a saved verifier.

After local validation and concrete review, one new draft PR against main
and ONE unchanged pinned25m CI dispatch on the final new head, including
all actual Lean build/audit/controls. No head changes/second dispatch/retry
or increased timeout after starting. Stop and preserve any resource failure.
Inspect full logs, same-head security and tested merge-tree identity before
user-authorized merge. PR37 remains historical; only a successful new gate
can validate the newer source. Attach the new PR; no Tao post/new reviewer.
Reader docs remain concise; keep theorem/operational test/CI/review scopes
separate and record exact source/run/merge statuses. No new cutoff gain or
full classification claim. The h1 bound remains50b and all-field h<=2 bound
2^52 (odd2^50). No mathematical proof attempt or replay in this phase.
