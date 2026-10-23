# The Tenth Discriminant

**A determinant argument you can reconstruct, run, and try to break.**

An AI-assisted investigation of [Terence Tao's tenth-discriminant challenge](https://terrytao.wordpress.com/2026/10/20/an-experimental-ai-math-challenge-using-tenth-discriminant-bounds-to-explore-arguments-ruling-out-siegel-zeroes/comment-page-1/): make an effective class-number-one argument explicit, without importing the known classification as a proof input.

[Current argument](ledger/ender.txt) · [Latest experiments](#beyond-hadamard-two-bounded-results) · [Tao-objective audit](TAO_OBJECTIVE_AUDIT.md) · [Reproduction](#reproduce-the-record) · [Review history](review/) · [Prior art](PRIOR_ART.md)

> **Status · 22 October 2026:** candidate mathematical argument, with recorded interval certificates, finite computations, and AI review. No end-to-end Lean formalization or human mathematical review is recorded. The latest determinant experiments do **not** change the discriminant cutoff. No novelty or priority claim is made.
>
> This overview reflects the artifacts at [`062afd2`](https://github.com/Dojo-1/tenth-discriminant/tree/062afd2a6170a7569d1801c3938f05e63030949d). Numerical summaries below describe those recorded runs; they are not substitutes for the derivations or their dependencies.
>
> **23 October evidence update:** the later frozen checkout at
> [`4c034f9`](https://github.com/Dojo-1/tenth-discriminant/tree/4c034f9d2bd6c66aa3a7558d8a70a842be77ad29)
> contains merged PRs #15 and #16: a checked abstract interpolation/Gram
> component and clearer documentation. It does **not** change the candidate
> status of the end-to-end class-number argument. The [objective audit](TAO_OBJECTIVE_AUDIT.md)
> distinguishes these two evidence classes and records a bounded preregistered
> control replay.

## What bound are we claiming?

Write **$D=|\mathrm{disc}(K)|$** for the absolute fundamental discriminant of an imaginary quadratic field. It is not an unrestricted radicand. In the notation $q=|\mathrm{disc}(K)|$ used by [twinheterodox's contribution](https://github.com/twinheterodox/tenth-discriminant), **$q=D$**, not $\log D$.

The current factorial-based route, **Ender**, claims an **analytic exclusion threshold of $D\geq 7\times10^{11}$**. Combining that argument with the recorded finite endgame is intended to establish

$$
h(-D)=1\quad\Longrightarrow\quad
D\in\{3,4,7,8,11,19,43,67,163\}.
$$

Thus **$D\leq163$ is the candidate endpoint after the finite check**, not the determinant's analytic cutoff and not a newly certified theorem announced by this README.

### The coverage chain

| Range | Recorded component | Evidence |
|---|---|---|
| Fundamental $D<92$ | Primitive reduced-form enumeration returns $3,4,7,8,11,19,43,67$ as the one-form cases. | [Formic output](ledger/formic.txt), [derivation §5](ledger/ender.txt) |
| $92\leq D<7\times10^{11}$ | A full CRT residue-sieve run leaves **163 only**. Its base filters are not asserted valid below 92. | [Sieve output](ledger/sieve_ender.txt), [implementation](tools/sieve_crt.py) |
| $7\times10^{11}\leq D\leq10^{36}$ | **250 contiguous Arb-certified intervals**, with exact integer endpoints; smallest printed lower/upper ratio approximately **1.027747792**. | [Interval record](ledger/coverage_ender.txt), [implementation](tools/ender.py) |
| $D\geq10^{36}$ | Written floor-safe, all-$D$ envelope, with normalized margin slope **$15/64$** in $\log D$ and certified starting margin approximately **7.84016012450**. | [Derivation §4](ledger/ender.txt), [endpoint checks](ledger/asymptotic_ender.txt) |

The inequalities certify their stated numerical bounds. The class-number conclusion additionally depends on the quadratic arithmetic, determinant divisibility, nonvanishing, ellipse estimates, and reduced-form correspondence spelled out in the argument. The all-$D$ step needs its written monotonicity proof, not just a positive endpoint printout.

## The argument, without the codenames

**Arithmetic.** Under the contradiction hypothesis $h(-D)=1$, a hypothetical $D>163$ is prime, $D\equiv3\pmod8$, and every prime $p<(D+1)/4$ is inert. Ender chooses $R$ strictly inside that threshold; the boundary is not rounded into an inclusive inertness claim.

**Geometry.** Evaluate Green's derivative Gram construction on the norm ellipse

$$
\mathcal E_{D,\rho}=\{x+y\sqrt{-D}:x,y\in\mathbb Z,\ x^2+Dy^2\leq\rho^2\}.
$$

The point counts and interpolation conditions must establish nonvanishing for this actual set. Inert-prime divisibility supplies a lower bound for $\log\det G$; Hadamard supplies an upper bound. A strict lower-over-upper contradiction excludes the candidate discriminant.

**Prime input.** Ender obtains the required prime-weight bound from factorials and Legendre's identity, subtracting small-prime powers exactly and bounding the remaining tail by an explicit integral. It removes Dusart and other prime-distribution estimates from this route. Green's determinant lemmas and the geometric and quadratic-arithmetic dependencies remain.

**Trade-off.** This is a reduction in analytic inputs, **not a better numerical cutoff** than the earlier split-prime-counting route. The older $1.5\times10^4$ threshold and its Dusart-dependent calculations remain historical artifacts; they should not be mixed into Ender's dependency chain. Start with [the current derivation](ledger/ender.txt), not the historical [constant ledger](LEDGER.md).

## Beyond Hadamard: two bounded results

### 1. Exact determinant structure and prime-power layers

The [108-case experiment](ledger/determinant_lifts.txt) varies matrix size, derivative order, and sampling geometry. It records **101 nonsingular cases and 7 singular cases**. A disjoint-block Fischer bound is strictly sharper than ordinary Hadamard in all 101 nonsingular cases. Only 23 cases satisfy the chosen sufficient interpolation guard; exact rank, not that guard alone, identifies the other nonsingular cases.

Smith layers describe contributions to **one** prime-adic valuation, not independent gains to be added twice. A guarded, genuine class-number-one example at $D=19$ has

$$
v_3(\det G)=2F(3)=2,
$$

which refutes a universal replacement of Green's bound by $2F(p)+2$. It does not exclude improvements under additional hypotheses. These are finite observations, not an all-dimensional determinant improvement. [Raw cases](ledger/determinant_lifts.jsonl) · [Fixed protocol](flow/PREREG_LIFTS.txt).

### 2. Analytic radial correlations

The [radial follow-up](ledger/radial_bounds.txt) derives moment formulas and an annulus correlation bound. For a positive definite Gram matrix, an annulus $b/2\leq |z|^2\leq b$ with $b>0$, and $m$ disjoint available row pairs $(r,s),(r+1,s+1)$ satisfying $r\geq2(J-1)$, it gives

$$
\det G\leq\text{moment-block product}
\leq\left(\prod_i G_{ii}\right)(9/25)^m.
$$

The fixed 18-case campaign records **16 certified cases**: 8 with strict saving and 8 with no eligible pairs. The other 2 fail the sufficient independence guard; that is not a proof of singularity.

**The limitation is part of the result.** This uniform guarantee contributes at most $\log(25/9)/(2R)$ after normalization by $R^2S$, so it does not improve Ender's leading slope. That ceiling concerns the guarantee, not every possible actual saving. The annulus changes the witness, and all 18 cases lie outside the strict inertness cutoff, so the campaign uses only actually inert primes. No improved discriminant cutoff follows. [Raw cases](ledger/radial_bounds.jsonl) · [Fixed protocol](flow/PREREG_RADIAL.txt).

## What the checking does — and does not — establish

**Formic** is the local verification suite. Its [recorded run](ledger/formic.txt) includes 2,984 arithmetic comparisons, 320 integer-radius ellipse checks, all 250 replayed intervals, small reduced-form enumeration, arithmetic and cutoff mutations, and three comparisons of the asymptotic envelopes with raw normalized bounds.

The limitations remain visible:

- **Finite controls have finite scope.** Direct prime-sum comparisons extend only through $R=80001$. The inherited genuine-field calculator has vacuous lower bounds, so its lack of contradictions is a weak control. The older mutation suite catches M1 and M3 but **does not catch M2**, an overstrong Hadamard bound.
- **AI review is not an independent end-to-end certificate.** The [Ender audit record](review/ENDER_AUDIT.txt) is a parent summary of agent findings. It reports rederivation of the factorial and universal-envelope steps, not formal verification of the inherited determinant lemmas. Shared code and assumptions must not be counted as independent witnesses.
- **Corrections are preserved.** The earlier false auxiliary prime-mass bound and its repair remain in the [review response](review/RESPONSE_Claude.md). The [BEAN audit](review/BEAN_AUDIT.txt) records the strict-endpoint issue, incomplete old all-$D$ justification, and saved-sieve range mismatch. Ender's replacement argument does not retroactively validate the old asymptotic script.

The next mathematical obligation is an end-to-end review of the stated dependencies and their application to the actual sampling set. For the experimental branch, a finite block improvement must be connected to a valid large-$D$ family before it can strengthen the global bound.

## Reproduce the record

Run from the repository root. The recorded environment uses **python-flint 0.9.0**, **SymPy 1.14.0**, and **160-bit Arb** for Ender/Formic and the two new campaigns. [Environment notes](ENVIRONMENT.md) include earlier tools; they are not themselves a proof certificate.

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt "sympy==1.14.0"

# Focused controls for the latest experiments.
python tools/test_determinant_lifts.py
python tools/test_radial_bounds.py

# Current analytic route and local verification.
python tools/ender.py cover 7e11 1e36
python tools/ender.py asymptotic
python tools/formic.py

# Full finite sieve: separate from the interval replay.
python tools/sieve_crt.py 92 700000000000
```

Keep fresh outputs separate from the saved evidence:

```bash
mkdir -p /tmp/tenth-discriminant-rerun
python tools/determinant_lifts.py > /tmp/tenth-discriminant-rerun/determinant_lifts.jsonl
python tools/radial_bounds.py > /tmp/tenth-discriminant-rerun/radial_bounds.jsonl
cmp ledger/determinant_lifts.jsonl /tmp/tenth-discriminant-rerun/determinant_lifts.jsonl
cmp ledger/radial_bounds.jsonl /tmp/tenth-discriminant-rerun/radial_bounds.jsonl
```

The pre-existing exact determinant and mutation suites additionally require **PARI/GP**; the recorded version is 2.15.4:

```bash
python tools/verify_exact.py
python tools/mutation_test.py
gp -q tools/verify_exact_large.gp
```

A successful command establishes only what that program checks. Report the commit, environment, command, output, and any disagreement; do not replace a failed record with a passing one without preserving the correction.

## Provenance, AI assistance, and review

**Credit comes before comparison.** Ben Green supplies the derivative determinant method. The [prior-art record](PRIOR_ART.md) acknowledges twinheterodox's earlier split-prime/Green route and Kyle Pratt's disk-interpolation contribution; [BEAN](BEAN.md) also credits van Dijk for the route family and Jesús Vilela for the norm-ellipse experiment. This repository does not claim priority for that route or offer a current leaderboard. The dated prior-art snapshot is not an exhaustive literature review.

**The names are workflow labels.** Bean, Ender, and Formic were used in semantic priming for AI-assisted exploration and adversarial checking. They name stages of the research, not mathematical entities, independent authorities, or evidence that priming improves research quality. The claims must stand without the narrative. Review provenance and limitations belong in the [review records](review/).

For a first reading, use [the objective audit](TAO_OBJECTIVE_AUDIT.md), then [the Ender derivation](ledger/ender.txt) and its [audit record](review/ENDER_AUDIT.txt). [STATUS.md](STATUS.md) preserves the broader chronology, including the unreviewed higher-class-number track; its historical entries are not all current claims. A blind-first reviewer should instead begin with [REVIEW_BRIEF.md](REVIEW_BRIEF.md), while noting that it describes the earlier route.

Useful criticism identifies the exact statement, violated hypothesis or counterexample, consequence, and reproduction path. Unchecked, missing, and false are different findings. The same discipline applies to favorable reviews and to the [Doubt the Machine framework](https://github.com/Dojo-1/doubt-the-machine) itself.

**The aim is not an impressive verdict. It is an argument whose joints remain visible.**
