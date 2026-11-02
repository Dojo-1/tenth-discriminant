# Phase175: Integrating the exact 377^4 prerequisites

**This is an integration of prior verified theorem sources, not a claim of a new field bound.**

The following exact source blobs are preserved without rewriting:
- Phase172 [PR #91](https://github.com/Dojo-1/tenth-discriminant/pull/91): `Lower377.lean` SHA `39eb00df98f1922ffff7d30afd5793fac75d0a90`. This establishes a conditional normalized lower on the **original positive integer trace Gram**. It states the positivity and number-field assumptions explicitly.
- Phase173 [PR #92](https://github.com/Dojo-1/tenth-discriminant/pull/92): `BinaryGap377.lean` SHA `3ad9d753c79a83e7bdc3e86240ac983f606c0e8e`. This normalizes the *existing* binary exponent and isolates the conditional scalar separation; it adds no auxiliary prime.
- Phase174 [PR #93](https://github.com/Dojo-1/tenth-discriminant/pull/93): `SourcePositivity377.lean` SHA `5aa1921d96cef4c4cf7761bd213bd278186ce594`. The original thin/padded source support and integer ordinary-jet trace Grams are preserved.
- Previously merged Phase169 [PR #88](https://github.com/Dojo-1/tenth-discriminant/pull/88) supplies the **true** log floor `log D >= 23.7` at `D >= 377^4`, Phase170 [#89](https://github.com/Dojo-1/tenth-discriminant/pull/89) the thin-ellipse interpolation criterion, and Phase171 [#90](https://github.com/Dojo-1/tenth-discriminant/pull/90) the original radius/dimension ratio.

## Scope of the combined audit

The only modified existing Lean file is the root module's import list; all three new theorem bodies are reused byte for byte. Their previously passing focused and full-root builds are **correlated checks on separate branches**, so this combined branch must pass its own exact-head `lake build`, source correspondence, permitted axiom audit, known-false negative controls and CodeQL before integration.

## Semantic direction

There is exactly one potential field-level comparison:

```
old source integer observations Qthin
        |
original integer ordinary-Z-jet Gram G(Qthin,D,R,S)
     /                              \
odd-prime + binary lower          real analytic upper
     \                              /
        same positive log(det G) / (R^2 S)
```

All the prime divisibility is re-applied to the actual chosen source Q. The older padded count bounds **number of nodes**, not its determinant. The existing analytic upper is still verified only for the old domain `D >= 450^4`. Its extension to `D >= 377^4` is an independent theorem target, and therefore the proposed cutoff `377^4 = 20,200,652,641` is **not proved**. The strongest established actual-field threshold is `41,006,250,000`.

**Stop condition**: fail compilation, source/axiom/negative controls, or any attempted substitution of the padded determinant for the thin one. Independent semantic reconstruction remains open in [Issue #50](https://github.com/Dojo-1/tenth-discriminant/issues/50); mathematical future work is [Issue #82](https://github.com/Dojo-1/tenth-discriminant/issues/82).
