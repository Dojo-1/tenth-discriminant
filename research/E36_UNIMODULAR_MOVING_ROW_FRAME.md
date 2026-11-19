# E36 — THE PRIME FACTOR MOVES WITH AN INTEGRAL ROW FRAME

*19 November 2026 · research-only, stacked on E35.*

## An adversarial limit to E35

E35 proves a useful SUFFICIENT condition: if every actual original
jet coefficient in the second rectangular row is p-divisible,
then p² divides the actual original two-row integer Gram
determinant.

It is NOT a necessary condition, even when the determinant
has a genuine p² factor.

Consider the same source algebra D=25, derivative convention
J=1,R=2,S=1 and original support

    Qshift={(1,0),(6,0)}.

The exact source original Gram is

    Gshift=[[4,14],[14,74]], det=100.

The original second-row ordinary-Z jet values at the two points
are 1 and 6, neither divisible by 5. The offdiagonal entry
14 is also not divisible by 5. Thus E35's raw absolute
coordinate-row premise fails, **yet 25 divides det(Gshift)**.

## The genuinely compatible moving frame

Within the SAME original two-row polynomial space (1,Z), move
to the integral row basis (1,Z-1). This uses

    U=[[1,0],[-1,1]], det(U)=1.

On the ORIGINAL Qshift, without resampling or changing derivatives,

    U Gshift U^T = [[4,10],[10,50]].

The right-hand matrix is numerically equal to the E34
positive control on Qfive={(0,0),(5,0)}, but this equality
is a *comparison of exact matrices after an allowed integral
row transformation*. E36 never declares Qshift=Qfive or
replaces the source in its theorem.

The moved second row now has the p=5 factor that the
absolute original (1,Z) row basis concealed. The determinant
is unchanged by unimodular congruence, so the prime-square
divisibility is genuine and survives frame transport.

## What survives, and what does not

**Invariant at this finite original source:**
- original determinant and prime valuation,
- original sampled support Qshift,
- ordinary derivative convention and positive trace,
- existence of an integer unimodular row basis showing
  p-divisible original-jet observations.

**Covariant, not invariant:**
- offdiagonal Gram entries and the particular choice of
  absolute row with p-divisible coefficients,
- the coordinate matrices and row-label interpretation.

**Not established:**
- a universal n-row Smith/decomposition theorem,
- an improved 307⁴ actual-field cutoff,
- a new computational complexity hardness signal,
- sheaf curvature or nontrivial geometric holonomy.

This is an example of integral arithmetic frame compatibility,
not proof that a geometric lift automatically finds a better bound.

## Required controls for the 307 bridge

1. Generalize to an integer unimodular U acting on the original
   complete rectangular ordinary-jet row index set.
2. Prove the equality G' = U G U^T on the actual source, retaining
   SAME Q, derivative slots, trace metric, positivity and support.
3. Prove p-divisibility of the transformed original jet row
   coefficients. No auxiliary minor, resampling or untracked
   denominator may enter.
4. Check the p² factor with a genuine unimodular certificate;
   reject determinant gains manufactured by nonunimodular U.
5. Only then insert the factor into the independently audited
   Phase350 same-source arithmetic lower and analytic upper.

A negative control: multiplying a row by 5 is NOT unimodular
and produces an artificial determinant factor. E36 uses det(U)=1.

## Release gate

Lean: TenthDiscriminant/E36UnimodularMovingRowFrame.lean
CI: e36-moving-original-row-frame.yml
Stack: E35 #240 → E34 #239 → E33 #238 → E32 #237, etc.

A passed focused Lean build establishes the encoded finite
claims, not field-level source-fidelity or external novelty.
