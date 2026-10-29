# Referee report: the tenth discriminant

## Recommendation

**Editorial recommendation: Insufficient evidence to judge.**

The frozen source is at the requested commit, `39e9ce34d09ed9f990fab4b9ed5e3980cee64119`, in a detached worktree. The original checkout was clean and was not edited. Source inspection supports a positive semantic reading of both public theorems: the first is the class-number-one theorem for the canonical fields \(\mathbb Q(\sqrt{-d})\), and the second is stated for arbitrary totally complex degree-two number fields. Mathlib defines class number as the cardinality of the ideal class group of the maximal order. No concrete mathematical counterexample to the frozen claims was found.

That is not a proof review adequate for acceptance. The pinned project did not finish compiling: the Mathlib cache hostname was unresolvable, and a source-build attempt timed out after making substantial progress. Consequently, the public theorems were not kernel-replayed, `#print axioms` was not run, and the reported allowed-axiom set remains unverified here. The determinant-to-cutoff chain was source-traced but not independently rederived end-to-end. Antoine Olivier's source artifact was not located. The report therefore records meaningful partial audit evidence, not a clean bill of health.

## Principal mathematical assessment

The most serious risk is the quantitative bridge from small-prime nonsquareness to the **actual** integer trace-Gram determinant, followed by the extremely narrow analytic separation at the proposed cutoff. The report finds the intended chain in the source and no specific invalid inequality, but only a successful pinned Lean replay and a separate derivation can close this risk.

The strongest statement that survives source-level semantic review is the *meaning* of Theorem A: for every positive squarefree \(d\), the actual maximal-order discriminant is \(-d\) when \(d\equiv3\pmod4\), and \(-4d\) otherwise. Thus the listed radicands correspond exactly to the nine classical fundamental discriminants. The strongest theorem actually proved by the reviewed Lean source remains unconfirmed until the frozen project builds and its proof terms are checked in the pinned environment.

## Formalization fidelity and completeness

Theorem A is not, in its surface type, a theorem about arbitrary field types; it is about `ImaginaryQuadraticField d`. The separate representation argument is not needed to interpret the classical classification, since every imaginary quadratic field has a positive squarefree radicand. Theorem B does range over arbitrary `K` satisfying the displayed field, number-field, totally-complex, degree-two, and class-number hypotheses; the source constructs a squarefree radicand and transports class number and discriminant through an algebra equivalence. No hidden supplied generator or class-number-specific instance was found in that construction.

The inert-prime statement is not “all primes are inert.” It is a guarded claim for odd primes strictly below \((D+1)/4\), under squarefreeness, \(D\equiv3\pmod4\), and class number one. The source route is residue root \(\Rightarrow\) quotient of the maximal order of index \(p\) \(\Rightarrow\) a principal generator with norm \(p\) \(\Rightarrow\) contradiction from \(4N=(2x+y)^2+Dy^2\). The strict endpoint is mathematically necessary: for \(D=163,p=41\), \(-D\equiv1\pmod{41}\) has a root, while \(41=(D+1)/4\) is excluded.

Theorem A's classification chain uses a separate \(700\)-billion **radicand** cutoff and the quotient sieve; it does not simply invoke Theorem B's \(50\)-billion **field-discriminant** theorem. The source makes that dependency visible through `QuotientFiberClassification` and `QuadraticChartEquivalence`. Both proofs share determinant/prime-mass machinery, but have distinct cutoff assemblies.

The sieve has an explicit universal coverage argument in the source, not merely a list of survivors. I independently reconstructed the 200 serialized quotient masks and checked 92,964 deterministic affine-root comparisons in Python. This measures the correctness of the mask literals and sampled affine translation; it does not prove complete range coverage. Completeness still rests on the inspected Lean lemmas and the all-fibers Boolean certificate, which were not compiled in this audit.

The project contains an explicit axiom-audit command and a source-coverage checker. Their design is auditable, but the audit was not executed to completion. The statement “only `propext`, `Classical.choice`, and `Quot.sound`” must therefore be treated as unverified, not confirmed.

## Originality and readiness

The Green derivative-Gram / small inert-prime / two-sided determinant-divisibility architecture is not shown to be mathematically independent of the earlier elementary route. More strongly, Murphy's frozen `ELEM/Main.lean` source directly formalizes the elementary twinheterodox companion's eight-step proof, including a generic degree-two field statement and the same Green divisibility/finite-sieve route. The present work appears to replace that route's auxiliary-prime/rectangular-radius construction with a guarded all-small-prime bridge and ellipse/trace-Gram estimates, and it targets a much larger bound; those may be technical contributions, but the reviewed evidence does not establish a new underlying obstruction. Murphy's 7/8 zero-free-region/Chowla–Selberg route is genuinely different in its principal analytic dependency. Olivier's artifact could not be located, so no conclusion about that comparison is warranted.

The current evidence does not justify a novelty claim or publication-ready proof certification. A decisive next audit should (i) build the exact frozen tree with the pinned cache or a complete source build, (ii) run the compiled project-wide axiom audit, and (iii) independently reproduce the Gram valuation and the normalized inequalities leading to the \(5\times10^{10}\) cutoff.

## Final challenge

**Q1.** **Yes, semantically.** The field chart is \(\mathbb Q(\sqrt{-d})\), \(d\) is positive and squarefree, and the actual fundamental discriminant map gives exactly the classical list. This conclusion is supported by source inspection and the standard discriminant derivation, not a completed project build.

**Q2.** **Not established by this audit.** The relevant implications and guards were source-traced and no counterexample was found, but the complete analytic/Gram chain was not independently reconstructed or replayed. The cutoff margin is especially sensitive.

**Q3.** **Strong structural evidence, not a completed verification.** The code has universal wheel and quotient coverage lemmas and an explicit all-fibers certificate; the separate Python check confirms every serialized mask and sampled translations. The Lean certificate itself was not replayed.

**Q4.** **A formalization and quantitative integration are visible; a new mathematical obstruction is not.** The principal determinant/inert-prime architecture closely matches the earlier elementary route. The exact extent of independent novelty cannot be assessed without Olivier's artifact and a more complete prior-source comparison.

**Q5.** The most damaging plausible defect would be a false exponent \(2F(p)\) divisibility claim for the **actual integer trace-Gram** under the stated local nonsquareness hypotheses. That would invalidate the prime-mass lower bound and therefore the large-discriminant contradiction. No such defect was confirmed.

### Bias check

The three conclusions most exposed to recognition or prior-design bias are: (1) the positive semantic verdict for the two theorem statements, (2) the view that the guarded inert-prime bridge is sound, and (3) the view that the sieve coverage is exhaustive. The first is downgraded to source-audited semantics, not an end-to-end checked theorem; the second is downgraded to an open proof-replay concern despite the boundary controls; the third is explicitly limited to structural inspection plus measured mask checks, not a verified certificate. I cannot independently establish whether prior participation occurred; this downgrade is based on the evidence available in this session rather than assumed familiarity.

> **The strongest claim I am willing to defend, on the evidence actually examined, is: the frozen Lean statements have the intended classical semantics, and the quotient-mask data agree with an independent Python reconstruction in 92,964 tested affine cases.**
>
> **The strongest claim I am not yet willing to defend is: the frozen proof establishes the universal 50-billion bound with only the three advertised axioms.**
>
> **The next decisive falsification attempt should be: complete the pinned build and axiom audit, then independently verify the concrete two-sided Gram factorization and the cutoff's small positive separation.**
