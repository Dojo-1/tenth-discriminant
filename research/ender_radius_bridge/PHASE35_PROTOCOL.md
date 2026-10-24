# Phase 35: fused wheel traversal with complete seed partition

Base 29a155e5843e1764ebcccc48c8bbb78ff5718cbf. Previous goal turn made
verified progress: exact root-mask/test/wheel equivalence and four preserved
negative cost results, with pinned CI 40139545303/security 40139542493 PASS.
Remote head/main and draft/unmerged PR28 refreshed; only inherited
lean/lake-manifest.json untracked. No local proof process remains. No agents.

## One bounded proof/certificate-organization attempt

The remaining target stays the ENTIRE [1000000,700000000000). Attempt a
fused traversal that checks a leaf as soon as it is generated, without
constructing the full wheel list. Prove equality with `.all` over the old
materialized list for arbitrary predicates, not just the pilot predicate.
Use only natural arithmetic, all old guards and unchanged mask meaning.

Split the fixed base [3,5,7,11,13,17,19,23] at its final prime 23. The
seed list is exactly the old wheel for [23], of modulus 184. Prove it has
eleven entries and prove that visiting all seeds under the other seven
primes covers exactly the old full wheel. Reordering traversal is allowed
only with the universal all-predicate correspondence proof. A length
check, generated assertion or empirical agreement is insufficient coverage.

Keep all 208 existing literal masks, their exact order, and all four fixed
quotient indices [0,1,392,784]. For each quotient attempt ALL eleven seed
blocks, with the original interval filter. Separate kernel certificates
may reset evaluator memory between blocks. Each certificate has the same
8192 MB / 180-second limits as Phase34, and the whole cost pilot has a
720-second aggregate wall budget. If a block fails, stop further blocks
for that quotient and still test the first block for each later registered
quotient; report every skipped block explicitly. No retuned primes,
replacement seed, smaller interval, budget increase or hidden restart.
Preserve every terminal proof failure and resource stop.

Masks may be certified once per literal with a checked aggregate proof,
to avoid retaining one monolithic reduction. Generated data or proof
scripts remain untrusted until the kernel accepts them. If all eleven
blocks for a quotient pass, assemble them into the original translate
predicate using the proved partition. Do not count blocks as complete
translates. If enough concrete interfaces compile, expose actual-field
exclusions for the sampled translates with all positivity, squarefreeness,
primality, strictness and no-loss coverage premises supplied, not hidden.
These are sampled-translate results, NEVER full 785-quotient coverage.
No extrapolated full cold-CI runtime from successful warm/local pilots.

## Controls and delivery

Require a false leaf predicate to be detected on a nonempty seed traversal;
show that an empty/omitted seed partition cannot stand in for the complete
one. Retain the half-open interval filter, d=163,p=41 endpoint, zero residue,
wrong-mask, composite-modulus and all earlier coverage controls. Do not
discard Phase34's failed implementation or rewrite its result as success.

Commit this protocol before code edits. Update task state and a short human
guide; consolidate current README/STATUS/FORMALIZATION/objective notes with
the exact new frontier. Run monitored root build, source correspondence,
import coverage, compiled axiom audit and exact signatures. Scope any local
parent timeout separately; require full unchanged audit/negative gates in
exact-head pinned Linux CI. Only update existing draft PR28; no merge,
Tao post, new axiom, native_decide, changed pins/production tools/frozen
campaign/cutoff or optimized/global classification claim. The larger goal
and all other unsatisfied challenge objectives remain active.
