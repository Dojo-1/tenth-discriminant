# Phase298 — composable original Gram-cokernel transport with exact remainder

**13 November 2026 — post-result arithmetic ledger.** Work is AI-authored, each experiment preregistered before its own implementation, with exact source-frozen GitHub Actions; no human-independent mathematical review or Lean kernel formalization of the new composition law is claimed. DRAFT PR #190 is stacked on Phase297 #189 and its unmerged predecessors. No Work mode, no original-source edits, no merge, no changes to draft field cutoff PR #157 or original 322^4 result.

The aim is not to sum more scalar valuations. It is to formalize a true *transport with remainder* whose carrier is the **original integral row lattice**, its restriction pairing, and a finite quotient module recording failure of integral orthogonalization.

## 1. Composition law — conditional, integral and non-additive [P-paper]

Let R be a DVR such as Z5. For a symmetric nondegenerate Gram on three row modules `L0,N1,N2`, write

```
G = [ A    C1     C2 ]
    [ C1^t B1     E  ]
    [ C2^t E^t    B2 ].
```

Assume **T1=A^{-1}C1 is integral over R**. The integral unipotent row transformation sending every N1 row to itself minus its T1-linear combination of L0 rows has determinant1 and changes the first-stage Gram to `diag(A,S1)`, where `S1=B1−C1^t T1`. The cross pairing with N2 changes to `(C2, E−T1^t C2)`. Consequently the actual second-stage cokernel map decomposes into two typed components:

```
eta_12: N2 → coker(Gram(L0⊕N1))
           ≅ coker(A) ⊕ coker(S1),

eta_12(t) = ([C2 t], [(E−T1^t C2)t]).
```

**Proof:** the integral unipotent matrix is in GL_R and its congruence block-diagonalizes the first-stage Gram. It therefore induces an actual isomorphism of module cokernels; applying it to the stage-two cross block gives exactly the displayed pair. No sheaf/cohomology metaphor is required for the claim.

For **one** new generator, each component is a finite p-primary class with order p^h0 and p^h1; the PAIR has order `lcm(p^h0,p^h1)=p^max(h0,h1)`, not p^(h0+h1). For multiple new rows the generated subgroup must be measured jointly: do not extrapolate the single-generator max law to a sum or scalar. The theorem is CONDITIONAL on the first-stage projection being R-integral. A nonintegral first stage does not permit this split and must be evaluated directly in the new Gram.

This is standard finite module/Schur algebra [P-paper]; originality is NOT checked. The geometric interpretation as a moving-frame transport is a **typed realization** using original integral row bases, not evidence of extra mathematical holonomy or worldlet invariants.

## 2. Phase298-A — complete original D587 J5 composition and reversed order [M]

