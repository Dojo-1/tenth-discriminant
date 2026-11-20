# E44 — A LABELLED CRT OBSERVER CAN SEPARATE A GRAM FIBER

19 November 2026 · source-locked observer comparison, NOT a field-bound gain.

## Correct common carrier and source

The compared finite supports lie in the SAME Gaussian integer-pair
ring D=1. The original ordinary-jet positive trace Gram is computed
with the exact same Q,J,R,S; the additional observation is not
silently substituted for the original determinant.

Qplus={(0,1),(1,1)}
Qmixed={(0,1),(1,-1)}

E43 proposes the source-exact original Gram equivalence
    G(Qplus,1,J,R,S)=G(Qmixed,1,J,R,S)
for every original J,R,S, by an injective per-point conjugation.

## New instrument, not new determinant

E33 defines two LABELLED Gaussian split-prime residues mod 5:
    r_plus(a,b)=a-2b,
    r_minus(a,b)=a+2b.

Their difference is
    gap(a,b)=r_minus-r_plus = 4b (mod 5).

Apply the exact E33 gap to each ORIGINAL sample and sum over Q:
    totalGap(Q)=sum_{q in Q} gap(q).

On the two supports:
    totalGap(Qplus)=3 (mod5),
    totalGap(Qmixed)=0 (mod5).

Thus the ADDITIONAL labelled CRT observation distinguishes these
two supports even though the entire ORIGINAL positive trace-Gram
does not, for any unchanged jet rectangle.

This is not a full source-recovery result. A different support
Qmirror={(0,-1),(1,1)} also has totalGap=0 and the same
complete Gram as Qmixed, but is not equal to Qmixed.

## Necessary source-algebra and evidence boundaries

- This CRT probe is defined for D=1, where 2+i and 2-i are
  the Gaussian split-prime labels above 5.
- Evaluating the SAME Gaussian multiplication probe as if it were
  a ring homomorphism for D=3 would be a regime error.
- The labelled gap is additive, not a ring homomorphism.
- Without ordered plus/minus labels, sign information can be lost.
- The original trace Gram remains unchanged: no extra prime factor
  or 307^4 analytic/arithmetic gap is created by adding a new probe.
- HK-032/033 established complementary labelled Gaussian
  residue reconstruction and source Bézout witnesses separately.
  E44 reuses the Tenth source's E33 native labelled versions,
  not an unverified imported Lean theorem from HK.
- E31 proves that ambient coefficient-information loss does
  not force original-Gram prime divisibility.
- Distinguish provable instrument refinement from solver advantage,
  awareness, curvature, nontrivial holonomy, or ETH/P vs NP claims.

## Release

Lean source: lean/TenthDiscriminant/E44LabelledCRTObserverRefinement.lean
Focused CI: .github/workflows/e44-labelled-crt-observer-refinement.yml
Stack: E43 #255 → E41 #253; E33 #238 is an earlier existing module.

The new theorem candidates are H until exact-head focused and
full-root Lean/axiom checks pass. Bounded integer simulations,
where available, are M and not substitutes for formal verification.

## Next discriminating test

Compare additive tagged CRT observations against alternative
orientation-sensitive controls with identical measured information
and cost. Pre-register the original carrier, any branch transition,
reconstruction metric, accidental collisions and stop rule.

Do not interpret an enriched observer as an invariant of the
original positive trace Gram without a proved typed arrow.
