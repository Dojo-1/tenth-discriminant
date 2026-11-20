# Phase372 — GitHub attempt identity, causal time and non-recirculation

20 November 2026. RESEARCH DRAFT. Parent Phase371 PR #281, final checked head b07bb172ad819b297bed46be1547488d3c215d73.

## Central question

When a GitHub run executes multiple attempts, which execution identity survives transport across the causal evidence loop, and what must be independently witnessed before the bandit may update its routing statistics?

## Real Phase371 GitHub execution (M, previously inspected)

- SOURCE_CONTRACT task was recorded in PR #281 comment 7049599129 at 2026-11-20 20:14:40 UTC, for commit b07bb172ad819b297bed46be1547488d3c215d73, task ID c930bcad33042b0f7004f74252f5ae6789617e5f36abfda6728287c4dc135c01.
- Run 44809412040 attempt 1 job 136541801767 preceded issuance; it printed PHASE371_INITIAL_PUSH_NOT_ISSUED_NO_CREDIT.
- Run 44809412040 attempt 2 job 136542423196 started 20:14:48 UTC, succeeded, and its actual output included exactly one standalone TASK_ID, RUN_ID, RUN_ATTEMPT=2, VERIFIED_PHASE371_SOURCE_ANCHOR. Seven original probe tests passed.
- Therefore run_id alone is NOT an injective execution identity. Use (run_id, run_attempt, job_id, head_sha) without assuming that job IDs alone remain globally unique forever.

## Formal targets, H until exact-head Lean builds

Define ExecutionKey(runId,attempt,jobId,head), IssuedTask(task,issuedAt), AttemptReceipt(issued,execution,startedAt,external booleans). CREDIT requires pending issuance, no previous task credit, no previous execution or job credit, matching source/head, issuedAt < startedAt, and separately authorized verification with success and exact marker. Prove duplicate-free credit lists over arbitrary finite permitted traces.

The Lean model assumes faithful external booleans, time, signatures, role, execution logs and head labels. It does not implement Ed25519, GitHub or a proof of mathematical truth. Its Nat-based head is a symbolic code, not SHA256.

## Python protocol and bounded adversarial tests

Phase372/attempt_contract.py wraps the Phase370 pending-aware scheduler with an AttemptEvidenceLoop. Its signed payload includes run ID, attempt, job, head, task, issuer reference, timestamps, source, scope, cost and verifier ID. Credit state deduplicates complete executions AND job IDs while allowing separately issued tasks to consume different attempts of one run family. It contains no claim promotion interface.

The register_issuance method is a TRUST INPUT, not proof that a remote GitHub comment exists. GitHubAttemptObservation is another read-only input, not an authenticated fetcher. Tests use synthetic Ed25519 keys and frozen metadata from Phase371; these are not new independent attestations. The in-memory hash chain is not tamperproof against its owner.

## GNU Prolog bounded oracle

Phase372/attempt_lineage.pl encodes the observed same-run two-attempt counterexample plus finite false-green, wrong-head, failed-job, missing-marker and recycled-job worlds. It is a search/falsification instrument, not a production verifier or number-theory theorem.

## Typed unresolved remainders

- [R]_formal: Lean-to-Python state transition correspondence is not yet verified by extraction or refinement.
- [R]_transport: authenticated read-only GitHub log/time retrieval is absent from this library.
- [R]_attr: external key custodian, signer revocation, independence and durable issuer record remain open.
- [R]_sem: independent quadratic number-field review is still open in issue #50.
- [R]_emp: no validated allocation advantage over matched baselines exists.

## Kill conditions

Reject a notion of execution identity based solely on run ID; reject unissued, replayed, mismatched-head, preissue, invalidly signed, wrong-role and false-green outcomes, including shell command echoes. Never promote a field theorem on automated CI alone. No 301^4, class-number or Siegel-zero conclusion follows from Phase372; public main remains unchanged.

## Reproduce

    cd lean
    lake build TenthDiscriminant.Phase372ExecutionAttempts

    python3 -m pip install cryptography==46.0.4
    python3 -m unittest discover -s research/phase372 -p 'test_*.py' -v
    gprolog --consult-file research/phase372/attempt_lineage.pl --query-goal phase372_main

Require fresh exact-head CI and inspection of actual output, not exit code alone. Leave draft unmerged until external source semantics are reviewed.

## E137 — Frozen clock mismatch found by first CI (not silently repaired)

The historical Phase371 source-guard issuance had research_clock=fast and a real matching GitHub execution. The inherited Phase368 manifest, however, declares source.original/source_anchor_mutation on the mesoscopic clock, not fast. At budget 1, the Phase369 PendingParetoBandit refuses the fast task as ineligible. This is a real cross-interface authorization mismatch, not merely a test fixture error. Historical Phase371 stays M for GitHub execution provenance but is NOT an authorized Phase368 scheduler decision. Phase372 formal/Python policy fixtures must use the meso clock; a separate adversarial test insists the historical fast interpretation is rejected. Do not alter the historical task ID or comment retroactively. A later explicit, preregistered clock-authorization revision would be required to make a fast source diagnostic eligible.
