# Phase294-D — preregister multi-level signed p-adic support filtration, not a Gram theorem

**2026-11-12, AFTER Phase294-A/B/C positive CI, BEFORE this new source-level enumeration.** Phase294-A measured the raw mod5 support rank40 from four Galois orbits (104 residue-multiset edits); Phase294-B transported the complete OLD normalized 725×3830 source modulo5^9 if the observation support moves; Phase294-C transported ALL p5-primitive rows modulo125 in synchronized parity row gauges on the MOVED support. Neither proves a transport back to the ORIGINAL D583 ellipse. This final, bounded experiment records exactly how the signed support remainder **refines** at higher 5-adic precision.

## Fixed geometry and carrier

Original literal `Q=Q583=Q587`, rho53, points383, y strata y0:107, y±1:95 each, y±2:43 each. The actual D587 full original source remains n730, but the comparison uses its first725 diagnostic rows. Nothing about monomial, jet, trace B, original source p5 index or fixed-Q Phase293-D negative result is changed.

Let `alpha∈Z5^×` be the unique root `583 alpha²=587`, `alpha≡2 mod5`; the previously verified root is `647814942 mod5^13`. For k∈{1,2,3,13} let

```
m_k(a,b)      = #{(x,y) in Q: (x,y)=(a,b) mod5^k},
m_k^phi(a,b)  = #{(x,y) in Q: (x,alpha y)=(a,b) mod5^k},
delta_k       = m_k^phi-m_k, signed integer residue multiplicities,
M_k           = (1/2)*sum_{a,b}|delta_k(a,b)|,
A_k           = #{(a,b):delta_k(a,b)!=0 as INTEGER},
A_k^unit      = #{(a,b):delta_k(a,b)!=0 mod5}.
```

At every level delta is conjugation and central inversion invariant, total signed mass zero, and is the pushforward of delta at higher precision. Thus the elementary contraction inequality `M_k<=M_(k+1)` holds for **every** support, whether or not it comes from our ellipse. This is a theorem about the l1 norm of signed measures under residue pushforward—not a theorem of positive Gram increments or determinant monotonicity.

Freeze the following SOURCE-COMBINATORIAL predictions BEFORE code:
| precision | M_k | A_k integer nonzero | A_k^unit | active Galois conjugate pairs | inversion-fixed Galois orbits |
|---|---:|---:|---:|---:|---:|
| 5 (k1) | 104 | 20 | 8 | 4 | 0 |
| 25 (k2) | 276 | 200 | 200 | 100 | 4 |
| 125 (k3) | 276 | 552 | 552 | 276 | 4 |
| 5^13 (k13) | 276 | 552 | 552 | 276 | 4 |

Why: mod5, cancellation of ±10 reduces 20 signed coordinates to 8 unit directions. At mod25, alpha≡17: its images of y=±1,±2 have residues ±17,±9, disjoint from the original ±1,±2; only the central y0 layer (107 points) overlaps, leaving 383−107=276 moves. Original four nonzero-y layers and their four moved counterparts each occupy all25 x residue classes at k2, giving 8*25=200 active coordinates and 100 Galois pairs. At mod125, every x coordinate in each original fixed y stratum is distinct, hence there are 2*276=552 active coordinates and 276 conjugate pairs. Central inversion acts on a Galois orbit `(x,±y)` by x→−x, so at k2/3/13 the four active conjugate pairs with x≡0 are INVERSION-FIXED, whereas mod5 active x∈{2,3} has no such pairs. **The balanced 20+20 parity calculation from k1 must NOT be naively extrapolated to the higher-level boundary modules.**

## Controls, falsifiers and scope

1. Freeze original Q via Phase206 source blob, Hensel alpha via Phase294-B source blob; assert exact D583/D587 Q equality, y counts, F5 inertia and root alpha mod all four powers.
2. Compute EACH m_k from the 383 original integer pairs independently, for alpha moving Q; assert pushforward delta_{k+1}→delta_k entrywise, and no scalar claim based on merely counting SET intersections. Verify the preregistered table EXACTLY or STOP; any wrong count must be preserved.
3. Check signed delta conjugation `(x,y)→(x,-y)` and central inversion `(x,y)→(-x,-y)` entrywise, unit support as above, Galois orbits of the nonzero mod5 coefficients and inversion-fixed orbit counts.
4. Counterworld: equal-width rectangle `Qrect={-21<=x<=21,-2<=y<=2}` has zero boundary mass at k1 because alpha2 permutes all five y residues, but **nonzero** mass at k2 (alpha17 cannot preserve the literal ±1/±2 support). This proves zero residue-level defect does NOT guarantee source support equivalence at the next p-adic digit.
5. Counterworld: alpha=1 (no moving support) gives all M_k=0. Alpha replaced by -alpha gives the same signed measure because Q is conjugation-symmetric; check all four levels.
6. Do NOT assert A_k^unit counts are the rank of p^k-jet Gram or primitive H. The 40-dimensional rank at k1 used a **field** F25 and CRT; the p^k ring for k>=2 is not a field and has more constrained row degree and p-adic divisibility. The filtration is an exact boundary *measure*, not an order of vanishing or new p-valuation.
7. Root Lean, field cutoff PR157, human source-to-field gates #50/#51, and all earlier PRs remain untouched/draft; no Work.

[P-paper] signed residue measure pushforward, L1 contraction, conjugation/inversion combinatorics. [M after CI] exact k1/k2/k3/k13 table on the frozen original ellipse and counterworlds. [H] a p-adically filtered *primitive* boundary source-surgery theorem with valuation control. [R] equating first-residue support rank40 with all higher-prime-level boundary complexity or a new determinant factor.
