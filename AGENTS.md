# Repository instructions — one readable main, faithful proof transport

This repository concerns the actual Tenth Discriminant, its integer ordinary-jet Gram, and Lean proofs. **`main` is the only continuing reader-facing source of truth.** A short-lived PR is an implementation/testing mechanism, not a parallel published version. Do not claim an unmerged experiment is on `main`.

## Every experiment turn — mandatory

Before ending **each** experiment cycle (including a failed, partial, corrected, or resource-stopped cycle):

1. **Run an @Rizz review** of the mathematical exposition and developer interface. Here “rizz” means reconstructability, recognizable author voice, consideration for other mathematicians, and honest limitations — not rhetorical polish. Avoid repetitive boilerplate, dramatic headlines, or claims stronger than evidence.
2. **Update the root `README.md`** in the same publication cycle: one short statement of what changed, its mathematical consequence (or lack thereof), verification status, and the link to the exact artifact. Keep it easy to read, not a running transcript.
3. **Update `RESEARCH_NOW.md`** when the trusted result, active experiment, verification status, or reviewer obligation changes. Put detailed logs in the relevant research folder; preserve historical records unchanged.
4. Preserve exact source SHA, checks, and failures. Declare `P` (checked encoded theorem), `M` (measured finite result), `H` (unproved hypothesis), `S` (semantic design), and `R` (unresolved or disproved obligation). Passing CI does not establish the correctness of an independently intended mathematical statement.
5. If a proof or check fails, **record the failed attempt before repairing it**. Fix proofs without silently changing hypotheses, original objects, thresholds or verifier configurations.
6. Verify that production `lean/TenthDiscriminant.lean` only imports modules that compile against the pinned Lean dependency versions. An experimental proof with red CI must not be merged as a checked theorem.
7. Prefer normal merge commits to preserve research provenance. Do not rewrite historical evidence or silently turn a cancelled workflow into a passed check. The user requested consolidation of previously reviewed PRs into `main`.
8. For user-facing updates, name the **actual** result, what does not follow, and the smallest next falsification/verification obligation. Do not manufacture an independent referee, novelty or an improved cutoff.

## Stable mathematical nucleus

Use the actual integer coordinate matrix of **ordinary** polynomial jets `E`, original positive trace metric `B`, and `G = E B Eᵀ`. The field discriminant is not `det(G)`. Arithmetic `U_p` and radial `T_a` are integer frame operations with explicit guards, and a change in row norms does not change `det(G)`. A finite frame commutator or geometric analogy is not a uniform analytic determinant improvement.

The accepted main theorem is the **47.1-billion actual-field upper bound**, with exact-head successful full Lean CI and open independent mathematical semantic reconstruction. The 47.5-billion theorem remains a checked predecessor. Phase133's proposed **47.0-billion** tightening is an experimental PR and must not be promoted before complete checked field composition and its own full-root audit.

## Entry points

- `README.md`: short human-oriented front door — update every experiment turn.
- `RESEARCH_NOW.md`: verified versus measured versus hypothesis, current blocker.
- `research/ender_radius_bridge/`: original reconstruction and frozen evidence.
- `research/proof_transport_v0/`: bounded finite Rust/Lean transport pilot.
- `STATUS.md`: historical research log; do not rewrite old claims as present-tense facts.
