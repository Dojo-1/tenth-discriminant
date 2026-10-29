# Why the prime power appears twice

Every transformed observation has an integral prime-power factor. Pairing two
observations therefore supplies two factors, including at a diagonal entry.
The point is to establish this before taking determinants. Here is the
calculation for the actual matrix, with no substitute observation family.

This is a mathematical reconstruction by the same assistant, not a new
independent peer review. The finite check below supports its implementation;
the universal argument is the sequence of identities and divisibilities here.
Existing Lean statements are mapped at the end. No new cutoff is claimed.

## 1. Identify the integer before changing its coordinates

Fix D>0, a finite set Q of distinct integer pairs, and row labels
0<=r<R, 0<=s<S. Work in A=Z[t]/(t^2+D), writing z=x+yt and bar(z)=x-yt.
This selected order is not silently identified with the full ring of integers.
When D is squarefree, K=Q(sqrt(-D)) has actual signed field discriminant
-D for D congruent to 3 modulo 4, and -4D otherwise. The local matrix
argument itself needs no squarefreeness assumption.
At each z from Q take j=0,...,J-1 ORDINARY Z-derivatives of Z^r W^s,
with W held fixed, then substitute (Z,W)=(z,bar(z)):

\[
v_{r,s}(z,j)=(r)_j z^{r-j}\bar z^s\quad(j\le r),\qquad v_{r,s}=0\quad(j>r).
\]

Here (r)_j is a falling factorial. Put BOTH integer coordinates of these
values into E, one row per (r,s). Let B repeat the diagonal pair (2,2D)
for every original sample and derivative. The integer Gram is exactly

\[
G=E B E^T,\qquad G_{i\ell}=\sum_{z,j}2(x_i x_\ell+D y_i y_\ell).
\]

Under t -> i sqrt(D), this pairing is 2 Re(v_i conjugate(v_l)). This is
precisely integerRectangularTraceGram, including its factor 2 and row order.
All sample and derivative slots remain present; no residue-image set replaces Q.

## 2. The local congruence and why differentiation preserves a factor

Let p be an odd prime and assume -D is nonsquare modulo p. Reduce the two
integer coordinates modulo p. In this ring tau^2=-D. Euler's criterion gives
(-D)^((p-1)/2)=-1, hence tau^p=-tau. The characteristic-p binomial identity
and x^p=x for scalars give (x+y tau)^p=x-y tau for every pair. Thus

\[
z^p-\bar z\in pA.
\]

For completeness, Euler's criterion here needs only elementary finite-field
counting: the (p-1)/2 nonzero squares satisfy X^((p-1)/2)=1 by Fermat;
this polynomial has at most that many roots. A nonsquare is not one of them,
and its half-power squares to 1, so it must be -1.

For H(Z)=Z^p-bar(z), the zeroth derivative has this p factor. Every positive
ordinary derivative has the coefficient p(p-1)...(p-j+1), or is zero for
j>p. Consequently EVERY derivative of H at z belongs to pA. In every term
of the higher product rule for C(Z)H(Z)^k, each of the k copies of H supplies
one such factor, irrespective of how derivatives are distributed:

\[
\partial_Z^j(C H^k)(z)\in p^k A\quad\text{for every }j.
\]

No factorial is inverted. This fails for divided/Hasse derivatives: the third
Hasse derivative of Z^3 is 1, whereas the ordinary derivative is 6.

## 3. A change of observations inside the same rectangular lattice

Assign row (r,s) the weight k=min(floor(r/p),S-1-s). Replace its monomial by

\[
P_{r,s}=Z^{r-pk}W^s(Z^p-W)^k
 =\sum_{a=0}^k(-1)^a\binom{k}{a}Z^{r-pa}W^{s+a}.
\]

All exponents stay inside the original rectangle: pk<=r and s+k<S.
The leading monomial is Z^r W^s with coefficient 1. Other terms precede it
in row-major order rS+s; their index drops by a(pS-1). If S=1, k=0 and
there are no other terms. Thus the integer coefficient matrix U_p is lower
unitriangular and det(U_p)=1. It depends on the row labels and p, not on Q.
Differentiation is linear, so its action on the original jets is exactly
U_p E. Section 2 applies to every new row, giving coordinatewise divisibility
by p^k at EVERY original slot.

## 4. Construct the integral middle matrix; do not assume it

Let Delta_p=diag(p^k). Divide each coordinate of transformed row i by p^k_i.
Section 3 proves these quotients are integers. Call their matrix Ehat. Then

\[
U_p E=\Delta_p\widehat E,\qquad
U_p G U_p^T=\Delta_p K_p\Delta_p,\qquad K_p=\widehat E B\widehat E^T\in M_n(\mathbb Z).
\]

