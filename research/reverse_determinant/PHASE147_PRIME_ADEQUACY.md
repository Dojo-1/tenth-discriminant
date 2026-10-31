# Phase147 — Prime-local adequacy and exact minimal ordinary-jet supports

31 October 2026. [P-paper] Elementary Smith/Hermite and reduction-mod-prime arguments, not Lean formalized. [M] **Exact finite computations** for eight fixed parameter values using the original ordinary Z-jets. [R] Passing only the convenient primes 2,3,5 is not a universal adequacy certificate. [H] Parameter-uniform admissible support construction, analytic determinant upper, and actual-field discriminant consequences remain open.

The independently executable [Phase147 prime-adequacy verifier](phase147_prime_adequacy.py) inherits the source-matched [Phase144](phase144_verifier.py), [Phase145](phase145_ortho_anti_ambig.py) and [Phase146](phase146_translation_newton.py) experiments without altering the ordinary derivative convention. Full source-to-certificate lineage begins at [Phase140 original source](../ellipsoid_trimming/phase140_exact_trim.py). The parameterized Phase147 evaluator is independently compared entrywise against the actual D=19 Phase140/144 evaluator before any result is accepted.

## What is the object?

Freeze rho=5, R=8, S=J=4. For each integer D>0, let Omega_D={(x,y) in Z^2 : x^2+D y^2<=25}. E_Q(D) is the **32 by 8|Q| integer matrix** of ordinary partial Z-derivatives of Z^r W^s with W held fixed, at pairs (x,y), preserving both integer real and imaginary coordinate channels. The positive metric is B_D=diag(2,2D,...) and the original integer Gram G_Q=E_Q B_D E_Q^T.

Let M_D=im_Z(E_Omega), assumed rationally full rank, and choose an integral HNF basis H_D of M_D. For each subset Q, define

$$ C_Q=H_D^{-1}E_Q\in Z^{32\times8|Q|}, \qquad
F_Q=Z^{32}/\operatorname{im}_Z C_Q\cong M_D/\operatorname{im}_Z E_Q. $$

The right-hand quotient is finite for rationally full-row-rank Q. Equality of integer column images is exactly F_Q=0; equality of **rational rank** or a small real Gram determinant is not enough.

## A genuinely local-to-global criterion [P-paper]

For every prime p, the number of nontrivial p-primary Smith factors of F_Q is

$$
\delta_p(Q)=\dim_{\mathbf F_p}(F_Q/pF_Q)
=32-\operatorname{rank}_{\mathbf F_p}(C_Q\bmod p).
$$

Proof: tensor the defining presentation Z^{8|Q|} -> Z^{32} -> F_Q -> 0 with F_p; right exactness identifies F_Q/pF_Q with the indicated cokernel. Thus a nonzero delta_p is a **typed arithmetic obstruction**, not merely a heuristic low-rank score.

Furthermore suppose a 32-by-32 integer column minor X of C_Q has nonzero determinant b. Then |F_Q| divides |b|, since it is the gcd of all maximal minors. Hence

$$
\boxed{\ F_Q=0\quad\Longleftrightarrow\quad
\delta_p(Q)=0\;\text{for every prime dividing }b.\ }
$$

This is an exact finite-local certificate *if the prime factors of b are known*. Factoring a huge b may be costly; the checker does **not** pretend to have a free factorization oracle. It instead uses ranks modulo 2,3,5 for inexpensive **necessary lower-bound exclusions**, and an independently justified exact modular HNF with an explicit nonzero odd square minor for every positive support certificate.

