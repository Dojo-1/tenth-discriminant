# Phase166 — One integer, two families of prime factors

The central integer is not the quadratic field discriminant. It is the positive determinant of the **original ordinary-derivative trace Gram**, evaluated on the **same thin ellipse** as the Lean-checked 41.00625-billion field theorem:

\[
z=\det G_{\mathrm{thin}}, \qquad
G_{\mathrm{thin}}=E_{Q_{\mathrm{thin}}}\,B\,E_{Q_{\mathrm{thin}}}^{\mathsf T}.
\]

Its row support, fixed-W derivative convention, integer coordinates and the trace weights \(2,2D\) remain unmodified.

## The proof in ordinary mathematics

Phase164 already shows that, under the same squarefree odd-chart class-number-one assumptions and the same geometric floor \(D\ge 450^4\),

\[
2^{\Lambda_1(R,S)}
\prod_{\substack{p<R\\p\ {\rm odd\ prime}}}p^{2v_p(R,S)}
\mid z,\qquad z>0.
\]

Call the odd product \(P_{\rm odd}\). Both factors are positive integers, so the divisibility implies \(2^{\Lambda_1}P_{\rm odd}\le z\). Taking the increasing real logarithm and expanding its factors gives the *exact* target

\[
\boxed{\Lambda_1(R,S)\log2+
\operatorname{exactOddPrimeMass}(R,S)
\le \log z.}
\]

The empty odd-prime product is 1, with logarithm zero. The original \(\operatorname{exactOddPrimeMass}\) **excludes prime 2** by definition. We may therefore multiply the coprime families without counting the binary factor twice.

The old recovered arithmetic estimate has an independent chain

\[
\operatorname{recoveredPrimeMassLower}
\le \operatorname{exactOddPrimeMass}.
\]

Combining this with the boxed inequality gives an exact logarithmic lower bound including the certified binary contribution.

## How to read the Lean

Start at [BinaryThinGramBridge](../../lean/TenthDiscriminant/BinaryThinGramBridge.lean), which proves positivity and the integer bound. Then read [BinaryThinLogBridge](../../lean/TenthDiscriminant/BinaryThinLogBridge.lean):

1. oddFactor_pos — even the empty product is strictly positive
2. log_oddFactor_eq — exact odd-product logarithm, without a new prime source
3. log_binary_odd_le_of_int_le — monotonicity of log for one positive integer
4. original_binary_and_exact_odd_mass_log_of_pos — **arbitrary original Q** given positive Gram and source arithmetic
5. thin_binary_and_exact_odd_mass_log — source-typed thin-Q theorem
6. recovered_mass_le_exact_odd — existing recovered-to-exact odd inequality, exposed independently
7. thin_binary_and_recovered_mass_log — both contributions on the same determinant

Every premise is visible in the declaration. The abstract elementary product-log argument is kept separate from field-specific arithmetic.

## Why the arbitrary-support theorem matters

The strongest new interface deliberately avoids the production ellipse's large-D assumption. For **any** finite original observation support Q, let z = det G_Q > 0 be the exact integer trace-Gram determinant. Under the original odd-chart, squarefree, class-number-one and inert-prime cutoff hypotheses, the existing source proof establishes

\[
2^{\Lambda_1(R,S)}P_{\rm odd}(R,S)\mid z
\quad\Longrightarrow\quad
\Lambda_1(R,S)\log 2+\operatorname{exactOddPrimeMass}(R,S)\le\log z.
\]

The new Lean declaration **original_binary_and_exact_odd_mass_log_of_pos** takes **the positive determinant as a hypothesis**, instead of pretending a large-D ellipse count is necessary. It is the nonvacuous reusable arithmetic module. A later geometric theorem may supply positivity for a new Q and a new D-range; neither construction nor a lower field cutoff is claimed here.

For the current thin ellipse, **thin_binary_and_exact_odd_mass_log** specializes that arithmetic with the *existing* positivity certificate, but its full field assumptions at D >= 450^4 are already excluded by the current field-discriminant theorem. We preserve this logical distinction: a correct conditional theorem is not a new field result.

**Current verification (2 November 2026):** [Phase166 PR #85](https://github.com/Dojo-1/tenth-discriminant/pull/85) is merged. The exact-head [focused Lean proof](https://github.com/Dojo-1/tenth-discriminant/actions/runs/41429815246), whole-library Lean compilation, source correspondence, permitted-axiom audit, source regressions and CodeQL passed. The [extensive negative-control suite](https://github.com/Dojo-1/tenth-discriminant/actions/runs/41429815239) [subsequently completed successfully](https://github.com/Dojo-1/tenth-discriminant/actions/runs/41429815239), closing the controlled merge-time exception. All full-root proof, source, permitted-axiom and negative-control checks are now green on the exact source head. This supports the encoded generic conditional theorem, not a new discriminant cutoff or independent mathematical peer review.

Even after this proof passes, there is **no new field bound**: the existing geometry, analytic upper, prime-tail and field transport are only verified at \(D\ge450^4=41{,}006{,}250{,}000\). The proposed \(377^4\) frontier and the four-generator \(2^{1358}\) Gram divisor require separate proof.

**Kill conditions:** reject any attempted proof that takes a log of a nonpositive determinant, switches Gram supports, changes ordinary to Hasse derivatives, or double-counts the prime 2. Preserve failing checks and their source heads. Human semantic review remains open in [issue #50](https://github.com/Dojo-1/tenth-discriminant/issues/50).
