# Phase370 — Provenance-bound adversarial research feedback

**20 November 2026. Research-only. Parent:** Phase368 PR #279 and Phase369 local adversarial correction. Evidence levels: **P** only for already-checked Phase367 Lean source identities; **M** for synthetic contract/regression tests; **H** for live verifier security or research allocation advantage.

## Question

Can a constrained Pareto Worldlet bandit consume a finding only when it is bound to a task it issued, the original integer trace-Gram source and claim scope, the exact Git commit, and an authorization record signed by an independent verifier?

## Source and evidence invariants

Use the Phase367 source `integerTraceGramMatrix Q D J rows` with ORIGINAL ordinary-Z derivative holding W fixed, full `Fin J x Q` observations and `G=2(AA^T + D BB^T)`. No padded source as Gram replacement, no selected minor transfer, no new conductor p-factor. Phase306 D203 maximal-order world is an incompatible contrast.

The selector has no theorem-promotion API. Lean success may discharge a locally encoded proof obligation, bounded Prolog or source checks only diagnostic work, external human review only a review task. None alone validates a novel number-field statement.

## Protocol (H for deployed system)

1. Issue a task with nonce, epoch, arm, source identifier, exact 40-hex commit SHA, claim scope, clock, and cost. Its ID is the canonical SHA256 digest of these fields. One unresolved task per arm; an unissued receipt cannot be consumed.
2. An independent process obtains **real** run/job metadata and complete logs from authenticated read-only GitHub access. It verifies run head, exact task-ID output marker, successful execution, error-free body, a completion marker, and stable artifact SHA256. This GitHub reader is NOT implemented by the fixture.
3. A separate key custodian signs the complete outcome with Ed25519. The research selector owns **only pinned public keys** and a scope-to-role policy.
4. After validation, a signed outcome updates routing observations **once** and releases the pending arm. The event is stored in an in-memory SHA256-linked ledger. This detects local mutation but is neither durable nor cryptographically anchored against full rewrite.
5. Never treat signed data as proof of impartiality, correct science, or independent field semantics. Never allow the bandit to choose its own signing authority.

## Hostile controls

Reject signatures from wrong keys, mutated signed payload, unissued task, duplicate/replay, stale commit, changed D203 source, wrong claim scope/cost, unauthorized role, missing output marker, exception-bearing CI with success status, and a transcript showing only shell-command echoes of an expected marker.

Historical anti-control: GitHub run #44753105275 returned `success` despite an ignored GNU Prolog consult directive and an uncaught exception. Its successor #44753393399 passed actual tests, but it was **not** issued by Phase370 and must be rejected for retroactive attribution.

## Test and publication boundary

```sh
python3 -m pip install cryptography==46.0.4
python3 -m unittest discover -s research/phase370 -p 'test_*.py' -v
```

The 20 tests use **synthetic signing keys and fixture log strings**. They do not constitute an independent deployed verifier. Source and clock gates come from Phase368/369; the Phase370 branch carries Phase369's pending-aware policy but not the separately archived full Phase369 synthetic benchmark.

**Promotion gate:** Build a real read-only Github fetcher and externally isolated signer, durable independently anchored event log, key revocation, task expiry/retry, and held-out adjudicated real-task baseline comparison. Do not merge into public main on green fixture tests. The `301^4` source-to-field arithmetic and number-field semantic reconstruction remains independently open (issue #50). No Siegel-zero inference.