The shared pivot is not an exception: entry (i,i) is p^(2k_i) times the
integer (K_p)_(i,i). Merely knowing that row i and column i are divisible
by p^k_i would NOT establish this; the one-entry matrix [p] disproves that
shortcut. The integral quotient observations are the missing witness.

Taking determinants now gives an exact integer equality:

\[
\det G=p^{2\sum k_i}\det K_p,\qquad
\sum k_i=\sum_{r<R}\sum_{s<S}\min(\lfloor r/p\rfloor,S-1-s)
       =\sum_{r<R}\sum_{a<S}\min(\lfloor r/p\rfloor,a)=F(p).
\]

The second equality just reverses the s index. Therefore p^(2F(p)) divides
THE ORIGINAL det(G). Positivity, class number and ellipse geometry have not
been used to obtain this local divisibility. Empty row sets have determinant
1 and F=0; empty observations give zero determinants when there are rows.

## 5. Where class number one enters, and where positivity enters

For squarefree D congruent to 3 modulo 4, the maximal order has basis
1,omega=(1+t)/2. If Z^2+D has a root modulo an odd p, the root defines a
surjection O_K -> F_p, with kernel an ideal of norm p. Class number one
makes it principal. Its generator has absolute norm p; imaginary-quadratic
norm positivity makes its norm p. In the maximal-order coordinates,

\[
4p=(2x+y)^2+D y^2.
\]

If y=0, p=x^2 is impossible. Otherwise 4p>=D. But p<(D+1)/4 implies
4p<=D; equality is impossible since D is 3 mod 4. This contradiction
supplies nonsquareness, and only for the guarded prime range. D=163,p=41
is exactly the excluded endpoint and has a residue root. The selected-order
calculation above never needed to pretend that its lattice was maximal.

Separately, D>0 makes the complex coordinate map injective. Interpolation
with R,S>=1, J>=S and |Q|>2(R-1)+(S-1) makes G positive definite, hence
detG a positive integer. Distinct eligible prime powers are coprime, so
their product divides detG and cannot exceed it. Logarithms are taken only
now, yielding the arithmetic lower pressure on that SAME integer.

## 6. Two frames can serve different purposes

The arithmetic frame U_p exposes prime factors. The later radial frame
T_a improves geometric row bounds and also has determinant 1. They need
not commute, be isometries or be the same frame: each is explicitly anchored
to G. The determinant comparison uses this shared invariant. It does not
infer preserved row norms, real rank after prime reduction, or a new ring
automorphism from determinant equality.

## Exact source correspondence and evidence boundary

| Step | Existing Lean declarations |
|---|---|
| Original coordinates and factor-two Gram | [IntegerTraceGram](../../lean/TenthDiscriminant/IntegerTraceGram.lean): integerDerivativeRow, integerRectangularTraceGram_cast |
| Local conjugating Frobenius | [InertFrobenius](../../lean/TenthDiscriminant/InertFrobenius.lean): integerPair_frobenius_of_nonsquare |
| All ordinary derivatives retain each factor | [JetPower](../../lean/TenthDiscriminant/JetPower.lean): frobenius_polynomial_power_dvd |
| Exact integral basis and actual jet action | [RectangularBasisMatrix](../../lean/TenthDiscriminant/RectangularBasisMatrix.lean): rectangularBasisMatrix_det; [RectangularRowAction](../../lean/TenthDiscriminant/RectangularRowAction.lean): rectangularBasisMatrix_integerDerivativeRow_action |
| Integral quotients and two-sided identity | [RectangularGramFactor](../../lean/TenthDiscriminant/RectangularGramFactor.lean): rectangularNormalizedJet, rectangularTraceGram_basis_factor_of_frobenius |
| Weight sum and determinant exponent | [RectangularValuation](../../lean/TenthDiscriminant/RectangularValuation.lean): sum_rectangularBasisExponent; [GramDivisibility](../../lean/TenthDiscriminant/GramDivisibility.lean): pow_dvd_det_of_unimodular_gram_factor |
| Actual maximal-order class-number premise | [ClassNumberInertBridge](../../lean/TenthDiscriminant/ClassNumberInertBridge.lean): rectangularTraceGram_valuation_of_classNumber_one |

These inherited modules are byte-identical to Argon's frozen39e9ce3 source.
Argon did not complete kernel replay or independently close this factorization.
This reconstruction supplies a checkable derivation, not an endorsement from
Argon. Current project CI and independent semantic review remain separate.
[Phase123 protocol](PHASE123_PROTOCOL.md) records one sealed exact check of
80 cases, 15,840 jet coordinates and four negative controls; all passed.
Eighteen zero determinants remain zero. Finite checks do not prove the
universal quantifiers. Memory was not measured. [Current proof](FORTY_EIGHT_BILLION_GUIDE.md).
