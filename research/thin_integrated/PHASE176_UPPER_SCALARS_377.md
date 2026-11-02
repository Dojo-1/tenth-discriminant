# Phase176 — the original analytic scalar envelope at fourth-root 377

**Evidence:** new Lean candidate (H), not yet kernel-checked and not yet a determinant upper or field cutoff.

This file keeps the existing definitions
(R(D)=lfloor D/4floor),
(S(D)=lfloor R(D)/25floor),
(ho(D)=lceil(13/25)D^{3/4}ceil),
and the original padded ellipse cardinality majorant
(N_{mathrm{old}}(D)).

The specific goal is to reprove **the very same old analytic scalar**
[
rac{mathrm{enderUpperB}(R,S,S,ho,N_{mathrm{old}})}
     {R^2S}
le rac45log D-rac{813}{1000}
]
for the smaller domain (Dge377^4). This does **not** yet upper-bound (logdet G_{mathrm{thin}}).

The proof intentionally rederives the ingredients from source:
- Phase170's fourth-root lower bound;
- Phase171's (hole(521/1000)D^{3/4}) and (ho/Rle521/90000);
- Phase172's original dimension and (log R) estimates;
- Phase169's true (log Dge23.7), rather than the **false at 377** premise (log Dge24);
- the original cardinality expression and (pi)-bound.

The old scalar lemmas are copied as **new theorem targets with explicit smaller domains**, rather than silently weakening their established old hypotheses. The file also tries to recover (10leho_{m thin}<ho<R), an input to the final source-exact thin-Q Hadamard step.

**Kill gates:** the focused pinned Lean build or whole-root source/axiom/negative-control audit fails, any new scalar assumption exceeds what is proved at 377, or the old padded majorant is treated as an equality of Gram determinants. In particular, positivity of the padded count is supplied by Phase174's independent thin-count route, not by the invalid 3R+S sufficient certificate.

**Next**: reapply `TightRadialSaving.normalized_integer_upper_tight` to (Q_{m thin}) with the **same** ordinary-jet integer trace Gram. Combine with the generic unchanged-radius subtraction theorem to target (rac45log D-rac{1849}{2000}). That remains a separate conjectural bridge.

Cross-check [Issue #82](https://github.com/Dojo-1/tenth-discriminant/issues/82) and independent semantics [#50](https://github.com/Dojo-1/tenth-discriminant/issues/50). The existing actual-field discriminant bound remains (41,006,250,000).
