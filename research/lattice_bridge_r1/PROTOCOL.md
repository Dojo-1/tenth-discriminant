# Registered bridge attempt — integer ellipse to the trace-Gram theorem

Registered on 23 October 2026 before editing the Lean proof or running a new
bridge test. Base: merged `main` at `9f713b8`. Scope is one formal bridge.

## Target

Use the existing `latticePoint` map and `rectangularTraceGram` matrix. For
positive natural `D` and natural integer radius `rho`, define the finite set
of integer pairs satisfying `x² + D y² ≤ rho²`, and its image in `Complex`.

Prove in Lean:

1. The complex coordinate map is injective for `D > 0`; this must include
   negative integer coordinates and the origin.
2. The finite set exactly describes the stated norm ellipse, not just a
   truncated sampling subset. Its complex image has the same cardinality.
3. A point-count hypothesis on this *actual set*, together with the existing
   derivative-depth hypotheses, yields positivity and Hadamard's upper bound
   for the repository's original rectangular trace-Gram matrix.

A conditional numerical guard is acceptable here. Do not assume Gram
positivity, jet injectivity, or the target conclusion. Do not modify Ender,
its certificates, or the older interpolation proof.

## Controls and stop rule

Compile the new module with pinned Lean 4.19.0 / Mathlib
`c44e0c8ee63ca166450922a373c7409c5d26b00b`, run the compiled axiom audit
and inherited negative controls, and instantiate one small ellipse as a
boundary control if feasible. A type error or timeout is a failed attempt,
not a passed proof. Preserve the exact obstacle if the proof cannot be closed
within this bounded slice.

This target does not derive Ender's analytic lower point-count estimate,
prove its chosen radius meets the guard for every `D`, establish integer
matrix correspondence or prime divisibility, or classify class-number-one
fields. A successful result closes the construction and formal application
interface only.

## Local execution and negative record (23 October 2026)

Pinned Lean 4.19.0 and Mathlib revision above were installed by `lake update`.
`lake env lean TenthDiscriminant/LatticeEllipse.lean` and `lake build` passed.
`python verify_sources.py` passed its endpoint-identity check, which is not an
Arb inequality check. The `D=rho=1` five-point boundary control is checked by
Lean in the new module.

The first local attempt ran `python audit.py` and
`python negative_controls.py` concurrently on Windows. The compiled axiom
scan reported `AUDIT_OK` with only the three permitted axioms, but the audit
wrapper exited 1 when its apparatus-control subprocess exceeded 240 seconds.
The negative suite's completed probes rejected false claims as expected, but
its jet-control subprocess exceeded its 120-second wrapper limit; it too
exited 1. These are **failed full-suite runs**. A sequential retry and pinned
CI must be reported separately, without rewriting this record.
