# Phase78: one controlled actual ideal basis and count per class

Registered22ee09b before production changes on72035ba. Accepted73/76/77
are transported to PrincipalBasis/LeastNorm/BasisCompletion with ONLY
first-import replacement by IdealCoordinates+AxiomAudit. Every other
body/type/control/print is identical. Failed69/75 remain frozen, unimported
and unreplayed; unused74 remains its separate standalone record.

`ControlledClassCount.controlled_class_basis` assumes actual class number
at most two for the squarefree odd-chart quadratic field. For each actual
class C it constructs a bounded nonzero ideal J with mk0J=C and an actual
basis/FormData with0<a<=N(J). No ideal, basis, minimal/primitive vector,
norm bound, form or coefficient bound is a caller premise.

`controlled_class_form_and_count` keeps the SAME J/e/FormData, lifts EVERY
ideal I of classC to NormLift I J, and for ALL natural t and finite actual
U:J with norm magnitude<=N(J)*t and nonzero second coordinate proves

    cardU<=2*pi*t/sqrtD+4*sqrt(M(K)*t/D).

It derives a<=M(K) from actual a<=N(J)<=M(K). The off-axis guard is retained;
this is not yet aggregate split-prime B or a new numerical range.

Commands from the repository root, each invoked once:

```powershell
& research/ender_radius_bridge/run_phase78.ps1 build
& research/ender_radius_bridge/run_phase78.ps1 root
& research/ender_radius_bridge/run_phase78.ps1 input
& research/ender_radius_bridge/run_phase78.ps1 audit
```

All first-attempt PASS: target93.9790186seconds, root24.8548143,
input32.7270587, audit32.1214912. No repair, extra probe, default-heartbeat
increase, time/memory stop or old numerical/regression campaign replay.
New namespace6/6/0; transported namespaces15/13/0,12/12/0,6/6/0 as before.
Whole-library audit5002logical/4233theorem/16993runtime auxiliaries excluded,
standard three axioms. Structural coverage179modules, no source escapes.
The unchanged verify_sources.py still matches250endpoint pairs; that check
does not validate Arb inequalities.

Input closures54328 and54613 exclude exactly the same34 listed older
h1/cutoff/classification/finite-answer roots as72, with no unsafe or
unresolved declarations and standard axioms only. This is scoped input
provenance, not an unrestricted independence or novelty theorem.

All37rawfiles (four sets of six source snapshots/stdout/stderr/result,
plus source checks) are losslessly archived. Saved-evidence command:

```powershell
python research/ender_radius_bridge/verify_phase78_results.py
```

It checks registration, transport, root imports, exact production/raw/source
hashes, four first-attempt results, input/audit markers and preserved earlier
source/protocol/runner/raw/results/verifier bytes. It does not invoke Lean.
Older fixed-root verifiers are historical at their original refs after these
four imports; their manifests/code are unchanged and are not weakened.

Only four new modules/root imports change production math. Original Gram,
ordinary derivatives, radii, old proofs, tools, certificates, pins and CI gates
are unchanged. README stays61lines with its verification pointer refreshed.
No external exact-head CI/security/full-regression success is inferred from
local build/input/audit. PR35's older exact CI is a separate result.

The PR35 final audit comment was auto-review rejected for public metadata
disclosure; explicit authorization remains pending. No publication workaround,
new PR, merge, reviewer or Tao posting. Axis accounting/class aggregation,
usable B, even/field transport, new cutoff, independent human review and
Mathlib acceptance remain open. No full-classification announcement.
[Human proof](CONTROLLED_CLASS_GUIDE.md).
