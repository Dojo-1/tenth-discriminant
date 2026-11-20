# Phase373 — Clock-authority compatibility square (pre-registration)

**20 November 2026 · Research-only draft. Parent:** Phase372 PR #282; exact original source remains Phase367 integer trace Gram and ordinary-Z derivatives with W held fixed.

## Falsifiable question

Can a bandit preserve **separate** issuance authorization, native Worldlet clock, execution identity, wall-time ordering, immutable policy version and external-verifier authority, without inventing a privileged global scalar clock?

A previous genuine source-guard GitHub execution was declared on the research phase \`fast\`, but its \`source.original\` Worldlet is native to \`meso\` under the Phase368 manifest. It is **M for executed event** and **R_transport for claimed Phase368-scheduler authorization**. Do not edit the historical comment, task hash or CI log retroactively.

## Frozen clock semantics

From the actually inspected Phase368 \`PolyBandit.eligible\`:

| Selected scheduling tier | Eligible native clocks |
| --- | --- |
| fast | fast |
| meso | fast, meso |
| review | fast, meso, review |

This means scheduling phase and native clock are **not necessarily identical**. For example, Prolog's fast-native Worldlet may be scheduled during meso; the meso-native source Worldlet may NOT be scheduled during fast. Human review remains a distinct execution authority and requires review-phase scheduling.

No logical research clock is itself a wall UTC timestamp. GitHub \`run_started_at\`, issue/comment time, and external validation time are separate observation surfaces. Their relative order must be independently grounded; no semantic clock equality is assumed.

## Mathematical targets (H until exact-head checked)

1. Lean \`Allowed\` and \`TierAdmits\`: a typed audited four-arm projection of native-clock and tier authority from Phase368; prove the historical fast-source rejection and meso-tier/fast-native-Prolog admission.
2. Lean strict time transport \`f\`: \`StrictMono f\` preserves and reflects order on Nat. A merely monotone constant map collapses distinct event times. This is a theorem about a specified map, **not proof** the external timestamps obey that map.
3. Lean clock bridge: only a permission-preserving, strict-order-preserving mapping may carry authorization. Show no permission-preserving source meso→fast bridge is possible under this frozen projection. Composition must preserve both obligations.
4. Lean evidence square: source/version compatibility, original authorization, issue→start, start→validation; prove order result under explicit assumptions. Do not ascribe authenticity to an in-memory label, a symbolic Nat version, or an externally provided Boolean.

## Implementation and bounded falsifiers (M only if exact-head tested)

- \`clock_contract.py\` pins canonical SHA256 of the original JSON manifest at task issuance. It records both requested tier and actual native Worldlet clock using the *real* inherited selector; signed clock metadata binds to the original signed attempt's full execution key.
- No policy clock can be invented by a remote signer: authorization comes from the pinned manifest snapshot. It must be revalidated at acceptance without trusting an arbitrary signer assertion.
- Explicitly reject historical fast-source issuance, stale or mutated policy manifest, changed native clock, changed tier, wrong Worldlet/source, different commit/attempt, wrong signer or forged signed payload, preissue execution, invalid validation ordering, replay and proof-promotion by a source guard.
- Positive affine clock maps are a *mathematical control*, not a real claim about GitHub clock synchronization. Constant/negative maps fail admission.
- GNU Prolog adversarial worlds include nested tiers, wrong manifest, cross-source D203 contrast, human review mistakenly treated as CI, false-green execution, non-strict clock map, and preissue result.

## Structural and semantic limits

The Lean policy is an explicit finite four-arm **projection** of the actual external manifest; no Lean parser or proof that an arbitrary JSON file matches it exists. Tests cannot authenticate a GitHub issuance/comment, an independent signing key or timestamps. SHA256 in Python binds only the in-memory manifest snapshot, not independently anchored policy history. The external reviewer time source and an isolated signer remain H. No new 301^4 bound, number-field class-number proof or Siegel-zero result follows.

Evidence tags: P only for exact compiled Lean theorem; M only for bounded Python/Prolog controls and previously inspected Phase371 GitHub execution; H for real deployed signer/clock synchronization/allocator performance; R_transport for the historical fast/meso authorization mismatch; R_sem remains independent field chart reconstruction issue #50.

## Promotion/kill conditions

- Fail on any clock authorization inferred solely from a successful execution or from a generic monotone map.
- Fail if a signed receipt can override a manifest-native clock, a task's requested scheduling tier, a source identity or its execution attempt.
- Fail if Phase373 proves only a new tautological wrapper while implying provenance authenticity, a better bandit, or a field result.
- Compare clock-safe and clock-ablated policies using independent real-task outcomes later, at matched cost, to test any claimed empirical advantage.
- Keep PR as draft, no public main merge on fixture CI alone.

## Reproduce

    cd lean && lake build TenthDiscriminant.Phase373ClockAuthoritySquare
    python3 -m pip install cryptography==46.0.4
    python3 -m unittest discover -s research/phase373 -p 'test_*.py' -v
    gprolog --consult-file research/phase373/clock_authority.pl --query-goal phase373_main