Grouped-column ranks r_p(Q)=rank_Fp(C_Q) are monotone submodular functions of observation **blocks** Q. This is a polymatroid viewpoint. The integral quotients carry strictly more information than any single reduced matroid; the general theory of matroids over a ring is established prior art (Fink and Moci, *Matroids over a ring*, JEMS 18 (2016), DOI [10.4171/JEMS/600](https://doi.org/10.4171/JEMS/600)). The contribution here is a source-matched finite interrogation of this particular ordinary-jet geometry, not a novelty claim for Smith forms.

## Eight independently certified finite minima [M]

Each candidate support is explicitly recorded in the verifier. The following is a **global minimum cardinality among subsets of that fixed Omega_D**, not a greedy or merely local minimum.

| D | Full points | Minimum support | Exhausted size | Number examined | Pass F2 | Pass F2 and F3 | Pass F2,F3,F5 |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 13 | 25 | 7 | 6 | 177,100 | 2,592 | 0 | 0 |
| 17 | 21 | 8 | 7 | 116,280 | 9,720 | 0 | 0 |
| 18 | 21 | 7 | 6 | 54,264 | 4,560 | 0 | 0 |
| 19 | 21 | 6 | 5 | 20,349 | 0 | 0 | 0 |
| 21 | 21 | 7 | 6 | 54,264 | 1,296 | 0 | 0 |
| 23 | 17 | 9 | 8 | 24,310 | 224 | 0 | 0 |
| 24 | 17 | 6 | 5 | 6,188 | 56 | 0 | 0 |
| 25 | 13 | 9 | 8 | 1,287 | 48 | 20 | 0 |

Why this proves *finite minimum* rather than merely a lower-bound guess:

1. Every candidate of size k_min-1 fails to generate full image because at least one of the tested finite-field ranks is below 32. Every smaller candidate extends to one of these and therefore also fails by rank monotonicity.
2. Each displayed k_min has an **explicit subset witness** in the script. All its original columns, expressed in the full Hermite basis, have a modularly certified HNF equal to I_32. A nonzero **odd** square minor (found by mod-2 pivots, then checked by an exact determinant) supplies the valid modular-HNF modulus. Hence the generated integral image is exactly M_D.
3. The fast binary and ternary bitset rank routines are cross-checked against a separate generic modular elimination at multiple subsets including both full and witness supports. Source definition, bounded enumeration count, exact HNF, and matrix dimensions are asserted.

These tests do **not** assume D is squarefree or that the corresponding imaginary quadratic field has class number one. D=18,24,25 and other control values are valid matrix parameters, not additional number-field inputs to the original arithmetic lower theorem.

## A deliberately surviving counterexample [M/R]

At D=21 the seven-point support

$$ Q_{\rm bad}=\{(-2,0),(-1,-1),(-1,0),(0,0),(0,1),(1,1),(5,0)\} $$

has rank 32 modulo each of 2,3,5 in the **correct full-image HNF coordinate basis**. Nevertheless exact HNF and Smith show

$$F_{Q_{\rm bad}}\cong(\mathbf Z/7\mathbf Z)^4,$$

and rank modulo 7 is only 28. Therefore the implication "the first three convenient modular ranks suffice" is **retired**. This example is also a control against mistaking Gaussian rank or a passing five-prime protocol for integral image equality. The criterion above is exact only with a provably complete set of possible index primes (or a full HNF).

## Metric consequence, still not an analytic discriminant result

All exact candidate Grams are positive with the original trace weights, and the script asserts for both full and minimal supports that det G is divisible by [Z^32:M_D]^2. Thus the **arithmetic image factor** can remain unchanged while the positive metric volume decreases.

| D | log det full | log det minimal | log (raw Hadamard upper) at minimal |
|---:|---:|---:|---:|
| 13 | 533.650106 | 442.404488 | 575.930254 |
| 17 | 524.339771 | 459.568219 | 571.961569 |
| 18 | 527.353309 | 469.626633 | 597.626610 |
| 19 | 530.285191 | 424.342642 | 580.460129 |
| 21 | 535.941562 | 432.607323 | 586.188766 |
| 23 | 516.595921 | 474.808531 | 594.807584 |
| 24 | 518.930026 | 438.107286 | 595.516201 |
| 25 | 475.441676 | 408.470015 | 571.285038 |

The determinants and divisibilities are exact arbitrary-precision integers; **only the displayed natural logs are approximate**. No numerical discontinuity here is evidence for chaos or complexity hardness. The loose raw Hadamard bound warns against transporting finite exact Gram gains into the certified production upper inequality.

## Next frontier / promotion rules

The finite experiment shows that support-minimum cardinalities can jump from 9 at D=23 to 6 at D=24 under fixed rho,R,S,J, while other D support structures behave differently. The integer arithmetic, not just geometric sample count, determines sufficiency.

A credible uniform theorem should specify a deterministic, D-dependent original-jet support construction Q(D), require full rank and explicit p-primary index control, and separately provide an inverse-free analytic majorant for **that same Gram integer**. In particular, the old sufficient interpolation cardinality guard is not automatically satisfied by these minimal supports, and identical finite integral image **does not** transport any class-number or prime-divisibility proof by itself. Compare candidate bounds against the prior analytically certified upper, not a raw Hadamard pilot. Do not merge or modify existing numerical-bound PRs while this remains a separate exploratory branch.

An alternative mathematical target is a controlled generalized block-arithmetic-matroid cover: identify which primes must be checked before support selection, prove a scalable sufficient coverage theorem, and bound the cost of producing its certificate. The finite counterexample at 7 is an explicit kill condition for any scheme checking an unjustified fixed prime list.

Evidence status: [P-paper] local-to-global rank/Smith identity, [M] eight exhaustive finite minimum certificates and exact metric consequences; [R] fixed three-prime sufficiency and literal uniform D=19 support; [H] scalable uniform construction, Lean port, improved actual-field bound and any claimed algorithmic complexity consequence.

**Reproduce:** run the [Phase147 verifier](phase147_prime_adequacy.py) using Python 3 and SymPy 1.14. It imports Phase144's original D=19 source evaluator. A GitHub Actions workflow tests Phase144/145/146 regressions followed by Phase147 exact certificates. Exact-head CI must be inspected before promotion.
