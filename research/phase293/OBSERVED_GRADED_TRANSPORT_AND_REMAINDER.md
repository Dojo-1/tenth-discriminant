# Phase293 — from identical elementary divisors to explicit graded primitive pairing isometry

**Post-result synthesis, 12 November 2026.** All experiments were AI-authored with preregistration, frozen original-source helpers, exact modular arithmetic and source-faithful controls. All reported Phase293-focused GitHub CI receipts passed; neither those receipts nor the older Lean root compilation provide independent mathematical or actual-field peer review. This is a stacked DRAFT on Phase292 PR #183 → Phase291 PR #182, neither merged. No editing of PR #157 or the integrated 322^4 proof.

## The exact carriers (do not collapse types)

- **A:** full ORIGINAL D583 source: `rho53/R145/S=J5/Q383`, 725 integer monomial rows (r,s), 3,830 original ordinary Z-jet real/imag observation channels, original trace B583=diag(2,1166).
- **B:** first725-row **DIAGNOSTIC** of original D587 full source `rho53/R146/S=J5/Q383`, same 725 row labels but D587 field multiplication and B587=diag(2,1174). The actual original full D587 730-row source is separate and retains v5(det)=3924; this diagnostic is **not** an actual-field theorem replacement.
- Both are inert at p5 and share the same literal centered Q383 and odd-p central inversion, but are not the same quadratic field or integer Gram. Old Frobenius F5=1350 in each matched n725 source (counted ONCE); full secondary source index560; primitive H valuation35; original full/diagnostic 725-row trace Gram v5=3855.
- All calculations preserve the original ordinary ∂_Z^j with W held fixed, all five jet orders, original observation points and metric except in the explicitly labeled **formal transported-support** moment diagnostic. No binary half projector, invented valuations or p-adic field theorem.

## Result A — the moment-support remainder is NOT zero [P-paper + M]

For frozen original Q383, the row Z=(1,0) has exact diagonal
`G_D(Z,Z)=2 Σ_Q(x²+D y²)+2|Q|`. Original y layer counts y0:107, each y±1:95, each y±2:43 give `Σ_Q y²=534`. Therefore

```
G_587(Z,Z)−G_583(Z,Z)
   = 2*(587−583)*534
   = 4272 ≡ 2 (mod 5).
```

