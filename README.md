The Tenth Discriminant
A determinant argument, an explicit bound, and an open invitation to try to break both.

An experimental, AI-assisted number-theory investigation responding to Terence Tao's October 2026 tenth-discriminant challenge.

The question is deliberately narrow: can a variant of Ben Green's Gram-determinant argument yield a fully explicit, independently checkable bound excluding a hypothetical tenth class-number-one imaginary quadratic discriminant?

The broader ambition is methodological: turn an attractive mathematical argument into a chain of claims that another mathematician—or another model—can reconstruct, compute, falsify, and audit.

Latest continuation: **Ender** replaces Dusart with factorials and Legendre's identity; **Formic** adds adversarial arithmetic,
geometry, mutation and coverage checks. See [the derivation and reproduction commands](ledger/ender.txt) and
[the BEAN audit limitations](review/BEAN_AUDIT.txt). The computational campaign is complete; formalization and human review are not.
The route descriptions and review history below predate this continuation.

Research status (21 Oct 2026, evening) — candidate proof, reviewed, not a new result.
- Prior art: the core route (h=1 split-prime lattice count + Green's derivative Gram determinant) was posted first by
  *twinheterodox* in the comments of Tao's challenge post (v4: q < 4000; v5: q < 2000). Ours is an independent
  rediscovery; see [PRIOR_ART.md](PRIOR_ART.md).
- Our variant (norm-ellipse evaluation set) gives h(−D) ≠ 1 for all D ≥ 1.5·10⁴: 43 Arb interval certificates on
  [1.5·10⁴, 10¹⁰²] (`ledger/coverage_v4.txt`) + a monotone asymptotic inequality beyond. Below: finite check.
- Independent review (GPT-6.1 Sol, [review/](review/)): re-derived N1–N8; found defects F1–F4 in the code (incl. a false
  auxiliary tail bound, labelled FATAL); all fixed and recertified ([review/RESPONSE_Claude.md](review/RESPONSE_Claude.md)).
- External input: Dusart 2010 (arXiv:1002.0442, Thm 5.2), θ(x) ≥ x(1 − 0.2/ln²x), x ≥ 3 594 641 — primary checked.
- Not yet independently reviewed: the tighter split-prime partial summation (cover.split_mass) and the Dusart switch.

Why a tenth discriminant?
There are exactly nine positive squarefree integers $d$ for which the imaginary quadratic field $\mathbb{Q}(\sqrt{-d})$ has class number one:
\[
\boxed{1,\ 2,\ 3,\ 7,\ 11,\ 19,\ 43,\ 67,\ 163.}
\]
This is a classical theorem, established through the work of Heegner, Baker, and Stark. Long before its resolution, the tenth discriminant was the hypothetical missing case. The modern challenge is not to rediscover the list by quoting its proof, but to ask how far different arguments can be made effective: with explicit constants, finite checks, and no hidden appeal to the desired classification.

For the candidate range considered here, one studies a fundamental discriminant $-D$, with $D>163$ prime and $D\equiv3\pmod 8$, under the contradiction hypothesis
\[
h(-D)=1.
\]
The aim is to derive an explicit contradiction from independently justified estimates. An estimate that works for selected $D$, or a program that prints a positive margin, is not yet such a contradiction for all remaining $D$.
The proposed route
The experiment brings together four ingredients:
1. Geometry of the sampling set. Adapt Green's Gram-determinant construction from a rectangular lattice grid to the norm-elliptic set
   \[
   \mathcal E_{D,\rho}=\{(x,y)\in\mathbb Z^2:x^2+Dy^2\leq\rho^2\}.
   \]
   This change of geometry is substantive: any use of the original grid's interpolation or nonvanishing argument needs its own justification on the ellipse.
2. Arithmetic lower bounds. Use divisibility information at inert primes, while exploiting the restrictions that the class-number-one hypothesis would impose on split primes. The principal binary quadratic form is
   \[
   Q_D(x,y)=x^2+xy+\frac{D+1}{4}y^2.
   \]
   The exact representation counts, exceptional cases, and all constants in a split-prime estimate matter.
3. Analytic upper bounds. Apply a determinant upper bound of Hadamard type and explicit estimates for the Chebyshev function $\vartheta(x)$. The resulting inequalities must be stated with their true domains, integer floors, endpoint choices, and error terms intact.
4. Effective closure. Attempt to connect finite computations, interval certificates, and an all-larger-$D$ argument without leaving a gap between regimes. Every interval must be covered, every monotonicity assertion justified, and every use of floating-point arithmetic given an appropriate error guarantee.
The envisioned chain is:
class-number-one hypothesis
          │
          ├── geometric / interpolation obligations
          ├── inert-prime divisibility + split-prime bounds
          └── explicit determinant / prime-mass estimates
                         │
                 quantitative inequality
                         │
            exact checks + interval coverage
                         │
              independently audited bound
That last box is a target, not a status claim. See the [proof ledger](LEDGER.md) for the actual argument and its dependencies.
What is established, and what is not?
Layer	What the repository provides	What it does not automatically establish
Mathematical framework	A proposed determinant-based route and its intermediate claims	That each adaptation of a published lemma is valid
Computation	Scripts, exact-arithmetic checks, and numerical/interval experiments	A universal theorem outside the checked domains
Coverage	Recorded attempts to join finite and asymptotic regimes	Gap-free coverage without validated endpoints and monotonicity
Independent criticism	A blind-then-audit review process, concrete objections, and counterexample work	Endorsement of the main conclusion


Review obstacle (21 October 2026), resolved: an adversarial reviewer reproduced a false auxiliary prime-mass lower bound (F1). It was a code defect (tail added over an empty range); the guarded version passes the reviewer's counterexample and all certificates were recomputed. See [review/RESPONSE_Claude.md](review/RESPONSE_Claude.md).

The rule throughout is simple: a computed inequality is evidence about that computation; a proof requires the quantified mathematical bridge.
Navigate the evidence
Start here	Purpose
[STATUS.md](STATUS.md)	Current result, blockers, and next proof obligations
[LEDGER.md](LEDGER.md)	The argument broken into auditable claims and dependencies
[`ledger/`](ledger/)	Recorded calculations and coverage artifacts
[REVIEW_BRIEF.md](REVIEW_BRIEF.md)	Instructions for an adversarial, blind-first mathematical review
[`review/`](review/)	Review reports, counterexamples, and stated validation limits
[`tools/`](tools/)	Exact checks, candidate inequalities, interval and asymptotic experiments
[ENVIRONMENT.md](ENVIRONMENT.md)	Reproduction environment and external arithmetic dependencies
[`lit/`](lit/)	Literature and source-provenance support


For a first reading, use STATUS.md → LEDGER.md → review/. For a genuinely blind review, instead begin with [`REVIEW_BRIEF.md`](REVIEW_BRIEF.md) and follow its phase ordering before reading the proposed proof or code.
Reproduce, then challenge
Follow [ENVIRONMENT.md](ENVIRONMENT.md) for the supported environment and tool versions. Selected verification entry points include:
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt

python tools/verify_exact.py
python tools/mutation_test.py
python tools/asymptotic.py

# Requires PARI/GP in addition to the Python environment:
gp -q tools/verify_exact_large.gp
The larger arithmetic workflow may require PARI/GP and python-flint; consult the environment notes rather than assuming that pip install alone is sufficient. The scripts above are entry points, not a single command certifying the theorem. See the ledger and review reports for the tested parameters, outputs, and limits.

Useful ways to contribute a substantive check:
- Re-derive before comparing. Start from the source lemmas and the stated class-number-one hypothesis, without reading the proposed estimates first.
- Attack the boundaries. Probe negative coordinates, irregular point sets, small prime exceptions, floors, interval endpoints, and the transition to the asymptotic regime.
- Separate arithmetic from its certificate. Report whether a result was checked exactly, enclosed by rigorous intervals, approximated numerically, or inferred heuristically.
- Give a failing instance. An explicit counterexample, its input, and a command that reproduces it are more valuable than an unqualified verdict.
The repository's review protocol deliberately distinguishes blind derivation from informed audit. An AI-generated argument reviewed by another AI is not automatically independent evidence; models may share assumptions or failure modes. Record the model, tools, prompts/protocol, sources, and commands when those details affect reproducibility.
Intellectual provenance
This is an independent response to a mathematical challenge, not an official submission or endorsement by its organizers or by the authors of the source results.
- Terence Tao, An experimental AI-math challenge: using tenth discriminant bounds to explore arguments ruling out Siegel zeroes, 20 October 2026 — motivation and challenge design.
- Ben Green, On Landau–Siegel zeros — the determinant approach being investigated; the proposed ellipsoidal adaptation is not claimed to be Green's result.
- Primary references, downloads, and integrity material: see [`lit/`](lit/) and the citations inside [LEDGER.md](LEDGER.md).
The intended output is not a dramatic theorem announcement. It is an argument whose every joint can be inspected—and whose failures can be found before its conclusions are believed.
