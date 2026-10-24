# Keep the primes fixed; let the dimensions vary

**Later update (Phase 28):** the estimates below now feed a universal
odd-discriminant cutoff. See the [short cutoff proof](ODD_CUTOFF_GUIDE.md).
The original Phase 27 scope and pilot below remain historical records.

The first interval is already excluded in Lean. The next problem is to
extend the argument without generating a new 1229-row prime-power table
for every rectangle. Phase 27 proves the arithmetic estimate in a form
that separates changing dimensions from fixed prime information.

This is a general bound, **not a new global class-number exclusion**.

## The two elementary estimates

Write `V=R(R−1)/2`, `W=R(R−1)(2R−1)/6`, and `a=S−1/2`.

Each floor loses less than one, so summing over R rows gives

    floorSum(R,p) ≥ V/p − R.

Bounding each prime-power floor sum from above and summing the geometric
series gives

    factorialPowerSum(R,p) ≤ V/(p−1).

The determinant weight is not the factorial weight. The checked global
staircase inequality, including its quadratic loss, gives

    valuationWeight(R,S,p) ≥ a*(V/p−R) − W/(2p²).

The `−R` error and the quadratic loss are essential. Lean includes concrete
counterexamples to omitting them. It also rejects removing `S≥1` or allowing
prime two into the retained odd-prime sum.

## Four constants, certified once

For all primes `p≤10000`, define A as the sum of `log(p)/(p−1)`.
For retained primes `7≤p≤10000`, define B, C and E as the sums of
`log(p)/p`, `log(p)/p²` and `log(p)`, respectively. The exact certified bounds are:

| Constant | Bound |
|---|---:|
| A | ≤ 8.646130782816 |
| B | ≥ 6.856198325360 |
| C | ≤ 0.133259338177 |
| E | ≤ 9892.590181957053 |

These are terminating rational bounds, not floating-point assumptions.
Prime coverage and log enclosures are reused from the checked first interval.
Each new rounding is checked by integer cross multiplication, with exact
row pairing and exact chunk totals. The generator is not trusted.

For every `R≥2` and `S≥1`, Lean therefore proves

    factorialSmallMass(R,10000) ≤ V*A_upper
    smallOddValuationMass(R,S,10000)
      ≥ a*V*B_lower − a*R*E_upper − W*C_upper/2.

The signs explain the rounding directions: the positive B contribution uses
a lower bound, while the two subtracted contributions use upper bounds.
Wrong-direction rounding and a missing certificate row have rejection controls.

## What this removes—and what it does not

The four constants have no R or S in them. Future intervals can use the
same certificates; they need not repeat large prime-power computations.
Both clipped contributions remain below the unchanged production lower
bound on the **same actual determinant**. The fixed reciprocal-tail budget
is also reusable: its proof depends only on `P=10000`, not the interval.

The registered pilot recovers the original first interval's two budgets
without changing Q, P, radius, rounding scale, or a numerical target. Lean
now proves that recovery, not just the external rational calculation.

This does not supply the geometric guards or strict upper-versus-lower
comparison for another interval. The other 249 intervals, unbounded closure,
even-discriminant cases and finite classification remain open. No new
optimized cutoff, novelty or independent human-review claim is made.

## Source map

- [Uniform estimates](../../lean/TenthDiscriminant/UniformPrimeMass.lean): elementary bounds,
  clipping, counterexamples and composition to the actual-Gram comparison.
- [Rounding checker](../../lean/TenthDiscriminant/PrimeLogCertificate.lean): sound pairing and aggregation.
- [Fixed constants](../../lean/TenthDiscriminant/PrimeLogConstants.lean): checked finite certificates.
- [Reusable comparison](../../lean/TenthDiscriminant/UniformPrimeMassCertified.lean): arbitrary R,S
  with four literal constants, rational tail budget and unchanged interval guards.
- [Preregistration](PHASE27_PROTOCOL.md) and [recorded results](PHASE27_RESULTS.json).

Run from `lean/`: `lake build`, `python verify_sources.py`, `python audit.py`,
`python negative_controls.py`. Source correspondence alone does not certify
numerical inequalities. Complete pinned CI must be attached to the exact
published commit/tree; local parent-driver timeouts remain separately recorded.
