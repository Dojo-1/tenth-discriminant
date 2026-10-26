# Phase 31: prove wheel coverage, then check one fixed finite interval

Base 9102f8a065613c796a7640eb80a61087063788b5. Previous goal turn made
verified progress: modulo-eight and necessary prime tests compiled; exact-tree
Lean CI 40128348264 and security 40128344427 passed. Live refresh confirms
zero divergence and PR28 OPEN/DRAFT/UNMERGED. Preserve the inherited untracked
lake manifest. No subagents. Full classification and other Tao objectives remain open.

## Target and alternatives

The remaining middle interval is [92,700000000000), not [92,1000000).
Direct kernel evaluation of every integer wastes the established modular
structure. Importing the Python result would leave coverage unproved.
Instead prove a universal wheel-coverage theorem: successive prime-residue
lifts preserve every integer meeting the modulo-eight and nonsquare tests;
quotient/remainder enumerates every interval point in a covered residue class.
Filtering by the already proved guarded tests then gives a sound exclusion.
The checker must not assume complete input residue lists by filename.

Use a smaller wheel for a fixed resource-bounded certificate of a genuine
initial part of the remaining interval. Start modulus 8, residues [3]; lift
by exactly [3,5,7,11]. Product modulus is 9240. Extra primes are exactly
[13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101,103,107,109,113,127].
Require checked primality/oddness of these data. Enumerate the COMPLETE
interval [92,1000000), not sampled points. Seek the sole survivor [163].
Do not change the endpoint or prime list after seeing the result. If it
fails or hits resources, preserve it and report the actual surviving list
or unclosed proof. This does not certify the original full CRT campaign.

The universal coverage infrastructure must remain applicable to the full
middle interval and larger wheels. A successful bounded certificate should
give an actual-field necessary nine-candidate theorem below 1000000, joined
to Phase30's small list, and an explicit remaining interval obligation.
Do not assert positive class-number equalities or full classification.

## Guards and controls

Retain strict binding 4*p<=d, all squarefreeness/positivity hypotheses where
needed, and the d=163/p=41 endpoint control. Require complete wheel coverage
including both interval endpoints in their correct half-open roles.
Check malformed/omitted residue or quotient coverage is not accepted as a
complete certificate; check 163 is retained. The universal proof, not
matching a finite output, must justify coverage. A Boolean root test is only
used through its already proved soundness; no new trust primitive.

Use kernel-checked decision/reflection, not native_decide, external oracle
proofs, added axioms or weakened audit gates. Default elaboration budgets
and existing 8192 MB owned-process monitor apply. Preserve every terminal
development failure/resource stop. An independent exact calculation may
generate/read the same fixed data, but does not replace the Lean proof.
Do not run or modify the frozen full campaign, CRT tool, old ledgers,
dependency pins or numerical cutoff. No parameter search in this phase.

## Delivery

Commit this protocol before proof edits. Add the smallest mathematical
coverage/checker slice and a short human explanation. Update current status,
formalization and objective accounting without rewriting frozen snapshots.
Run full pinned build, source correspondence, compiled axiom audit, readable
API and inherited adversarial controls; separate local driver deadlines from
actual proof failures and exact-head Linux CI. Update only draft PR28,
without merging or posting to Tao. Keep the global goal active.
