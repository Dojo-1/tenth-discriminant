# Phase296 — affine field frames, p-adic depth-two debt, and thin-row rigidity

**13 November 2026. Post-result mathematical / implementation ledger.** All work AI-authored, source frozen, preregistered per experiment and verified by GitHub Actions. This is internal computational corroboration and paper reasoning, **not** independent human mathematical review or new formal Lean kernel theorem. This is **draft PR #188**, stacked on Phase295 #186 and its draft ancestors. No change to actual tenth-discriminant field theorem PR #157 or integrated prior 322^4 arithmetic cutoff.

## What exactly is being transported

The original D583 field sampler has `rho53/R145/S=J5/Q383`, **725 original rows**. The original D587 field sampler has `rho53/R146/S=J5/Q383`, **730 original rows**. Both retain the original exact integer ellipse (107 points at y=0, 95 at EACH y=±1, 43 at EACH y=±2), all original ordinary Z-jets holding W fixed, and original real/imag trace metric `diag(2,2D)`. The row modules are different dimensions: **there is no claimed GL_725 integer conjugacy between them**.

At the inert p5 common local residue field `F25=F5[u]/(u²+583)`, the fixed D587→D583 quadratic algebra isomorphism `phi` sends `u587 → 2u583`, respecting conjugation and trace norm. This step alone does NOT preserve Q, as Phase295 proved from the W-module spectrum. Phase296 allows additional *moving* field-coordinate frames

```
g(z)=a*conjugate^epsilon(phi(z))+b,
a∈F25^×, b∈F25, epsilon∈{identity,Galois}.
```

The group tested at p5 is MUCH wider than integer/metric source gauges: 24 nonzero a, 25 translations b, two epsilon branches, **1200 total**, including a that does not preserve norm and b that does not preserve the original formal monomial coefficient lattice.

Define the weighted multiset matching debt `d(g)=383−sum_z min(count_Q(z),count_g(phiQ)(z))`. This is a point-fiber count, NOT a p-adic determinant or Smith valuation.

## Phase296-A — exact finite affine no-go; surprising near-repair [P-paper and M]

**Preregistered BEFORE code** at `research/phase296/PRE_REGISTERED_AFFINE_FIELD_AND_ROW_GATE.md`, commit `cbe92c33`. The first CI failed because a *test control*, not the theorem, incorrectly asserted every nonmaximal multiplicity≤19; the original y0 centerline also has multiplicity21. Corrected the bound to21 at `d47255a3` without changing the mathematical claim; the failed CI is preserved.

