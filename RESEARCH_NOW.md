# Start here — current Tenth Discriminant research state

**Canonical branch: [main](https://github.com/Dojo-1/tenth-discriminant/tree/main).** This is the sole publication and reader entry point. Old PRs and commits are evidence provenance, not competing versions readers must follow. The register below separates *integrated mathematics*, *bounded experiments*, *proposed improvements*, and *independent review*.

## What a reader can currently rely on

**Actual-field bound (formally checked, interpretation still open to independent human review).**
The Lean statement `EndpointCutoff.totallyComplex_degree_two_classNumber_one_discriminant_bound_47_5b` says that a totally complex number field of degree two and class number one has **absolute field discriminant strictly below 47,500,000,000**. It is a bound on the field's actual discriminant, not on a surrogate observation discriminant or the Gram determinant.

[Read the short proof](research/ender_radius_bridge/STRUCTURAL_BRIDGE_CURRENT.md) · [Lean theorem](lean/TenthDiscriminant/EndpointCutoff.lean) · [#45 merged](https://github.com/Dojo-1/tenth-discriminant/pull/45) · [exact-head Lean CI PASS](https://github.com/Dojo-1/tenth-discriminant/actions/runs/41021656669) · [security PASS](https://github.com/Dojo-1/tenth-discriminant/actions/runs/41021651935).

**One integer through arithmetic and geometry.** For the original integer matrix of ordinary quadratic-order polynomial jets (E) and its original trace metric (B), the Gram is (G=EBE^{\mathsf T}). The arithmetic bridge constructs integer quotient observations for each guarded inert prime and gives (U_p G U_p^{\mathsf T}=\Delta_p K_p\Delta_p), with (det U_p=1), hence (p^{2F(p)}\mid\det G). The integral radial frame changes row estimates but preserves this SAME determinant. The exterior-volume explanation is a change of language, not a new proof of the integral quotient.

[Independent finite reference oracle](research/ender_radius_bridge/TWO_SIDED_ARITHMETIC_BRIDGE.md) · [exterior-volume guide](research/ender_radius_bridge/EXTERIOR_VOLUME_GUIDE.md) · [#44 merged](https://github.com/Dojo-1/tenth-discriminant/pull/44) · [#46 merged](https://github.com/Dojo-1/tenth-discriminant/pull/46). An independent implementation path is **not** an independent human referee.

**Existing canonical classification.** The arbitrary-field equivalence interface transports the existing nine-field classification; its finite endgame has its **own** 700-billion route. The 47.5-billion estimate is not claimed as the source of that separate endgame. [Classification interface](research/ender_radius_bridge/CLASSIFICATION_INTERFACE_CURRENT.md).

## Bounded representation experiments — integrated, with explicit limits

[Proof-transport atlas](research/proof_transport_v0/PROOF_ATLAS.md) and [Rust experiment](research/proof_transport_v0/README.md) compare the actual integer arithmetic and radial frames (U_p,T_a). Their orders need not commute, but both preserve the same Gram determinant. Exact finite Rust checks passed on [PR #47's recorded head](https://github.com/Dojo-1/tenth-discriminant/actions/runs/41044427391), including a nonreal quadratic-coordinate control. The Lean source compiled, source/certificate correspondence and allowed-axiom audit passed, and negative-control families passed; the [overall CI run was subsequently cancelled](https://github.com/Dojo-1/tenth-discriminant/actions/runs/41044433938) at its time limit. **Do not relabel the cancelled workflow green.** No new cutoff follows from these finite experiments. [#47 merged](https://github.com/Dojo-1/tenth-discriminant/pull/47).

## Open mathematics: not an accepted improvement

A sharper rounded radial envelope `101/200`, ordinary-jet factor `63/100`, and uniform saving `0.011` now have a [successful focused Lean build](https://github.com/Dojo-1/tenth-discriminant/actions/runs/41053237537). The first full build compiled but its audit rejected a missing module import. The corrective [commit `b16e835`](https://github.com/Dojo-1/tenth-discriminant/commit/b16e835adf58287a198186376cbe8b31d60bd4a1) adds that import without weakening the audit and introduces a new five-term logarithm certificate, a complete proposed **47.1-billion actual-field theorem**, and a [human reconstruction](https://github.com/Dojo-1/tenth-discriminant/blob/research/sharp-radial-same-gram-v1/research/sharp_radial_v1/ENDPOINT_RECONSTRUCTION.md). **The new endpoint is not yet accepted in `main`**: its [exact-head focused Lean build passed](https://github.com/Dojo-1/tenth-discriminant/actions/runs/41087748532), including the actual-field theorem and rational certificate, while the [full root build, transitive dependency audit and negatives](https://github.com/Dojo-1/tenth-discriminant/actions/runs/41087748526) are still a separate pending gate. Independent human semantic review also remains open. The established published bound remains **47.5 billion**.

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
