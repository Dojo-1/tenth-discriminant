# Round201: the residue-count measure is the first exact source/geometry transport

Date: 2026-11-04. **P:** elementary factorization theorem, paper proof here (not compiled in Lean). **M:** T8 exact source-CI. **H:** uniform source-exact determinant gain remains unproved. This explanation was derived after T7 and preregistered as T8 before testing.

## Exact general factorization

Fix integers D>=0, J,R,S>=0 and a prime p. Let Q be any finite subset of integer coordinate pairs. Let v_{i,j}(q)=(a_{i,j}(q),b_{i,j}(q)) be the original ordinary-Z-jet pair at q, indexed by rectangular row i and derivative j<J. This is an integer-coefficient polynomial function of (x,y), with the W=conj(Z) substitution performed after differentiation; hence its image modulo p depends only on (x modp,y modp). The integer pair trace is B_D((a,b),(c,d))=2(ac+Dbd).

Define the **residue-count measure**

    mu_{Q,p}(u,v) = #{q=(x,y)∈Q : x≡u, y≡v (modp)} (modp)

for (u,v)∈F_p². Let F_{D,J,R,S,p}(u,v) be the n-by-n Gram summand of exactly one observation with residue (u,v), computed using the same jet formula and trace form modulo p, summed over derivative index 0<=j<J.

**Claim P (elementary, all finite Q):**

    integerRectangularTraceGram(Q,D,J,R,S) (modp)
       = sum_{(u,v)∈F_p²} mu_{Q,p}(u,v) * F_{D,J,R,S,p}(u,v).

Proof: the original Gram is a sum, over q∈Q and j<J, of integer polynomial trace-pairing terms. Reduction modulo p commutes with sum and products, and every summand depends only on q modp. Reindex by residue class. No inertness, class number, ring-of-integers chart or analytic bounds are required.

**Immediate implication:** mu(Q1)=mu(Q2) implies G(Q1)=G(Q2) modp and so they have identical ranks and kernels over F_p. **Non-converse:** the measurement map mu -> G may itself have a nontrivial kernel. The source-to-valuation map has two distinct potential losses:

    Q --(count residues modulo p)--> mu_{Q,p}
      --(linear jet/trace observation)--> G(Q) modulo p.

Neither arrow should be assumed invertible. This is a mathematically precise, source-faithful "information loss" interface; no F1 or ordered-blueprint identification is asserted.

## T8: original D19 support collapses modulo three to the real axis

T8 was preregistered in [PREREG_T8_MODULAR_COLLAPSE_2026-11-04.md](PREREG_T8_MODULAR_COLLAPSE_2026-11-04.md) **before** the code [T7_extended_rectangle.py](T7_extended_rectangle.py) was extended. Exact test [CI 41793934701](https://github.com/Dojo-1/tenth-discriminant/actions/runs/41793934701) passed.

Use D=19, p=3, R=4,S=J=4 and Q_rho=ellipsePairs D rho. Let A_rho be the y=0 slice of Q_rho (a **diagnostic comparison**, not a replacement production determinant).

At rho=6, all nonreal y=±1 layers contain exactly x=-4,...,4, so each x residue mod3 occurs precisely three times. Thus their residue measure vanishes modulo3 and

    G(Q6) ≡ G(A6) (mod3) entrywise,

verified for all 16×16 entries. Every ordinary Z derivative of order j>=3 vanishes in characteristic3 (falling factorial divisible by3); on y=0, all remaining entries depend on only three x residues, yielding rank bound 3*min(J,3)=9. The exact RREF rank of G(A6) and G(Q6) is **9**. This is much smaller than the universal p=3 rectangular-row exponent-only rank upper 16-3=13.

At rho=7, the nonreal layers each have eleven nodes x=-5,...,5 and are no longer balanced modulo3. The constant-row (0,0) entry gives a diagnostic

    (G(Q7)-G(A7))_(0,0)=2*22=44 ≡2 (mod3),

so equality fails. The exact full Gram rank is **13**, saturating the universal Frobenius bound in this finite case.

This supplies a structural explanation of the rank shift 9 ->13 under inclusion Q6 subset Q7; neither PSD monotonicity nor source field equality implies rank monotonicity modulo p.

## Geometric and arithmetic governance

- This factorization is about the *same* original source Gram for each fixed Q, not equality between two production supports under an arbitrary moving frame.
- The residue measure is modp information. It cannot reconstruct integer determinant, higher p^m depth or real shape without additional carriers/maps; the earlier Round201 T0/T1/T5 counterworlds demonstrate those gaps.
- The finite rho6 geometry produces extra modular rank nullity compared with the universal Frobenius row factorization, but **extra rank loss does not by itself force a new p-adic determinant valuation beyond the existing two-sided factor**. A full Smith/determinantal-divisor and geometric upper analysis is needed.
- For the actual huge original Q_thin(D), no theorem currently establishes that all relevant nonreal residue counts vanish modulo p, and choosing a modified support would require an independently justified analytic upper/positivity proof. Do not promote this example to a uniform D>=322^4 result.
- Oliver Lorscheid's ordered-blueprint tropicalization provides an established framework for valuations with retained algebraic relations; this finite residue measure is our own elementary source-specific projection, not a realization of his scheme-theoretic construction.

**Best next formal target:** the exact mod-p factorization of original jet Gram through mu_{Q,p} for arbitrary finite Q, then a concrete counterexample to converses. Next number-theoretic target, if justified, is a uniform residue-multiplicity constraint on the *unchanged* thin support or a quantitatively bounded loss term. Stop if the correction is merely case-specific.
