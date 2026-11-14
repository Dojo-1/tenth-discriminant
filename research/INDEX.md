# Tenth Discriminant — research index

**Current research parent:** research/phase309-original-source-picard-minors  
**Publication boundary:** main is unchanged; the accepted actual-field (322^4) endpoint remains the public theorem.  
**Date:** 14 November 2026.

This index is the navigable map of the research programme. It keeps finite source calculations, formal statements, global ideal arithmetic, analytic hypotheses and independent review obligations distinct.

## Phase209–268 — original-Gram geometry and the 321⁴ candidate

**Current integration:** PR #219, research-only, exact-head verification in progress.

- Phase209: ordinary-jet Taylor flow, divided-Frobenius depth and original-source conjugate folding.
- Phase210–211: class-number-free inert-prime budget, exceptional-zero scale audit and fixed-support rank obstruction.
- Phase223–228: horizontal transport and the combined integral Frobenius frame on the same original Gram.
- Phase259–268: enhanced same-Gram lower, analytic upper, scalar overlap and actual-field 321⁴ candidate.

Reader guide: [research/phase209-268/README.md](phase209-268/README.md).

The formal Phase267 theorem states (|\operatorname{disc}(K)|<321^4) for totally complex degree-two class-number-one fields. It passed focused and whole-root Lean CI on its original 10 November proof-changing head. The current consolidated branch is being rechecked. Independent semantic reconstruction remains open in issues #50 and #51. The Phase210 zero-exclusion comparison is not a zero-free theorem.

## Phase269–270 — finite CRT and inert-sieve certificate

A bounded finite arithmetic certificate at the accepted (322^4) endpoint, with a Lean CRT proof and two differently ordered integer enumerations. This is a finite certificate, not a new unconditional class-number-one classification or Siegel-zero exclusion.

Entry point: [research/phase269/FINITE_INERT_SIEVE_321.md](phase269/FINITE_INERT_SIEVE_321.md).

## Phase277–292 — primitive pairing, Noether and Smith

- Phase277–278: primitive p-adic pairing and safe overlap accounting.
- Phase287–288: moving frames, adiabatic leakage, integral transverse transport and weighted remainders.
- Phase289–290: Fischer/Schur, held-out source controls, primitive radical and Noether–Smith walls.
- Phase291–292: D563/D587/D583 source controls and parity-resolved Schur extension.

Reader guide: [research/phase277-292/README.md](phase277-292/README.md).

## Phase293–303 — Hermite/Frobenius, Picard and maximal-order bridges

Graded Jordan transport, source-moment saturation, Picard/minor controls, maximal-order source completion and the exact D163 Frobenius primitive-Gram explanation.

Reader guide: [research/phase303/OBSERVED_MAXIMAL_ORDER_AND_FIELD_BRIDGES.md](phase303/OBSERVED_MAXIMAL_ORDER_AND_FIELD_BRIDGES.md).

## Phase306–319 — source transport and wild-ray realization

Inert trace, conductor-125 logarithms, exact norm-preserving local lifts, radical pencils, norm-fibre vetoes and D163 maximal-order completion.

Reader guide: [research/phase319/README.md](phase319/README.md).

## Phase320 — cross-field source completion and second-wild normal maps

D163, D187 and D203 (class numbers 1, 2 and 4), with matched and native row/jet geometries and even-suborder/full-maximal-order controls.

**Exact-head CI passed.**

PR #217 merged into the research parent at 1b9461d. The exact head passed the Phase320, Phase318, Phase319, finite CRT, whole-root Lean and Markdown checks. Ten source arms and all local lift/first-wild-digit checks are reproducible finite-source results, not a field-uniform valuation theorem.

Reader guide: [research/phase320/README.md](phase320/README.md).

## Phase321 — ideal-aware ray class groups and exact invariant factors

**Integrated research-only:** [PR #218](https://github.com/Dojo-1/tenth-discriminant/pull/218), merged at `d16238d`. Its exact-head Phase321 construction, whole-root Lean replay and Markdown checks passed.

The full ray class groups modulo 125 were constructed for D163, D187 and D203 using exact ideal lattices, reduced forms and the extension cocycle. Their orders are 7,500, 15,000 and 30,000. The bounded prime-ideal catalog retains nonprincipal ideals and maps them into the full ray groups.

**Phase321-B:** [PR #221](https://github.com/Dojo-1/tenth-discriminant/pull/221), merged at `549514a`. The exact-head workflow passed all 9 adversarial tests after correcting five stale expected-value assertions from the first run. The invariant factors are:
- D163: C25 x C300;
- D187: C50 x C300;
- D203: C100 x C300.

The ray exact sequence splits in all three tested fields. D187 has 2 section lifts among all 7,500 local lifts; D203 has 4. Nonidentity cocycle entries for a canonical transversal do not imply nonsplitting: alternate lifts give explicit sections. The first failed expectation run remains in the audit manifest.

Reader guides: [Phase321](phase321/README.md) · [Phase321-B results](phase321/PHASE321B_RESULTS.md) · [Phase321-B preregistration](phase321/PRE_REGISTERED_PHASE321B_RAY_INVARIANT_FACTORS.md).

The finite results do not establish a full character table, a uniform ray-class formula, a zero-free region or a new discriminant bound.

## Open review and publication boundaries

- [PR #157](https://github.com/Dojo-1/tenth-discriminant/pull/157): original 321⁴ actual-field candidate against main. It remains a draft and is not merged.
- [Issue #50](https://github.com/Dojo-1/tenth-discriminant/issues/50): independent semantic reconstruction of the actual-field 321⁴/322⁴ statements.
- [Issue #51](https://github.com/Dojo-1/tenth-discriminant/issues/51): source identity and cross-method comparator audit.
- [PR #218](https://github.com/Dojo-1/tenth-discriminant/pull/218): Phase321 ray groups.
- [PR #219](https://github.com/Dojo-1/tenth-discriminant/pull/219): Phase209–268 source and 321⁴ line.

No research PR changes main. No new determinant valuation is inferred from a changed residue modulo 25. No class-number-(>1) global character family is inferred from principal generators alone. No general-character zero-free theorem is claimed.


## Historical branch audit — no duplicate merges

The earlier lines were checked against the current main tree before deciding whether to consolidate them again:

- **Phases134–148:** the original minor, residue-transport, moving-frame and arithmetic-chamber work is already in main. Phase144–148 was merged via [PR #68](https://github.com/Dojo-1/tenth-discriminant/pull/68); issue [#67](https://github.com/Dojo-1/tenth-discriminant/issues/67) records the completion and exact finite controls. The surviving old branches are provenance, not missing work.
- **Phases190–196 and 199:** the audited branch heads are ancestors of main. Their later scalar and prime-gain results are already represented in the main history.
- **Phases200–206:** the source-to-field, exact arithmetic, p-adic valuation, factorial filtration and geometry modules are already in main; the Phase200 same-Gram branch files inspected are byte-identical to main.
- **Phase201–206:** the independent reconstruction and source-geometry branches are ancestors of main.
- **Phase192 and Phase197:** these retain branch-only intermediate floor/scalar experiments (328⁴ and 324⁴ scales). They are preserved as historical references, but not re-imported into the active research parent: the accepted 322⁴ endpoint and the stronger 321⁴ candidate supersede their target bounds.

This avoids duplicate or stale integrations while keeping the proof lineage discoverable.