On the six frozen original polynomial rows `[(0,0),(1,0),(2,0),(1,1),(4,0),(4,1)]`, the FULL **six-by-six** original fixed-support Gram difference has rank **5 mod5**. [Phase293-A #43289725778](https://github.com/Dojo-1/tenth-discriminant/actions/runs/43289725778) passed the exact mixed-moment and original-jets oracle.

The local Z5 quadratic-order map `φ:u587→α u583` has `α≡2 mod5,17 mod25,67 mod125` and `583α²=587` modulo the indicated modulus. If the observation points move too, the six-row original-jet Grams satisfy `G_587(Q) ≡ G_583(φQ) mod 5^k` for k1,2,3; all 36 pairings were verified at each modulus. Consequently the signed moment **remainder** `G583(φQ)−G583(Q)` equals the original fixed-support Gram difference modulo the corresponding power. At residue level, transformed support overlaps only 279/383 literal sampled points and 104 leave; the mod5 residue-multiplicity imbalance also has mass104. This is a real typed source-observation obstruction, NOT a PSD increment, determinant gain, or proof that no other arbitrary observation isometry exists.

## Result B — higher quadratic invariants AGREE as well [P classification + M]

Smith factors of a symmetric integer matrix do NOT in general classify its local integral pairing; the hostile toy `<1>` versus `<2>` over Z5 has identical valuation profile but opposite unit determinant Legendre classes, hence no Z5 isometry.

For odd p5, Jordan decomposition `H ≃ ⊥_e 5^e U_e` has invariant `(rank U_e, Legendre(det U_e mod5))` for each scale. This is CLASSICAL; see [Magma pAdicJordanDecomposition](https://docs.magma-maths.org/LatticesQuadraticForms/Lattices/genus.html) and [Peters *Quadratic Forms*, §10.2](https://www-fourier.univ-grenoble-alpes.fr/~peters/Books/QuadraticForms/QuadForms.pdf). The Phase293-B symmetric-congruence test [#43289725529](https://github.com/Dojo-1/tenth-discriminant/actions/runs/43289725529) saturated the 363-even+362-odd source separately at fixed p5 K9, retaining all 3830 original observation columns and original B. It matched prior independent third-layer Smith profiles exactly and verified ALL even/odd primitive pairing cross-entries vanish mod125. Both A and B have the SAME graded signs:

| Central row parity | primitive p^0 grade | primitive p^1 grade |
|---|---|---|
| EVEN n363 | rank345, Legendre + | rank18, Legendre − |
| ODD n362 | rank345, Legendre + | rank17, Legendre + |
| Total n725 | rank690, Legendre + | rank35, Legendre − |

No p² or ≥p³ primitive grades. Classical odd-p Jordan classification therefore gives an **abstract** parity-equivariant primitive trace-pairing isometry over Z5. This DOES NOT imply original Gram equality or source-evaluation compatibility.

## Result C — actually construct and verify finite-precision pairing isometries [M]

The second preregistration `PRE_REGISTERED_CONSTRUCTIVE_PAIRING.md` at commit `e84e3ce` fixed the construction AFTER Jordan results and BEFORE code. [Phase293-C #43290487081](https://github.com/Dojo-1/tenth-discriminant/actions/runs/43290487081) passed:

- Produce the source and target primitive H matrices from the SAME frozen actual 725-row original-jet evaluation source and field-specific original metrics, via exact tracked-row p5 saturation, never applying internal Smith **column** operations to metric B.
- Implement a NEW tracked symmetric `T H T^T=diag(5^e u_i)` over Z/125 using only simultaneous integral-modular row and column transformations. Check **FULL matrix equality** and invertibility, not just determinant.
- Match each unit Jordan constituent using an explicit binary norm representation `a x²+c y²=b`, odd-p Hensel lift and 2×2 unimodular congruence `[[x,y],[-c y,a x]]`, then take a final square root. Construct the full block isometry S, invert the target diagonalizer and set `X=T_target^{-1} S T_source`. Check `rank_F5 X=n` and **all matrix entries** of `X H_583 X^T ≡ H_587 mod125`.
- Verified explicit maps:
  - `X_even∈GL_363(Z/125)`; SHA256 digest of uint8 residues `5a0702f9a5f39dfbd0991ed3602a3735df7bd861b193059c54b83c7a657aed59`.
  - `X_odd∈GL_362(Z/125)`; digest `4a7e270e5f231f163723f4af6bda063eb9fff7dc6afcc43c0bd86f005234ecd2`.
- The source code reproduces the full matrices, while the CI logs keep small verifiable digests. A <1>→<2> nonsquare case is rejected; rank-two equal-determinant, mixed-grade and offdiagonal-source Hensel cases pass.

This is an **actual constructed, parity-preserving isometry of the PRIMITIVE pairings modulo125**, a nontrivial new FINITE operator. It is NOT an integer `GL_725(Z)` gauge, a pairing congruence of the unsaturated original 725-row Grams, an isomorphism of D583 and D587 number fields over Q, nor a transform of each original observation point/jet source into the other.

## Result D — the canonical fixed-observation evaluation square is obstructed [P exact rowspace logic + M]

**Preregistered at commit `2474a57` AFTER the constructive isometry and BEFORE code.** [Phase293-D focused CI #43291441401](https://github.com/Dojo-1/tenth-discriminant/actions/runs/43291441401) PASSED the *negative* result with both positive and negative pivot-rowspace toys.

Use the EXACT previously saturated original observation matrices `C_A,prim125` for D583 full and `C_B,prim125` for D587 first725-row diagnostic, each 3,830 columns. In the D583-to-D587 **value-coordinate orientation**, the only canonical field-value map on fixed observation labels is `Y=diag(1,alpha^{-1})` on each original (j,q) coordinate pair, where `alpha^{-1}≡28 mod125`. Its metric orientation is checked:
`Y B_587 Y^T = B_583 (mod125)`. This is a legitimate pointwise coordinate map but **NOT** the actual geometric map q→phi(q), whose support leaves the original ellipse.

In each odd-p parity sector, `A=C_A,prim125 Y` has FULL row rank n mod5. Choose n original observation columns P with invertible `A_P` over F5. If ANY row matrix X over F5 satisfied `B=X A`, it would be uniquely forced by `X=B_P A_P^{-1}`; hence a SINGLE disagreement in any other column is a mathematical proof of nonexistence for this fixed Y. The exact code constructs the unique candidate modulo125 from the *same* invertible pivot columns and replays all original observation channels modulo5 and125.

**Measured (pivot-dependent residual counts, but invariant existence verdict):**

| parity | n | candidate rank mod5 | nonzero candidate residual entries mod5 | first explicit nonmembership |
|---|---:|---:|---:|---|
| even | 363 | 362 | 41,164 | primitive row314, jet3, original q=(-37,-1), real: predicted3, target4 mod5 |
| odd | 362 | 362 | 37,786 | primitive row312, jet4, original q=(-12,-2), real: predicted1, target2 mod5 |

Both sectors' candidate X reproduce their pivot columns exactly modulo125. Both fail at a nonpivot original channel modulo5. So **NO row X, invertible or otherwise, can complete this specific fixed-Q-index canonical value-map evaluation square over F5**, and therefore none modulo125 or Z5. This is strictly stronger than saying the previously constructed pairing X happened to fail the source map. It is NOT a no-go theorem for ALL possible original-observation-side maps Y: allowing point moves, signed jet permutations, broader B-orthogonal mixing or different field/source conditions is a DIFFERENT question.

The result is structurally consistent with Result A's rank5 six-row moment defect and the 104-point support escape. It also coexists with Result C's genuine parity-preserving **primitive pairing** isometries: the two mathematical propositions have different objects and requirements. Neither provides new p-adic determinant mass for the same source.

## Unclosed source-to-pairing square (precise next theorem target)

The present computed square closes only on the primitive-form level:

```
   L_583,prim -- X (mod 125, parity) --> L_587,prim
       | C_583,prim                       | C_587,prim
       v                                  v
 (Z5^3830, B583)  -- Y ? -->       (Z5^3830, B587)
```

Here `C` is an original-observation embedding of the p-saturated rows and B is the actual original trace metric. An observation-side map Y compatible with original channel/point/jet structure is still MISSING. In row convention `C_B = X C_A Y` and `Y B_B Y^T=B_A` would be a SUFFICIENT exact source-and-metric covariance condition (with correct typed fields), implying the Gram congruence. Our explicitly constructed X was selected using only primitive pairings and has **not** been shown to satisfy this square for any source-compatible Y. Merely knowing an abstract ambient orthogonal extension exists would also be weaker than a channel-permutation/field-value map and would not give a uniform field-theorem factor.

**Next legitimate theorem target:** Phase293-D has ruled out every row map for the **fixed-index canonical field-value Y**, not just the constructed pairing X. Specify the permissible larger observation-side group (point moves, jet-compatible signed permutations, and/or full B-orthogonal maps), then test whether the original primitive embeddings have compatible orthogonal complements or a source-support obstruction in that larger category. A freely chosen ambient isometry, even if it exists, is weaker than a permutation of original samples. No uniform h1 consequence follows from the finite matched sources.

## Evidence boundary

[P-classical/paper] explicit moment identity, local field isometry when support moves, odd-prime Jordan/Legendre classification, Hensel binary norm congruence and source/metric diagram implication.

[M] frozen 6-row original moment defect rank5 mod5, complete original n725 parity primitive Jordan signs, deterministic full Xeven/Xodd mod125 congruences and negative controls under AI-authored exact GitHub Actions runs.

[H] source/jet/point-channel compatible Y and a provable uniform transverse-wall/Schur transport across h1-admissible growing discriminants. [R] Smith alone implies isometry; local field isometry preserves literal Q; abstract primitive congruence can be added as an independent Gram divisor; a finite pair guarantees an asymptotic law.

**Source-to-field/human review #50/#51 remains open**; no theorem updating 322^4/321^4, exceptional-zero bound or Heegner classification is claimed. Draft only, no Work mode.
