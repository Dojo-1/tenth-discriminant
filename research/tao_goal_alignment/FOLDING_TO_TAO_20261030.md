# Folding our investigation into Tao's challenge

**30 October 2026 — Phase134 publication update:** [PR #52](https://github.com/Dojo-1/tenth-discriminant/pull/52) merged after [exact-head full-root Lean CI](https://github.com/Dojo-1/tenth-discriminant/actions/runs/41108320303), permitted-axiom audit and known-false controls **passed**. The narrative below preserves the original preregistration; the generic all-minors divisibility and positive rectangular-weight lemmas are now [P], but the cross-method interface and any improved cutoff remain [H].

The [original challenge](https://terrytao.wordpress.com/2026/10/20/an-experimental-ai-math-challenge-using-tenth-discriminant-bounds-to-explore-arguments-ruling-out-siegel-zeroes/) does not ask solely for the smallest tenth-discriminant bound. It asks for effective Heegner-free bounds extracted from different methods, optimization *within* each method, finite endgames, potentially reusable high-quality formalization, comparison of arrangements, revisiting failed arguments, extensions to higher class number, and an honest human-facing account with AI assistance disclosed and prior authors credited. Even a poor bound or a killed improvement can be useful when it reveals a mathematical cost that a stronger but opaque argument hides.

## Post-review mathematical correction — retain the normalization

The external [rStation exact-rank route](https://github.com/dualverse-ai/tenth_discriminant/blob/main/bound-331/latex/rank.tex) already divides the triangular $(Z^p-W)^m$ rows by $p^m$ and rescales Taylor-jet columns by $p^\ell$ before asking for rank over the residue field. Our theorem about **E before normalization** therefore does not exclude rank of their transformed matrix. Nor can we freely identify their triangular support and chosen distinct-residue nodes with our full original ellipse, or their Taylor coefficient jets with our ordinary derivatives: the change introduces $j!$, possibly zero modulo $p$. For $p\le \rho$, our original lattice contains two nodes with the same reduction, $(0,0)$ and $(p,0)$, so their distinct-residue premise fails there. Such losses must be carried as typed remainder rather than waved away by a geometric metaphor.

The useful problem for the next round is now **simultaneous row and column integral normalization with source-accountable prime and sampling constraints**, tested against the classical positivity proof at matched cost. Until that is built and falsified, the 47.0-billion cutoff is unchanged and no Siegel-zero theorem follows. External contributors' existing normalization ideas receive their original attribution; this is not a novel no-go theorem for them.

What remains of **our** approach when we submit it to those goals?

The verified object is the *actual field discriminant* at the endpoint. The bridge, however, is another integer: the determinant of the full positive trace Gram of the **original** finite ordinary-jet observation matrix E. A row-unimodular prime extraction gives a two-sided integral p-adic factor in the Gram. An integer radial change of frame lets the same determinant face a sharper Archimedean upper bound. The present checked result is the actual-field strict bound |disc K| < 47,000,000,000 for totally complex degree-two K of class number one (PR #49, exact-head whole-root Lean success). It is not the strongest numerical bound on the challenge; other contributors report dramatically smaller constants under different methods.

Our last rounds kept lowering a *single scalar threshold* while the cost to another mathematician of reconstructing each new theorem remained high. That is a methodological shortcoming, even if every Lean endpoint is formally checked. The frozen Argon report did not independently replay the later proof; fresh models discussing our own argument remain correlated witnesses. We should not substitute longer readmes, a 360-by-360 controller, or further metaphorical symmetries for an independent mathematical objection, concise proof, or measurable transfer.

For this round, a different kind of progress is preferable: **show which plausible cross-method substitution is impossible, with exact hypotheses.** This has a place in Tao's challenge even if it moves no cutoff.

Our direct method gives an integer extraction

    U_p E = Delta_p Ehat,   det U_p = 1,
    Delta_p = diag(p^(k_1),...,p^(k_n)),  F(p)=sum_i k_i.

For every choice I of n original observation columns,

    det(E_I) = p^F(p) det(Ehat_I).

The exact matrix is the point: if F(p)>0, no maximal minor of E is nonzero modulo p. The *same* p cannot be both a nontrivial row-divisor prime and a full-rank witness modulo p. In the repository's specific R-by-S rectangle, F(p)>0 whenever 0<p<R and S>=2. The formalization under test in Phase134 aims to prove both statements in Lean, not to assume a general finite-field rank theorem or a magically chosen prime.

There is an important remainder. Van Dijk-style auxiliary-inert-prime rank arguments operate on a chosen evaluation/derivative matrix and often a selected minor. They need a separately admitted prime q and a justified nonzero minor. To use one on **our fixed E**, we must match the monomial labels, original lattice samples and ordinary derivative slots, prove the existence of a compatible q without circularity, and pay any q-size penalty. Under the present factorization, q<R with nontrivial F(q) is impossible as the rank witness. For the odd large-field class-number-one regime, small eligible odd primes are exactly where the arithmetic divisor comes from. That makes a small-auxiliary-prime transplant particularly suspect, not universally impossible for a *different* E.

The inverse mistake is equally tempting: a selected minor may prove that E has full row rank, but a sharp *upper bound* for that one minor does not bound the entire Gram determinant; the latter is a weighted Cauchy–Binet sum of squared maximal minors. A full new endpoint must reconstruct both sides of the determinant comparison, not promote a local lemma by analogy.

The experiment therefore has an unusually clear stopping point. If the generic integer all-minors lemma and the strict F(p)>0 rectangular weight guard cannot be expressed as short Lean statements without altering E, we preserve the failure and stop. If they compile and pass permitted-axiom/negative controls, they are small **formal compatibility results**, not a new bound. If a later independent admissible q produces a compatible nonzero minor and a real reduction in sampling or analytic cost, that can motivate a new determinant round. Until then, the 47-billion theorem stays unchanged.

For a human reader, the smallest counterexample is E=diag(3,1): p=3 forces a minor divisor and modular rank loss, while q=5 still witnesses rank. For the mismatch between a chosen minor and the whole Gram, take E=[1,1], B=I_2: each selected one-by-one minor is 1, yet det(EBE^T)=2.

The purpose of our geometry is not to evade those elementary facts. It is to make every move between the arithmetic, modular, analytic, field-theoretic, and human-readable views a **typed transport with an explicit remainder**. That keeps our exploratory style available while allowing Tao's collective project to reuse or reject the contribution without inheriting our whole ontology.

**Evidence distinctions:** [P] the 47-billion actual-field theorem at exact source SHA, [H] the new generic minor/rectangular compatibility until Phase134 Lean accepts it, [M] finite pilot controls only at their exact parameter range, [S] polyholonomic and 360-by-360 organization until tied to a falsifiable effect, [R] failed elaboration attempts preserved, and human independent mathematical review still open. AI involvement remains extensive; no external post was made here.

Source map: [Tao's objectives](../../TAO_OBJECTIVES_CURRENT.md) · [current original Gram](../../lean/TenthDiscriminant/RectangularGramFactor.lean) · [rectangular valuation](../../lean/TenthDiscriminant/RectangularValuation.lean) · [initial two-prime note](../rank_divisor_interface/ONE_MATRIX_TWO_PRIMES.md) · [Phase134 issue #51](https://github.com/Dojo-1/tenth-discriminant/issues/51) · [independent review issue #50](https://github.com/Dojo-1/tenth-discriminant/issues/50) · [merged 47-billion proof](https://github.com/Dojo-1/tenth-discriminant/pull/49).
