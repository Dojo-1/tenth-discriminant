# What the proof uses—and what it does not borrow

This is an internal source-provenance audit of proof head
`ebf14c2564102ef54139024ce9f9c46228307692`, not independent peer review.
It changes no mathematical statement or proof. Start with the
[one-page mathematical argument](CLASSIFICATION_GUIDE.md) for the theorem itself.

## The question an axiom audit cannot answer

A proof can use only standard axioms and still borrow a known classification
theorem. That would not meet the challenge of deriving a bound without
Heegner's methods. So we inspected reached proof inputs, not just imports.

The auditor reuses Lean4.19's `CollectAxioms` traversal, including declaration
types and definition/theorem/opaque bodies. It inventories every reached
constant, source module, declaration kind and safety flag. No unresolved
constant or unsafe declaration was found. The complete inventory is archived,
not replaced by a keyword search. All four component closures are subsets
of the final theorem's closure.

| Root of the inventory | Reached constants | Relevant separation |
|---|---:|---|
| Odd large-discriminant exclusion | 55,435 | Does not reach the final classification, nine-positive theorem or full finite certificate. |
| Combined radicand cutoff | 55,568 | Does not reach those results or the million-sieve module. |
| Complete finite certificate | 699 | Does not reach `NumberField.classNumber` or any Mathlib number-theory module. |
| All nine positive cases | 54,971 | Does not reach the finite certificate or million-sieve module. |
| Final canonical-field iff | 61,044 | Joins the positive cases, cutoff and finite computation. |

These are dependency counts, not measures of mathematical difficulty or
claims of independent methods/models. The separation matters: the cutoff
is not proved by assuming the finite answer; the positive cases are not
proved merely by passing a necessary sieve.

## The class-number inputs actually inspected

The final closure reaches147 declarations in five Mathlib class-number/
class-group source files, including compiler-generated proof auxiliaries.
Their actual source bodies were inspected at pinned Mathlib
`c44e0c8ee63ca166450922a373c7409c5d26b00b`:

- `NumberTheory/NumberField/ClassNumber`: actual class-number definition,
  its PID equivalence, a small ideal in each class, and the small-discriminant
  PID criterion. The small-ideal result comes from the geometric norm bound
  in `NumberField/Discriminant/Basic`, not a classification table.
- `NumberTheory/ClassNumber/Finite`: class-group finiteness for integral
  closures, using norm bounds, approximation and a finite family of ideals.
- `NumberTheory/ClassNumber/AdmissibleAbs` and `AdmissibleAbsoluteValue`:
  integer remainder partitions and pigeonhole approximation.
- `RingTheory/ClassGroup`: fractional ideals modulo principal ideals,
  integral representatives, and equivalence between a trivial group and PID.

Exact generic input signatures were also checked separately. In particular,
`NumberField.classNumber.eq_1` is **the definition's first equation**:
class number equals the cardinality of the ideal class group. It is not a
pre-existing assertion that a field has class number one.

No pre-existing class-number-one classification input was identified in
this inventoried and inspected frontier. The complete reached number-theory
module list is recorded in [the inventory summary](PHASE38_INVENTORY.json).
This finding is stronger than an import/name grep, but it is not a claim
that every one of61044 constants received independent semantic review.
General analysis—including gamma-function machinery—does occur in the
transitive library foundations; no claim of a minimal elementary dependency
set is made.

## Controls, failure and reproduction

All three traversal controls passed: an unused simulated forbidden input
was absent from a clean proof; a private relay exposed an opaque input;
a dependency present only in a theorem's statement was retained.
The fixed five-root run passed in98.3112308 seconds, peak3305865216 bytes,
within180 seconds/8192MB. There was no resource retry or theorem change.

The first discovery filter falsely matched `LFunction` inside
`SpecialFunctions`. Its original output survives in `PHASE38_DISCOVERY_V1.zip`.
The corrected token-prefix filter has explicit positive/negative controls.
Zero discovery flags are not, by themselves, a semantic verdict.

The36,786,783-byte raw output is stored losslessly in `PHASE38_RAW.zip`.
[Archive metadata](PHASE38_ARCHIVES.json) gives verified SHA256 and recovery;
only its recoverable unpacked duplicate was removed. Reproduce the summary:

```text
python research/ender_radius_bridge/collect_phase38_provenance.py PHASE38_CHECK_20261025011708695.result.json
```

The collector reads the archive directly and verifies its raw hash. The
[registered protocol](PHASE38_PROTOCOL.md) and [source fingerprints](PHASE38_SOURCE_REVIEW.json)
preserve scope. This is a local frozen audit, not a new permanent CI gate.
Published exact-head CI verifies the unchanged mathematical library and its
existing gates; it must not be described as executing this new local auditor.
Independent human review, upstream acceptance, analytic optimization,
systematic comparison and human-authored reporting remain open.
