# Tao-objective audit — 23 October 2026

This is an evidence audit, not a proof of the candidate argument. It compares
the twelve-item status table used in this project with Terence Tao's
[20 October challenge](https://terrytao.wordpress.com/2026/10/20/an-experimental-ai-math-challenge-using-tenth-discriminant-bounds-to-explore-arguments-ruling-out-siegel-zeroes/)
and the frozen checkout at `4c034f9`. It does not treat a passing program,
a Lean theorem about one component, or an AI review as a completed
classification proof.

## First correction: the PR status changed

The earlier conversation described PRs #15 and #16 as drafts. In the frozen
current history they are **merged into `main`**:

| Pull request | Current merge commit | What it establishes |
|---|---|---|
| #15 | `47ec647` | The abstract factor/jet-to-trace-Gram positivity chain. |
| #16 | `4c034f9` | A smaller public interface, a broader dependency audit, and reader documentation. |

The PR #16 source head `8aca367` passed its pinned GitHub Actions workflow
`39897529309`, job `120231301146`: source correspondence, `lake build`, the
compiled dependency audit, and negative controls. That is evidence for the
encoded formal apparatus. It does not prove the unformalized arithmetic,
analytic, numerical, or class-number links below.

## Reading the statuses

* **Candidate only** means that a repository argument and recorded computations
  exist, but the connected theorem required by the objective does not.
* **Partial** means a bounded component is checked or documented, while the
  requested end-to-end result remains open.
* **Process record** concerns disclosure, attribution, or preservation of
  failures; it is not mathematical validation.

## Objective-by-objective result

| # | Objective derived from Tao's post | Evidence-aware status at `4c034f9` | Why this is the narrow status |
|---:|---|---|---|
| 1 | Effective AI-assisted tenth-discriminant bound, without Heegner methods | **Candidate only** | Ender records a $7\times10^{11}$ analytic exclusion threshold and a finite endgame, but `lean/FORMALIZATION.md` keeps the arithmetic-to-determinant, analytic, numerical, and classification links open. |
| 2 | Best-effort optimization of the constant | **Not met** | The repository explicitly trades the earlier $1.5\times10^4$ historical threshold for a factorial route at $7\times10^{11}$; reduced external analytic input is not constant optimization. |
| 3 | A low enough threshold to finish by direct computation | **Conditional candidate only** | The recorded CRT sieve leaves 163 on $[92,7\times10^{11})$, conditional on the candidate analytic chain. It is not a new certified solution of the class-number-one problem. |
| 4 | Lean formalization suitable for high-quality upstream work | **Partial** | The actual rectangular trace-Gram interpolation criterion is checked and exposed through a small API. The concrete ellipse, integer Gram correspondence, divisibility, analytic estimates, numerical inequalities, and finite classification are still open. No Mathlib-upstreamability review is recorded. |
| 5 | Compare the strength of different writeups | **Not met** | `PRIOR_ART.md` is a dated, deliberately non-exhaustive snapshot and the README rejects a current leaderboard. It is provenance, not a systematic comparison. |
| 6 | Stimulate new arguments or arrangements | **Exploratory only** | The BEAN-to-Ender replacement and the bounded determinant experiments are useful arrangements, but none supplies a connected new theorem or improved global cutoff. |
| 7 | Preserve and report negative results honestly | **Process record present** | The repository retains the false prime-mass bound, BEAN gaps, failed controls, and the radial $O(1/R)$ ceiling. This supports honest internal reporting; it does not establish that every result has been externally reported. |
| 8 | Help higher class-number problems beyond Watkins's $h\le100$ | **Not delivered** | The $h\le2$ track is preregistered and explicitly unreviewed. It neither addresses the requested range nor supports an external claim. |
| 9 | Disclose AI use | **Process record present** | The README identifies the work as AI-assisted and review records disclose reported models/tools. This says nothing about a future public comment, which has not been made. |
| 10 | Submit a repository link plus a human-generated comment summary | **Not delivered** | Tao's post asks for both. A page search on 23 October found no `Dojo-1` string; absence in this search is not proof that no related comment exists, but the repository contains no permalink or prepared posting record. |
| 11 | Independent-AI due diligence before a purely AI-generated submission | **Partial** | The blind-then-audit records and the separate Ender review are useful, but remain AI-side, share some assumptions, and are not a human or independent semantic certificate. No submission has occurred. |
| 12 | Quality, collaboration, and attribution over speed or priority | **Process record present** | Current documentation credits Green, twinheterodox, Pratt, van Dijk, and Vilela; it keeps candidate status and failure records visible. This is a documented practice, not a measured quality result. |

## Bounded preregistered replay in this audit

The audit reran the control suite mandated by
[`flow/PREREG_RADIAL.txt`](flow/PREREG_RADIAL.txt), without changing the
campaign, witness, or saved raw output:

```text
Python 3.13.16
python-flint 0.9.0
SymPy 1.14.0
.venv\\Scripts\\python.exe tools\\test_radial_bounds.py
9 tests, 0 failures, 1.525 s
```

The replay checks the registered moment identities, annulus and derivative
boundaries, disjoint pairing, no-certificate semantics, an explicit failed
strengthening, and small full-determinant comparisons. It is a reproducibility
check of a finite control suite. It neither reruns the 18-case campaign nor
changes the established limitation: its uniform saving is $O(1/R)$ and does
not improve Ender's leading slope or cutoff.

## The one sentence a reader should retain

The formal interpolation component is now a real checked theorem, and the
candidate Ender evidence is reproducible; the bridge that applies that theorem
to the specific arithmetic witness and thereby classifies discriminants is
still open.
