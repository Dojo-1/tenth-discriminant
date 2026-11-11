# Phase273 — sharp p-adic tubular jet transport

**Design before the finite tests.** Primary: preserve the original ordinary-Z derivative convention with W held fixed; compare the first J jets before and after an integer translation by p modulo p². Positive control: J>=p. Negative control: J<p, f=(X-a)^J. Multi-prime finite test: p=2,3,5,7; J=p,p+1,p+3, a=-2,0,1, translations -p,p,2p, monomials through degree 2p+4; negative tests every J<p. Group-law test: U_p U_-p=id and U_p²=U_2p on the full truncated jet vector. These deterministic checks are not independent external validation.

## General paper-level theorem (not yet generalized in Lean)

Let p be prime, J>=1, a an integer, and set
j_a^J(f)=(f(a),f'(a),...,f^(J-1)(a)) modulo p²
for f in Z[X]. For delta=p*t with t not divisible by p, the following are equivalent:

1. There is a well-defined function L on the set of J-jet vectors modulo p² satisfying L(j_a^J(f))=j_{a+delta}^J(f) for every integer polynomial f.
2. J>=p.

If J>=p, a stronger statement holds: the explicit linear map
`(L_delta v)_i = v_i + delta*v_(i+1)` for i<J-1 and
`(L_delta v)_(J-1)=v_(J-1)` works on the entire ambient module
(R=Z/p²)^J. It is invertible, and
L_delta L_eta=L_(delta+eta) for delta,eta divisible by p (because
delta*eta=0 modulo p²).

**Proof.** For any integer polynomial g,
g(a+delta)=g(a)+delta*g'(a) mod p² because every term of degree >=2 in
the integer binomial expansion is divisible by delta². Apply to g=f^(i).
At i<J-1, the required next derivative is present in the input. At
i=J-1, the missing f^(J)(a) is divisible by J!, hence by p when J>=p.
Therefore delta*f^(J)(a)=0 mod p².

If J<p, take f=(X-a)^J and g=0. Their first J ordinary derivatives
at a vanish identically, but f^(J-1)(a+delta)=J!*delta is nonzero
modulo p² because J! is prime to p and delta has p-adic valuation
exactly one. Hence NO function on the reduced jets can implement this
translation for all integer polynomials.

This threshold is *different* from Phase272's global unit-translation
result on the degree-bounded space P_m over F_p: that transport exists
for m<p. Confusing domain and precision reverses the conclusion.

## Hasse-to-ordinary return and the missing jet

For polynomials of degree <=m, the ordinary-vs-Hasse diagonal is
F_m=diag(0!,...,m!). Over Q_p the conjugate of the Hasse translation is
`(L_delta)_{i,j}=delta^(j-i)/(j-i)!` for i<=j.
At delta in p Z_p these coefficients are p-adic integers
by Legendre's factorial valuation bound.
For unit delta and m>=p the i=0,j=p entry is nonintegral, and
mod p^e descent fails for every e>=1 using f=p^(e-1)(X-a)^p.
Over Z_p itself, however, F_m is INJECTIVE: unit translation still
acts on the *image lattice* F_m Z_p^(m+1). It generally cannot be
extended as a Z_p-linear operator on the entire ambient ordinary-jet
module. Do not confuse a rational change of coordinates, an integral
extension, and modular information loss.

## Connection to the original bivariate tenth-discriminant Gram

This is a directional univariate result and does not change the
production source. At a real-axis translation, BOTH Z and W shift
together. For bivariate F(Z,W), the correct modulo-p² first-order law
is
`partial_Z^i F(Z+delta,W+delta) =
 partial_Z^i F(Z,W) +
 delta*(partial_Z^(i+1)F + partial_W partial_Z^i F)(Z,W)`,
with the top Z-jet term suppressed precisely when J>=p.
Phase204 previously implemented the corresponding W-lowering row
term for monomials; Phase273 establishes the sharp J threshold
for arbitrary Z-polynomials. No new Gram determinant valuation
follows from this transport alone.

**No-go for factorial overcount.** For an illustrative one-row
evaluation E_H=[1,1], column factorial matrix F=diag(1,p!),
metric B=diag(2,2), the ordinary Gram is
`2*(1+(p!)²)`, whose p-valuation is ZERO for odd p. Thus one
nonunit factorial column does not by itself force a p factor in the
determinant of an oversampled rectangular Gram. Any claimed new
prime-mass contribution must compare all maximal minors and avoid
recounting Frobenius row factors.

## Local geometric interpretation

The first-order near-identity translations form a *flat*
unipotent representation: L_delta L_eta=L_eta L_delta=L_(delta+eta).
A 'diamond' composed of such moves has TRIVIAL holonomy.
There is presently no constructed nonflat connection or new
holonomy invariant here. The genuine obstruction is precisely
failure of translation to descend to truncated reduced ordinary
jets below the sharp depth threshold.

**Evidence:** the general theorem is a paper derivation [P-paper];
the bounded arithmetic controls are finite [M] once executed;
the new Lean file is a candidate until exact-head build/axiom audit.
No new field cutoff, exceptional-zero result, or mathematical novelty
claim is made.

**Next check:** run exact-head compilation, then independently audit
whether the full original rectangular source, at all chosen local
primes and actual ellipse supports, has any unaccounted residual
Smith depth after factorial and Frobenius budgets are subtracted ONCE.
A split-prime control and all original derivatives are mandatory.
