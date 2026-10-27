# Phase89: actual even ideal form and finite lattice count

The full registered standalone statement is proved. For every positive
squarefree d with d=1or2mod4, and every actual nonzero integral ideal J of
Q[sqrt(-d)], it constructs one actual integer basis and integral form

    Norm(x*e0+y*e1)=N(J)*(a*x^2+b*x*y+c*y^2),
    a>0, 4*a*c-b^2=4*d.

The SAME basis and coefficients serve every finite U in J and natural t:
if actual norm magnitude<=N(J)*t and all ycoordinates are nonzero,

    cardU <= 2*pi*t/sqrt(4*d)+4*sqrt(a*t/(4*d)).

No class-number assumption, PID, supplied form or discriminant is used.
[Human explanation](EVEN_IDEAL_LATTICE_GUIDE.md).

## Registration and complete attempts

Base `4278fb186ff0e0fec13b1a92af9daa94c55e0702`.
[Protocol](PHASE89_PROTOCOL.md) and [runner](run_phase89.ps1) committed at
`e65003d4cf5b2887761cc52a5ad3500dacb4aa07` before source and execution.
Lean4.19.0, Mathlib `c44e0c8ee63ca166450922a373c7409c5d26b00b`.

| Invocation | Result | Seconds | Observed peak bytes |
| --- | --- | --- | --- |
| Target1 | FAIL, final Nat-to-Real cast normalization | 46.283882 | 3132473344 |
| Target2 | PASS | 50.0552128 | 3221680128 |

Total96.3390948s. Caps: at most3targets600s/8192MB each,1200s cumulative;
no internal/outer resource stop. No third invocation or old campaign replay.
The only change was `simpa only [hcard,hdR] using hb` to
`simpa only [hcard,hdR,Nat.cast_mul,Nat.cast_ofNat] using hb`.
It identifies the cast of the natural4*d with4times the real cast ofd.
All14public theorem statement texts,3definitions, main theorem and controls
are unchanged. The failed proof depended on sorryAx and was rejected by
both the namespace audit and input checker; it is not accepted evidence.

Final source SHA256:
`30efad93fbd66ff427c16cc5c8d5bd9e14eac66481a3ab7c7ed02ce27faeb316`.
Namespace:24logical/21theorem/5runtime auxiliaries. Standard3axioms only:
`propext`, `Classical.choice`, `Quot.sound`. Fresh target closure44910
excludes the same35old inputs as88 PLUS the odd-chart cutoff and arbitrary
odd-field bound (37total). All four controls pass: Gaussian norm, d2shear,
actual field discriminant8!=2 and the zero-threshold/off-axis empty set.

## Saved evidence verification

```sh
python research/ender_radius_bridge/verify_phase89_results.py
```

PASS. This verifies exact source repairs,14types/3defs/controls, caps,
transcripts,37exclusions, [8raw files](PHASE89_RAW.zip), [manifest](PHASE89_RESULTS.json)
and1458frozen prior files. It does not execute Lean. The runner records
exact executed command `lake env lean -j 1 ../research/ender_radius_bridge/Phase89EvenIdealCount.lean`
from lean/. No additional Lean invocation was made outside the bounded attempts.

This is standalone research. All production source/root, pins, numerical
tools, certificates, CI gates and prior evidence/reviews remain unchanged.
The previous full-library audit belongs to88, not to a new89root build.
No production integration or external CI is claimed. Argon's announced
review has not landed; no report is assessed and no reviewer agent started.

## Remaining proof obligations

The even cutoff still requires controlled bases over all actual ideal
classes, prime lifts with full axis/multiplicity accounting, a complete
weighted loss budget and a contradiction on the SAME original Gram.
The field discriminant4d and the Gram's radicand parameter must be related
explicitly; they cannot be substituted silently. This theorem gives the
local norm-form/count component, not that whole comparison.
The odd actual-field h<=2bound remains2^50; the h1field cutoff remains
50billion. No classification, novelty, optimality or upstream acceptance
is asserted. No publication or merge was performed.
