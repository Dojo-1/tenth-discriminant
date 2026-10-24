# Phase 34: exact residue-mask bridge and fixed full-range cost pilot

Base a4a343c64c5bc296a7611ff90e704ac03983a992. Phase33 made verified
progress: all nine positives and both directions below one million passed
pinned CI 40136870017 and security 40136867529. Remote main remains
392b6dbb12d7c451225afde6c964ef4b70f614e8; draft PR28 head matches local.
Only the inherited lean/lake-manifest.json is untracked. No subagents.

## Target and invariant

The full remaining target stays [1000000,700000000000), not an easier
replacement interval. First attempt a reusable computational bridge:
precompute the bit mask of residues -r^2 modulo p, and prove for every
positive p and every natural d that querying bit d%p equals the existing
modularRootTest d p. Retain zero residues and the exact guard 4*p<=d.
No probabilistic test, finite-word truncation, native_decide or new axiom.

Separate thin computational definitions (Lean core/Std only) from the
Mathlib semantic proof, so future certificate modules need not each load
the number-field development. Generated masks are untrusted until their
equality with the defined mask is kernel checked. Do not replace the
original predicate or its existing proof by an assumed mask interpretation.

## One bounded cost pilot

After the bridge compiles, use exactly the frozen base primes
[3,5,7,11,13,17,19,23] and the first 200 primes from 29, as specified in
tools/sieve_crt.py. Determine their literal list deterministically; no prime
or wheel tuning. Attempt kernel-checked certificate computations for the
four fixed quotient indices [0,1,392,784] of the base period 892371480,
filtered to the ORIGINAL half-open remaining interval. The last sample
includes its cutoff endpoint padding. These are a performance/semantics
pilot only, not coverage of the other quotients and not classification.
Record the exact padded quotient count for the full range; do not infer
full runtime by multiplying a warm local timing.

Use ordinary natural-number arithmetic (the cutoff exceeds 2^39), short
circuit prime tests and streaming enumeration where possible. A pilot
failure must not be hidden by a smaller prime list, a smaller wheel, an
easier replacement quotient or a larger proof budget. Generic elaboration
repairs may be made with each terminal failure preserved. Stop any owned
Lean process at the existing 8192 MB cap. A time limit of 180 seconds per
pilot certificate applies; preserve terminal logs even on a stop. If a
sample cannot finish, that is the bounded result, not evidence of a false
mathematical claim. No full campaign or full 785-quotient run this phase.

## Controls and delivery

Check p=1 and composite p to demonstrate the semantic equivalence is not
silently prime-dependent; reject p=0 from the general theorem. Retain
d=163,p=41 strict-versus-inclusive endpoint control, zero-square residues,
an altered mask bit, half-open bounds and omitted-quotient coverage control.
The original wheel coverage theorem remains authoritative; a fast pilot
without its full correspondence theorem is not a field exclusion theorem.

Commit this protocol before proof/experiment edits. Preserve raw failures
and report their meaning. Update task state, a short human guide, and current
README/STATUS/FORMALIZATION/objective notes without rewriting frozen evidence.
Require monitored build, import closure, compiled axiom audit and unchanged
pinned CI gates before reporting a published proof as checked. Do not change
production tools, pins, cutoff, historical certificates or old protocols.
Only update draft PR28; no merge or Tao post. All other objectives remain
open to their existing extent; no global classification or optimization claim.
