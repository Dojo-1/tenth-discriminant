# Phase 30: make the finite sieve's mathematical preconditions checked

Base: `165d11082da069a45b44620e89c72b3c45dc81f6`. Previous turn was progress:
the effective bound for every positive squarefree radicand passed pinned
Lean CI 40125864965 and security 40125864826; merge/head/local trees matched
25acc980c24bb31145ab1433167513b954dc6d27. Refresh confirms zero divergence;
PR28 remains draft/unmerged. Preserve untracked lake-manifest.json. No live
local proof process remains. No subagents, new trust primitive or changed pin.

## One proof-bridge attempt

The frozen CRT program begins with d=3 mod 8. Prove this from actual class
number one for every positive squarefree radicand d>7. Do not assume it or
confuse the bound on d with a classification below it.

In the odd half-integral order, d=7 mod 8 makes c=(d+1)/4 even. Construct
the F2 quotient directly by omega -> 0; do NOT divide by two modulo two.
Use the actual maximal-order equivalence and general principal-kernel norm
theorem to force principalNorm=2 under class number one. The existing strict
small-norm obstruction rules this out above 7. Join the even chart through
the actual field equivalence already checked in Phase29.

Next formalize a finite, untrusted-input modular-root Boolean check and prove
its sound connection to the existing odd-prime nonsquare theorem. Retain
every strict endpoint: a prime test binds exactly when 4*p<=d on the odd
fundamental chart. At d=4*p-1 it must not bind. Prove actual class number one
supplies the finite sieve predicate; primality and coverage of any prime
list must remain checked hypotheses/data, never inferred from a filename.

Use the fixed base primes [3,5,7,11,13,17,19,23], exactly the saved program's
base. As a bounded kernel-control proof, check the complete range 0<=d<92,
with exceptional d=1,2,3,7 retained and the valid guarded base tests. Seek
the necessary small candidate list [1,2,3,7,11,19,43,67]. This is a finite
proof-control input, not an observational experiment or a substitute for the
unclosed interval [92,700000000000). Do not change that interval or threshold.

Expose a precise reduction from the actual class-number problem to a
complete middle-range survivor theorem. If a proposed Boolean condition
rejects a genuine small candidate, preserve that negative result before
changing it; no parameter tuning in this phase. Do not claim full
classification from conditional reduction or small-range checks.

## Controls and resource policy

Require the d=7 norm-two exception, a concrete d=23 exclusion, correct
acceptance of all nine known radicand candidates by the necessary test
(not proofs that their class numbers are one), and strict/inclusive endpoint
controls. Retain guards d>7, squarefreeness, prime primality and oddness as
applicable. Prove finite evaluations with kernel-checked decision/reflection,
not native_decide, oracle output or new axioms. Preserve every terminal
development failure/resource stop. Use the existing 8192-MB owned-process
monitor and default proof budgets unless a bounded elaboration repair is
explicitly recorded; never weaken mathematical targets to pass a budget.

## Delivery

Do not rerun/modify the frozen numerical campaign, CRT tool, saved ledgers,
flow protocols or dependency pins. Review finite-certificate obligations by
reading their implementations. Run full root build, source correspondence,
compiled axiom audit, direct matched controls and inherited negative controls
through exact-head pinned CI; report local parent deadlines separately.
Update README/STATUS/FORMALIZATION, current objective ledger and a short
human guide. Only update draft PR28; no merge, Tao post, novelty, optimized
cutoff, positive class-number classifications or full finite-classification
claim. Independent semantic review and other challenge requirements stay open.
