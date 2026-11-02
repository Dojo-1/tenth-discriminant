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
4. thin_binary_and_exact_odd_mass_log — source-typed thin-Q theorem
5. recovered_mass_le_exact_odd — existing recovered-to-exact odd inequality, exposed independently
6. thin_binary_and_recovered_mass_log — both contributions on the same determinant

Every premise is visible in the declaration. The abstract elementary product-log argument is kept separate from field-specific arithmetic.

**Status:** all the new declarations are **H until exact-head Lean compilation and the complete source/axiom/negative controls pass**. This branch depends on [Phase165](https://github.com/Dojo-1/tenth-discriminant/pull/84), whose exact exponent normalization has passed focused Lean but whose whole-root CI is still running.

Even after this proof passes, there is **no new field bound**: the existing geometry, analytic upper, prime-tail and field transport are only verified at \(D\ge450^4=41{,}006{,}250{,}000\). The proposed \(377^4\) frontier and the four-generator \(2^{1358}\) Gram divisor require separate proof.

**Kill conditions:** reject any attempted proof that takes a log of a nonpositive determinant, switches Gram supports, changes ordinary to Hasse derivatives, or double-counts the prime 2. Preserve failing checks and their source heads. Human semantic review remains open in [issue #50](https://github.com/Dojo-1/tenth-discriminant/issues/50).
