# Phase304 — matched non-h1 fields, real J2 ordinary jets, and the source-to-field correction

**2026-11-13, after the A/B/C source results, stacked DRAFT PR #196 over Phase303 #195.** Research conducted by an AI-assisted workflow with original source SHA gates and focused GitHub Actions; no human-independent mathematical peer review. All prior drafts remain open, no Work mode, merge, main edits or alteration to the integrated 322^4 field theorem and separate unmerged 321^4 draft #157.

## Provenance and logical accounting

**Initial PRE-REGISTRATION before ANY Phase304 source code:** [PRE_REGISTERED_ALL_LINES.md](PRE_REGISTERED_ALL_LINES.md), GitHub commit `6bc1cfa48b8e1731f48cd7e761a80e1366e9f3e7`. The matched negative fields `D∈{163,167,187}`, original-policy high-jet `D=203`, matched norm cutoff441, p5 K16, original full maximal order, original monomial labels and field status tests were all frozen in advance. Field-dependent MATCHED source results were not promised. **Separate post-result C prereg** [PRE_REGISTERED_J2_PRIMITIVE_RADICALS.md](PRE_REGISTERED_J2_PRIMITIVE_RADICALS.md), commit `41c2c7d9a1904ee738b3805bc65ed7f9374ebf26`, after Phase304-B was green and before C code. C is an explicitly FOLLOW-UP result, not a pre-specified prediction of B.

Evidence labels:
- **[P-paper / classical]** imaginary quadratic maximal-order norm, local p5 unramified quadratic isometry and Hensel lifts, elementary norm-p obstruction to h1 from split/ramified primes, ordinary-jet Frobenius relation, determinant index-square, rank of restricted bilinear form and trace radical.
- **[M]** exact finite field/observation/Smith computations below, dependent on AI-authored source code and CI plus selected independent alternate computations.
- **[P-Lean only after exact-head build]** narrow 4-lemma source file `lean/TenthDiscriminant/Phase304SourceJet.lean`; it formalizes an integer trace-coordinate identity plus mod5 value and FIRST ordinary derivative of `(Z^5-W)Z^k`. It does NOT formalize full arbitrary j, source matrix rank, class number or any new bound. Whole-root Lean CI must be checked at final head; compilation is not external independent proof.
- **[H]** any improved uniform class-one field/zero-free theorem or universal positive extra primitive Gram valuation.
- **[R]** treating a local p5 Smith profile or the 30 determinant valuation as CHARACTERIZING h1; treating saturated evaluation rows as additional original field discriminant mass.

## A. Matched source controls falsify class-number-one specificity [M + P classical h1 counterexamples]

