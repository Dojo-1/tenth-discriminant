# Gemini Argon peer-review assessment and corrections

**Date:** 9 November 2026  
**Source:** user-supplied `Texto pegado(20261109-162858).txt` (312 lines)  
**Purpose:** preserve useful independent arithmetic criticism while correcting the review's snapshot drift and its own calculation errors. This is an AI-to-AI review assessment, not independent human mathematical validation.

## 1. Scope and epistemic tier

Argon's report explicitly inspected a frozen repository snapshot whose latest observed root commit was `4b2492f` and whose inventory reported 410 commits. It explicitly did **not** clone and re-run `lake build`, `audit.py`, or `negative_controls.py`; it also listed uninspected upstream dependency modules. Its findings should therefore be read as:
- direct source facts about the files and commit it inspected;
- independent derivations of selected formulas in those files;
- explicitly uninspected dependency closure and historical version metadata.

It is not an audit of the 9 November 2026 mainline or of Phase209 PR #157.

## 2. Current repository state (checked separately)

The live mainline at this refresh is `98d5b684`, following the Phase203 merge. The current [README](../../README.md) and [RESEARCH_NOW](../../RESEARCH_NOW.md) identify the integrated actual-field theorem:
```math
|\operatorname{disc}(K)| < 322^4 = 10,750,371,856.
```
The theorem is `Threshold322.totallyComplex_degree_two_classNumber_one_discriminant_bound_322` in [ActualField322.lean](../../lean/TenthDiscriminant/ActualField322.lean), integrated by [PR #126](https://github.com/Dojo-1/tenth-discriminant/pull/126) at [f41ce45b](https://github.com/Dojo-1/tenth-discriminant/commit/f41ce45b9dd7d722faa682d3f1dc1c204fb571da). Its 21 associated exact-head workflows passed. The independent human semantic reconstruction remains open in [Issue #50](https://github.com/Dojo-1/tenth-discriminant/issues/50).

Thus Argon's statements that the current README headlines below 50 billion and that 47b / 41.00625b are current are false for current main. Its broader warning about version drift is nevertheless valid: `STATUS.md`, `TAO_OBJECTIVES_CURRENT.md`, and `TAO_REPLY_BRIEF.md` contained stale current-status panels. This documentation branch updates those panels while preserving dated historical entries. `TAO_OBJECTIVE_AUDIT.md` and `TAO_OBJECTIVES_HISTORY.md` remain historical records.

## 3. Mathematical corrections to Argon's derivations

### 3.1 Binomial source basis: identity right, triangular orientation reversed

The binomial identity is correct, for a commutative coefficient ring and (pk\le r):
[
X^{r-pk}w^s(X^p-w)^k
=\sum_{t=0}^{k}(-1)^t\binom{k}{t}X^{r-pt}w^{s+t}.
]

The orientation stated in Argon §2A is reversed. In the repository's row-major convention, row (i) has non-leading target columns (j<i). The matrix is therefore **lower triangular**, not upper triangular. This is explicitly formalized by [`rectangularBasisMatrix_lowerTriangular`](../../lean/TenthDiscriminant/RectangularBasisMatrix.lean) and [`rectangularBasisMatrix_det`](../../lean/TenthDiscriminant/RectangularBasisMatrix.lean). The determinant-one conclusion is unaffected.

The same lower-triangular orientation is formalized for the later combined two-factor matrix in `Phase228CombinedBasis.lean`.

### 3.2 Ordinary derivative divisibility: include the endpoint m=p

For (f(X)=X^p-W), with W held fixed,
[
\partial_X^m f(X)=
\begin{cases}
\dfrac{p!}{(p-m)!}X^{p-m},&1\le m\le p,\\
0,&m>p.
\end{cases}
]
The coefficient is divisible by p for every (1\le m\le p), including (m=p), where it is (p!). Argon's prose only mentioned (1\le m\le p-1), leaving the endpoint unstated.

The clean factorwise Leibniz argument is: in each term of a derivative of (f^k), each of the k factors either receives zero derivatives and evaluates to (z^p-W\equiv0\pmod p) at an inert-prime observation, or receives at least one derivative and contributes a coefficient divisible by p. Hence every term retains p^k divisibility. The horizontal factor (W^{p^2}-W) is constant under the ordinary Z derivative and contributes its own p^ell value divisibility. This is the mathematical content now formalized in the combined ordinary-jet source branch; it must not be confused with replacing the two defects before differentiation.

### 3.3 Logarithm lower bound in Argon §2B: the displayed two-term fraction is wrong

For (x=37/163),
[
2\left(x+\frac{x^3}{3}\right)
=\frac{5,999,624}{12,992,241}
\approx0.4617851531541
<0.462=\frac{231}{500}.
]
So the displayed Argon fraction (3,221,372/6,972,243\approx0.46202808) is not the stated two-term series value and does not follow from that calculation.

The first adequate positive truncation adds (x^5/5):
[
2\left(x+\frac{x^3}{3}+\frac{x^5}{5}\right)
=\frac{797,436,114,022}{1,725,954,255,645}
\approx0.4620262161722.
]
Its exact excess over (231/500) is
[
\frac{4,524,791,401}{172,595,425,564,500}>0.
]
All remaining terms in the atanh series are positive. Therefore the desired (log(100/63)>231/500) bound is true, but Argon's written two-term derivation does not prove it. The repository's own rational logarithm checker supplies the required certificate.

### 3.4 Other calculations

The displayed 47-billion affine separation arithmetic is correct as written. The thin-radius coefficient calculation at (450^4) is correct under its stated source geometry hypotheses. The ideal norm-form discriminant cancellation is correct under the stated integral ideal-basis and index assumptions. These local checks do not re-audit their transitive Lean dependencies or replace the repository's exact-head CI.

## 4. Phase209 current state — outside Argon's inspected scope

Draft [PR #157](https://github.com/Dojo-1/tenth-discriminant/pull/157) has advanced well beyond the frozen Argon snapshot.

At exact head `c1d3d2c915e175618e731cd176d196e1198123db`:
- The previous Phase253 attempt at `7e95b879` genuinely failed because `combinedBasisMatrix_det` was referenced before its declaration. This was a Lean declaration-order failure, not a mathematical counterexample.
- Repair commit `c1d3d2c9` moves `combinedTraceGram_valuation_of_inert` below `combinedBasisMatrix_det`, without changing its statement or proof.
- Focused [Phase209 workflow 42657830775](https://github.com/Dojo-1/tenth-discriminant/actions/runs/42657830775) passed both `lean-scalar` and `exact-source`.
- The inspected axiom reports for `combinedBasisMatrix_original_integer_jet_compact`, `combinedBasisMatrix_original_integer_jet_dvd`, `combinedTransformedJet_scale`, `combinedTraceGram_basis_factor_of_inert`, and `combinedTraceGram_valuation_of_inert` contain only `propext`, `Classical.choice`, and `Quot.sound`; no `sorryAx`.
- Whole-root [workflow 42657830691](https://github.com/Dojo-1/tenth-discriminant/actions/runs/42657830691) completed successfully, including the known-false strengthening rejection controls. All 24 associated workflows at this exact head passed.

If whole-root CI completes successfully, the focused result proves the local same-original-Gram factorization
[
U_pG U_p^{\mathsf T}=\Delta_pK_p\Delta_p,
\qquad K_p\in M_{RS}(\mathbb Z),
\quad (\Delta_p)_{ii}=p^{k_i+\ell_i},
]
and therefore (p^{2\sum_i(k_i+\ell_i)}\mid\det G) for each odd inert p under the theorem's hypotheses. This is a per-prime source theorem, not a 321^4 actual-field theorem. The 321-domain analytic lower/upper comparison, class-number-one inertness bridge at the new floor, field return, and independent semantic reconstruction remain separate.

## 5. What to retain from Argon's review

Retain:
- the insistence on separating observed source facts, independent derivations, and uninspected closure;
- the same-positive-integer principle (G=EBE^{\mathsf T});
- the need to audit Mathlib's actual field invariants and maximal-order charts;
- the caution that CI proves the encoded proposition, not independent human understanding;
- the recommendation for one canonical current theorem table and explicit historical labels.

Correct:
- its current endpoint inventory;
- the triangular orientation;
- the omitted (m=p) derivative case;
- the two-term logarithm arithmetic;
- the scope label: this is an AI review of an older snapshot, not an independent human referee report or current-head audit.

## 6. Final epistemic disposition

Argon found useful local mathematical material and important documentation drift, but its own report contains a genuine arithmetic error and its repository snapshot predates the current integrated theorem. No fatal defect in the historical 47b / 41.00625b local derivations was established by this assessment. No claim of novelty, priority, optimality, a new classification, or a general Siegel-zero exclusion is made.

The 322^4 theorem remains the current integrated field result. Phase209's combined same-Gram divisor is a promising, focused-CI-verified draft extension; whole-root CI and the 321 source-to-field argument are not yet closed. AI-to-AI agreement is not independent human mathematical validation.
