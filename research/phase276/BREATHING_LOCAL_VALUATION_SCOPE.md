# Phase276 — the breathing asymmetry of real Gram order and p-adic depth

## Claim frozen before implementation

**Primary object:** the unchanged original integer ordinary-Z-jet trace Gram `integerRectangularTraceGram Q D J R S` with `D=163, R=S=J=1` and complete lattice-ellipse supports `Q_rho=ellipsePairs 163 rho` for `rho=1,2,3`. No selected minor, surrogate Hasse derivative, altered trace metric, or point-selection oracle is used. The small dimensions are deliberate: this is a *falsifying control* for a general monotonicity claim, not a production-scale class-number-one argument.

**Hypothesis attacked:** enlarging admissible observation support monotonically increases an inert prime's divisor depth of the same original determinant.

**Predicted control:** the original real trace Gram increases under `Q_1 ⊆ Q_2 ⊆ Q_3`, but at least one inert-prime p-adic valuation decreases. Report both p=3 and p=5, no cherry-picking.

## Classical calculation and exact outcomes

The only source row is `Z^0 W^0 = 1` at derivative order 0. For every positive D and every finite integer-pair set Q,

```text
G_Q = [2 * |Q|]       (original 2,2D trace pairing).
```

When `rho < sqrt(D)`, the complete ellipse has only horizontal-axis points `(x,0)`, `-rho <= x <= rho`. At D=163 and rho=1,2,3:

| radius | complete ellipse size | original 1x1 det | v3(det) | v5(det) |
|---|---:|---:|---:|---:|
| 1 | 3 | 6 | 1 | 0 |
| 2 | 5 | 10 | 0 | 1 |
| 3 | 7 | 14 | 0 | 0 |

Both p=3 and p=5 are inert since -163 is a nonsquare modulo both. Both satisfy p<163/4; neither the inertness nor the known class-number-one status of Q(sqrt(-163)) is a new derivation. The change rho=1->2 decreases v3 but increases v5, while rho=2->3 decreases v5. The real determinants strictly increase throughout.

The exact support nesting, point counts, determinant values, local nonsquare controls, opposite-prime valuations and second-step drop are encoded as independent kernel-computable propositions in `lean/TenthDiscriminant/Phase276BreathingValuation.lean`. Their true verification status is **pending exact-head CI**; do not cite this file as formally proved until that check passes. The separate Python regression recreates the original jet/trace evaluator from Phase204 and compares against the closed 2*|Q| formula.

## Real-positive order versus local arithmetic

For arbitrary fixed source D,R,S,J and finite Q⊆Q', every added ordinary-jet observation contributes a positive-semidefinite real matrix to the original trace Gram. Therefore `G_{Q'} >= G_Q` in Loewner order. In particular its **real determinant is nondecreasing** for positive-semidefinite Grams, and strictly increases in the one-row example. This is elementary real Gram algebra [P-paper], not yet a general Lean theorem in Phase276.

There is **no corresponding universal monotonicity law for v_p(det G_Q)**, even when p is inert and Q,Q' are complete nested ellipses. In this example the valuation moves oppositely at two inert primes. Therefore positive-semidefinite support expansion and a uniform p-adic prime-mass increase are *inequivalent objectives*.

A general bound of the form `v_p(det G_{Q'}) >= v_p(det G_Q)` under mere support inclusion is **refuted** by these exact instances. A new bound can survive only with additional hypotheses that hold for the actual production source, including R=floor(D/4), S=J=floor(R/25), the required radius, the combined Frobenius frame, and non-overlap with all already-counted factors.

## Provenance and known prior art

The general constant-row behavior extends Phase167's one/two/empty-node controls. Phase205 (#139) already distinguishes evaluation-index contributions from restricted pairing radicals; Phase206 (#143) already measures finite deeper Smith layers. This is a **new negative regression at source-parameter level**, not a new mathematical field theorem or priority claim. It does not establish a stronger `321^4` cutoff, an exceptional-zero exclusion, or a uniform asymptotic obstruction.

**Kill condition:** if a script computes any nonoriginal source determinant, loses one signed channel, or the Lean same-source tuple differs from (6,10,14), the interpretation is withdrawn. **Stop condition:** do not invoke extra geometric, hypercomplex, or adiabatic terminology to restore an unproved monotone p-valuation. **Promotion:** exact-head root Lean + axiom/source/negative audit and focused source regression make this a checked finite counterexample only. Independent human semantics remains open under issue #50.
