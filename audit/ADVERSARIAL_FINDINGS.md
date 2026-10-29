# Adversarial findings

## Summary and severity

**Confirmed defects: none found.** This is not a claim that the proof is defect-free. The highest-ranked open concern is that the concrete integer trace-Gram factorization and the near-zero cutoff margin have not been independently replayed. The pinned Lean build and axiom audit remain incomplete.

| Rank | Status | Severity | Attempted falsification | Evidence and disposition |
|---:|---|---|---|---|
| 1 | Open concern | High | Challenge the step from local nonsquareness to \(p^{2F(p)}\) divisibility of the actual integer trace-Gram. | `GramDivisibility.lean` correctly requires matching row/column factors and an integral middle matrix; `RectangularBasisMatrix.lean`, `RectangularRowAction.lean`, `GramDivisibility.lean`, and `RectangularValuation.lean` construct the concrete route. `IntegerTraceGram.lean` connects integer and real Gram matrices. This is the central unclosed bridge: no independent full derivation or Lean replay. |
| 2 | Open concern | High | Perturb the normalized estimates, rounding, tail cutoff, or endpoint and see whether the 50-billion contradiction survives. | Source gives upper \(0.8\log D-0.813\), lower \(0.999997\log D-5.739\), and margin \(0.0000061088\) at \(\log D=24.6304\). The exact source composition was inspected; all estimates were not independently reconstructed and the project did not finish building. |
| 3 | Discharged by evidence, subject to replay | Medium | Replace the strict small-prime bound by a non-strict one; check ramified and split primes at the boundary. | The source requires \(p<(D+1)/4\), odd \(p\), squarefree \(D\equiv3\bmod4\), and class number one. At \(D=163,p=41\), \(-D\equiv1\bmod41\) has a root, and \(p\) is exactly the excluded endpoint. A root at a small ramified prime would likewise contradict the class-number-one norm argument. No boundary defect in the stated strict lemma was found. |
| 4 | Discharged by evidence, subject to replay | Medium | Seek a semantic weakening: class number of a nonmaximal order, or a theorem restricted to a chosen field model. | Mathlib's pinned definition uses the class group of \(\mathcal O_K\), and `classNumber_eq_one_iff` identifies it with a PID. Theorem A is chart-specific but covers every imaginary quadratic field through squarefree radicands. Theorem B explicitly constructs a squarefree chart from arbitrary totally complex degree-two `K` and transports the discriminant. |
| 5 | Discharged by measured checks; completeness still open | Medium | Look for a malformed modulus, wrong inverse, high-bit truncation, endpoint error, or nonexhaustive residues in the quotient sieve. | `audit/sieve_oracle.py` exactly reconstructs 200 arbitrary-precision masks and reports 92,964 deterministic affine-root comparisons passed. The Lean source includes wheel/interval quotient coverage and an 11-seed all-fibers proof. The actual Lean certificate was not compiled; random/deterministic sampling alone is not an exhaustive proof. |
| 6 | Inconclusive due to access | Medium | Check whether the project-wide proof depends on nonstandard axioms, `native_decide`, `sorry`, an external oracle, or an unvisited module. | `lean/AxiomAudit.lean` audits every project namespace constant and allows only three axioms; `lean/audit.py` checks module reachability and forbidden escapes before compiling the audit. Neither checker completed. No conclusion that the advertised axiom set is confirmed. |
| 7 | Inconclusive due to access | Low | Compare the mathematical architecture with previous formalizations; search for inherited lemmas or overclaimed novelty. | The inspected twinheterodox materials describe the same Green determinant/inert-prime route; Murphy has separate analytic and determinant routes. Olivier's artifact was not found. The current review does not substantiate a priority or novelty claim. |

## Persona-specific attempts

### Number theorist

Attempt: ramified primes may violate “inertness,” and the class-number hypothesis may not rule them out. The source's public lemma is narrower than that slogan: it proves nonsquareness from a root contradiction for odd \(p\) strictly below the norm threshold. The norm formula and positivity force \(p\ge(D+1)/4\) if the second coordinate is nonzero, while a zero second coordinate would make a prime a square. Thus the source is not asserting unconditional inertness at ramified primes; rather, class number one excludes any root in its guarded range. **Disposition: discharged by source inspection, proof replay pending.**

### Geometer

Attempt: a determinant bound may be inferred from a one-sided row/column divisibility, or an area argument may count axis points as full cells without justification. The generic determinant lemma explicitly shows why one-sided factors are insufficient and demands the two-sided pivot. The ellipse proof restricts the area-cell argument to off-axis points and includes a source-level counter-control for the naive all-points version. The remaining concern is whether the constructed Gram really meets the generic factorization hypotheses in every use. **Disposition: partial discharge; central bridge remains open.**

### Formal-methods specialist

Attempt: class number could be for an order rather than the maximal order; `IsTotallyComplex` could be too weak; the arbitrary-field theorem could secretly assume the canonical model; or a Boolean computation could be trusted externally. The pinned Mathlib source resolves the first two definitions. The arbitrary-field theorem has only the displayed hypotheses and applies an explicit representation/transport argument. The sieve certificate uses Lean Boolean definitions and `decide +kernel` source terms; no external executable is visible in the proof source. However, the actual terms and axiom closure have not been replayed. **Disposition: semantic mismatch not found; kernel evidence pending.**

### Numerical auditor

Attempt: corrupt a prime inverse, mask, shift, quotient endpoint, or root truth value. An independent Python implementation recomputed each of the 200 mask literals and directly tested 92,964 translated root conditions. It found no mismatch. Source lemmas supply quotient bounds, exact half-open intervals, no-phantom-bit bounds, and coverage from residue plus quotient. **Disposition: literals and samples discharged; full certificate incomplete.**

### Skeptical historian

Attempt: identify a claimed new proof architecture that is an implementation variant of an existing one. The twinheterodox source description already has the h=1 Green derivative determinant, inert/split-prime input, and finite sieve. Murphy's earlier analytic and elementary determinant efforts are also distinct prior routes. This is enough to reject an unqualified claim of a new mathematical obstruction, but not enough to assign priority or assess Olivier's work. **Disposition: novelty not established; no attribution defect confirmed.**

## Counterexample discipline

No counterexample to either frozen principal theorem or to a stated load-bearing lemma was found. The endpoint example \(D=163,p=41\) is a counterexample only to the stronger, *unstated* non-strict variant; it confirms why the formal strict guard matters. The \(D=15,p=3\) source control checks that the class-number-one premise is not silently discarded. Neither is a defect in the reviewed theorem.
