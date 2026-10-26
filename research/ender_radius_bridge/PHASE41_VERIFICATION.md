# Phase41 local verification and publication boundary

Protocol35dbd4c7ce3e3d5c6c7dce5d3cfdf3d4b1b1f2af preceded all new
proof/pilot edits and executions. The [results manifest](PHASE41_RESULTS.json)
points to every terminal attempt and separates acceptance from verification.
Commands, from the repository root:

```powershell
powershell -NoProfile -File research/ender_radius_bridge/run_phase41.ps1 -Mode pilot
powershell -NoProfile -File research/ender_radius_bridge/run_phase41.ps1 -Mode build
powershell -NoProfile -File research/ender_radius_bridge/run_phase41.ps1 -Mode root
powershell -NoProfile -File research/ender_radius_bridge/run_phase41.ps1 -Mode input
powershell -NoProfile -File research/ender_radius_bridge/run_phase41.ps1 -Mode audit
python lean/verify_sources.py
python research/ender_radius_bridge/verify_phase41_results.py
git diff --cached --check -- . ':!research/ender_radius_bridge/PHASE41_*.log' ':!research/ender_radius_bridge/PHASE41_*.result.json'
```

`verify_phase41_results.py` passes all five terminal record checks,17
recorded assertions, final source fingerprints, raw-archive recovery and
326 local reader targets in six selected documents. It never reruns the
pilot or upgrades its scope to a universal theorem.

Do not rerun the pilot: its runner deliberately rejects a second recorded
execution. It passed once in1.5159136s with all17 fixed checks. The first
Lean target passed in72.5397946s, observed peak2870804480 bytes, within
600s/8192MB; no failed or resource-stopped proof attempt. An unused-hypothesis
name was then prefixed with an underscore, without changing the proposition
or proof. The full6808-step root rechecked that source in49.3788185s.

Fresh `Phase41InputCheck.lean` passed in22.5338803s. The new theorem's
13525-declaration closure contains none of the13 listed forbidden inputs:
finite answer, positive cases, classification, old700-billion and200-billion
cutoff roots, or the old fixed-ratio uniform lower theorem. Types and
private/opaque bodies are traversed by Lean's collector. All entries
resolve and are safe; only the three permitted axioms. This does not
purport to be an independent semantic review or whole-method exclusion.

The full compiled namespace audit passed in35.178560999999995s:
4543 logical declarations,3812 theorems,16951 runtime-only auxiliaries
excluded. Its1996145-byte raw stdout is losslessly preserved in
`PHASE41_AXIOM_AUDIT_RAW.zip`; the manifest gives both hashes. Byte-identical
readback was checked before deleting only the redundant unpacked duplicate.
The root/import check finds154 reachable, acyclic project modules and no
source proof escapes. The frozen ledger check passes250 endpoint pairs;
it does not certify every historical Arb comparison.

Verification-helper repair retained: the first results/link check rejected
README's valid `review/` directory link because it required every target
to be a file. The predicate was corrected to target existence (files or
directories); no mathematical source, record or acceptance threshold changed.
This was a link-checker scope error, not a failed proof or pilot, and is
not counted as another observational run.

Raw Windows runner outputs retain CRLF (and result JSON retains its BOM).
The all-file whitespace check consequently flags their carriage returns;
do not rewrite raw evidence to make that presentation check pass. The
source/document/script whitespace check above excludes only those raw
logs/runner-result records. The evidence verifier parses the original
records and separately verifies archive bytes; no proof gate is changed.

No local full parent-apparatus/rejection replay is claimed from the compiled
audit alone. Unchanged pinned CI supplies that gate at the eventual exact
publication head. Prerequisite run40154838691 onf7bbfaa finished SUCCESS
at2026-10-25T02:47:57Z, job15m22s; security40154836580 and CodeQL passed.
Its same-tree merge9dca199 was verified. The
[final record](https://github.com/Dojo-1/tenth-discriminant/pull/28#issuecomment-6394261827)
was posted before the newer proof push. No prior head's success transfers
automatically to changed mathematics. New-head CI remains a separate gate;
its final PR28 comment supersedes pending publication checkpoints.

No production tools, frozen campaigns, finite certificates, previous proof
modules, cutoff statements, dependency pins or workflow gates change. One
new theorem module plus its root import is the mathematical diff. The
inherited untracked lake-manifest.json remains excluded. No merge or Tao post.
