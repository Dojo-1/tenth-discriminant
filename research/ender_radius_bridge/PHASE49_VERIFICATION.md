# Phase49 verification: central-negation sectors

Protocol6cada73 preceded the new104-line module and every attempt.
The unchanged target includes generic sample symmetry, ellipse stability,
mixed-parity zero entries and a nonsymmetric nonzero control.

Attempt1 FAIL63.7927406s: over-broad neg-power simplification hit recursion
depth, and the cast-injectivity argument name was wrong. Attempt2
FAIL22.9454932s: the remaining sign/distributivity identity needed ring
normalization. Complete failed sources and raw records are preserved.
Attempt3 PASS23.291557s. Total110.0297908s, no resource stop, no fourth
attempt or parameter search. Statements, sample set and caps unchanged.

Root build PASS23.8260569s,6813 steps. Public-signature/axiom examples
PASS24.233005s; all four public declarations use only propext,
Classical.choice and Quot.sound. Compiled namespace audit PASS35.3512301s:
4637 logical declarations,3900 theorems,16958 runtime-only auxiliaries
excluded. Import coverage159 reachable/acyclic modules; no proof escapes.
The unchanged source checker matches250 historical interval endpoint pairs;
that is not an Arb-inequality replay.

The generic entry theorem requires the actual finite sample set to be
closed under simultaneous negation and the sum of the four degree labels
to be odd. It does not require positivity, a nonzero determinant, inertness
or class number one. The ellipse instance uses positive D. The negative
control has entry2 for singleton(1,0),D=J=1,rows(0,0),(1,0).

Grouping rows by parity gives a block decomposition as a mathematical
consequence. No determinant-product API, stronger divisibility exponent,
strict Hadamard saving or new cutoff is exported by this addition.
The [human guide](CENTRAL_SYMMETRY_GUIDE.md) keeps those claims distinct.

Commands from repository root:

```powershell
powershell -NoProfile -File research/ender_radius_bridge/run_phase49.ps1 -Mode build
powershell -NoProfile -File research/ender_radius_bridge/run_phase49.ps1 -Mode root
powershell -NoProfile -File research/ender_radius_bridge/run_phase49.ps1 -Mode input
powershell -NoProfile -File research/ender_radius_bridge/run_phase49.ps1 -Mode audit
python lean/verify_sources.py
python research/ender_radius_bridge/verify_phase49_results.py
```

The build command records an attempt and is capped; do not rerun it as an
evidence verifier after the three-attempt budget is consumed. The Python
verifier checks preserved records/hashes/exact repairs and import coverage;
it does not execute Lean. The raw audit was archived and read back exactly
before removing its sole unpacked duplicate. PHASE49_RESULTS.json freezes
the source and raw-file hashes. Older Phase47 verification retains its
historical root fingerprint and must not be presented as a current-root
check after the new import.

Local acceptance is separate from exact future publication-head CI.
No new human/AI semantic reviewer covered this module. The broader goal
remains active; no full classification, novelty, optimality, merge or Tao post.
