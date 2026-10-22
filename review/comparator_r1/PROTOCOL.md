# Comparator round 1

Frozen target: main `791ebf4815d8eb4be5da3b01527ca7f0877b6d0e`.

No existing mathematical definitions, hypotheses, proof bodies, numerical bounds or saved certificates are changed. New concrete Lean controls are included in the root import so CI cannot silently omit them. This is a same-author round with prior exposure, not blind review or independent authorship.

The local protocol was written before executing the comparator. Seeds: 20261022 and 1792679188. The reference uses SymPy 1.14.0 formal differentiation, polynomial remainder, symbolic coefficient matrices, determinants and resultants. Targets are the actual pure Gram functions in `tools/verify_exact.py` and `lean/multiplicity_exact_controls.py`; their Git blob hashes are pinned. The old Arb/PARI verifier entrypoint is not executed by selecting its pure functions.

Predeclared attacks: lost trace normalization, missing conjugation, divided instead of ordinary derivatives, dropped derivative columns, rebuilding a smaller resultant after degree loss, Sylvester sign conventions, degree overpadding, exponent m instead of m-1, positive characteristic, repeated factors, complex-versus-real linear dependence, point ordering, translated roots and empty cases.

A mismatch with identical conventions is a failure and must be preserved. Setup errors do not count as mathematical rejection. Agreement supports only the tested finite cases, not universal equivalence, the proposed jet uniqueness criterion, or classification. The existing proof, tests and new reference share authorship. No separate human or model reviewer participated.

Stop at comparator findings and explicit regression controls; do not extend the proof or revise the cutoff. Lean status must be tied to a completed exact-revision build and transitive axiom audit. Any correction during this round must retain the initial failed result.
