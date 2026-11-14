# Phase210 — What are we trying to understand?

*4 November 2026 · source-grounded research note · draft, not an external zero-exclusion theorem.*

> The tenth discriminant is a test case, not our research objective in disguise.

This note corrects a drift in emphasis: repeated reductions of a class-number-one cutoff became the local optimization target, even though Tao framed the challenge as an experiment in *Math 2.0*: human understanding of methods that bear on Landau–Siegel zeros, assisted by AI. We retain the meaningful determinant work while separating what it proves, what it may imply and what it teaches. This is a method comparison, **not** a claim of competition victory or mathematical priority. Preregistered in [issue #158](https://github.com/Dojo-1/tenth-discriminant/issues/158).

> **Status update (10 November 2026).** The distinct combined-integral-frame proof in [Phase267](../../lean/TenthDiscriminant/Phase267ActualField321.lean) now compiles the actual-field $321^4$ bound. This note preserves the 4 November *Taylor-flow* method comparison as historical research context; its statements that the $321^4$ field return is still missing do **not** describe the newer combined-frame proof. The independent semantic review in [#50](https://github.com/Dojo-1/tenth-discriminant/issues/50) and cross-method review in [#51](https://github.com/Dojo-1/tenth-discriminant/issues/51) remain open.

Primary source: [Tao's challenge, 20 October 2026](https://terrytao.wordpress.com/2026/10/20/an-experimental-ai-math-challenge-using-tenth-discriminant-bounds-to-explore-arguments-ruling-out-siegel-zeroes/). Internal exact-source comparators: [Issue #51](https://github.com/Dojo-1/tenth-discriminant/issues/51), [Phase208 PR #153 (merged)](https://github.com/Dojo-1/tenth-discriminant/pull/153), [Phase209 draft #157](https://github.com/Dojo-1/tenth-discriminant/pull/157); external contributors' public statements are **not** independently rechecked here.

## Three arrows that must not be reversed

Let $H_D$ mean that the imaginary quadratic field with **fundamental** discriminant $-D$ has class number one. Let $Z_D(\sigma)$ mean that $L(s,\chi_{-D})$ has a real zero in $(\sigma,1)$. Finally, let $G_D$ denote our original full integer trace Gram on the **complete** thin ellipse with all ordinary-Z derivative rows (holding W fixed), original metric (2,2D), and unchanged polynomial rectangle.

There are three fundamentally different proof interfaces:

1. **Direct determinant classification:** $H_D\Rightarrow\text{small primes inert}\Rightarrow\text{a lower bound on }v_p(\det G_D)$, while geometry gives an Archimedean upper on that **same** determinant. Strict contradiction above a threshold excludes $H_D$. This does **not** quantify over general primitive real characters and is **not** a uniform zero-free region.
2. **Analytic exceptional-zero comparison:** $H_D\land(D\text{ sufficiently large})\Rightarrow Z_D(\sigma_D)$ under a separate effective zero-forcing argument; an independently proved zero-free region $\neg Z_D(\sigma_D)$ gives a contradiction. The zero-dependent and zero-free inputs must be named and verified; they are not contained in the source Gram proof.
3. **Method-transfer research question:** could a class-one determinant technique produce *family-uniform* analytic information (not merely exclude H_D) under assumptions available for arbitrary primitive real characters? **Open here.** A constant prime $p$ inferred inert only from $H_D$ cannot by itself establish such a theorem.

A smaller classification cutoff compares numerical efficiency **within stated assumptions**. It does not establish a stronger zero-free region or make two different determinants the same object.

## An elementary arithmetic boundary (paper proof, not a new Lean declaration)

Take squarefree $D\equiv3\pmod4$, so $-D$ is an odd fundamental discriminant and
$\mathcal O_K=\mathbb Z[\omega]$, where $\omega=(1+\sqrt{-D})/2$. Its norm satisfies

$$
N(a+b\omega)=\left(a+\frac b2\right)^2+\frac D4b^2.
$$

Suppose $H_D$ and an unramified prime $p<D/4$ splits. A prime ideal of norm $p$ must be principal, so there is an element $a+b\omega$ of norm `p`. If $b=0$, its norm is an integer square and cannot equal the prime $p$. If $b\ne0$, its norm is at least $D/4>p$. Contradiction. Hence such primes cannot split; because $p$ is unramified, they are **inert**.

This establishes exactly why small $p=3$ and $p=5$ can be legal in the class-one source theorem at sufficiently large D. It also reveals the non-transfer: without $H_D$, an odd fundamental discriminant such as $-287$ has $\chi_{-287}(3)=+1$; the prime $3$ splits. The latter is a **negative control**, not a counterexample to the conditional inertness lemma.

There is no valid arrow from $H_D\Rightarrow\text{small-prime inertness}$ to $\text{all }\chi_D\Rightarrow\text{small-prime inertness}$. Any purported zero-exclusion claim crossing this boundary must identify and prove a replacement hypothesis.

## Two distinct arithmetic gains, neither counted twice

**Phase208 finite Smith/residue mechanism.** In the frozen $D=403$, $\rho=40$, $R=100$, $S=J=4$ experiment, rank/cokernel information after the *old* Frobenius normalization gave finite $p=3,5$ index gains. Their valuations are bounded measurements [M], not a uniform production theorem.

**Phase209 high ordinary-derivative-depth mechanism.** For the integer derivation $\delta=\partial_Z+Z^{p-1}\partial_T$ on $\mathbb Z[Z,W,T]$, the Taylor-flow argument yields the paper theorem

$$
\delta^j\bigl(\mathbb Z[Z,W,T]\bigr)\subseteq p^{E_p(j)}\mathbb Z[Z,W,T],
\qquad
E_p(j)=\sum_{m\ge 2}\left\lfloor\frac{j}{p^m}\right\rfloor.
$$

It has a sharp witness from the original monic transformed row at $r=j,s=0$. This Taylor-flow argument is a distinct paper-level route; its proposed weighted-column-depth divisor is **not** what the now-checked Phase267 proof uses. The combined integral Frobenius frame and same-original-Gram divisor are Lean-checked separately in [Phase228](../../lean/TenthDiscriminant/Phase228CombinedBasis.lean) and [Phase260](../../lean/TenthDiscriminant/Phase260EnhancedOriginalGram321.lean).

**New exact separation:** $E_p(j)=0$ when $j<p^2$. The Phase208 pilot has $j=0,1,2,3$, so $E_3(j)=E_5(j)=0$ throughout. Its finite rank/Smith gains therefore **cannot be credited to** Phase209's universal ordinary-jet depth. They measure distinct algebraic information. A future theorem combining them must show disjoint grades in the same normalized matrix; adding them informally would double-count.

There is also a prime-scale obstruction: if an auxiliary rank-witness prime $q$ has $q^2>J-1$, Phase209 yields no extra column depth at that prime. An auxiliary *large* prime used for modular nonvanishing is not automatically useful as a *small* divisibility prime. See the two-prime/source-type audit [#51](https://github.com/Dojo-1/tenth-discriminant/issues/51).

## Comparing approaches without laundering their evidence

| Route | Input that makes it work | Output and meaning | Non-transfer or caution |
| --- | --- | --- | --- |
| Our full positive trace Gram | Class-one small-prime inertness, original ellipse $Q$, same integer jets and metric; lower and upper on $\det G_D$ | Actual-field cutoff $|\operatorname{disc}(K)|<321^4$ on [PR #157](https://github.com/Dojo-1/tenth-discriminant/pull/157), Lean-checked on its branch; prior $322^4$ theorem merged in [PR #126](https://github.com/Dojo-1/tenth-discriminant/pull/126). Independent semantic review open | This is not a zero-free theorem for general $L(s,\chi)$; full Gram is a weighted *sum* of squared maximal minors |
| Green/van Dijk-style selected derivative minor (public participant routes) | Auxiliary prime proving full rank for the **specific** source, then arithmetic divisibility by permitted inert primes | Participant-reported smaller classification cutoffs and useful rank arguments | Different row/column types, Q and auxiliary prime; one chosen minor does not upper-bound our whole Gram; source match #51 open |
| Chowla–Selberg + zero-free input | An effective large-class-one => real-zero-forcing step; a *separate* effective zero-free region | Conditional (on checked analytic input) discrimination of class-number-one fields; stronger relationship with exceptional zeros | The analytic zero-free theorem is a load-bearing external dependency; cannot be inferred from our determinant cutoff |
| Banks/prime-bias variants in the public challenge | Explicit estimates connecting zeros and prime splitting/bias; theorem statements and constants from original authors | Tests the zero-exclusion mechanism more directly than a fixed-small-prime classification argument | Do not import constants or claims of independent verification without source review |

## What an AI-assisted proof should leave in a human reader's hands

**The one-sentence mechanism:** Ordinary derivative order carries arithmetic information; under conjugate folding, a finite supply of cheap observation columns can force some of that arithmetic depth into every maximal minor of an *unchanged* positive Gram determinant.

For example, at `p=3`, `E_3(8)=0` and `E_3(9)=1`; at `p=5`, `E_5(24)=0` and `E_5(25)=1`. At the same time, the D403 pilot cannot exhibit either jump. This makes a sharper distinction than a color plot or another cutoff table.

A reader should be able to answer without asking an AI:
- What is the exact ordinary derivative being computed, and which factor is held constant?
- Why is a *conjugate pair* two effective columns rather than four?
- Which hypothesis makes a small p inert, and why does that fail for a general character?
- Why does one nonzero complex minor not bound the whole Gram from above?
- What would the paper proof still need to become a verified theorem of the original field?

We should record provenance for each answer as user intuition / AI conjecture / mathematical derivation / exact computation / formalized theorem / independent reviewer. A generated readable note does **not** itself certify that the human collaborator understands the mathematics. This line closes only with honest reconstruction or critique by humans.

## Finishing, not endlessly extending

- **A / determinant** — The combined-frame route through Phase267 has passed focused and full-root Lean CI at the cited proof-changing head, including the $321^4$ field return. Keep Phase209 #157 under review until independent semantic reconstruction #50 is completed; the distinct Taylor-flow/weighted-column conjectures are not prerequisites for this formal result. If an independently checked source mismatch appears, record the counterexample and narrow the claim.
- **B / zero-exclusion comparison** — Publish the explicit hypotheses, input/output types and one positive and one negative control above; seek a *new general-character mechanism* only after specifying a zero-dependent analytic hypothesis. Do not rename a classification inequality “a zero-free region.”
- **C / understanding** — Keep README and RESEARCH_NOW synchronized with the **merged** mainline theorem, while labeling the $321^4$ branch result separately until merge; publish a five-minute human reconstruction and invite a mathematical reader to falsify the weakest seam. Do not close #50 or #51 on AI agreement.

**Finite stop rule:** no fresh 320^4 optimization or speculative geometric lift before the current source-to-field bridge is either proved or cleanly retired. A failed extension with a localized obstruction is a legitimate finished research result.

## Evidence register

[P formal, relative to definitions] Merged $322^4$ actual-field statement in PR #126 and branch-verified $321^4$ actual-field statement in PR #157; both remain subject to independent mathematical review.

[P paper, not separately Lean-checked here] Small-split-prime obstruction under h=1, vanishing E_p(j) below p^2, conditional weighted-minor Cauchy–Binet reasoning.

[M] Phase208 finite ranks/Smith and Phase209 exact test oracles, each on its frozen source and commit.

[H] The distinct Taylor-flow weighted-column-depth transport; any truly general Dirichlet-$L$ zero-exclusion upgrade. The combined-frame $321^4$ field theorem is no longer an H claim within its encoded Lean scope.

[R] Treating a fixed-small-prime, class-one determinant argument as an all-character zero-free region; re-attributing Phase208's J=4 extra Smith index to Phase209's p^2 ordinary-jet depth; treating selected-minor and whole-Gram bounds as freely interchangeable.

Source owner and AI contributions are recorded via commits and PR discussion, not by silently replacing one another.
