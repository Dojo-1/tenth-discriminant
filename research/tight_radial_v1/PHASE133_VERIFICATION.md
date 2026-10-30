# Phase133 — exact-head publication verification

**30 October 2026.** [PR #49](https://github.com/Dojo-1/tenth-discriminant/pull/49) merged using an ordinary merge commit
[`dddeae54cf09aee95add779afe8f5612f4d9fa69`](https://github.com/Dojo-1/tenth-discriminant/commit/dddeae54cf09aee95add779afe8f5612f4d9fa69),
retaining every predecessor and failed proof attempt. Accepted proof
source: [`761f4f11c31e5e53c8c40b74e56ef53173ee250d`](https://github.com/Dojo-1/tenth-discriminant/commit/761f4f11c31e5e53c8c40b74e56ef53173ee250d).

## What is kernel checked [P]

`TenthDiscriminant.TightRadialEndpoint.totallyComplex_degree_two_classNumber_one_discriminant_bound_47b`
establishes for every totally complex degree-two number field K with
class number one:

`(NumberField.discr K).natAbs < 47000000000`.

The target is the **actual field discriminant**, not the determinant of
the integer observation Gram G. `TightRadialSaving.production_normalized_upper_tight`
uses the SAME original E, B, G=EBE^T, ordinary derivative slots and
radial frame as the inherited arithmetic lower bound, preserving
all prior prime divisibility, counting and field chart guards.

For `t=R-25S`, `S>=100`, `25S<=R<=26S`, the exact identity
`676S(R-9S)-17R²=(S-t)(191S+17t)>=0` gives the uniform ratio.
The checked rational bracket `log(100/63)>=231/500` gives
normalized saving `23/2000`. A sound five-term rational bracket on
`log(47000000000)` and exact separation
`26281/1000000000>0` close the argument. The earlier
47.1-billion bound and all inherited theorems are unchanged.

## Verification receipts

- [Full-root exact-head Lean run 41098122516](https://github.com/Dojo-1/tenth-discriminant/actions/runs/41098122516): **SUCCESS**.
  `verify_sources.py`: source digest and 250 original interval pairs;
  `lake build` completed (6,864 entries);
  `audit.py`: 5,729 logical declarations and 4,914 theorem
  declarations, only permitted standard axioms in checked closures;
  `negative_controls.py`: all required true/false matched
  controls passed.
- [Focused PR 41098122564](https://github.com/Dojo-1/tenth-discriminant/actions/runs/41098122564) and
  [branch run 41098112184](https://github.com/Dojo-1/tenth-discriminant/actions/runs/41098112184):
  **SUCCESS** for the new geometric saving and actual-field endpoint.
- CodeQL and Rust/Python/Actions static analysis: **SUCCESS**
  at the same exact proof head. A nonfatal no-op `norm_num` Lean
  linter warning persists in the endpoint; it is not a gap in the
  theorem, and no statement was weakened to suppress it.
- [Initial source 534f742](https://github.com/Dojo-1/tenth-discriminant/actions/runs/41095139730)
  **FAILED** on missing proof nonnegativity side conditions. The
  [first repair 6163cd7](https://github.com/Dojo-1/tenth-discriminant/actions/runs/41096816617)
  **FAILED** on an extra tactic after the goal had already closed.
  Two proof-only corrections fixed elaboration; no constants, theorem
  types, mathematical objects or external gates were changed. Both
  failed runs and correction commits are preserved.

## Independent review and scope

This is a valid *formal proof of the encoded statement* under the
specified dependencies, not yet an independent mathematician's
semantic reconstruction of the intended number-theory argument.
[Review issue #50](https://github.com/Dojo-1/tenth-discriminant/issues/50) isolates
the four crucial obligations: original integer Gram, two-sided
prime-power extraction, positive radial upper bound and actual-field
return. The separate finite nine-field classification has its own
endgame and is not a consequence of tightening this inequality.
No optimal bound, novelty, Siegel-zero theorem or external referee
endorsement is claimed.

The Phase133 PR added just two new Lean modules, one root import append,
one focused CI workflow and two reader/protocol notes. The original
E, trace metric, source-certificate checker, negative controls and
toolchain pin were unchanged. Our canonical README and method comparison
have been updated after the merge, without rewriting the original
proof or negative results.

The next bounded mathematical question is **typed modular rank
transport**: given a *fixed* integer E and original observations,
can a separately admissible auxiliary prime witness a nonzero
maximal minor, making its real positive trace Gram positive?
If prime p already forces a nontrivial integral row factor
`U_p E=Delta_p Ehat`, then that very E cannot have full row
rank modulo p; the rank-witness prime must avoid this obstruction.
A chosen minor's upper bound also cannot automatically bound
the whole Cauchy–Binet sum. Treat this [H] as a new experiment,
not a stronger cutoff.
