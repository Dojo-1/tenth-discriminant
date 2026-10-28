# Phase112: static priority, fixed checks and resource bounds

Preregistration:`9c7071d4948c01f27fc9fb303cf77db7e161d2d6`.
Implementation base:`b66b5f8a86df9cf515ccdab57dca529b006eeb01`.
[Human explanation](CONTROL_PRIORITY_CURRENT.md) · [Protocol](PHASE112_PROTOCOL.md).

Only controller submission order changes: descending declared timeout,
stable on ties. Exactly two workers. Future results are reported in the
original declaration order. The driver, eight child/nested source files,
arguments, cwd, all timeouts, initial probes and final gate are unchanged.
All six inherited test bodies are exact; exactly two new methods were added.

ONE invocation from lean: `python control_schedule_tests.py`.
All eight synthetic tests passed FIRST invocation. Suite time3.002s;
monitored elapsed4.0488772s,120s outer cap,8192MB per owned process.
Maximum sampled owned-process working set27090944bytes. This is a sampled
per-process observation, not a measured simultaneous total or zero-overhead
memory bound. No repair, repeat, probe, resource stop, Lean invocation
or real mathematical control-family execution occurred locally.

The queue model records12versus9units for a long final task, and the
adversarial proxy case9versus12. No wall-clock or CI speedup is inferred.
Other tests preserve coverage, max2overlap, real child output/UTF8/order,
nonzero/timeout/launch rejection and validation before launch.

[Raw five-artifact archive](PHASE112_RAW.zip) contains controller/tests
snapshots, stdout, stderr and native result JSON. [Manifest](PHASE112_RESULTS.json).
After the run, Windows CRLF line endings were normalized to repository LF.
[Explicit format receipt](PHASE112_FORMAT_NORMALIZATION.json) records both
hashes; raw snapshots/archive remain untouched. The verifier requires
EXACT CRLF-to-LF identity and identical Python AST, with no executable
code/test repair or rerun. Six inherited methods match the base source.
Saved check: `python research/ender_radius_bridge/verify_phase112_results.py`.
It checks registered protocol ancestry, exact controller delta, unchanged
six test bodies/driver/call tuples and every frozen base Git blob, including
all mathematical sources/root/pins/workflow25m and old evidence. It also
verifies the preserved PR39 cancelled receipt and full log markers.

This is local executor validation, not new Lean/CI or human semantic review.
PR39's phase111 cycle stays stopped/draft/unmerged. One separately
registered final-head CI for the NEW policy must complete overall SUCCESS
before user-authorized merge; no retries or limit changes after dispatch.
No new cutoff, optimality, computational-hardness or classification claim.
