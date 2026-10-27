# Phase63: actual off-axis count, with an explicit integral

**Standalone local PASS**, outside production/root/CI. Registered commit
e19131e precedes source; base74d02d3, on a separate local branch while
PR31's existing CI continues untouched. No older campaign was rerun.

For a>0,D=4ac-b²>0,t>=0 and any finite integer-pair set U satisfying
Q<=t and y!=0, `off_axis_count` proves card(U)<=2 integral_0^Y w+2Y,
with Y=sqrt(4at/D), w(s)=sqrt(4at-Ds²)/a. No count estimate or integral
value is an assumption. The closed pi expression is not yet proved here.

First build FAIL28.4400993s: explicit endpoints needed in Int.card_Icc,
a lambda needed reduction before integer-index arithmetic, and the
adjacent-integral equality needed its type specified; an already solved
reflection goal also had an unnecessary final tactic. The complete first
source/stdout/stderr/result are preserved. Second build PASS29.0818965s
after one proof-body repair round. All14 public theorem type prefixes,
5 definitions and gates remain unchanged. Total57.5219958s, two builds
within3x600seconds/1200seconds cumulative/8192MB; no resource stop/reroll.

The namespace gate checks34 logical declarations/29 theorems/4 runtime
auxiliaries, including unused/private logical declarations, permitting only
`propext`, `Classical.choice`, `Quot.sound`. The compiled actual-count root
prints exactly those axioms. Actual interval/fiber/height/integral/reflection
steps and all fixed controls compile together. The origin at t=0 refutes
dropping y!=0; unit-circle and empty-input controls are included.

`PHASE63_RAW.zip` contains8 files with exact readback. The integrity
verifier checks protocol ancestry, both source hashes, budget records,
unchanged types/definitions/gates, final audit output and unchanged
production and Phase62 artifacts. It does not execute Lean or certify a
class-number theorem. Source/pins are Lean4.19.0/Mathlibc44e0c8 unchanged.

## Reproduction

From repository root, pinned elan on PATH:

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File research/ender_radius_bridge/run_phase63.ps1 build
python research/ender_radius_bridge/verify_phase63_results.py
```

No further build is needed to repeat this accepted result. Source-reading
on Windows initially hit a console encoding error; the reader was changed
to UTF-8, not the raw evidence. The existing numerical tools/certificates,
production proofs/gates/root and61-line README are unchanged.

No closed area evaluation, actual excluded-prime B, prime multiplicity,
class dictionary, ramified budget, higher-class-number cutoff, independent
review or new classification claim follows. [Human count](NONZERO_ROWS_GUIDE.md).
