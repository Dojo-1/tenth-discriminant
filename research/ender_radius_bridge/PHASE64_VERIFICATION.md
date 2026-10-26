# Phase64: closed quadratic point count in production

**All registered local checks PASS**, with new exact-head remote CI still
required. Protocol20d1db3 preceded proof source; basee92d05b. This cycle
integrates the frozen Phase63 proof and evaluates its actual width integral.

- Target first build PASS52.9580334s; no repair, second build or resource stop.
- Root PASS20.1056496s (6824 tasks).
- Statement/ordinary-polynomial API/input exclusions PASS26.1582986s.
  The area-integral root reaches35203 declarations; actual-count root35399.
  Neither reaches the34 listed h1/old-cutoff/classification/finite-answer roots.
  This checks those exclusions, not every conceivable semantic formulation.
- Whole-project compiled audit PASS27.9050467s:4869 logical declarations,
  4114 theorems,16982 runtime auxiliaries. The new namespace has48 logical,
  43 theorem and4 runtime declarations. Only `propext`, `Classical.choice`,
  `Quot.sound` are allowed, including private/unused logical declarations.
- Structural audit:170 reachable acyclic modules, no source proof escapes.
  Source correspondence:250 endpoint pairs match; identity check only,
  not a new Arb inequality certification.

The exact public statement was printed and applied to an ordinary expanded
real polynomial on finite integer pairs. The zero-threshold, original
zero-row falsifier, circle, actual sheared-form and transported row controls
compile with the full target. Homogeneous scaling avoids division by the
height, so t=0 is covered by the same area identity.

Two production modules and two Root imports are the mathematical diff.
QuadraticRowCount transports Phase63 through import/namespace/header changes
only; its definitions/statements/proof bodies are unchanged under transport.
QuadraticAreaCount evaluates the integral and composes it with that actual
count. No old production proof, numerical tool/certificate, pin or CI gate
changes. The61-line README stays unchanged. Old source/raw evidence remains
frozen. Prior current-root verifiers are historical after the new imports;
this cycle preserves their bytes at frozen refs without weakening their
original manifests or misrepresenting their old scope.

The timed-out local Phase61 negative campaign was NOT rerun. The unchanged
complete regression suite is reserved for independent pinned Linux CI at
the newly published head. No remote pass is assumed from the local checks.

## Publication baseline

PR31 head74d02d3 completed pinned production CI40407136985/job121867685012:
source250pairs21:47:30.8904391Z, audit4821/4071/16978 at22:03:44.6815368Z,
final controls22:09:14.3446004Z on26October2026. [Final record](https://github.com/Dojo-1/tenth-discriminant/pull/31#issuecomment-6428628179)
preceded this follow-up. That run covers the old production library, not
this new integration or Phase62's standalone file. The check API reported
only Lean for the stacked PR31, no security checks; absence is not a pass.
No older CI/review is transferred to Phase64. PR30 merge approval remains
pending and no automatic merge is authorized.

## Reproduction

From repository root, pinned elan on PATH:

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File research/ender_radius_bridge/run_phase64.ps1 build
powershell -NoProfile -ExecutionPolicy Bypass -File research/ender_radius_bridge/run_phase64.ps1 root
powershell -NoProfile -ExecutionPolicy Bypass -File research/ender_radius_bridge/run_phase64.ps1 input
powershell -NoProfile -ExecutionPolicy Bypass -File research/ender_radius_bridge/run_phase64.ps1 audit
python lean/verify_sources.py
python research/ender_radius_bridge/verify_phase64_results.py
```

The runner preserves both source snapshots and every raw result. The
saved-evidence verifier reads bytes; it does not execute Lean or certify a
class-number theorem. No further local target build is needed to repeat
the accepted proof. [Human argument](QUADRATIC_AREA_GUIDE.md).
