# Phase71: efficient arbitrary-basis arithmetic helper

**Current development:** [Phase72](PHASE72_VERIFICATION.md) now completes
the odd-chart actual basis/form/count bridge through separately registered
helper/composition proofs. Phase69 stays its original stopped failure;
Phase71 stays its original accepted helper. Their source/raw/verifiers
remain frozen; use the Phase72 verifier for the new integrated tree.

**Standalone helper PASS, not yet the complete coordinate/count bridge.**
Protocol981cbf9 precedes source and execution. A genuinely new decomposition
keeps the arbitrary basis as a parameter and proves the2x2 index and small
symbolic discriminant identities separately; it never unfolds a chosen
Smith basis. Phase69 remains a frozen stopped failure and was not rerun.

Two invocations: FAIL36.525770099999995s, PASS41.0094304s; literal total
77.535200499999995s. The first failed only on explicit integer algebra-map
normalization and absolute-square normalization. Repair preserves all14
public types,3 definitions and5 controls. No resource stop, heartbeat
increase, third invocation, separate probe or older campaign rerun.

For every given integral basis of an actual nonzero ideal J in the odd
maximal-order chart, the accepted helper proves integer coefficients a,b,c,
a>0,4ac-b^2=D, and actual Norm(combine e x y)=N(J)*(ax^2+bxy+cy^2).
It assumes no determinant/divisibility/form/discriminant identity. The
actual basis-index theorem and ideal-norm divisibility prove them.

The complete main type, actual ring combination definition and axiom list
are printed. Namespace audit23 logical/20 theorem/5 runtime declarations
allows only propext,Classical.choice,Quot.sound. Controls cover actual D=7
ambient and sheared norms/discriminant, proper ideal(2) norm4, scalar norm
scaling, and the counterexample to dropping positivity of a.

From the repository root, the runner was invoked twice:

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File research/ender_radius_bridge/run_phase71.ps1 -Mode build
python research/ender_radius_bridge/verify_phase71_results.py
```

The last command checks saved integrity without executing Lean. Exact
arguments, hashes, resources and all8 raw attempt files are preserved in
PHASE71_RESULTS.json and PHASE71_RAW.zip. The final source matches the
accepted snapshot; all older source/raw evidence and production are unchanged.

The arbitrary basis is an explicit helper argument. Actual basis construction,
coordinate/cardinality preservation, geometric count composition, uniform
leading coefficient, even chart and arithmetic B remain open in this cycle.
No new cutoff/classification/novelty/review/upstream claim. PR34's separate
production CI does not contain this standalone file.
