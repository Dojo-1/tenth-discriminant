# Phase274 — sharp p-adic precision horizon for moving ordinary jets

**Origin and evidence.** Motivating Leibniz–Newton/SDG synthesis is user-supplied; exact general result below is a paper derivation from classical integer-polynomial Taylor algebra, not a new field theorem. Existing repository Phase146/155/204 already covers integral translations, factorial-vs-Hasse precision, and the p² tube at J=p. This note sharpens the *univariate directional* precision threshold and distinguishes degree-bounded from arbitrary-degree domains. General Lean proof is OPEN. Local finite tests are deterministic model-authored evidence, not independent peer review.

## Exact theorem (paper proof)

Let p be a prime, e>=1, J>=1, a an integer, and u a nonzero integer with s=v_p(u)>=1. Define the retained **ordinary derivative jet**

  j_a^J(f) := (f(a),f'(a),...,f^(J-1)(a)) mod p^e

for **all** polynomials f in Z[X], with no restriction on degree. Then the following are equivalent:

1. There exists **some function**, not assumed linear, from the set of attainable retained ordinary jets to itself that sends j_a^J(f) to j_(a+u)^J(f) for EVERY integer polynomial f.
2. e <= s + v_p(J!).

If the inequality holds, a canonical **linear automorphism of the full ambient module** (Z/p^e)^J supplies the transport. In upper-triangular coordinates, for 0<=i<=k<J,

  (L_u)_(i,k) = u^(k-i)/(k-i)!  (interpreted as a p-adic integer mod p^e).

All other entries vanish. Here u^d/d! lies in Z_p because
d*s >= d > v_p(d!) for d>0. This is an integral p-adic coefficient, not an assertion that the rational number is always an ordinary integer.

**Sufficiency.** Formal polynomial Taylor gives over Q_p:

  f^(i)(a+u) = sum_(d>=0) [u^d/d!] f^(i+d)(a).

The visible terms (i+d<J) equal (L_u j_a^J(f))_i. Every missing term has n=i+d>=J and d>=1. Each f^(n)(a) is divisible by n!, so its p-adic valuation satisfies

  v_p([u^d/d!] f^(n)(a))
   >= d*s - v_p(d!) + v_p(n!)
   >= s + v_p(J!) >= e.

The middle inequality uses n>=J and d*s-v_p(d!)>=s for all d>=1, s>=1. Therefore all missing terms vanish modulo p^e, giving L_u.

**Necessity.** Take f(X)=(X-a)^J and g=0. Their first J ordinary jets at a are identical (all zero), but the (J-1)st derivative of f at a+u equals J!*u. Its p-valuation is precisely v_p(J!)+s. If this is <e, the moved jet differs from g's, so **no function** of the original reduced jet can implement the translation.

**Group structure.** Binomial convolution gives L_u L_v = L_(u+v) for u,v in pZ_p, and L_-u is the inverse. Thus the near-identity family is flat: *no nontrivial holonomy* is produced merely by following a rectangular translation diamond.

## Two sharp complementary cases

- e=2, v_p(u)=1: transport exists for all Z[X] iff J>=p.
- For degree-bounded P_m(F_p) with m<p, arbitrary translations are reconstructible from its ordinary coefficients. For m>=p and unit translations, reduction mod p loses data (Phase272); this is a DIFFERENT domain/precision question. Over Z_p itself the factorial map is injective, so the image lattice always carries a translated action; the ambient ordinary-jet coordinates need not admit an integral extension under a unit translation.

At p=3, J=3, u=3, e=2, the map reduces to
  (v0,v1,v2) -> (v0+3v1,v1+3v2,v2)
over Z/9; it handles monomials of *arbitrary* degree, not merely degree<=2.
At J=2, f=X² provides the negative control, with f'(3)=6 mod 9.

## General source-lift boundary

The actual tenth-discriminant source is bivariate F(Z,W), with W held fixed when taking ordinary partial derivatives. A real-axis shift changes BOTH coordinates. Consequently

  ∂Z^i F(Z+u,W+u) ≡ ∂Z^i F(Z,W)
        + u*(∂Z^(i+1)F + ∂W∂Z^i F)(Z,W)    (mod p²)

for u in pZ. The ∂W component is distinct and must be transported within the original rectangular row basis. Phase204 already models that two-sided row/jet action. The sharp J>=p depth threshold removes its missing top ∂Z derivative at precision p² only, under the original integer polynomial source.

Translation of the observation support Q does NOT imply Q+u remains in the production ellipse or preserves G_Q. The original Gram uses ordinary derivatives and 2/2D trace weights. No extra determinant mass may be credited to the Hasse factorials or to the transport without an independent **non-overlapping** lower bound on the same original Gram. No Siegel-zero or discriminant-cutoff improvement is claimed.

## Falsification protocol and executed finite checks

The script sharp_precision_horizon.py checks p in {2,3,5}, e in {1,...,5}, s in {1,2,3}, J in {1,...,11}; over monomials through degree J+4 at centers 0,2. It tests every predicted valid case, negative invisible-polynomial cases for invalid parameters, and inverses of the canonical transport on arbitrary ambient vectors. It passes 8,839 exact integer/modular comparisons on the initial run. This supports implementation consistency but not independent verification of the general proof.

**Most important negative control:** f=X^J and e=s+v_p(J!)+1 must defeat ANY descended transport; rejecting this invalidates the threshold.

**Remaining work:** independently review the paper proof; formalize a small universal Polynomial Int theorem (not merely bounded monomial computations); audit already-counted factorial and Frobenius factors, actual source support Q, W-direction transport and residual Smith strata before any new discriminant-bound claim.
