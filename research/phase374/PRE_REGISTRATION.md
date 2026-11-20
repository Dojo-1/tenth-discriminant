# Phase374 — Eight-arm manifest → Lean eligibility refinement (preregistered)

**20 November 2026. DRAFT. Parent:** Phase373 PR #283, frozen head \`f38fb25eb94ecb44f5101d14c12f1bbf1efb3230\`. Research-only; no public main merge.

## Scope and evidence floor

The prior Phase373 result proves a four-arm \`ResearchClock\` projection and strict time transport. It does **not** establish that its projection corresponds to the unchanged eight-arm Python research allocator. Phase374 addresses only this narrower cross-language eligibility gap, holding the entire original Phase368 manifest, \`PolyBandit.eligible\` implementation and all lower field sources fixed.

Existing **P**: Phase373 Lean declarations relative to their formal assumptions. **M**: bounded source tests and live Phase371 GitHub execution with historical fast/meso mismatch. **H**: full Python/Lean semantic equivalence, authenticated external receipt chain, any class-number inference, improved bandit performance.

## Frozen real data and complete finite domain

- Exactly 8 arms from \`research/phase368/manifest.json\`, indexed in their original insertion order (\`Fin 8\`). No selected-only or special four-arm projection.
- 3 scheduling tiers \`fast\`, \`meso\`, \`review\`; the inherited Phase368 nested tier semantics are \`{fast}\`, \`{fast,meso}\`, \`{fast,meso,review}\`.
- Two Boolean flags \`include_human\`, \`include_contrast\`.
- Budget values 0 to 9 inclusive, where **the original maximum arm cost is 8**; larger budgets cannot change cost eligibility until the manifest/selector changes.
- \`8 × 3 × 2 × 2 × 10 = 960\` Boolean eligibility cases.
- Source lock \`original-integer-pair-ordinary-Z-gram@phase367\`; Phase306 D203 maximal-order contrast remains opt-in and must not be silently interpreted as the same original source.
- Finite artifact contains Git **blob SHA-1 of the exact source manifest bytes** as a policy version label; the Phase373 runtime independently uses a canonical JSON SHA-256. These are different encodings of the same expected bytes and must not be identified without a checked conversion. A version label alone cannot authenticate external provenance.

## Refutation-first methodology

\`gen_refinement.py\` creates a Lean source definition for all eight arm costs, native clocks, source/contrast flags, human authority and forbidden-transport status. **Separately**, it invokes the unchanged Phase368 \`PolyBandit.eligible\` as the independent finite oracle, emitting 120 eligibility bitmasks (one per tier × flags × budget).

The generated Lean theorem target compares its own Boolean \`manifestEligible\` against these fixed oracle masks over all 960 cases. The three \`by decide\` theorems must compile and have no \`sorryAx\`/\`admitAx\`. Additional executable Python tests compare the unchanged runtime selector against an independent, plainly written specification and require that the committed Lean file regenerate **byte-for-byte** from the exact manifest.

**Invalidations:** A changed original JSON, reordered arm list, changed source, changed arm cost or clock, omission of contrast/human flags, fast-source authorization, failure to include fast-native Prolog during meso, or stale Lean oracle output must fail CI. Do not rewrite history to make Phase371 fast issuance legitimate.

## Formality, remainder and falsification boundaries

1. A passing Lean theorem establishes equality of the *finite encoded predicate and fixed expected masks*, not a theorem about arbitrary Python execution or the GitHub service.
2. The Python oracle comparison is bounded independently by 960 distinct decisions and saturation checks for budgets > 9, **not a language-semantics theorem**.
3. The generator and oracle are both authored within this research lineage: external independent code review and alternate implementation are still necessary for strong semantic assurance.
4. No real independent signer, append-only external issuer, authenticated clock, task-bound execution service, or reviewer is introduced.
5. No original Gram, selected row family, conductor, field chart or class-number claim is modified. The \`301^4\` discriminant assertion and Siegel-zero consequences remain independently unverified (issue #50).

**Promotion policy:** Only mark the bounded eight-arm finite refinement as **P relative to formal encoding** after exact-head Lean and test verification. Mark Python checks M; leave general semantic equivalence, external authorization and mathematical field theorem H. Retain PR as draft, no public main merge.

## Reproduce

    python3 scripts/phase365_lean_anchor_guard.py
    python3 research/phase374/gen_refinement.py --check
    python3 -m unittest discover -s research/phase374 -p 'test_*.py' -v
    cd lean
    lake build TenthDiscriminant.Phase374ManifestRefinement

Each command must operate on the same immutable commit and inspect actual output, not only GitHub green status.
