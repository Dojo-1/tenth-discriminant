# One integer, several faithful descriptions

**This branch integrates the 47.5-billion bound and two structural interfaces.**
All four local checks pass. Main retains the published 48-billion theorem;
exact-head CI and publication are recorded in the draft PR. Independent human
semantic review remains open. [Evidence and limits](PHASE128_VERIFICATION.md).

## The object before its coordinates

Let K be any imaginary quadratic number field with class number one.
Write D for its actual absolute field discriminant. A squarefree radicand
is a coordinate description: in the odd chart D equals the radicand; in the
even chart it is four times the radicand. The field equivalences in the proof
preserve class number and actual discriminant. They do not erase that factor.

In the odd chart, take integer-coordinate points in a norm ellipse. Observe
the monomials Z^r W^s and their ordinary Z-derivatives, holding W fixed,
with W specialized to the conjugate point. Splitting each value into its two
integer coordinates gives an integer observation matrix E. Its weighted Gram
is exactly G=E B E^t, with repeated blocks B=diag(2,2D). This is the original
trace-Gram, including its factor two; we do not replace it with an easier matrix.

## Why arithmetic supplies the factor twice

For each eligible odd prime p, class number one and the strict small-prime
norm obstruction imply that -D is nonsquare modulo p. Consequently Z^p-W
and all its relevant ordinary derivatives vanish modulo p on these samples.
Powers of that polynomial provide rows divisible by matching powers of p.

The actual integer basis matrix U_p has determinant one. Its observation
identity is U_p E=Delta Ehat, where Ehat is INTEGER and Delta has entries p^k.
Therefore

    U_p G U_p^t = Delta K_p Delta,   K_p=Ehat B Ehat^t integral.

Taking determinants gives p^(2 sum k) dividing det G. The two copies of Delta,
and the integral middle matrix, justify the exponent 2F(p). Row divisibility
alone would not justify doubling the exponent. [Full derivation](TWO_SIDED_ARITHMETIC_GUIDE.md).

## Why geometry bounds that very same integer

Cell-area estimates at the chosen radius give enough distinct sample points
for the ordinary jets to separate the rectangular polynomial space. Thus G
is positive definite and det G is a positive integer. The guards are explicit.

Now center the radial variable ZW using an integer matrix T_a of determinant
one. It changes row lengths, but det(T_a G T_a^t)=det G. Careful derivative
estimates, radius rounding and both point counts give a smaller Hadamard
ceiling. The arithmetic divisors still belong to that original determinant.
[All geometric inequalities](GEOMETRIC_COMPARISON_GUIDE.md).

With C=R^2 S>0, the inherited factorial/tail lower estimate and radial upper
estimate meet as

    0.999997 log D - 5.739 <= log(det G)/C <= 0.8 log D - 0.823.

For D>=47,500,000,000 the fixed rational logarithm certificate proves
log D>=24.582. The left expression exceeds the right by at least
0.000326254: contradiction. The final theorem handles the even chart and
transports to arbitrary K without a caller-supplied generator. This bound
does not assume the known list or the earlier cutoff. [Actual API](../../lean/TenthDiscriminant/EndpointCutoff.lean).

## What the structural additions contribute

The actual radial matrices satisfy T_0=I and T_a T_b=T_(a+b), with inverses,
on each fixed rectangle. A zero-sum parameter loop returns the frame, every
jet and the Gram. This is a linear action, not a ring automorphism; a fixed
counterexample proves the distinction. It gives no additional prime power,
and no commutation with U_p is assumed. [Radial laws](RADIAL_ACTION_CURRENT.md).

Separately, the arbitrary-field iff transports the existing canonical
classification and its 700-billion finite endgame. It is a cleaner interface,
not a new classification method or an application of this smaller cutoff.
[Exact meaning](CLASSIFICATION_INTERFACE_CURRENT.md).

The invariant is the thread connecting these descriptions. A transport is
useful only when its domain, preserved quantity and required guards are stated.
Kernel checks establish the encoded statements; a mathematician must still
judge their intended meaning. [Verification layers](VERIFICATION_LAYERS_CURRENT.md).
