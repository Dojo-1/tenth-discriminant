
Your goal is to @Rizz  the Readme.md of the repo, only thathttps://github.com/Dojo-1/tenth-discriminant

I inspected Dojo-1/tenth-discriminant through your open GitHub tab.

Two findings:

There is no README.md on main yet. GitHub displays “Add a README.”

The repository is internal, and the connected GitHub integration does not currently have access to it.

I can see the project's purpose—investigating tenth-discriminant bounds in arguments concerning Siegel zeroes—and its existing research structure (LEDGER.md, STATUS.md, REVIEW_BRIEF.md, and related files).

To do this properly, enable access to Dojo-1/tenth-discriminant for the GitHub connector. Then I can create a research-grade README with a compelling introduction, clear mathematical motivation, reproducibility guidance, and rigorously separated established results, computational evidence, and open proof obligations.

Scope remains exactly one file: README.md. No source code, proofs, experiments, or other documentation will be modified.

ok proceed
Created the polished README for The Tenth Discriminant.

README.md

GitHub-ready Markdown · 1,235 words
It includes a stronger opening, mathematical motivation, research architecture, reproducibility instructions, and an explicit distinction between established results, experimental evidence, and unresolved proof obligations.

GitHub status: Not committed. The connected GitHub integration still returns 404 for the internal repository, so I couldn't publish the file directly.

No repository files were changed. Once the integration has access, only README.md needs to be added.




The Tenth Discriminant
A determinant argument, an explicit bound, and an open invitation to try to break both.

An experimental, AI-assisted number-theory investigation responding to Terence Tao's October 2026 tenth-discriminant challenge.

The question is deliberately narrow: can a variant of Ben Green's Gram-determinant argument yield a fully explicit, independently checkable bound excluding a hypothetical tenth class-number-one imaginary quadratic discriminant?

The broader ambition is methodological: turn an attractive mathematical argument into a chain of claims that another mathematician—or another model—can reconstruct, compute, falsify, and audit.

Research status — not a completed proof. The class-number-one problem is already solved. This repository explores an alternative route, not a new classification result. The adversarial review recorded in review/ reports a reproducible defect in an auxiliary prime-mass lower bound. Numerical runs, interval outputs, and a plausible asymptotic argument must not be read as a certified exclusion until the relevant proof obligations are repaired and independently checked. Start with STATUS.md and the review record.

Why a tenth discriminant?
There are exactly nine positive squarefree integers $d$ for which the imaginary quadratic field $\mathbb{Q}(\sqrt{-d})$ has class number one:

1
,
 
2
,
 
3
,
 
7
,
 
11
,
 
19
,
 
43
,
 
67
,
 
163.
1, 2, 3, 7, 11, 19, 43, 67, 163.
​
 
This is a classical theorem, established through the work of Heegner, Baker, and Stark. Long before its resolution, the tenth discriminant was the hypothetical missing case. The modern challenge is not to rediscover the list by quoting its proof, but to ask how far different arguments can be made effective: with explicit constants, finite checks, and no hidden appeal to the desired classification.

For the candidate range considered here, one studies a fundamental discriminant $-D$, with $D>163$ prime and $D\equiv3\pmod 8$, under the contradiction hypothesis

h
(
−
D
)
=
1.
h(−D)=1.
The aim is to derive an explicit contradiction from independently justified estimates. An estimate that works for selected $D$, or a program that prints a positive margin, is not yet such a contradiction for all remaining $D$.

The proposed route
The experiment brings together four ingredients:

Geometry of the sampling set. Adapt Green's Gram-determinant construction from a rectangular lattice grid to the norm-elliptic set

E
D
,
ρ
=
{
(
x
,
y
)
∈
Z
2
:
x
2
+
D
y
2
≤
ρ
2
}
.
E 
D,ρ
​
 ={(x,y)∈Z 
2
 :x 
2
 +Dy 
2
 ≤ρ 
2
 }.
This change of geometry is substantive: any use of the original grid's interpolation or nonvanishing argument needs its own justification on the ellipse.

Arithmetic lower bounds. Use divisibility information at inert primes, while exploiting the restrictions that the class-number-one hypothesis would impose on split primes. The principal binary quadratic form is

