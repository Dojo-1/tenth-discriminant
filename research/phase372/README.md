# Phase372 | the run family is not an execution

Research-only continuation of the Polycosmic Adversarial Bandit, stacked on Phase371. The original Phase367 integer trace Gram and field-review limitations remain unchanged.

## Verified layers

- Formal target: Phase372ExecutionAttempts.lean. Run ID, run attempt, job ID and commit identity form an execution key; an issued task cannot be credited twice and credited job/execution lists remain duplicate-free over arbitrary admissible finite transitions. Authorization booleans and timestamp correctness are **external premises**.
- Routing guard: attempt_contract.py and test_attempt_contract.py. Separate-source, separate-scope, immutable-head, timestamp, signed-payload and role checks, with replay detection keyed by complete execution identity AND by job ID. Signed keys in the tests are synthetic.
- Prolog counterworld: attempt_lineage.pl, a finite demonstration that one GitHub run family can contain distinct executions, plus missing-marker, preissue, wrong-head and recycled-job nulls.

## A new concrete correction

The real Phase371 SOURCE_CONTRACT task was labelled research_clock=fast. The Phase368 manifest allows source_anchor_mutation only on the **meso** clock. Thus Phase371's authenticated-looking GitHub execution is valid as an observed *execution trace*, but it could not be issued by the inherited current scheduler under the same scope. Do not rewrite the Phase371 issuance or interpret it as proof that the current selector ran. Phase372 has an explicit negative test for that cross-interface clock mismatch and uses meso in correctly eligible controller fixtures.

## Reproduce

    cd lean && lake build TenthDiscriminant.Phase372ExecutionAttempts
    python3 -m unittest discover -s research/phase372 -p 'test_*.py' -v
    gprolog --consult-file research/phase372/attempt_lineage.pl --query-goal phase372_main

The focused CI checks are separate from independently validated arithmetic and cannot grant a new class-number claim. Check exact-head run statuses, not merely test files being present.

## Evidence boundaries

- P: Lean encoded finite-ledger theorem, once exact-head kernel/Axiom CI passes.
- M: 31 Python adversarial fixture controls and 15 GNU Prolog finite worlds, once exact-head CI passes.
- H: deployment safety, isolated signer, verified external comment reader, durable anchored ledger, measured bandit efficacy.
- [R]_transport: Phase371 fast-to-meso source-arm authorization mismatch, preserved as a falsifier.
- [R]_sem: independent arithmetic and maximal-order interpretation of the 301^4 discriminant remains open in issue #50.

No public-main merge, no new number-theoretic proof and no Siegel-zero claim.
