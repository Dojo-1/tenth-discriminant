# Phase57: exact staircase weight, no new cutoff

**Local PASS.** For natural R,S,p, p>0 and p*(S-1)<=R, Lean proves

    6*(valuationWeight R S p : Real)
      = S*(S-1)*(3*R-p*(S+1)).

The displayed right side uses real subtraction; the guard uses Nat
subtraction. The count remains the existing weight. The new clipped-column
recurrence and its exact sum explain the finite counting operator;
[human guide](STAIRCASE_EXACT_GUIDE.md). No new prime exponent or cutoff.

Protocol `a0765da675694d37f03bb8c789f9a7f797d1c189` fixed the target,
guards, three controls and caps before implementation. First target
PASS22.5869066s, no failed build, repair, second attempt or resource stop.
Root6820 PASS21.7516481s. Signature/generic-example/three-axiom-print and
boundary/coexistence checks PASS20.3948414s. The old false unguarded
quadratic-floor identity remains false atR8,S2,p2, while the new count
gives F=6 there. Dropping p>0 or the last-threshold guard is rejected.

Whole-project compiled audit PASS27.9744318s:4772 logical declarations,
4028 theorems,16971 runtime-only auxiliaries. Only `propext`,
`Classical.choice`, `Quot.sound` permitted.166 project modules are
reachable/acyclic, no source proof escapes. Source correspondence passes
250 endpoint pairs, checking identity only, not Arb inequalities.

The mathematical diff from21a1b88 contains only StaircaseExact.lean and
its root import. The50b proof, inherited definitions/statements/bodies,
production tools, pins, numerical tables and gates are unchanged. The
manifest seals four first-attempt terminal records, source/raw hashes and
the complete audit ZIP (exact readback before duplicate removal).

Phase56 source/raw evidence remains intact, with its root verified at
frozen21a1b88. Its raw records also match the committed Git-blob bytes,
not only the Windows working files. The first native Phase55 report's
Git and working bytes retain SHA256b8d659d555d8f2be460771ad03037f9cfbe8c7ed724004f4ed75b7ff1260c0da.
Older current-root verifiers are historical after the new root import;
the current verifier preserves their evidence without relabeling their
scope. Earlier reviews do not cover this lemma.

From repository root, pinned elan binaries on PATH:

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File research/ender_radius_bridge/run_phase57.ps1 -Mode build
powershell -NoProfile -ExecutionPolicy Bypass -File research/ender_radius_bridge/run_phase57.ps1 -Mode root
powershell -NoProfile -ExecutionPolicy Bypass -File research/ender_radius_bridge/run_phase57.ps1 -Mode input
powershell -NoProfile -ExecutionPolicy Bypass -File research/ender_radius_bridge/run_phase57.ps1 -Mode audit
python research/ender_radius_bridge/verify_phase57_results.py
git -c core.whitespace=blank-at-eol,blank-at-eof,space-before-tab,cr-at-eol diff --check
```

The saved target execution is not rerun to manufacture new timing. Source
correspondence was checked from `lean` with `python verify_sources.py`.
Integrity checks do not execute Lean or establish independent semantic
review. Exact-head publication CI remains separate. The current cutoff
stays50 billion; no novelty, optimality, measured speedup, higher-class-number,
classification, human review, merge or Tao-submission claim is added.
