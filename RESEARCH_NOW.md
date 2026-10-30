# Start here — current Tenth Discriminant research state

**Canonical branch: [main](https://github.com/Dojo-1/tenth-discriminant/tree/main).** This is the sole publication and reader entry point. Old PRs and commits are evidence provenance, not competing versions readers must follow. The register below separates *integrated mathematics*, *bounded experiments*, *proposed improvements*, and *independent review*.

## What a reader can currently rely on

**Actual-field bound (formally checked; independent human semantic review open).**
The Lean declaration `SharpRadialEndpoint.totallyComplex_degree_two_classNumber_one_discriminant_bound_47_1b` states that any totally complex degree-two number field with class number one has **actual absolute field discriminant strictly below 47,100,000,000**. This is a field statement, not an identification of the field discriminant with the much larger observation determinant. The predecessor `EndpointCutoff.*47_5b` remains unchanged, including its original exact-version proof receipts.

[Human proof reconstructed](research/sharp_radial_v1/ENDPOINT_RECONSTRUCTION.md) · [Lean theorem](lean/TenthDiscriminant/SharpRadialEndpoint.lean) · [#48 merged](https://github.com/Dojo-1/tenth-discriminant/pull/48) · [full proof, axiom audit and negative controls PASS](https://github.com/Dojo-1/tenth-discriminant/actions/runs/41087748526) · [focused new endpoint PASS](https://github.com/Dojo-1/tenth-discriminant/actions/runs/41087748532).

**One integer through arithmetic and geometry.** For the original integer matrix of ordinary quadratic-order polynomial jets (E) and its original trace metric (B), the Gram is (G=EBE^{\mathsf T}). The arithmetic bridge constructs integer quotient observations for each guarded inert prime and gives (U_p G U_p^{\mathsf T}=\Delta_p K_p\Delta_p), with (det U_p=1), hence (p^{2F(p)}\mid\det G). The integral radial frame changes row estimates but preserves this SAME determinant. The exterior-volume explanation is a change of language, not a new proof of the integral quotient.

[Independent finite reference oracle](research/ender_radius_bridge/TWO_SIDED_ARITHMETIC_BRIDGE.md) · [exterior-volume guide](research/ender_radius_bridge/EXTERIOR_VOLUME_GUIDE.md) · [#44 merged](https://github.com/Dojo-1/tenth-discriminant/pull/44) · [#46 merged](https://github.com/Dojo-1/tenth-discriminant/pull/46). An independent implementation path is **not** an independent human referee.

**Existing canonical classification.** The arbitrary-field equivalence interface transports the existing nine-field classification; its finite endgame has its **own** 700-billion route. The 47.1-billion estimate is not claimed as the source of that separate endgame. [Classification interface](research/ender_radius_bridge/CLASSIFICATION_INTERFACE_CURRENT.md).

## Bounded representation experiments — integrated, with explicit limits

[Proof-transport atlas](research/proof_transport_v0/PROOF_ATLAS.md) and [Rust experiment](research/proof_transport_v0/README.md) compare the actual integer arithmetic and radial frames (U_p,T_a). Their orders need not commute, but both preserve the same Gram determinant. Exact finite Rust checks passed on [PR #47's recorded head](https://github.com/Dojo-1/tenth-discriminant/actions/runs/41044427391), including a nonreal quadratic-coordinate control. The Lean source compiled, source/certificate correspondence and allowed-axiom audit passed, and negative-control families passed; the [overall CI run was subsequently cancelled](https://github.com/Dojo-1/tenth-discriminant/actions/runs/41044433938) at its time limit. **Do not relabel the cancelled workflow green.** No new cutoff follows from these finite experiments. [#47 merged](https://github.com/Dojo-1/tenth-discriminant/pull/47).

## New accepted bound, and the next unproved hypothesis

**Phase132 is integrated and full-audited on its exact source head.** It bounds the **same integer Gram** using rounded center `101/200`, actual ordinary-jet factor `63/100`, saving `0.011`, and the rational N=5 logarithm certificate with exact separation `31369/5000000000>0`. [Full-root CI](https://github.com/Dojo-1/tenth-discriminant/actions/runs/41087748526) accepted all **208 project modules**, exact source-certificate correspondence, the entire project's permitted-axiom audit and negative controls; CodeQL and focused new-module checks also passed. It does **not** establish originality, optimality or an independent mathematician's verdict. The initial failed controls and previous audit-import failure remain in [PR #48](https://github.com/Dojo-1/tenth-discriminant/pull/48) and git history.

**Future Phase133 candidate [H, not proved]:** an exact factorization for the same parameter interval gives `676S(R-9S)-17R²=(S-t)(191S+17t)` with `t=R-25S`; if the existing rational checker proves `log(100/63)>=231/500`, the savings may reach `0.0115` and permit a **47.0-billion** endpoint. [Exact rational precursor and required gates](https://github.com/Dojo-1/tenth-discriminant/pull/48#issuecomment-6527885186). No new Lean theorem, external referee, or performance gain is claimed for this suggestion.

The proposed polyholonomic 360×360 controller, hyperbolic shape geometry and typed Ortho/Anti/Ambig transport remain a conceptual research interface until they demonstrate an independently checkable advantage. Neither the exact finite commutator nor a geometric metaphor implies a stronger arithmetic inequality.

## What remains independently unresolved

The frozen 173-module Argon review, the old exact-version project replay, current Lean source compilation, bounded reference implementations and **independent mathematician semantic reconstruction** are separate kinds of evidence. The semantic reconstruction of the complete arithmetic prime-mass and geometric comparison remains open. [Verification boundaries](research/ender_radius_bridge/VERIFICATION_LAYERS_CURRENT.md).

## Reproduce or challenge

```sh
cd lean
lake build
python audit.py
python negative_controls.py
```

For the bounded Rust controls, use `cargo test --offline --manifest-path research/proof_transport_v0/Cargo.toml`. Read each historical receipt at the recorded source SHA; new changes to `main` do not retroactively turn a previous exact-head run into a different one.

**Publication rule:** small branches/PRs may be used transiently for review and CI, but *main* is the only continuing research surface. Experimental lemmas can enter `main` only with their exact proof status labelled and with the production Lean root still compiling. Do not promote speculative endpoints or merge compiler-failing proof modules.
