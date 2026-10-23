# Phase 14 preregistration: maximal-order coordinate criterion

Date: 2026-10-24. Base: draft PR #28 head `ca4bb0b`, open and
unmerged. This protocol precedes proof edits.

## Mathematical target

For positive squarefree `D ≡ 3 (mod 4)`, an algebraic integer in
`K=ℚ(√(-D))` should have unique coordinates

    x + y(1+√(-D))/2,   x,y ∈ ℤ.

The trace/norm route is: write `a+b√(-D)` with rational `a,b`.
Integrality makes `2a` and `a²+D b²` integers. Their discriminant
`(2a)²-4(a²+D b²)=-D(2b)²` is integral. Squarefreeness forces
`2b` integral. Modulo `4`, the norm condition forces `2a` and `2b`
to have the same parity, giving the displayed basis.

Attempt in Lean the central rational denominator lemma:

    Squarefree D, D*q² ∈ ℤ  ⟹  q ∈ ℤ.

Then prove the parity/coordinate reconstruction from integer trace,
integer norm and rational coordinates. If the pinned library permits,
attach the criterion to the actual quadratic number field and
maximal integer ring. The **full** target is that field-to-order
identification; a rational arithmetic lemma alone is only progress
toward it, not a replacement for it.

## Controls and stop rule

Use `D=15` as a positive squarefree/parity control and `D=9` as a
negative squarefree control: `9*(1/3)²=1` but `1/3∉ℤ`.
The `D=15,p=3` failure of unconditional principal norm lifting
remains unchanged. Do not infer class number one, inertness, cutoff
or classification from any coordinate lemma without a checked
maximal-order equivalence and the remaining geometric/analytic links.

If the field representation or rational denominator interface
requires a large new theory, stop after a bounded attempt, retain
the exact strongest checked lemma and log the missing theorem.
Run targeted Lean, full pinned build, source correspondence, compiled
dependency audit and negative controls on a proof head. Update the
human guide/current status; keep the PR draft and do not merge.
