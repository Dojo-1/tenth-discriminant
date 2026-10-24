# Phase 33: attempt the five remaining positive class-number equalities

Base 7c7f2c7f33fc38a1caee977b3db4d5e3660b0e4a. Previous goal turn made
verified progress: actual field-discriminant identity/bound and positive
cases d=1,2,3,7 passed pinned CI 40133608384/security 40133605897 on matching
tree 77af1da68e5127c2691e3d3afe3918310d9564d1. Live refresh confirms zero
divergence, draft/unmerged PR28 and only inherited lake manifest untracked.
No subagents. Full upper-middle exclusion and other objectives stay open.

## One bounded proof-bridge attempt

Attempt actual class number one for ALL five remaining radicands
[11,19,43,67,163], with no classification or Heegner-method input.
Use actual maximal orders, the Phase32 discriminant identity and pinned
Minkowski small-ideal representatives. Sieve acceptance is not a positive proof.

First prove an ideal of prime absolute norm p gives a quotient isomorphic
to ZMod p, using the pinned ringEquivOfPrime and actual quotient cardinality.
In the half-integral order, the generator image must solve
z^2-z+(d+1)/4=0. Thus a checked absence of such roots forbids ideals of norm p.
No division by two modulo two is permitted or needed.

Use exactly two tiers, fixed before proofs:

1. d=11,19: actual discriminant natAbs<=19, pi>3, degree two give a Minkowski
   representative of norm<3. Rule out norm two via the polynomial over F2;
   the representative then has norm one.
2. d=43,67,163: discriminant natAbs<=163 gives a representative of norm<9.
   Check root absence at precisely p=[2,3,5,7]. Any nonunit ideal of norm<=8
   is irreducible: a product of two nonunits would have both norms>=4,
   because norms two and three are absent, hence product>=16. Its quotient
   is a finite field of prime characteristic p dividing its norm n. Since
   p belongs to the ideal, n divides norm((p))=p^2 in degree two. The fixed
   small arithmetic leaves only n=4,p=2. The ideal then equals (2), by
   inclusion and equal nonzero absolute norms, and is principal. Every
   Minkowski representative is therefore principal.

Prefer reusable norm/ideal lemmas rather than five unrelated calculations.
The purely numerical guards are fixed: 4*19<9*3^2 and 4*163<9*9^2.
Do not replace an unclosed concrete case with a conditional theorem and call
it closed. If this chain fails, preserve the failure and state exactly which
bridge or concrete equality remains open. No new numerical parameter search.

## Controls

Require the d=23 counterexample: absolute field discriminant <=163 but
actual class number !=1 (already proved), showing the small-prime hypotheses
cannot be omitted. Its half-integral polynomial has root zero modulo two.
Require d=11's polynomial root zero modulo three, showing why it uses the
lower tier rather than the uniform four-prime hypothesis. Check the actual
norm of the principal ideal (2) is four in degree two; do not reject this
legitimate small ideal. Keep all positivity, squarefreeness, prime and
nonzero-ideal hypotheses explicit. Retain all earlier endpoint controls.

Use only kernel-checked proofs, default proof budgets and the existing
8192 MB owned-process monitor. Preserve every failed terminal attempt/resource
stop. Any bounded elaboration repair must be recorded; never weaken the
target to pass a resource cap. No native_decide, new axioms, dependency
changes or weakened gates. Do not rerun or modify the frozen campaigns,
production tools, old ledgers, cutoff or prior protocols.

## Delivery

Commit this protocol before proof edits. Explain the two norm tiers in a
short human guide, clearly separate from the unclosed interval
[1000000,700000000000). Update living README/STATUS/FORMALIZATION and the
objective ledger without rewriting frozen snapshots. Run full root build,
source correspondence, import closure, compiled axiom audit, signatures and
local readable-apparatus controls; require full unchanged parent-driver and
inherited negative suites in exact-head pinned Linux CI. Report local and
CI scopes separately. Only update draft PR28; no merge or Tao post, novelty,
optimized threshold, independent human review or full classification claim.
