# Phase 26: finish the fixed first interval's finite numerical certificates

Base: `260c6ba2b2212b63cbda1c199694770a8c5e99ac`, whose tested PR-merge tree
was verified identical to its branch tree. The preceding turn made progress:
all 1229 candidate rows, their checker soundness, guards and scalar reductions
are checked. Coverage and two total budgets are still unproved. No numerical
proof process remains live at registration.

## Fixed target and invariants

Only the same first saved interval `[700000000000,875000000000]` is in scope,
for squarefree `D≡3 (mod 4)`. Keep `R=175000000000`, `S=8750000000`,
`P=10000`, `rho=408406701`, padding `488`, eight log-series terms and scale
`10^12`. Do not change the 1229 labels, log bounds, coefficients, weights,
target budgets, production tools, saved certificates or dependency pins.
No parameter search, other interval campaign or new cutoff.

## Repair to attempt

1. First test proof-producing `norm_num` primality/filter normalization on
   at most 16 integers near the upper end, including the prime 9973.
2. Generate complete coverage proofs for consecutive integer ranges of
   length at most 16, partitioning each of the existing 39 prime-row chunks'
   integer intervals. Join these ranges with `List.range'_append_1` and
   `List.filter_append`, then join all 39 intervals. Check each chunk's row
   labels against the resulting explicit prime list. No skipped integer,
   trusted prime oracle, or assumed coverage.
3. Separately prove both exact integer sums for each 32-row chunk by
   proof-producing normalization. Compose these identities symbolically
   before checking the two already declared budgets. Avoid reducing the
   whole 1229-row arithmetic fold in one decision proof.
4. If all finite obligations pass, compose with `FirstIntervalRows` and
   `FirstIntervalConclusion` to prove the strict comparison and the actual
   quadratic-field class-number exclusion, with no numerical premise.

The generator supplies untrusted literals; only accepted Lean proofs count.
Permitted proof representations are ordinary proof-producing normalization
and pure kernel decision reduction. No native decision or added axiom.
Run the existing owned-process monitor at an 8192-MB working-set cap,
one raw-proof thread and the existing 16384-KB stack. If a complete module
hits the cap, preserve it and partition the *identical* checks into at most
four compilation units; no changed input or weakened obligation. Preserve
all terminal results, including failed pilots and configuration mistakes.

## Verification and reporting

Require full root import coverage, pinned build, source correspondence,
compiled transitive axiom audit, matched apparatus controls and inherited
negative controls. Preserve local driver-deadline failures separately from
individual-control and remote-CI results. Update current README/STATUS/
FORMALIZATION and the short human guide. Publish only to draft PR 28;
verify exact commit/tree and pinned CI. Do not merge or post to Tao.

Success here would exclude **one bounded interval** in the stated arithmetic
class, not establish the global cutoff, even-discriminant cases, remaining
249 intervals, unbounded tail, finite classification, optimality or novelty.
If an obligation remains open, name it and keep the overall goal active.
