# Phase40 verification checkpoint

Protocol `945b14910c1405478f12786cd345edf9625bb33c` preceded the full
source reading. This phase compares frozen sources, not numerical runs or
new mathematical proofs. The proof snapshot is
`f1638018085b0167dedd6f7ef13d69dedd51f148`.

Commands run from the repository root on25 October2026:

```powershell
powershell -NoProfile -File research/ender_radius_bridge/verify_phase40_sources.ps1
python lean/verify_sources.py
git diff --check
git diff --exit-code f163801 -- .github lean/TenthDiscriminant lean/TenthDiscriminant.lean tools flow ledger
```

Results: all seven frozen original-byte hashes, byte lengths and Git blob
IDs match. Both manuscript blobs also match the historical recency-control
commit. All319 local reader-link targets in the five selected current
documents resolve. The existing source checker passes the frozen ledger
hash and250 endpoint pairs; it does **not** certify the Arb inequalities.
Whitespace checks pass. No mathematical source, production tool, frozen
campaign, dependency pin or workflow/gate change is introduced here.
The inherited untracked `lean/lake-manifest.json` is preserved and excluded.

Primary-source anchor ranges in the human comparison were checked against
the complete source text. The root README's historical and numbered-series
claims are not used to substitute a different manuscript. The two selected
proofs have not changed since the earlier anchor; review and finite-run
claims remain attributed to their source. No external code was executed.

The exact mathematical-head pinned run
[40153287923](https://github.com/Dojo-1/tenth-discriminant/actions/runs/40153287923)
finished SUCCESS at2026-10-25T02:30:05Z, job21m57s. Full build, compiled audit
(4534 logical/3803 theorems/16951 runtime-only) and all inherited rejection
suites passed; only the three permitted axioms. Security run40153286062 and
the head's CodeQL check pass. The synthetic merge27ff84a has the same tree
3126fea27da5f0fc6c75dd072f509cd2ce511aca as the proof head. The
[final PR28 record](https://github.com/Dojo-1/tenth-discriminant/pull/28#issuecomment-6392486504)
was posted before the next push, superseding pending checkpoints. No old
head's success is transferred; the next publication head requires its own
unchanged pinned CI. The separate research input-check scripts are not
silently added to that CI's scope.

Limits: source integrity is not mathematical validation; source comparison
is not a permanent CI gate; owner-reported independent verification is not
independently authenticated here. No merge, Tao post, novelty, optimality,
arbitrary-field representation or higher-class-number result is claimed.
