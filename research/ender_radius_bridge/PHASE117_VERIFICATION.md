# Phase117: exact operator integration, all four first checks pass

The accepted116radial operator is integrated unchanged as
lean/TenthDiscriminant/RadialOperator.lean, with one new root import.
Status: EXACT_RADIAL_OPERATOR_INTEGRATION_ALL_FOUR_FIRST_CHECKS_PASS.
This record covers local integration. External CI/security/merge status
is versioned by final publication head and recorded separately in the PR.
No quantitative.013gain, smaller cutoff or full classification is claimed.
The published h1bound remains50billion;48b is the paper candidate.

Protocol2fd5881 preceded source/root edits and every Lean invocation.
The primary checkout moved to a NEW integration branch, preserving dirty
.agent state/notes byte-exact and keeping the old pinned branch ref7913eba.
The accepted standalone116source commit isd750f82. Secondary research
worktree and earlier stopped attempts remain untouched.

## Exact source correspondence

The accepted namespace body, including all27public types/proofs, six
complete definitions, private helpers and controls, is BYTE-EXACT.
Only its first import changes from the whole root to PassiveTransport.
That dependency already provides all required APIs, avoiding a root cycle.
One root import exposes RadialOperator. The accepted namespace/type/
definition/fresh-closure reports move to Phase117InputCheck.lean; only
diagnostic116markers are renamed117. No mathematical repair or style edit.
PHASE117_CORRESPONDENCE.json records these identities and inventory delta.

## One-shot local checks

From the integration repository root, each ONCE in this order:

    ./research/ender_radius_bridge/run_phase117.ps1 -Mode build
    ./research/ender_radius_bridge/run_phase117.ps1 -Mode root
    ./research/ender_radius_bridge/run_phase117.ps1 -Mode input
    ./research/ender_radius_bridge/run_phase117.ps1 -Mode audit

The runner records exact lake executable/arguments and source/root/harness
snapshots. All use the pinned Lean4.19.0/Mathlib environment in lean/.

| Check | Native exit | Seconds | Fixed cap seconds | Sampled process peak bytes |
| --- | ---: | ---: | ---: | ---: |
|module build|0|48.8540297|600|2877403136|
|full root build|0|38.9614954|1200|2797584384|
|fresh input check|0|48.4490393|180|3060015104|
|whole audit|0|55.3237184|180|3363024896|

Every attempt number is1, with empty stop_reason. No retries, resource
increases, standalone116replay or mathematical source changes between
checks. The cap is8192MB perownedprocess; observed peaks are sampled
per-process values, not exact simultaneous process-tree peaks.
Two inherited nonfatal linter warnings remain byte-exact.

Fresh namespace audit:57logical/51theorems/11runtime auxiliaries.
Fresh closures polynomial_action11194,complex_jet_action13985,
integer_bridge33149: each excludes the same70old result roots and
permits only propext,Classical.choice,Quot.sound.

The whole compiled audit reports5,450logical/4,644theorems/17,026runtime
auxiliaries. Source-only import coverage reports199reachable project
modules. Compared to the frozen5393-name logical inventory from111,
ALL57additions are RadialOperator declarations and ZEROold declarations
were removed. Counts come from actual logs, not a predicted increment.
No source/root/pin/controller/old-control weakening is involved.

## Preserved evidence and verification

PHASE117_RAW.zip stores25artifacts: six(source/root/input/stdout/stderr/
result) for each of four invocations, plus the correspondence receipt.
PHASE117_RESULTS.json contains every hash, fixed budget, outcome, inventory
and frozen-file scope. No previous proof/evidence source is changed except
the one registered root import and current reader documents.

    python research/ender_radius_bridge/verify_phase117_results.py

The saved verifier checks source correspondence, all four FIRST successes,
namespace/fresh/whole audit markers, the exact declaration delta, raw hashes
and previous Git blobs. It never invokes Lean or any previous trial.
The new publication uses ONE final-head draftPR and unchanged pinned25mCI;
no old green check is transferred to it. Any CI stop remains a stop.
No new reviewer or Tao posting. Quantitative bound/cutoff obligations remain.

[Current human scope](RADIAL_OPERATOR_CURRENT.md) ·
[Operator proof explanation](RADIAL_OPERATOR_GUIDE.md).

Reader checks: 572 relative file links resolve across nine current reader
documents; README and the objective ledger remain61lines. The staged
source/documentation whitespace check passes. Remote main was refreshed
pre-publication at4b2492f11a1b3d2bf7831eb15487504865a8ff88.
