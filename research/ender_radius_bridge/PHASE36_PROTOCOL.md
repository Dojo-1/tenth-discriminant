# Phase36: quotient-fiber bitsets for the FULL original middle interval

Base f0f6bae9c4191e9326ab0fd3e993d50c1eca1cd2. Previous goal turn made
verified progress: bounded actual-field iff below892371480, pinned
CI40143185318/security40143183607 PASS, matching treef7baecfb482f4bbf77dcadbf9820bf59b51f7adb.
Final record issuecomment-6391087799 supersedes its pending checkpoints.
Remote main392b6db/head refreshed; draft/unmerged PR28. Only inherited
lean/lake-manifest.json untracked. No agents or live local proof processes.

## Fixed representation, not a smaller target

Keep the original [1000000,700000000000), the eight base primes, all200
extra primes29..1289, their order, and periodM=892371480. For each covered
base residue r, encode ALL785 quotient positions k at once in a Nat bitset.
The initial bitset must represent exactly lo<=r+M*k<hi for r<M; do not
include the upper endpoint or discard a valid quotient. Natural-number
arithmetic avoids finite-word overflow.

For each extra prime p, use an explicitly checked inverse a with M*a=1
mod p. A p-periodic allowed pattern for M*j, shifted by (a*r)%p, represents
the necessary prime condition for r+M*k. A precomputed pattern of width
785+p suffices for all k<785 and all offsets<p. Filter by bitwise AND;
short-circuit only when the current bitset is zero.

Implement the periodic-pattern reference by finite residue-bit enumeration,
not an assumed external table. Prove its testBit meaning, the affine shift
identity, initial interval semantics and survivor-bit retention through all
filters. Reuse the Phase35 universal fused traversal/complete seed coverage.
Every literal inverse/pattern must be kernel checked before an actual-field
exclusion claim. Generated data are untrusted inputs, not theorem premises
to be silently left unsupplied.

## One bounded full-fiber cost pilot

After generic semantics compile, attempt the same eleven seed subtrees
[3,27,35,59,75,123,131,139,147,163,179], but with the ALL785-position leaf
predicate, starting at seed3. Limit each seed certificate to8192MB/180s,
and the whole pilot to720s. Stop further seeds after the first terminal
failure/resource stop or aggregate exhaustion; record all skips. Do not
replace that seed, reduce the quotient width, change primes/intervals or
raise proof/resource limits. Any polling/termination overshoot is disclosed.
No duplicate replay is disguised as a fresh observation.

A cost pilot before all literal data reflections finish is explicitly only
a measurement of that stated candidate checker. It cannot certify the
arithmetic/class-number assertion. If all eleven seeds AND all data/semantic
bridges pass, assemble complete middle-range exclusion and compose with the
already checked cutoff and all nine positive fields. Only then may a full
classification in the encoded positive-squarefree field family be claimed.
No extrapolation from one seed, period, or warm local timing to full CI.

## Controls, repairs and delivery

Require the p=29,r=163 control (quotient0 accepted by that prime test,
quotient1 rejected); a wrong shift sign or unchecked inverse must be rejected.
The initial bit for d=163 is excluded only because it lies below lo, not
by falsely rejecting its arithmetic. Check lower/upper interval endpoints,
zero residues, no phantom bits beyond784, empty filters, and omitted seeds.
Retain all existing controls and prior raw negative results unchanged.

Preserve every terminal proof failure/resource stop. Generic elaboration
or proof-grouping repairs may not weaken a hypothesis/target or increase
limits. If a stronger full certificate is accepted, expensive old q0 proof
bodies may be derived from it with unchanged statements and an explicitly
acyclic dependency chain; no old evidence is rewritten or gate weakened.

Commit this protocol before code/tests. Maintain task state, explain the
operator and exact remaining gap to humans, and update current reader and
objective accounting. Verify full root/import/axiom/signature scope and
unchanged exact-head pinned CI. Only update draft PR28, no automatic merge
or Tao post. No novelty, optimized analytic constant, independent human
review, upstream acceptance or fulfillment of all challenge objectives is
inferred from a Boolean check or a partial encoded-family proof.
