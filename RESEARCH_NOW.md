# Start here — current Tenth Discriminant research state

**Canonical branch: [main](https://github.com/Dojo-1/tenth-discriminant/tree/main).** This is the sole publication and reader entry point. Old PRs and commits are evidence provenance, not competing versions readers must follow. The register below separates *integrated mathematics*, *bounded experiments*, *proposed improvements*, and *independent review*.

## What a reader can currently rely on

**Actual-field bound (formally checked; independent human semantic review open).**
The Lean declaration `TightRadialEndpoint.totallyComplex_degree_two_classNumber_one_discriminant_bound_47b` states that any totally complex degree-two number field with class number one has **actual absolute field discriminant strictly below 47,000,000,000**. This is a field statement, not an identification of the field discriminant with the much larger observation determinant. The predecessor `EndpointCutoff.*47_5b` remains unchanged, including its original exact-version proof receipts.

[Reconstruction](research/tight_radial_v1/HUMAN_RECONSTRUCTION.md) · [Lean actual-field theorem](lean/TenthDiscriminant/TightRadialEndpoint.lean) · [#49 merged](https://github.com/Dojo-1/tenth-discriminant/pull/49) · [full root, axiom audit and negative controls PASS](https://github.com/Dojo-1/tenth-discriminant/actions/runs/41098122516) · [focused Lean PASS](https://github.com/Dojo-1/tenth-discriminant/actions/runs/41098122564) · [receipt](research/tight_radial_v1/PHASE133_VERIFICATION.md).

**One integer through arithmetic and geometry.** For the original integer matrix of ordinary quadratic-order polynomial jets (E) and its original trace metric (B), the Gram is (G=EBE^{\mathsf T}). The arithmetic bridge constructs integer quotient observations for each guarded inert prime and gives (U_p G U_p^{\mathsf T}=\Delta_p K_p\Delta_p), with (det U_p=1), hence (p^{2F(p)}\mid\det G). The integral radial frame changes row estimates but preserves this SAME determinant. The exterior-volume explanation is a change of language, not a new proof of the integral quotient.

[Independent finite reference oracle](research/ender_radius_bridge/TWO_SIDED_ARITHMETIC_BRIDGE.md) · [exterior-volume guide](research/ender_radius_bridge/EXTERIOR_VOLUME_GUIDE.md) · [#44 merged](https://github.com/Dojo-1/tenth-discriminant/pull/44) · [#46 merged](https://github.com/Dojo-1/tenth-discriminant/pull/46). An independent implementation path is **not** an independent human referee.

**Existing canonical classification.** The arbitrary-field equivalence interface transports the existing nine-field classification; its finite endgame has its **own** 700-billion route. Neither the 47.0- nor 47.1-billion estimate is claimed as the source of that separate endgame. [Classification interface](research/ender_radius_bridge/CLASSIFICATION_INTERFACE_CURRENT.md).

## Bounded representation experiments — integrated, with explicit limits

[Proof-transport atlas](research/proof_transport_v0/PROOF_ATLAS.md) and [Rust experiment](research/proof_transport_v0/README.md) compare the actual integer arithmetic and radial frames (U_p,T_a). Their orders need not commute, but both preserve the same Gram determinant. Exact finite Rust checks passed on [PR #47's recorded head](https://github.com/Dojo-1/tenth-discriminant/actions/runs/41044427391), including a nonreal quadratic-coordinate control. The Lean source compiled, source/certificate correspondence and allowed-axiom audit passed, and negative-control families passed; the [overall CI run was subsequently cancelled](https://github.com/Dojo-1/tenth-discriminant/actions/runs/41044433938) at its time limit. **Do not relabel the cancelled workflow green.** No new cutoff follows from these finite experiments. [#47 merged](https://github.com/Dojo-1/tenth-discriminant/pull/47).

## Two accepted radial bounds, and one open rank-transport bridge

**Phase132 is integrated and full-audited on its exact source head.** It bounds the **same integer Gram** using rounded center `101/200`, actual ordinary-jet factor `63/100`, saving `0.011`, and the rational N=5 logarithm certificate with exact separation `31369/5000000000>0`. [Full-root CI](https://github.com/Dojo-1/tenth-discriminant/actions/runs/41087748526) accepted all **208 project modules**, exact source-certificate correspondence, the entire project's permitted-axiom audit and negative controls; CodeQL and focused new-module checks also passed. It does **not** establish originality, optimality or an independent mathematician's verdict. The initial failed controls and previous audit-import failure remain in [PR #48](https://github.com/Dojo-1/tenth-discriminant/pull/48) and git history.

**Phase133 [P: encoded theorem checked, human review open]:** [PR #49](https://github.com/Dojo-1/tenth-discriminant/pull/49) merged with the **47.0-billion actual-field theorem** on the same original Gram as the prior 47.1-billion result. For `t=R-25S`, `S≥100`, `25S≤R≤26S`, the identity `676S(R-9S)-17R²=(S-t)(191S+17t)≥0`, sound `log(100/63)≥231/500`, and N=5 `log(47b)` certificate yield saving `23/2000` and an exact positive gap `26281/1000000000`. [Full root CI PASS](https://github.com/Dojo-1/tenth-discriminant/actions/runs/41098122516) checks the actual field theorem, audit, original falsifiers and source correspondence. [Failed first source](https://github.com/Dojo-1/tenth-discriminant/actions/runs/41095139730) and [failed first repair](https://github.com/Dojo-1/tenth-discriminant/actions/runs/41096816617) remain preserved; they were elaboration errors, not counterexamples. [Full receipt](research/tight_radial_v1/PHASE133_VERIFICATION.md).

**Next open mathematical interface [H]:** unlike a selected maximal minor, our Gram determinant aggregates **all** minors. An auxiliary inert-prime rank witness from an external proof cannot simply be imported without matching the original observation matrix, sample set, ordinary derivatives and modulus. Moreover a prime whose row-valuation factor contains `p` cannot make this SAME matrix full rank modulo `p`; any valid rank-witness prime must avoid that obstruction. No new cutoff follows from the interface alone. [Elementary proof and controls](research/rank_divisor_interface/ONE_MATRIX_TWO_PRIMES.md) · [Phase134 preregistration](https://github.com/Dojo-1/tenth-discriminant/issues/51).

The proposed polyholonomic 360×360 controller, hyperbolic shape geometry and typed Ortho/Anti/Ambig transport remain a conceptual research interface until they demonstrate an independently checkable advantage. Neither the exact finite commutator nor a geometric metaphor implies a stronger arithmetic inequality.

## What remains independently unresolved

The frozen 173-module Argon review, the old exact-version project replay, current Lean source compilation, bounded reference implementations and **independent mathematician semantic reconstruction** are separate kinds of evidence; [review issue #50](https://github.com/Dojo-1/tenth-discriminant/issues/50) identifies a bounded four-obligation external review. The semantic reconstruction of the complete arithmetic prime-mass and geometric comparison remains open. [Verification boundaries](research/ender_radius_bridge/VERIFICATION_LAYERS_CURRENT.md).

## Reproduce or challenge

```sh
cd lean
lake build
python audit.py
python negative_controls.py
```

For the bounded Rust controls, use `cargo test --offline --manifest-path research/proof_transport_v0/Cargo.toml`. Read each historical receipt at the recorded source SHA; new changes to `main` do not retroactively turn a previous exact-head run into a different one.

**Phase134 experimental interface [H; not yet checked]:** [a generic integral selected-minor proof target](lean/TenthDiscriminant/RankDivisorCompatibility.lean), together with the [human-readable Tao-alignment and no-go analysis](research/tao_goal_alignment/FOLDING_TO_TAO_20261030.md), tests why p-adic extraction with positive rectangular weight forbids same-prime full modular row rank. This does **not** alter the original E, field cutoff, or classification. [Issue #51](https://github.com/Dojo-1/tenth-discriminant/issues/51) defines the stop gate; no new theorem is accepted before exact-head CI.

**Publication rule:** small branches/PRs may be used transiently for review and CI, but *main* is the only continuing research surface. Experimental lemmas can enter `main` only with their exact proof status labelled and with the production Lean root still compiling. Do not promote speculative endpoints or merge compiler-failing proof modules.