[Successful exhaustive Phase296-A CI #43373033299](https://github.com/Dojo-1/tenth-discriminant/actions/runs/43373033299) reports:

| F25-affine field-semilinear class | exhaustive candidates | min unmatched d1 | max matched out of383 |
|---|---:|---:|---:|
| any unit a, any b, either epsilon | **1200** | **3** | 380 |
| norm-one a, any b | 300 | **64** | 319 |
| base-field a,b | 40 | **3** | 380 |
| norm-one and base-field a,b | 20 | **104** | 279 |

The near-repair (d=3) has REAL multiplier a=2 or3 mod5 and **N(a)=4**, not 1. The source ordinary-jet chain rule scales j-th derivative values by a^j; its trace pairing scales by `N(a)^j`. Since J=5 includes j1, this near-repair is **not a trace-metric moving gauge**. The best norm-one slope in the broader group still leaves64 unmatched points and requires transformations that need not preserve base-field coefficients or the original sample origin. These are diagnostic transport tradeoffs, not arithmetic valuation gains.

**Independent paper no-go for ALL affine candidates, even before metric constraints:** The unique two heaviest original residue sites are (2,0),(3,0), multiplicity22 each; all other sites have multiplicity≤21. The locally transported Q has the same two heaviest sites because y=0 is fixed. A full-multiset affine equivalence must permute these sites. Their difference is the field unit1, so the affine multiplier must be +1 or−1 and translation b=0, regardless of conjugation pre-twist. But `phi` maps the y±1 layers, of multiplicity19 per x residue, to y±2 residues, whose original multiplicities are8/9. Contradiction. Thus no exact F25-affine/semilinear match mod5; no such affine Z5 lift can exist at deeper precision. The actual 1200-search independently confirms zero exact candidates.

**Counterworld (do not overpromote):** The invertible F5-LINEAR map `(x,y)→(x,3y)` on the common chart exactly cancels phi's factor2, giving full original sample agreement, but FAILS the quadratic algebra law: for u²=2, the map sends u²→2 whereas its image u→3u has square3 mod5. It also changes the norm of u from3 to2. Therefore the affine-semilinear no-go does NOT rule out arbitrary 2×2 base-linear transforms if those are allowed to destroy field multiplication and trace metric.

**Ordinary jet / base lattice controls:** An independent formal binomial expansion checked 240 original affine j0..4 chain identities with W FIXED, including normone and nonnormone slopes. The formal original F5 coefficient row lattice allows only base-field coefficients; imaginary a or b in aZ+b cannot be represented in its one-coefficient-per-monomial base. The source's original R145≫S5 rectangular support excludes off-diagonal affine polynomial mixing, which Phase296-C strengthens into a complete polynomial-automorphism theorem.

## Phase296-B — deeper norm-one affine obstruction [M]

Preregistered separately at `research/phase296/PRE_REGISTERED_NORMONE_DEPTH2.md`, commit `0e874956`, AFTER Phase296-A and BEFORE B. At k=2, work over `A25=(Z/25)[u]/(u²+583)` with `phi(u587)=17u583` and `583*17²=587 mod25`. Norm-one multipliers a satisfy `a\bar a=1 mod25`; exactly30 such a exist. Exhaust all625 translations and two Galois branches, giving **37,500** exact candidates, with all best matching ties replayed by independent Counter and sorted-multiset procedures.

[Phase296-B CI #43373303089](https://github.com/Dojo-1/tenth-discriminant/actions/runs/43373303089) PASS:

| Norm-one multiplier class | checked p25 candidates | exact minimum unmatched d25 | maximum matching |
|---|---:|---:|---:|
| any translations in A25 | **37,500** | **245** | 138 |
| real/base-ring translations | 1,500 | **276** | 107 |
| real/base-ring multiplier, any translations | 2,500 | **245** | 138 |
| real multiplier and real translation | 100 | **276** | 107 |

The broad p25 best d=245 occurs with nonreal translations (source base polynomial lattice is not preserved). Even this permissive norm-one family cannot fully recover the raw original support. The 37,500-candidate exact weighted-debt histogram and 216 best ties are retained in the CI output. Under a fixed lift, mod25 matching implies mod5 matching, so the relevant debt cannot decrease as precision is refined.

**Post-result correction (not preregistered):** A separate enumeration of ALL60 p5 norm-one slopes with REAL translations found the exact minimum d5=**72** (16 ties), whereas the broad normone any-translation min d5=64. A previous plot erroneously labeled the narrower group's mod5 minimum as64; corrected clearly in the conversation and added the 60-case regression at commit `484eadb3` to preserve the distinction. The corresponding changes across depth are:
- norm-one, any b: 64→**245** unmatched;
- norm-one, b real: **72**→276 unmatched;
- norm-one, both a,b real: 104→**276** unmatched.
These are exact points-per-side under stated groups, not a claim that p-adic Gram valuations are monotone.

## Phase296-C — the polynomial-row category is more rigid than affine matching [P-paper + M]

Preregistered AFTER A/B as `research/phase296/PRE_REGISTERED_THIN_ROW_RIGIDITY.md`, commit `014f5d33`. The initial new executable mistakenly encoded the ghost as a Z power rather than a W power; corrected the sparse polynomial exponents to (0,25)/(0,1) at `67c4cb87` before accepting results. Preserve both commits for provenance.

**Thin-row rigidity theorem (elementary paper proof, NOT formalized in Lean):** For ANY field k, R>S>=2, `0<=delta<S-1`, and

```
L_(R,S)=span_k{Z^r W^s: 0<=r<R,0<=s<S} ⊂ k[Z,W],
```

any k-polynomial RING AUTOMORPHISM sigma satisfying `sigma(L_(R,S))⊆L_(R+delta,S)` is necessarily **diagonal affine**:

```
sigma(Z)=aZ+b, sigma(W)=cW+d, a,c∈k×, b,d∈k.
```

**Proof:** `Z^(R−1)` belongs to L. Its image `sigma(Z)^(R−1)` has W-degree `(R−1)deg_W sigma(Z)`, which must be <=S−1<R−1, so sigma(Z) has no W-dependence. Its Z-degree is at most floor((R+delta−1)/(R−1))=1, and invertibility forces sigma(Z)=aZ+b with a unit. An automorphism fixing k[Z] has `sigma(W)=cW+h(Z)` with c∈k× (the W-degree and inverse-degree multiply to1; leading coefficient must be unit of k[Z]). The W-free term of `sigma(Z^(R−1)W^(S−1))` equals `(aZ+b)^(R−1)h(Z)^(S−1)`. If deg h>=1 this has Z-degree >=R+S−2>R+delta−1, a contradiction. Hence h is constant. Converse: diagonal affine substitutions preserve the rectangle. No characteristic-zero requirement is used; all leading coefficients remain nonzero in the field.

**Sharp threshold:** For original R145,S5, delta1 (725→730 original row directions) falls in the rigid range. At delta4 (725→745 rows), the triangular *polynomial* automorphism `W→W+Z`, Z fixed, fits the broader rectangle because the corner expands to maximum Z-degree148. At delta0,1,2,3 it violates row bounds. HOWEVER it also violates ordinary fixed-W jets: `∂_Z(W+Z)=1` versus `sigma(∂_Z W)=0`. Thus the 20-row threshold is SHARP ONLY for polynomial-row embeddings, not source-jet/metric transport.

[Phase296-C focused CI #43373799925](https://github.com/Dojo-1/tenth-discriminant/actions/runs/43373799925) PASS. It runs exact sparse formal-polynomial hostile corner tests for the delta0..4 threshold and a finite-field/jet **ghost**:

```
sigma_ghost(Z)=Z+(W^25−W), sigma_ghost(W)=W.
```

This triangular sigma is a NONTRIVIAL polynomial automorphism over F5 (explicit inverse with opposite shear). Because every w∈F25 obeys w^25=w, it acts as IDENTITY on all original Q383 raw observation points and **7,660** exact original ordinary j0..4 monomial-jet checks modulo5. Yet the formal sigma(Z^144) contains a W^3600 term (leading coeff1), while the rectangle allows W-degree≤4: the original scalar-coefficient polynomial-row lattice is NOT preserved. At the actual original real-axis sample W=2, `2^25−2≡5 mod25`; the ghost even ceases to be invisible one p-adic digit later. This is a *direct counterexample* to equating finite-field raw jet agreement with original formal arithmetic lattice equivalence, especially after Frobenius/source division.

The conjugation involution `tau(Z)=W, tau(W)=Z` further forces diagonal affine parameters a=c,b=d over F5. To preserve trace metric at j1, real a needs a²=1, so a=±1. Phase296-A's exhaustive source test already disallows an exact sampling match in this strictly compatible group under phi.

## What this DOES and DOES NOT imply

[P-paper, novelty not checked] exact heavy-site anchor proof, the thin-rectangle polynomial-automorphism theorem, sharp delta=S−1 example and the characteristic-p ghost formal/evaluation mismatch. Their proofs are elementary algebra and must still receive independent human scrutiny.

[M, original source exact] A 1200 affine F25 search, a 37,500 normone A25 search, independent residual/matching controls, 240 original-jet chain checks, sparse formal degree checks and 7660 ghost raw-jet checks. Code and CI share AI authorship and original helper dependencies.

[H] Non-polynomial or non-automorphism source embeddings, movable W algebra with altered jet direction, original sample and saturated integer lattice compatibility, uniform h1-admissible field theorem. Thin-row rigidity does **not** forbid arbitrary injective row maps L145→L146, and norm-one affine with translation need not be a linear trace isometry. Full D583 and D587 polynomial row modules have DIFFERENT dimensions; one cannot infer a cross-field GL725.

[R] Affine-semilinear no-go is a no-go for arbitrary base-linear coordinate charts; finite raw jet agreement certifies original polynomial lattice; a norm4 geometry match is an original trace isometry; synthetic point/jet completions or deficits add p-adic determinant factors.

**Next smallest theorem/experiment:** abandon the assumption that the whole source morphism must be a polynomial automorphism and explicitly classify **non-surjective integer ROW embeddings compatible with both the original jet-evaluation map and metric**, alongside the five-row Schur complement in the SAME D587 field. This is the category where a real bridge to the source arithmetic might exist; it is not closed by the current automorphism no-go. Then test any candidate on an actual h1-admissible original source (the high-S5 stress fields here are NOT h1) before claiming a discriminant improvement.

**Integration gate:** all three focused workflows, mathematical Markdown and root Lean CI must pass at the exact final commit. The root Lean workflow checks previously existing formal results and does NOT turn this new paper theorem into a Lean formalized theorem. Keep PR188 stacked draft; independent source-to-field/math review #50/#51 remains required. No Work mode.
