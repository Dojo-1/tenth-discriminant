# Phase38: proof-input provenance, not another classification claim

Base proof head ebf14c2564102ef54139024ce9f9c46228307692. Previous turn
made verified progress: full proof CI40148050189 and security40148047110
passed; tree34f70cda25c28db1ccd0389ae418c8b4b9007b4d. Final verification
issuecomment-6391797752 supersedes its pending checkpoints. Live PR28 is
OPEN/DRAFT/UNMERGED; only inherited lean/lake-manifest.json is untracked.

## Question and fixed method

The axiom gate does not by itself establish that Heegner's classification
or another prohibited mathematical input was not used. Inspect the actual
compiled proof-input graph, not the import list or a source-name grep.
Reuse Lean4.19's existing CollectAxioms traversal and its visited set. This
traverses declaration types and theorem/definition/opaque bodies, including
private relays and inductive constructors. Record every visited constant,
its declaration kind, source module and safety metadata. Do not silently
equate an unknown/missing constant with a checked source.

Fixed five real roots:

- TenthDiscriminant.FirstCertificate.odd_large_classNumber_ne_one
- TenthDiscriminant.imaginaryQuadratic_classNumber_one_radicand_bound
- TenthDiscriminant.phase36_all_fibers
- TenthDiscriminant.known_nine_classNumber_one
- TenthDiscriminant.imaginaryQuadratic_classNumber_one_iff

Require three controls in the same environment: a clean theorem must not
inherit an unused simulated forbidden input; a private/opaque relay must
expose that input; a dependency occurring in the statement type must be
retained. These are traversal controls, not mathematical counterexamples.

After a syntax-only implementation check if needed, run one fixed compiled
provenance driver under180s/8192MB, one thread/16384KB stack. Preserve every
failure or stop; at most three generic elaboration repairs may correct code
without changing roots, controls or limits. Do not retry a resource-stopped
run in this phase or infer a clean mathematical verdict from missing output.

## Interpretation and limits

Print the complete reached graph before selecting human-facing highlights.
Inspect all reached external class-number/PID/Minkowski inputs and their
actual pinned sources. Name matching is a discovery aid, not a proof that
an unnamed method is absent. Any alleged classification/circular input must
be verified by reading its source. Classify undecided cases explicitly.
The result is an internally performed, frozen proof-input audit, NOT an
independent human review or a replacement for the kernel/axiom checks.

Do not modify mathematical statements, proof bodies, frozen campaigns,
production tools, dependency pins, CI gates or resource limits. Add a small
research auditor, raw evidence and a concise human input map. Update current
reader status/accounting, clarifying that finite d<=163 is distinct from
optimizing the analytic7e11 cutoff. Maintain task checkpoints. The new audit
is a local snapshot, not an unannounced permanent CI gate. Re-run pinned CI
on the publication head; report exactly what that CI covers. Publish only
to draft PR28, never merge or post an AI-written summary to Tao.
