# Phase382 — Three-prime finite closure of the conditional Tao bound

**21 November 2026 · AI-assisted mathematical derivation and exact arithmetic · RESEARCH DRAFT.**

## Objective, assumptions and prior art

Terence Tao's 20 October 2026 tenth-discriminant challenge asks for effective bounds derived from stated zero-free inputs or independent arguments, without using Heegner's proof. The challenge discussion already records the GRH-conditional bound d≤199, the 199.1208 central Epstein threshold, related elementary inert-prime sieves, and external formalizations. No numerical or priority novelty is claimed here.

Primary source: https://terrytao.wordpress.com/2026/10/20/an-experimental-ai-math-challenge-using-tenth-discriminant-bounds-to-explore-arguments-ruling-out-siegel-zeroes/

The parent Phase381 states, conditional on absence of real zeros in (1/2,1) of the **actual primitive quadratic Dirichlet L-functions**, standard analytic continuation / Epstein-Poisson identities and the quadratic field-character dictionary, that every imaginary quadratic class-number-one field has absolute **fundamental field discriminant** d≤199. Phase382 does NOT re-prove those analytic inputs; it replaces the finite class-number enumeration by a small, source-faithful, exact sieve.

## Necessary inert-prime lemma

For a negative fundamental D=-d and K=Q(sqrt(D)), the maximal order has integral basis 1,ω where ω=(b+i sqrt(d))/2, b=0 or 1. Therefore

\[
N(m+n\omega)=(m+bn/2)^2+(d/4)n^2\quad(m,n\in\mathbb Z).
\]

If h(K)=1 and a rational prime p<d/4 is split or ramified, a prime ideal above p has norm p and must be principal, say (α). Hence N(α)=p. For n=0 the norm is m², not prime; for n≠0 it is at least d/4>p. Contradiction. Thus every prime p<d/4 is inert and the genuine Kronecker value χ_D(p)=-1. The strict inequality 4p<d is essential. In particular ramified χ_D(p)=0 is not inert.

## Three-prime finite certificate

The standalone entrypoint [three_prime_199.py](three_prime_199.py) checks all 62 negative fundamental discriminants with 3≤d≤199. It uses the exact fundamental criterion:

- d≡3 (mod 4), d squarefree; OR
- d=4m, m squarefree and m≡1,2 (mod 4).

For each admissible d, test χ_D(p)=-1 **only when** 4p<d for p=2,3,7. For odd primes, the symbol is Euler's criterion; for p=2, use the actual Kronecker congruence D mod 8, including value zero if D even.

Exact result: 62 total, **53 excluded**, nine survivors

\[
3,\ 4,\ 7,\ 8,\ 11,\ 19,\ 43,\ 67,\ 163.
\]

A separately written quadratic-residue-table implementation independently matches every symbol in this finite domain. Omission/mutation controls show all three primes are necessary **for this precise three-filter sieve**, not for all possible class-number arguments:
- without p=2: 79,88,127,148,151,184 are additional survivors;
- without p=3: 51,107,123,155,179;
- without p=7: 91,115,139,187.

The historical Phase380 certificate using two distinct finite class-number algorithms independently yields the same nine, but is not needed for the short *necessity* proof.

## Minkowski verifies sufficiency for the nine

The classical imaginary-quadratic Minkowski theorem says every ideal class contains an integral ideal of norm ≤(2/π)sqrt(d)<(2/3)sqrt(d), using π>3.

For each survivor, let c_d be the maximum positive integer with 9 c_d²<4d. The exact [nine_minkowski.py](nine_minkowski.py) checks:

| d | 3 | 4 | 7 | 8 | 11 | 19 | 43 | 67 | 163 |
|---|---|---|---|---|---|---|---|---|---|
| c_d | 1 | 1 | 1 | 1 | 2 | 2 | 4 | 5 | 8 |

For every displayed d, all rational primes p≤c_d are inert: none are relevant for the first four; p=2 for 11/19; p=2,3 for 43; p=2,3,5 for 67; and p=2,3,5,7 for 163. Their unique prime ideals (p) are principal, even though their ideal norms are p². Thus every integral ideal of norm ≤c_d factors into principal prime ideals. Minkowski therefore forces each class to be trivial. No Heegner classification, reduced-form class-number enumeration or GRH input is needed **for this reverse direction**. The script checks integer bounds and residues only; it does not prove Minkowski's theorem.

**Combined conditional theorem:** assuming the external central Epstein/Dirichlet zero-free hypothesis, h(K)=1 if and only if |disc K| belongs to the nine-element list. The analytic bound and field-to-character normalization remain separate formal proof obligations. The result and its numerical bound are already classical/discussed in Tao's thread; the contribution here is a very small, independently audited finite proof.

## Reproducibility, objections and gates

Local runs PASSED for both new exact Python programs, plus Phase380 two-algorithm reduced-form/character comparison and Phase381 exact-rational central threshold. Code identifies 0, +1, -1 as ramified/split/inert without confusing them. A field discriminant is not an order discriminant, a quadratic radicand, or the original integer trace Gram determinant. Unimodular frame transport and the class-number-one norm argument concern distinct mathematical objects.

No Lean/Lake or SWI-Prolog executable was available in this session; no new kernel proof, Prolog test, comprehensive CI or independent human number-theory review is claimed. Mainline 322^4 trace-Gram, proposed 301/302 developments and independent field-review issue #50 remain untouched.

**Next theorem targets:** pin the actual Mathlib quadratic-field Dirichlet character and norm-form correspondence, implement the inertness lemma in Lean, verify the 62-case finite classifier and Minkowski sufficiency, and then replace the external central Epstein identity with source-faithful analytic lemmas. Kill any step that replaces source field/discriminant/character types by a surrogate.

Evidence: P for elementary paper lemmas and cited standard theorems under exact premises; M for finite integer checks; A for external zero-free/analytic identities/Minkowski and unformalized source correspondence; H for source-level Lean proof and referee review. No unconditional new theorem is asserted.
