# Phase56: local verification of the50-billion field bound

**Local PASS.** For any actual totally complex rational degree-two number
field K with actual class number one, Lean proves

    (NumberField.discr K).natAbs < 50000000000.

The caller supplies no generator, isomorphism, numerical premise or
finite-range certificate. [Human argument](FIFTY_BILLION_GUIDE.md).
Exact-head CI and independent human semantic review remain separate.
The Phase55 bounded review is preserved at frozen86abe21 and62.5b;
it does not cover these new gain and geometric-helper changes.

Protocol `a42ab4fdbc7da06e1fb528703b4c6904e09db567` fixed the81/1000
gain,450^4 helper guard,50b endpoint, controls and budget before source.
The single target build PASS121.4529248s. No failed build, repair, second
target run, resource stop, pilot or parameter search occurred. Earlier
failures remain unchanged in their own archived records.

Full root PASS40.6872364s,6819-step build, including the old62.5b wrapper
after explicit weaker-helper guard conversions. Fresh signatures,
controls, generic-field example and two axiom prints PASS40.0445155s.
New odd-chart/canonical/abstract dependency closures reach55475,55810,
58604 constants; none reaches the25 explicitly listed old-cutoff,
classification, finite-answer or fixed-ratio roots. The list now includes
the old62.5b conclusions. Unresolved/unsafe constants and nonstandard
axioms are rejected. This is an explicit dependency check, not a semantic
claim that a finite denylist detects every imaginable circular proof.

Whole-project compiled audit PASS31.8192312s:4755 logical declarations,
4012 theorems,16968 runtime-only auxiliaries; only `propext`,
`Classical.choice`, `Quot.sound` allowed.165 project modules are reachable
and acyclic, with no source proof escapes. Source correspondence passes
all250 endpoint pairs; this checks identity, not Arb inequalities.

The evidence verifier checks four first-attempt terminal records, raw
and source hashes, exact helper generalizations/old-caller conversions,
and the new root imports. Complete audit stdout is retained in a ZIP,
read back byte-for-byte before removal of its duplicate. Pins, numerical
tables, production tools and gates are unchanged.

Phase54 raw records and source hashes are checked at their frozen86abe21
version. Phase55 first-report/dispatch/receipt bytes and frozen source
hashes also remain intact. Their old current-root verifiers are historical
after this mathematical change; use the new verifier for current source.
No older report is silently transferred to the50b proof.

Commands from repository root, pinned elan binaries on PATH:

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File research/ender_radius_bridge/run_phase56.ps1 -Mode build
powershell -NoProfile -ExecutionPolicy Bypass -File research/ender_radius_bridge/run_phase56.ps1 -Mode root
powershell -NoProfile -ExecutionPolicy Bypass -File research/ender_radius_bridge/run_phase56.ps1 -Mode input
powershell -NoProfile -ExecutionPolicy Bypass -File research/ender_radius_bridge/run_phase56.ps1 -Mode audit
python research/ender_radius_bridge/verify_phase56_results.py
git -c core.whitespace=blank-at-eol,blank-at-eof,space-before-tab,cr-at-eol diff --check
```

Do not rerun a bounded target to manufacture another timing. The saved
records preserve its original execution. From `lean`, source correspondence
was checked with `python verify_sources.py`. Integrity verification does
not execute Lean, prove mathematical validity independently or establish
human/model-family independence.

Previous mathematical head86abe21 passed pinned CI40355317865 and
security/CodeQL; its review/documentation publication80107ff has distinct
CI40358914884. The new50b source requires its own exact-head publication
record. No merge, Tao submission, full-classification announcement,
novelty, optimality, higher-class-number result or Mathlib acceptance follows.
