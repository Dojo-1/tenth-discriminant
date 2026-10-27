# Phase77: actual basis completion and coefficient transport

Registration `8dc321c` precedes source/execution on `cc6bd85`. This uses
Mathlib Matrix.toLinearEquiv/Basis.map rather than the hand-built
coordinate equivalence in stopped75. That failed source remains frozen;
accepted76 is not re-executed or silently imported in this cycle.

`BasisCompletion.primitive_completion` constructs an actual rank-two
integer-module basis with first vector equal to the supplied actual
primitive element. `actual_form_of_primitive_bound` applies this to an
actual nonzero ideal in the odd squarefree maximal-order chart. From
coordinate gcd1 and actual norm magnitude<=N(J)^2 it constructs that
basis, integer FormData with a>0 and discriminant D, and proves a<=N(J).
No form, leading bound or basis completion is a caller premise.

Exactly two invocations from the repository root:

```powershell
& research/ender_radius_bridge/run_phase77.ps1 build
```

FAIL30.4289926seconds: local abbreviations hid the gcd rewrite in Bezout;
canonical integer zsmul and the module scalar action were not definitionally
equal. PASS35.0070539seconds: expose the gcd coordinates and normalize
with int_smul_eq_zsmul. All six public theorem types are unchanged. The
entire actual norm/coefficient proof, controls and reporting are identical.
Total65.4360465seconds. No heartbeat/time/memory stop or limit increase.
No third invocation after acceptance.

The final run prints all6public types, complete FormData, two root axiom
lists and namespace audit6logical/6theorem/0runtime, standard three axioms
only. Four controls check an actual basis starting with(2,3), zero and
nonprimitive(4,6) guards, and an existing first basis vector. The failed
first source and its sorryAx audit rejection remain in the8-file raw ZIP.

Saved-evidence check, without executing Lean:

```powershell
python research/ender_radius_bridge/verify_phase77_results.py
```

It verifies registration and runner, all source/result/raw hashes,
unchanged statements and norm/coefficient proof, budget, final printed
audit/axioms, and unchanged stopped75/accepted76/production/README.
Saved integrity is distinct from semantic review or production CI.

This closes the basis/coefficient interface with the exact inputs supplied
by76. The actual class-family composition with76 remains a separate check;
none of these standalone additions is covered by PR35 production CI.
Class-wide B, even chart, field transport and new range remain open.
No merge/reviewer/publication/upstream/Tao claim.
[Human proof](BASIS_COMPLETION_GUIDE.md).