[Focused GitHub Actions #43410350633](https://github.com/Dojo-1/tenth-discriminant/actions/runs/43410350633) **PASS**, independently rerun on later Phase304 heads. Three squarefree D≡3mod4, all p5 inert, genuine maximal quadratic integer rings O_K=Z[(1+√−D)/2]:

- D163: classical h(K)=1; no split/ramified prime below (163+1)/4=41.
- D167: classical **h(K)≠1**, since 2 splits (fundamental discr−167≡1mod8) but norm form a²+ab+42b² cannot represent norm2. The prime ideal over2 cannot be principal.
- D187: classical **h(K)≠1**, since 7 splits ((−187 mod7)=2 a nonzero square) but a²+ab+47b² cannot represent norm7; also 11 ramifies with norm11 and similarly obstructs h1. These are hand-checkable norm/prime-ideal arguments, NOT inferences from the source Gram.

All three local p5 quadratic extensions are isomorphic. For D167,D187, the code deterministically Hensel-lifts alpha≡2mod5 satisfying `163 alpha²≡D (mod5^16)`, and checks mod5^16 hermitian norm transport in half-integral coordinates. **The local isometry does not transport finite norm-ball observation supports as equal sets.** Actual fields were sampled as ALL half-integral points `(p+q√−D)/2`, p≡qmod2, with p²+Dq²≤1764, exactly the SAME norm≤441 and SAME 40 monomial source rows J=1. A distinct omega-coordinate integer trace-oracle matched all1600 Gram cells in EACH field and arm. Frozen half-integral DVR Smith arithmetic (Phase303-F) resolved every p5^16 grade.

| Matched FULL maximal order D | Actual h1? | Q | F5 evaluation rank | F5 Gram rank | original G40 p5 Smith | exact v5(det) |
|---|---|---:|---:|---:|---|---:|
| 163 | yes | 225 | 25 | 25 | `{0:25,2:15}` | **30** |
| 167 | no; split2 | 221 | 25 | 21 | `{0:21,1:8,2:11}` | **30** |
| 187 | no; split7 | 205 | 25 | 25 | `{0:25,2:15}` | **30** |

**The decisive RETIREMENT:** non-h1 D187 has EXACTLY the same FULL matched-source 40-row p5 Smith profile, Gram rank and valuation as h1 D163. The naive converse 'this local Frobenius/Gram pattern implies h1' is FALSE. D167 independently demonstrates that even the scalar valuation30 is weaker: its source has 25 distinct residue classes and polynomial evaluation rank25, but 4 classes have zero multiplicity mod5, so the original Gram rank is 21 and the Smith profile differs. It still has v5(det)=30, and its divided Frobenius primitive Gram rank40 but first25 Gram block rank21. This matters: primitive full-unit determinant suffices for v5=30, while the more precise profile 0^25/2^15 additionally requires top25 Gram unit.

The matched old-suborder negative controls:
```
D163 Qeven109   v5(det)=77   Smith{0:15,2:8,3:7,4:10}
D167 Qeven109   v5(det)=77   Smith{0:15,2:8,3:7,4:10}
D187 Qeven105   v5(det)=81   Smith{0:15,2:4,3:11,4:10}.
```
These rows are actual even-q maximal-order points; no fabricated observations were used. **Separately**, the *NATIVE* original repo parameter policy `params(D)` produces:
```
D163 rho21 R40/J1 FULL maximal Q225  v5 30 Smith{0:25,2:15}
D167 rho21 R41/J1 FULL maximal Q221  v5 34 Smith{0:21,1:8,2:11,4:1}
D187 rho23 R46/J1 FULL maximal Q249  v5 53 Smith{0:23,1:2,2:12,3:9}.
```
Native policy changes R and sometimes rho with D; do NOT compare those valuations as a controlled class-number experiment. The D187 matched counterexample is exact at the specified common norm cutoff and common 40-row operator.

## B. Genuine original-policy HIGH ordinary J2 at non-h1 D203 [M + P polynomial identity]

[Focused GitHub Actions #43410611926](https://github.com/Dojo-1/tenth-discriminant/actions/runs/43410611926) **PASS**. D203=7·29 squarefree≡3mod4, p5 inert, and NOT h1 because p3 splits with norm3 <(203+1)/4=51 (also small ramified primes). This is the first high-J example in this PARTICULAR fixed suite that genuinely respects the ORIGINAL source parameter rule, but **it is not a known h1 field**.

The unchanged `source_probe.params(203)` gives `rho24,R50,S=J2`, 100 original monomial rows `Z^r W^s` and **ordinary Z derivatives j0,j1 holding W fixed**, with old integer-order Q127 and full genuine maximal-order Q263 (136 new odd-half-integral observations). Actual old source raw jets transported to maximal-even source in **50,800** ω-coordinate checks; 100 cells of the old original exact mixed-moment source oracle and 100 independent full maximal integer-trace cell checks pass. The full 100x100 original Gram retains the original single trace operator throughout.

**Exact classical Frobenius jet identity:** inert p5 gives `z^5≡conj(z) mod5` for every original z. The polynomial `F=Z^5-W` satisfies `F(z,conj(z))≡0 mod5`; every positive FORMAL ORDINARY derivative `∂_Z^j F` has coefficients divisible5 for all j≥1, since `d^j Z^5/dZ^j` contains 5 or is zero. By Leibniz, `∂_Z^j(F H)` vanishes mod5 at source points for ANY polynomial H and any j≥0 with W held fixed. In the 100-row original source, exactly **45** independent source-row expressions `(Z^5-W)Z^(r-5)`, r5..49, lie in the mod5 nullspace of all **both** original j0/j1 channels. These are real ORIGINAL row combinations in the unimodular row lattice U, not arbitrarily moved flags.

The code verifies EVERY one of the 45×2 ordinary jets×2 channels on BOTH samples (22,860 old, 47,340 full raw divisibility checks) and **ALL 10,000 original source Gram entries** of
```
 U G_original Uᵀ = D5 Gprim D5,
 D5=diagonal(5 on 45 selected source rows; 1 elsewhere).
```
Division by5 forms a separate evaluation superlattice; the original Gram retains its valuation. For nonsingular Gram, `v5(det Goriginal)=90+v5(det Gprim)≥90`. This is a source level bound that DOES NOT require h1, as the non-h1 D203 instance confirms.

Measured original FULL 100-row p16 elementary divisors:
```
integer-order old Q127:
 {0:22,1:8,2:20,3:10,4:30,5:6,6:4}, v5(det)=252;
genuine maximal full Q263:
 {0:38,1:12,2:25,3:24,4:1}, v5(det)=138.
```
All grades uncensored K16, and both exceed the universal 90 from the 45 source Frobenius rows.

## C. Primitive source, Gram and trace radical are DISTINCT carriers [M + P rank-nullity]

**Separately preregistered after B, before C code:** `41c2c7d9a1904ee738b3805bc65ed7f9374ebf26`. [Focused CI #43411272337](https://github.com/Dojo-1/tenth-discriminant/actions/runs/43411272337) **PASS**. Reconstruct the new primitive E/G on the exact frozen B source and resolve full primitive Gram Smith at **K15**, with all100 levels strictly below15. Confirm the unchanged original determinant splits correctly as 90 plus primitive:

| Original source D203/J2 | Integer-order Q127 | Maximal-order Q263 |
|---|---:|---:|
| Primitive E image dimension (mod5) | 60 | **95** |
| Primitive G rank (mod5) | 42 | **58** |
| Kernel of Eprim (original 100 rows) | 40 | **5** |
| Radical of trace pairing on im(Eprim) | 18 | **37** |
| Primitive Gram Smith | `{0:42,1:18,2:15,4:15,5:6,6:4}` | `{0:58,1:36,2:6}` |
| Residual `v5(det Gprim)` | **162** | **48** |
| Original `v5(det G)` =90+residual | **252** | **138** |

**Why the distinction matters:** Let E: F5^100→V be original observation map, and let the ambient original ω trace form B be nondegenerate because `det Bω=203≡3mod5`. The restricted pairing on `im E` need NOT be nondegenerate, so
```
  rank(E)=dim(im E),
  rank(E B Eᵀ)=rank(E)−dim(rad(B|im E)).
```
Consequently `100=dim ker(E)+dim(rad(B|im E))+rank(G)`. The CI actually selects a basis of the E image using a separate F5 Gaussian procedure, restricts the original Gram to that image basis, checks its rank, and verifies these identities—not just taking a difference of two unexamined scalar counts. For MAXIMAL full source it gives `100=5+37+58`; old source `100=40+18+42`.

This distinction is stronger than an abstract 'higher geometry' metaphor: part of the residual is **genuine evaluation-kernel information loss**, and part is a **nonzero source subspace invisible to the restricted trace pairing**. These are mathematically typed different phenomena, both tied to the precise sampled source. Neither implies class-number one nor creates extra original field discriminant mass. The residual val48 for full source has 42 positive primitive elementary grades, with six higher-order valuation units beyond one per positive level; old residual val162 has 58 positive grades with 104 excess units.

## D. Formalization and actual source-to-field implication map

Existing ROOT Lean already includes [ClassNumberInertBridge.lean](https://github.com/Dojo-1/tenth-discriminant/blob/main/lean/TenthDiscriminant/ClassNumberInertBridge.lean), which proves (subject to its imported Mathlib/definitions and axioms) the **class-number-one hypothesis implies an odd small prime is inert**, via principal norm lifting, and then derives `(p:ℤ)^(2*valuationWeight R S p) ∣ det(integerRectangularTraceGram Q ...)`. It explicitly excludes p2 from that theorem and handles a separate D15 ramified counterworld. The **prime-local Frobenius divisibility works WITHOUT h1**; global h1 is used only in the bridge to justify inertness for eligible primes. This source-vs-global direction is crucial, especially after D187 matched counterexample.

The newly introduced narrow [Phase304SourceJet.lean](https://github.com/Dojo-1/tenth-discriminant/blob/research/phase304-field-discrimination-and-jets/lean/TenthDiscriminant/Phase304SourceJet.lean) contains source-order trace pairing transport and j0/j1 ZMod5 identities for `(Z^5-W)Z^k`. The new module is reachable from the audited `lean/TenthDiscriminant.lean` root. **The exact-head Lean CI must pass BEFORE claiming new kernel proof**. It does NOT prove general all-j Frobenius, trace radical rank, Gprim full Smith, maximal-order data, or a new field discriminant result. The root prior [ActualField322.lean](https://github.com/Dojo-1/tenth-discriminant/blob/main/lean/TenthDiscriminant/ActualField322.lean) already encodes the class-number-one **322^4** field bound by applying the SAME source Gram's earlier lower and upper comparison; its successful build is separate from independent semantic review. Nothing in Phase304 changes that existing proof's statements or improves the bound.

**Most important OPEN hypothesis**: can an additional *uniform* source-specific primitive-G rank/valuation inequality be proved under the same hypothetical large-h1 conditions as the integrated 322^4 argument AND inserted into BOTH the arithmetic-lower and geometric-upper sides of the SAME original source Gram without illegitimate denominator/moving-frame transport? A D187 non-h1 clone refutes class-one specificity of the fixed D163 p5 profile, but does not itself refute every conditional uniformly quantified h1 inequality. To derive a tighter field bound, a theorem must use more than these small sampled fields, and must compete with the actual normalized Hadamard analytic upper at the same source dimensions. Keep this as **H** until a fully typed theorem is written and independently checked.

**Classical source comparison and novelty boundary:** [Tao's original tenth-discriminant challenge](https://terrytao.wordpress.com/2026/10/20/an-experimental-ai-math-challenge-using-tenth-discriminant-bounds-to-explore-arguments-ruling-out-siegel-zeroes/) explicitly welcomes bounds from specific methods and negative experiments. The public comments already discuss divided-Frobenius rank methods (Stephen Chung / rStation, reported D≤331) and determinant-family improvements (twinheterodox, reported q<570), as well as other proofs and certificates. They are third-party **source-reported** results, not independently reproduced here; Phase304 Frobenius methods should not be described as a new invention. The novelty claim for Phase304 remains **NOT CHECKED** beyond this limited corpus.

## E. Evidence corrections, stopping rules and next rigorous steps

- **RETIRE:** 'the full maximal-order p5 Gram profile `{0:25,2:15}` characterizes h1'. This is explicitly FALSE at fixed source scale: D187 h>1 exhibits the SAME 40-row signature as D163 h1. **Do not rescue it by moving to arbitrary flags.**
- **RETIRE:** 'v5(det original G)=30 detects h1'; D167 and D187 (both non-h1) also have exactly 30 under matched source geometry.
- **RETAIN [P conditional + M source]:** exact source order / local ring transport; original Frobenius row divisibility, index-square; finite-field residue multiplicity and trace-rank mechanism; typed evaluation-kernel vs restricted trace radical.
- **DON'T REWRITE:** the original source J for D203 is 2, genuine; its class number is *not* 1. The D187 native R46/rho23 is NOT the matched R40/rho21 experiment. D167 has 4 residue weights zero mod5 (Gram rank21 despite evaluation rank25), so Frobenius-primitive determinant unit does NOT alone imply `{0:25,2:15}`.
- **Current independent-review gap:** all Phase304 implementation, tests and formal proposal are AI-authored, with one pinned alternative DVR Smith helper and distinct trace basis. Multiple green runs on one repo are correlated, not external peer review. Keep PR196 DRAFT and do not merge.

**Next decisive research choice:** an invariant actually linked to h1 beyond inertness, e.g. a prime-factor/ideal norm condition feeding the same original Gram lower bound uniformly across hypothetical large D; or improved analytic Hadamard geometry with unchanged source. Preregister a matched non-h1 control and failure criterion for either direction. Avoid running further unbounded p5 flag scans without that bridge.
