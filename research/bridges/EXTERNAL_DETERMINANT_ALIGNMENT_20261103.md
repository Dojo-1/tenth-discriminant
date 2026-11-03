# A mathematical alignment contract — original thin Gram and external determinant programs

**Internal comparison, 3 November 2026.** This note does **not** claim a common determinant, a new bound, coauthorship, priority, endorsement, or independent verification. It documents an exact source-to-source comparison before any proposed mathematical bridge or communication.

## Fixed sources

- Our baseline: [integrated Phase199](https://github.com/Dojo-1/tenth-discriminant/pull/123), mainline merge `dc7e19ebefe2aecb0f2644b2ccd2b42203200a55`; `ActualField323.lean`, `SourceOddBinary323.lean`, `ThinUpper323.lean`. The root-322 extension is still **H as a field theorem**, even if its isolated source lemmas compile.
- [twinheterodox, v0.7.0](https://github.com/twinheterodox/tenth-discriminant/tree/v0.7.0/versions/v7), published 26 October 2026; [its reproducibility guide](https://github.com/twinheterodox/tenth-discriminant/blob/v0.7.0/versions/v7/README.md) and [review record](https://github.com/twinheterodox/tenth-discriminant/blob/main/versions/v7/REVIEW.md). The reported cutoff is `q < 570` followed by finite classification. The numerical and model cross-checks reported there are **not** Lean or human peer review of v7.
- [twinheterodox, elementary companion](https://github.com/twinheterodox/tenth-discriminant/tree/elementary-v0.1.0/companions/elementary): different, shorter `q < 32768` argument; external [Murphy Lean adaptation](https://github.com/DrMurphyIsIn/tenth-discriminant/tree/f0995bf604056a98f0af0d182ed152c6bd996419/determinant) is explicitly for this companion, **not** the v7 theorem.
- [rStation challenge](https://rstation.ai/problems/tenth_discriminant) and [independent node-window example](https://rstation.ai/problems/tenth_discriminant/papers/28): further source-dependent reductions that must not be read as a proof of equivalence between architectures.

## The common codomain and what is *not* common

All programs discuss imaginary quadratic class-number-one fields. For a number field `K`, the comparable numerical observable is the **absolute fundamental field discriminant** `q = |disc(K)|`, *not* an arbitrary radicand or lattice-area parameter. Our encoded theorem says `q < 323^4 = 10884540241`; twinheterodox v7 says `q < 570`. These bounds are comparable **as endpoints**, and v7 is vastly stronger. They are not comparable as **proof efficiency**, proof novelty, or normalized gaps merely from the numerical values.

| Typed feature | Our original thin-Gram chain | twinheterodox v7 / elementary distinction | Alignment obligation |
|---|---|---|---|
| Field object | Arbitrary totally complex degree-two `K` reduced to odd/even imaginary-quadratic charts | Fundamental discriminant `q`, imaginary quadratic class-number-one | Verify exactly the discriminant and field chart map; preserve sign and even cases |
| Rank/dimension | `R = floor(D/4), S = floor(R/25)`; thin support `ellipsePairs` | v7: auxiliary inert prime and common finite-field rank; elementary: rectangular interpolation with `S=floor(R/12)`, `J=ceil(R/48)` | **Do not identify different R, S, J or evaluation modules** |
| Jet/basis | Original ordinary Z-derivatives, W held fixed, integer trace Gram | Green derivative determinant and van Dijk Frobenius nonvanishing; divided derivatives and factorial refinements appear elsewhere | Require a fully typed basis/jet transform and proof of integrality, rank, determinants and local valuations |
| Arithmetic source | Inertness from class-one original source, fixed p=3,5 valuation gains and one binary factor | Split-prime primitive-norm counting, auxiliary inert prime, Frobenius and factorial divisibility | Compare valuations of a **common integer** only if one is exhibited; otherwise keep incomparable |
| Archimedean source | Same thin ellipse; padded ellipse enters **count only**; rowwise Hadamard and radial saving | Smoothed prime sums, analytic kernels, norm Euler products and size estimates, regime dependent | Must prove common upper-bounded object and account for changed normalization |
| Evidence | Lean exact theorem relative to encoded definitions, standard axioms, source fidelity still open | Paper + exact numerical programs + reported AI-model checks; elementary Lean adaptation independent and scope-limited | **Neither** proof certificate automatically validates the other's interpretation |
| Outcome | Current integrated `q<323^4`; 322 is unmerged research | v7 `q<570` and nine-field finite finish | No statement that our bound is state-of-the-art, competitive, or new classification |

## A candidate algebraic common layer: weighted Cauchy–Binet [H for source instantiation]

The source definitions in [`IntegerTraceGram.lean`](https://github.com/Dojo-1/tenth-discriminant/blob/main/lean/TenthDiscriminant/IntegerTraceGram.lean) explicitly evaluate ordinary `Z` derivative jets and sum their integer trace pairing `2(x x' + D y y')` over the ORIGINAL pair support and derivative orders. Accordingly, an integer evaluation matrix `E` with separate real/imaginary columns and diagonal weights `W = diag(2,2D, ...)` is a natural exact **candidate representation** of the same integer Gram. The formula below is an abstract algebraic identity once the representation and dimensions are checked; its specialization to `integerRectangularTraceGram` still needs a source-identity Lean lemma.

$
G=EWE^{\\mathsf T},\\qquad
\\det G=\\sum_{I:\,|I|=n}\\det(E_I)^2\\prod_{i\\in I}w_i.
$

By contrast, [v7, §3](https://github.com/twinheterodox/tenth-discriminant/blob/v0.7.0/versions/v7/proof.tex) constructs an ordinary-derivative matrix with `R=p_0` an **auxiliary inert prime**, proves full row rank by reduction to `F_{p_0^2}` and `nJ >= RS`, then **fixes one nonzero square minor** `M` and sets `Delta=|det(M)|^2`. That is a different determinant *even where the derivative algebra looks alike*. They use `S=floor(3R/64)`, `J=ceil(R/9)`; ours uses `R=floor(D/4)` and `S=floor(R/25)`. These parameter names have distinct types and scales.

**What a legitimate transport would demand:** write down both evaluation arrays with typed indices, points, derivative conventions and number-field embeddings; prove whether any change of rows/columns preserves integrality, rank and determinants; then prove a concrete map (if any) from their selected complex minor to our weighted real-coordinate Gram-minor sum. Weighted Cauchy–Binet alone does **not** identify their chosen minor with a term in our sum, and certainly does not transport their auxiliary-prime valuation bounds. Absent that map, preserve `R_formal` and `R_transport` as unresolved.

**Minimal discriminating test, deferred:** a small explicit matrix built from one identical polynomial/jet/point family in both coordinate conventions, computing both the weighted Gram determinant and all maximal minors with exact integer arithmetic. This is a semantic mapping test, not a new geometric optimization or a proof for all `D`. Do not run it as a substitute for the active 322 source-to-field audit.

## Proposed semantic bridge — an experiment, not a theorem

1. **Reference and hypothesis.** Compare exactly the class-number-one hypothesis, fundamental discriminant sign convention, and permitted inputs (including additional auxiliary-prime existence). Demand a source link for each.
2. **Two determinants.** Write down their domains, row/column index sets, evaluation maps, derivative operators and bilinear forms. The same word *Gram* is not an equivalence. Try to build a natural typed map `T`; only if it exists ask whether `G_ours = T^T G_theirs T` (or a different precisely stated relation) holds.
3. **Valuation transport.** Check one small exactly computable instance and one known class-number-one field as a sanity test, but note that our large-`D` theorem's geometric guards **do not apply at 163**. A mapped finite example cannot replace the universal determinant-divisibility theorem.
4. **Uniform bounds.** Keep the normalized gaps separate until denominators, parameters, support and quantifiers agree. Do not compare `0.018345` in v7 with our `2853/500000000` by naked scalar magnitude.
5. **Coherence audit.** Only then ask whether an alternative path through the common field discriminant commutes. A pentagon sketch without typed associators is a visualization, not a Mac Lane coherence theorem.
6. **Independent witness and outreach.** Preserve their priority and exact release/tag citations, copy no unlicensed or uncredited artifacts, mark all unreviewed transfers H, and ask permission before any external message, issue or PR addressed to collaborators.

**Pre-registered geometric test is separate:** [Issue #124](https://github.com/Dojo-1/tenth-discriminant/issues/124). Block-Hadamard or mesh results only count if they improve the **same original Gram** against the fixed baseline with the preregistered controls; none has yet been run.

## Gate for a legitimate connection

A bridge graduates from *conceptual adjacency* [S] to *formal conjecture* [H] when both determinants and all transport maps are explicitly typed. It becomes [P] only for a Lean-checked source theorem on those exact objects; external semantic agreement remains a separate audit. If an intended map changes the proof object, report the remainder instead of forcing equivalence.

The appropriate initial collaboration question is narrow: *does any rank or valuation mechanism from v7 or the elementary companion descend to the unchanged ordinary-jet thin trace Gram without altering the positive integer determinant?* The current evidence does not establish that it does. A negative answer is useful and should be recorded.
