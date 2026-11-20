# Phase371 — Issued-task state machine and real GitHub feedback

20 November 2026. RESEARCH ONLY. Parent Phase370 PR #280 (formal encoding and synthetic Ed25519 guards). No change to the Phase367 original integer trace Gram. The 301^4 field-bound semantics remain open for independent review.

## Pre-registered claims

1. Lean: a typed state machine distinguishes ISSUE from CREDIT, with pending tasks, credited task IDs, credited run IDs and external authority/success booleans. Every legal CREDIT requires issuance, unused task and run IDs, valid authority and successful execution. Over arbitrary allowed transition traces, credited task and run lists remain duplicate-free if they start duplicate-free.
2. Actual GitHub: a real SOURCE_CONTRACT CI task can produce an externally inspectable result at an immutable exact head. The first push is deliberately NOT an issued task and is NEVER creditable. After a GitHub PR issue comment records exact SHA, canonical SHA256 task ID, scope and nonce, a MANUAL RERUN of that same job may produce a valid task marker. No manual rerun means the bound experiment is still incomplete.
3. No signing: a CI completion marker is execution evidence only. No signer is independent merely because it runs in another job; no false mathematical acceptance or number-theoretic theorem follows.

## Frozen public task spec

- arm: source_anchor_mutation
- scope: source_contract
- source: original-integer-pair-ordinary-Z-gram@phase367
- issued_epoch: 1
- research_clock: fast
- cost_units: 1
- nonce: phase371-source-anchor-external-issue-20261120-v1
- repository_head: final exact 40-hex branch head, not known until commit is created
- task_id: sha256 of compact, sorted-key ASCII JSON object with exactly the preceding fields.

The real probe checks the original integer trace-Gram Lean-source anchors and five deliberately invalid textual mutations, not the independent semantics of the 301^4 number-theory proof. A genuine source control success must show the task ID and VERIFIED_PHASE371_SOURCE_ANCHOR printed by the executed Python process, not just a shell-command echo. The GitHub run and job conclusions, attempt number, repository commit and genuine log content must all be inspected through read-only GitHub access.

## Adversarial controls

Reject historical false-green run 44753105275, missing task issuance, old successful but unissued run 44753393399, initial push attempt as a credit, SHA mismatch, wrong source / D203 category, duplicate job/run attribution, invalid role, absent original source control marker and any unverified signer.

## Stop conditions

If the Lean proof fails compilation, do not claim a verified state-machine theorem. If GitHub cannot rerun the job with available permissions, report the blocker; do not claim actual task-bound evidence. No branch merge on mocked receipts or successful CI alone.

This phase does not implement a durable public ledger, independently held signing keys, human review, or a production verifier. The evidence floor is H for the full deployed loop, M for bounded real execution and model tests, and P only for exact Lean-checked statements relative to their encoded assumptions.
