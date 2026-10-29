# Phase114 verification: full target not accepted

Status: RESOURCE_STOP_FULL_TARGET_NOT_ACCEPTED. The registered full
Fischer/moment/original-integer-prime bridge did not pass. No component is
substituted for the full target, and printed proof terms are not promoted
to independently audited theorems. Production mathematics is unchanged.

Protocol: ecfe1db (f853434 initial registration; the control prediction14
was corrected to18 before source/Lean execution). Prior evidence b9bf8c5;
published source7913eba remains the production baseline.

## Exact execution

Command, from ../tenth-discriminant/lean with its existing pinned cache:

    C:/Users/HAL900/.elan/bin/lake.exe env lean -j 1 ../../tenth-radial-blocks/research/ender_radius_bridge/Phase114RadialBlocks.lean

The saved runner was invoked twice from this research checkout:

    ./research/ender_radius_bridge/run_phase114.ps1 -Mode build

| Attempt | Native exit | Monitored seconds | Sampled process peak bytes | Outcome |
| --- | ---: | ---: | ---: | --- |
|1|1|93.9184484|2941247488|Elaboration, type and audit failures|
|2|1|84.9480633|2951196672|Default internal heartbeat stop plus other errors|

Cumulative178.8665117seconds. Both outer limits were600s and8192MB per
owned process. Sampled peaks are per-process observations, not an exact
simultaneous tree peak. Neither outer limit caused the stop. Attempt2 hit
Lean's DEFAULT200000heartbeat limit at whnf in fischer_partition and
rectangular_det_le_moments. The diagnostic's suggestion to increase it
was NOT followed. Its process terminated natively with1; the runner records
lean_internal_resource_limit. The third slot is forfeited permanently.
No repair, replay or further Lean invocation after that resource stop.

## What failed, and what cannot be claimed

Attempt1 had a reversed product-reindex equality, missing classical finite
fiber instances, a comparison-token spacing error, and unresolved audit
names outside the imported environment. Some control matrix expressions
also failed field-notation elaboration. In attempt2 the general-partition
composition hit the kernel resource limit; the whole namespace audit
rejected PROJECT_AXIOM on the final bridge, and its fresh closure rejected
a nonstandard axiom. No AUDIT_OK or PHASE114_INPUTS_OK acceptance marker.
The final source is a FAILED research artifact and has no production import.
The error-generated placeholders in these failed compilations are evidence
of rejection, never mathematical assumptions accepted by this project.

The first repair is preserved as PHASE114_REPAIR1.diff. It changed two
control signature annotations by adding parentheses, and changed comparison
spacing inside momentBlock. All other public signature/definition
characters remain unchanged. These are intended syntax repairs without
changed sample data, but an unchanged ELABORATED surface was not verified;
strict frozen-surface acceptance is therefore NOT claimed. Some annotation
errors remained. The registered all-public-type reporting gate also did not
complete: the source printed the six main types, not every control type.
These are protocol/implementation shortcomings, not mathematical refutations.

The general block proof and moment identity are explained in the
[human guide](RADIAL_BLOCK_PROOF_GUIDE.md). They remain paper mathematics
at this acceptance boundary; a failed file's printed declarations do not
supply a passing transitive audit. No uniform quantitative block saving,
new cutoff, prime exponent, full classification or independent review.
The h1 bound remains50billion. Phase113 remains stopped separately.

## Preserved evidence and read-only verification

PHASE114_RAW.zip contains exactly8raw files: source/stdout/stderr/result
for each invocation. PHASE114_RESULTS.json records hashes, exact commands,
terminal statuses, disclosure and frozen-file count. The final source is
byte-exact to the second snapshot. No root build, production integration,
new CI, publication, merge, reviewer or Tao posting occurred in this cycle.

    python research/ender_radius_bridge/verify_phase114_results.py

This saved verifier reads preserved files and Git blobs only. It NEVER
runs Lean, repairs a failed source or repeats either stopped campaign.
A verifier PASS means evidence integrity and honest failure accounting;
it does not mean the full bridge passed. PR40's historical CI receipt
remains separate from this failed standalone work.

Reader checks:546relative file links resolve in the eight current reader
documents; README and the objective ledger remain61lines. Selected changed
reader paths pass git diff --check. No new Lean execution was used.

Whitespace disclosure: the full staged diff check flagged ten blank CONTEXT
lines in PHASE114_REPAIR1.diff. Each is the single-space prefix required
by the preserved unified diff. That evidence is retained byte-exact; the
full check was not clean. The selected reader check above did pass. A
separate committed-content check excluding only this raw repair diff
passes. No proof source or raw snapshot was changed for formatting.