Q
D
(
x
,
y
)
=
x
2
+
x
y
+
D
+
1
4
y
2
.
Q 
D
​
 (x,y)=x 
2
 +xy+ 
4
D+1
​
 y 
2
 .
The exact representation counts, exceptional cases, and all constants in a split-prime estimate matter.

Analytic upper bounds. Apply a determinant upper bound of Hadamard type and explicit estimates for the Chebyshev function $\vartheta(x)$. The resulting inequalities must be stated with their true domains, integer floors, endpoint choices, and error terms intact.

Effective closure. Attempt to connect finite computations, interval certificates, and an all-larger-$D$ argument without leaving a gap between regimes. Every interval must be covered, every monotonicity assertion justified, and every use of floating-point arithmetic given an appropriate error guarantee.

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
That last box is a target, not a status claim. See the proof ledger for the actual argument and its dependencies.

What is established, and what is not?
Layer	What the repository provides	What it does not automatically establish
Mathematical framework	A proposed determinant-based route and its intermediate claims	That each adaptation of a published lemma is valid
Computation	Scripts, exact-arithmetic checks, and numerical/interval experiments	A universal theorem outside the checked domains
Coverage	Recorded attempts to join finite and asymptotic regimes	Gap-free coverage without validated endpoints and monotonicity
Independent criticism	A blind-then-audit review process, concrete objections, and counterexample work	Endorsement of the main conclusion
Known review obstacle (21 October 2026): an adversarial reviewer reproduced a false auxiliary prime-mass lower bound. This is a defect in the proposed proof route; it does not contradict the already-known class-number-one theorem. The current state of any attempted repair must be read from STATUS.md, LEDGER.md, and `review/`, rather than inferred from this introduction.

The rule throughout is simple: a computed inequality is evidence about that computation; a proof requires the quantified mathematical bridge.

Navigate the evidence
Start here	Purpose
STATUS.md
Current result, blockers, and next proof obligations
LEDGER.md
The argument broken into auditable claims and dependencies
`ledger/`
Recorded calculations and coverage artifacts
REVIEW_BRIEF.md
Instructions for an adversarial, blind-first mathematical review
`review/`
Review reports, counterexamples, and stated validation limits
`tools/`
Exact checks, candidate inequalities, interval and asymptotic experiments
ENVIRONMENT.md
Reproduction environment and external arithmetic dependencies
`lit/`
Literature and source-provenance support
For a first reading, use STATUS.md → LEDGER.md → review/. For a genuinely blind review, instead begin with `REVIEW_BRIEF.md` and follow its phase ordering before reading the proposed proof or code.

Reproduce, then challenge
Follow ENVIRONMENT.md for the supported environment and tool versions. Selected verification entry points include:

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

Re-derive before comparing. Start from the source lemmas and the stated class-number-one hypothesis, without reading the proposed estimates first.
Attack the boundaries. Probe negative coordinates, irregular point sets, small prime exceptions, floors, interval endpoints, and the transition to the asymptotic regime.
Separate arithmetic from its certificate. Report whether a result was checked exactly, enclosed by rigorous intervals, approximated numerically, or inferred heuristically.
Give a failing instance. An explicit counterexample, its input, and a command that reproduces it are more valuable than an unqualified verdict.
The repository's review protocol deliberately distinguishes blind derivation from informed audit. An AI-generated argument reviewed by another AI is not automatically independent evidence; models may share assumptions or failure modes. Record the model, tools, prompts/protocol, sources, and commands when those details affect reproducibility.

Intellectual provenance
This is an independent response to a mathematical challenge, not an official submission or endorsement by its organizers or by the authors of the source results.

Terence Tao, An experimental AI-math challenge: using tenth discriminant bounds to explore arguments ruling out Siegel zeroes, 20 October 2026 — motivation and challenge design.
Ben Green, On Landau–Siegel zeros — the determinant approach being investigated; the proposed ellipsoidal adaptation is not claimed to be Green's result.
Primary references, downloads, and integrity material: see `lit/` and the citations inside LEDGER.md.
The intended output is not a dramatic theorem announcement. It is an argument whose every joint can be inspected—and whose failures can be found before its conclusions are believed.

