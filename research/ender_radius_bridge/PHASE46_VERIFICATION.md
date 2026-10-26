# Phase46: the generator-to-field bridge

Protocol e3619c66 preceded all Lean edits. Fixed-control addendum bc2574c1
preceded its first input check. [Results](PHASE46_RESULTS.json) preserve
every terminal record and both failed source snapshots. The scope and
remaining normalization premise are in the [human guide](GENERATOR_BRIDGE_GUIDE.md).

The main module was accepted in24.5086311s on attempt2, after a69.393486s
failure caused solely by one extra explicit argument to liftHom_root.
Deleting that argument is the only main proof repair. Cumulative main
build cost93.9021171s; same600s/8192MB per-process cap, no resource stop,
parameter change, pilot or theorem weakening.

Full root PASS6811 steps in24.5555875s. All157 project modules reachable
and acyclic; no proof-source escapes. Source correspondence PASS250 saved
interval pairs; this checks endpoint identity, not Arb inequalities.

Fresh input attempt1 FAIL33.0731518s: public signatures and both input
closures passed, but the outside-library controls had an anonymous
instance-name collision, noncomputable field operations without their
context, and an unsimplified polynomial constant. The source and raw
failure survive. Explicit instance names, noncomputable section and
normalization of that constant repair elaboration only. Same witnesses
and statements; attempt2 PASS26.2956286s within180s/8192MB.

The public constructor takes a root equation and degree two, with no
isomorphism premise. The actual bounds additionally take squarefree d
and actual class number one of K. Fresh closures55578/55781 exclude the16
listed old-cutoff/finite-answer/fixed-ratio inputs. The new accepted100b
bounds are deliberately used, not excluded. Only the standard three
axioms; no unresolved or unsafe reached declaration.

Negative-root d19, native half-integral chart c5, and the fixed Q(i)
rescaling control all pass. The last proves why the radicand conclusion
cannot omit squarefreeness; it does not refute the actual-discriminant bound.
All controls remain outside the library and outside the transported proof
inputs. No complete classification theorem is used by the new bounds.

Full compiled namespace audit PASS29.3093956s:4614 logical declarations,
3878 theorems,16955 runtime-only auxiliaries excluded. Its raw2007231-byte
stdout is losslessly archived, with byte-identical recovery checked before
removing only the unpacked duplicate. Raw CRLF/BOM evidence is not reformatted.

Historical attempt/check commands from repository root:

```powershell
powershell -NoProfile -File research/ender_radius_bridge/run_phase46.ps1 -Mode build
powershell -NoProfile -File research/ender_radius_bridge/run_phase46.ps1 -Mode root
powershell -NoProfile -File research/ender_radius_bridge/run_phase46.ps1 -Mode input
powershell -NoProfile -File research/ender_radius_bridge/run_phase46.ps1 -Mode audit
python lean/verify_sources.py
python research/ender_radius_bridge/verify_phase46_results.py
```

Do not treat a reproduction as part of the recorded timings. No fresh full
local parent-apparatus/rejection replay is inferred from the compiled audit;
the unchanged pinned CI provides that separate publication gate. Prior
Phase43/45 source fingerprints belong to their historical roots and must
not be silently weakened to fit this new root import. Use the new Phase46
record verifier for the current root.

Baseline9f5bf6a passed CI40175210613/security40175208401/separate CodeQL,
with final record6398734105 posted before new work. New publication-head CI
remains separate. No old mathematical source, finite certificate, frozen
campaign, production tool, dependency pin or gate changes. The prior AI
review covered the underlying cutoff, not this new constructor. No
independent human review, unqualified full-classification, optimality,
novelty, merge or Tao post claim.