**Preregistered at commit `e2571b3172cfddc02886b15b9f3702b4c7cbc14a` BEFORE the source executable.** [Successful exact-original-source CI #43378797260](https://github.com/Dojo-1/tenth-discriminant/actions/runs/43378797260). It replays all Phase297 source/metric/jet guards, with ORIGINAL full D587 `Q383,R146,S=J5,B=(2,1174)`, all undivided monomial rows, 800 direct exact ordinary-jet checks and all original parity source cross-pairing guards. Everything computed modulo5^16=152,587,890,625, with uncensored old Smith exponents no larger than14.

Define:
- `L0`: the first725 ORIGINAL monomial rows r<145.
- `N1`: the ORIGINAL r145 rows s=0,1,2,3 (four rows).
- `N2`: the ORIGINAL r145 row s=4 (one row).

First stage: `L0→L1=L0⊕N1` has **integral** projection in every one of its four ORIGINAL transverse directions. The script constructs `T1=A725^{-1}C1 mod5^16` in ORIGINAL old-row order with parity-preserving tracked Smith solvers, and reconstitutes the four corrected ORIGINAL Eraw observation rows. It directly verifies ALL 725×4=2,900 old–corrected-row trace pairings vanish, their exact 4×4 symmetric Schur Gram and their 4×1 cross pairing to s4. The deterministic integral matrix `725×4` SHA256 is

`50586b261e2e1ec839e52873afc087c968de3d29834e06c55876e9210c4cec60`.

The new four-row Schur Gram `S1` has exact uncensored p5 Smith profile **{14:4}**, so `v5(det S1)=56`. The residual `E−T1^t C2` creates a **new** order5 class in `coker(S1)`: the profile of `[S1 | residual]` is **{13:1,14:3}**. Simultaneously, the original first-725-row class of s4 was already order5 by Phase297. The actual ORIGINAL intermediate odd 364×364 Gram `G729,odd`, after adding s4's true cross column, has **ONE grade14→13** and exact image-index log5=1; its old Smith max remains14. Therefore

```
  eta_s4 has two nonzero order5 components,
  order(eta_s4) = lcm(5,5) = 5, NOT 25.
```

This is a **concrete original arithmetic source** example of the conditional composition formula, not just a synthetic toy.

The REVERSED original order `L0→Lbad=L0⊕<r145,s4>→L2` starts with a NONintegral projection, so the theorem CANNOT be applied there. Directly inspecting the original odd 363×363 Gram of Lbad and its cross pairings with the two remaining odd-safe original rows gives **zero additional second-stage image-index**; its old Smith max is14 and fully resolved. The even-safe two rows are already original integrable. Hence the **same final** D587 730-row lattice has genuinely path-dependent *intermediate* cokernel defects, but an unchanged final Gram and determinant.

The full historical same-field Schur valuation `69=28 even+41 odd` is preserved. Its determinant decomposition also obeys (derived algebraically from the original measured profiles):

```
  SAFE FIRST: v5(det intermediate four-row S1)=56,
              v5(det final scalar Schur)=13, total 69.

  BAD FIRST:  v5(det initial one-row Schur)=12,
              v5(det remaining four-row Schur)=57, total 69.
```

These Schur DETERMINANT valuations legitimately telescope because the Gram determinant multiplies across nested rational Schur complements. The COKERNEL CLASS orders do NOT telescope by naive summation. Neither is an extra add-on beyond `v5(det G_730)=3924`. The original full row lattice is never modified in Phase298.

Two independent *positive-definite* hostile toys (also CI green):
- `G=[[1,0,0],[0,5,1],[0,1,2]]`, det9: old component zero, new Schur component order5, combined order5.
- `G=[[5,5,1],[5,10,2],[1,2,10]]`, det240: old component order5 and new Schur component order5, combined order5 **not25**.

## 3. Phase298-B — the complete original class-number-one D163 control [P background + M]

**Separately preregistered at `a967d4994a3fa15f198047c47519a7908371de0c`, AFTER A passed but BEFORE B code/results.** [Complete exact class-one source CI #43379240150](https://github.com/Dojo-1/tenth-discriminant/actions/runs/43379240150) SUCCESS.

The imaginary quadratic **field** K=Q(sqrt(-163)) has class number one: discriminant Δ=-163, Minkowski bound `(2/pi) sqrt(163)<9`; primes 2,3,5,7 are inert, so every integral ideal of norm≤8 is principal (only possible 1 or4, with norm4 ideal (2)). This is a **classical theorem plus elementary residue calculation**, not a theorem proved by this AI artifact.

The repo's ORIGINAL source at D163, however, has `rho21,R40,S=J1,Q109`, and uses the integer-order real/imag sampler, **not** the maximal-order two-coset representation. It is a source-faithful actual-h1 control, with J1 instead of D587's J5. No claim that the positive field has a high-jet uniform property follows.

The test constructs the complete original 40×40 Gram from two exact original evaluation and mixed-moment methods and verifies all 1,600 entries. It exhausts **all 38 contiguous nested original row triples** `L_n⊂L_(n+1)⊂L_(n+2)` for n=1..38, with the genuine original consecutive monomials Z^n and Z^(n+1). K16 capped Gram Smith is uncensored for all old/intermediate systems involved. Results:

| Source-exact D163 control quantity | Measured value |
|---|---:|
| All contiguous two-stage cases | 38 |
| First stage has integral Z5 orthogonal projection | **31** |
| First stage has nonintegral Z5 projection | **7** |
| Second-stage order5 obstruction (any first stage) | **8** |
| Conditional direct-sum composition tests, all passing | **31** |
| New Schur-only obstruction after an integral first stage | **0** |
| Simultaneously positive old and Schur components after an integral first stage | **0** |
| Any finite-p16 censorship among eligible first stages | **0** |

This is a **strong negative control** for extrapolating D587's two-nonzero-components phenomenon: it is NOT seen in the actual-h1 D163 J1 contiguous sample. It is also an explicit counterexample to the broader but false hypothesis that class-number-one status alone ensures every original trace-Gram row projection is integral.

## 4. Phase298-C — explicit short h1 dual obstruction [M + P implication]

Preregistered AFTER the exhaustive B scan at commit `3346912c7c256d5300c2f7830b2ffcee484e56a6`, BEFORE C code. The decision to inspect `n=13` was explicitly RETROSPECTIVE: it was the **first** nonintegral original row attachment in the exhaustive n=1..38 D163 scan; no hidden prior prediction. [Source-exact dual witness CI #43379482469](https://github.com/Dojo-1/tenth-discriminant/actions/runs/43379482469) SUCCESS.

Let `A13=G_D163[:13,:13]` be the ORIGINAL trace Gram on monomials `1,Z,...,Z^12` with original Q109/J1/trace B=(2,326), and `c13=G_D163[:13,13]` the ORIGINAL cross column of next monomial Z^13. It finds the **explicit 13-component row vector mod5**:

```
  ell=(0,1,0,4,0,2,0,2,0,3,0,1,0),

  ell*A13=(0,...,0) mod5  (ALL13 original old columns),
  ell*c13=2 mod5.
```

The two displayed congruences are checked against the complete ORIGINAL Gram (whose source was independently verified). If `A13 x=c13` had a solution in Z5^13, multiplying by ell would force 0=2 mod5, contradiction. This is an explicit, human-reconstructible **local row-projection nonintegrality certificate even for an actual class-number-one FIELD**, scoped to this ORIGINAL repo sampler, not a new class-number-one theorem.

The adjacent prior original n12→13 projection is **integral**, independently verified through ALL12 original Gram equations modulo5^16 with the uncensored Smith profile. The compact JSON witness vector SHA256 is

`e0ec7fed718fcc4c7e9311e3ef11476a34fb083954b243d4f80eb7274745e32b`.

No primitive source filtration, Frobenius index, evaluation Smith factor, synthetic ellipse point, or extra determinant valuation was introduced.

## 5. Epistemic and field-theorem boundary

**[P-paper, not Lean kernel formalized]** Exact conditional integral-split cokernel decomposition, single-generator lcm/max order law, positive-definite toy counterexamples to additive order; classical Minkowski class-number-one argument for D163 and the elementary dual-functional contradiction.

**[M]** Original D587 complete five-row J5 trace Gram two ordering schemes and source-correct 725×4 first-stage integral matrix; precise old/Schur residual and actual odd Gram Smith profiles, complete opposite-parity source checks. Original D163 actual field source 40×40/109 observations/J1; all 38 nested two-step cases, source-exact dual witness for n13 and adjacent n12 positive control. CI tests remain AI-authored and correlated by shared source helpers, not external replication.

**[H]** Arbitrary sequences with NONINTEGRAL first stages admit additional extension/derived gluing structure not covered by the split formula; transport of the high-dimensional Worldlet observable back into all original trace-gram sources while preserving the original arithmetic lattice; any UNIFORM p-adic mass inequality across hypothetically large h1 field discriminants; any stronger tenth-discriminant upper cutoff.

**[R]** Summing each stage's coker image order as though they were independent determinant valuation factors; applying the split lemma when the first frame is nonintegral; treating the integer-order D163 J1 source as an S5 experimental surrogate; asserting h1 automatically makes every original sampled row projection integral; claiming new p-adic determinant gain from formal/subsample transport.

**Next smallest theorem experiment:** Model a nonintegral first-stage attachment as a short EXACT sequence of discriminant modules with a nontrivial extension class; define a functorial map between the discriminant groups `coker(G_n)` and `coker(G_(n+1))` only after specifying the actual inclusion and its dual, rather than pretending that cokernels have a canonical covariance under arbitrary row injections. Test this on the D587 bad-first stage and the D163 n13 dual witness. A composable remainder **category** may be a useful invariant, but its connection to a tenth-discriminant class-number-one cutoff remains H until a uniform arithmetic implication is proved. Keep the entire PR stack DRAFT and independent reviewer gates #50/#51 pending. 
