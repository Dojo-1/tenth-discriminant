# Why the odd-discriminant bridge now closes

## The result, before the machinery

Lean accepts the following statement:

> If D is squarefree, D is 3 modulo 4, and D >= 700000000000,
> then the quadratic field of discriminant -D does not have class number one.

The precise encoded field is `QuadraticField (((D : Int)+1)/4)`, generated
by a root of `X^2-X+(D+1)/4`. Its discriminant is -D in this arithmetic
class. The public declaration is
`TenthDiscriminant.FirstCertificate.odd_large_classNumber_ne_one` in
[UniformUpperEnvelope.lean](../../lean/TenthDiscriminant/UniformUpperEnvelope.lean).
It has no radius, numerical-comparison or finite-certificate premise.

**This is an odd-discriminant cutoff, not the full classification.** Even
fundamental discriminants, the finite endgame below the cutoff, independent
human semantic review and Mathlib-upstream suitability remain separate.
The frozen 250-interval campaign is preserved, not retrospectively declared
kernel-checked. The universal proof avoids needing its other 249 comparisons
for this odd-discriminant statement.

## The contradiction in one sentence

If class number one held, arithmetic would force one positive integer Gram
determinant to be too divisible by small primes to fit inside its geometric
upper bound.

The earlier bridges already connected class number one, inertness, ordinary
derivatives, integer divisibility, real positivity and Hadamard's bound for
the **same actual Gram**. Phase 27 reduced the remaining arithmetic to four
fixed certified prime-log constants. Phase 28 makes the final comparison
uniform in D.

## Choose one family; keep both sides on it

Put

    R = floor(D/4), S = floor(R/20), t = D^(1/4),
    rho = ceil((11/20)*t^3), T = R^2*S, u = log D.

The radius is a **new auxiliary choice**, not the frozen campaign's chosen
radius. We instantiate the existing generic construction at this rho; the
upper and lower estimates never switch determinants mid-argument.

Lean proves every floor, ceiling and geometric guard. In particular,
`R >= D/5`, `R/21 <= S <= R/20`, `t >= 300`, `rho < R`, and the required
chosen-radius lower bound all hold. The padded point-count input is at most
`4D`. The strict inertness endpoint uses `D = 3 mod 4`, not an inclusive
approximation.

## Divide out the shared size

Both logarithmic bounds grow like T. Dividing by this positive quantity
reveals the comparison rather than changing it.

For the unchanged production upper expression U, the exact identity is

    U/T = log(2*n*S)/R + (1-S/R)*log rho
          + 2*(S-1)/R*(log R-1)
          + 2*(S-1)/R^2*(rho+log(R/rho)).

The last term is retained. The derivative correction cancels just enough
radius dependence to expose the coefficient `13/16` of log D.

The lower expression keeps the floor error, quadratic loss and all prime
powers. Removing the two clipping maxima only weakens it, so that removal
is valid even without asserting signs. The four certified constants are
reused unchanged.

The checked envelopes are

    L_raw/T >= 0.999997*u - 5.845,
    U/T     <= 0.8125*u   - 0.7965.

These decimal constants are exact rationals. No measured floating-point
inequality is an assumption of the theorem.

## Why the error bounds stay small

The main lower-bound losses are the triangular sum, the floor error and
the quadratic moment. On our family, `R <= 21S` makes the quadratic loss
uniform after normalization. The predecessor log is controlled by the
elementary inequality `1-1/x <= log x`; no limiting argument is substituted
for a finite bound.

On the upper side, `log D <= 2*sqrt D` gives `log D/R <= 1/9000`.
The count-log contribution is at most `1/4000`; the final correction is at
most `1/1000`. Only coarse checked pi bounds `3 < pi < 4` are needed for
the new geometry/count estimates. Large exact log and prime certificates
are reused rather than regenerated.

Finally `u >= 27`. Subtracting the two affine envelopes gives at least

    (0.999997-0.8125)*27 - (5.845-0.7965) = 0.013919 > 0.

Thus `U < L_raw <= L_certified`. But class number one forces
`L_certified <= U` on the same Gram. That is the contradiction.

## What was tested, what was proved, what remains

The [preregistered](PHASE28_PROTOCOL.md) single Arb pilot used
`D=700000000003`, 256-bit balls, `rho=420907069`, and `Y=503`. All its
checks passed; its normalized gap is about 0.34782349. It was a diagnostic,
not the universal proof. The [record](PHASE28_PILOT.json) preserves ball
enclosures and exact inputs. No radius/threshold search was performed.

The universal result is supplied by the Lean proofs, including the two
envelopes and all guards. Development failures (definition unfolding,
cast/rewrite mismatches and a proof-search deadline) are retained separately
from mathematical counterexamples. Controls reject a zero normalization,
the same affine comparison at u=26, and an identity missing its final term.

Source map: [normalization](../../lean/TenthDiscriminant/NormalizedComparison.lean),
[lower envelope](../../lean/TenthDiscriminant/UniformLowerEnvelope.lean),
[family and geometry](../../lean/TenthDiscriminant/UniformRadiusFamily.lean),
[upper envelope and final theorem](../../lean/TenthDiscriminant/UniformUpperEnvelope.lean).

From `lean/`, run `lake build`, `python verify_sources.py`, `python audit.py`,
and `python negative_controls.py`. Exact published-commit/tree CI and audit
results belong in the PR verification record. Passing source correspondence
alone is not a numerical proof; a local parent timeout is not a full audit pass.

No optimized threshold, novelty, human-review verdict, Tao endorsement or
full class-number classification is claimed. The next mathematical work is
the even-discriminant chart and the finite classification, not more isolated
matrix identities.
