# Phase373 — clock authority is not event execution

Polycosmic Adversarial Bandit, research-only continuation of [Phase372 PR #282](https://github.com/Dojo-1/tenth-discriminant/pull/282). The actual Phase368 manifest and selector define a **tiered capability relation**:

| Requested scheduling phase | Admissible native Worldlet clocks |
| --- | --- |
| fast | fast |
| meso | fast, meso |
| review | fast, meso, review |

This is separate from UTC issuance, workflow start, and validation time. Native source.original is meso, so historical Phase371 fast source issuance is an authentic observed execution but **not** an authorized selection by the inherited scheduler. Never erase that discrepancy.

- Lean module: \`lean/TenthDiscriminant/Phase373ClockAuthoritySquare.lean\`. A four-arm policy **projection** from the Phase368 JSON manifest, explicit TierAdmits, strict-order clock transport and permission-preserving bridges, a constant clock counterexample, and an evidence square with externally assumed source/version and time constraints. Lean does not authenticate the JSON file, signer or GitHub.
- Python: \`clock_contract.py\` + \`test_clock_contract.py\`. A SHA256 manifest snapshot, original tier, native clock, and externally signed clock stamp are verified before consumption by the Phase372 attempt-specific gate. Test signing keys are **synthetic**. The collector is not an authenticated GitHub reader.
- GNU Prolog: \`clock_authority.pl\`. Finite counterworlds for phase nesting, an unapproved source-fast selection, human-review/CI confusion, wrong manifest and clock flattening.
- Preregistration: \`PRE_REGISTRATION.md\`.

## Verification targets

All workflows must pass on the SAME frozen commit before promoting the *encoded* Phase373 statements to P or describing the bounded Python/Prolog tests as M. The relevant runs are:
\`phase373-clock-lean.yml\` and \`phase373-clock-controls.yml\`.

The theory does **not** prove independently authenticated timestamps, Ed25519 key custody, source-to-field arithmetic for the 301^4 discriminant, Siegel-zero implications, or greater research-allocation performance. All of these remain open. PR #283 stays draft and unmerged.

## Run

    cd lean && lake build TenthDiscriminant.Phase373ClockAuthoritySquare
    python3 -m pip install cryptography==46.0.4
    python3 -m unittest discover -s research/phase373 -p 'test_*.py' -v
    gprolog --consult-file research/phase373/clock_authority.pl --query-goal phase373_main

This is a typed governance mechanism, not a numerical hypercomplex performance claim. No higher algebra is imported without a measurable obstruction distinguishing it from the simpler typed clock model.
