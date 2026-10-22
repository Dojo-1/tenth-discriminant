# Comparator round 1 - finite agreement, explicit boundaries

Target: main `791ebf4815d8eb4be5da3b01527ca7f0877b6d0e`. This round freezes existing definitions, proofs, numerical bounds and saved evidence. No global proof promotion or new cutoff.

## Executed locally

Python 3.13.5 / SymPy 1.14.0, exact rational arithmetic. Both compared source files are checked against current Git blob hashes before execution. Direct container GitHub access failed; connector reads and hash-verified local source copies were used instead. No local Lean runtime is available. The code does not import the old Arb/PARI entrypoint: it selects the original pure Gram functions by AST. These limitations must not be relabeled as full-entrypoint or blind verification.

- 102 actual production Gram matrices agree entry-for-entry with direct symbolic differentiation and quotient-ring specialization. There are 65 nonzero determinants (including empty controls), 37 zero determinants, 102 point-order checks and 102 real-translation checks.
- Seven planted production mutations are all caught: factor two (74 detections), conjugation (66), imaginary coordinate (66), D weight (53), ordinary versus divided derivatives (24), final derivative column (50), and truncation at j=r (74). These are finite detection counts, not exhaustive mutation coverage.
- 48 fresh fixed-size Sylvester families agree with symbolic determinants/resultants and the existing rational elimination/interpolation code, including 336 integer matrix evaluations and 96 held-out rational/integer evaluations. All 48 require a positive exponent and all determinants are nonzero; 24 lose leading degree and 23 attain exactly m-1.
- The inherited 48-case multiplicity campaign and its three reference formulas also pass. Only 22 inherited cases have positive-exponent obligations; those counts are not conflated.
- Normal and python -O executions produce byte-identical primary JSON outputs.

## Findings

**Input robustness:** `tools/verify_exact.py:vp(0,3)` never terminates. The actual selected function hit an externally imposed one-second timeout; source inspection identifies the invariant zero loop. Seven copies of the origin with D=7,R=3,S=2,J=8 pass the Python list-based guard (56>52) but have determinant zero. This input violates the mathematical finite-SET contract. Reject duplicate samples consistently and reject nonpositive determinants before logarithms/valuations in a separate correction. No saved legitimate case is thereby falsified.

**Critical next-theorem guard:** for F=Z^2-W, a=2 gives det=-4W, whereas overpadding to a=3 gives det=0. The existing local divisibility theorem permits a degree upper bound and remains correct. A NONZERO determinant theorem must use the exact global Z degree, then retain that size under specialization. Do not infer nonvanishing from local divisibility.

**Conventions:** for F=Z+W,G=Z+1,a=b=1, the fixed coefficient-map determinant is W-1 while the standard resultant is 1-W. General exact-degree comparison has sign (-1)^(a*b); the derivative application a*(a-1) is even. This is not a defect. Likewise complex translation can change a REAL Gram determinant: rows 1,Z give det=0 at {0} and det=4 at {i}. Real and complex coefficient independence must not be conflated.

**Historical M2:** after the primary campaign, a separately declared targeted control uses P={0,1,2},D=19,R=S=1,J=4. Its old sufficient independence guard holds (12>10), its actual G=[6], and the false bound det<=floor(product diagonal/10^6) demands 6<=0. M2 is now caught by this NEW witness; historical uncaught records are left intact.

## Lean regressions

ComparatorR1.lean and ComparatorM2.lean use actual definitions to record padding, degree loss, translated roots, Taylor coordinates, characteristic three, real/complex behavior and the M2 matrix. They are imported by the root library so existing CI and the transitive axiom audit include them. Compilation is pending for the initial branch commits; consult the exact completed workflow before calling these new examples checked. No existing mathematical definition or theorem body has changed.

## Independence and residual obligations

The reviewer has prior exposure and authored earlier work. Reference algorithms differ (symbolic differentiation/resultants versus integer pairs/rational elimination), but test selection and interpretation share authorship. This is not independent semantic or human peer review. No end-to-end classification theorem, global jet-uniqueness criterion, or Python/Lean semantic-equivalence theorem follows.

The next gate is the nonzero fixed derivative determinant and W-degree bound for a primitive irreducible mixed factor in characteristic zero with exact global Z degree. Retain padding, repeated-factor, positive-characteristic and degree-loss controls. Stop at that gate before global promotion.

## Reproduce from repository root

```sh
python -m pip install sympy==1.14.0
python review/comparator_r1/comparator.py --source-root . --output /tmp/tenth-comparator-r1
python -O review/comparator_r1/comparator.py --source-root . --output /tmp/tenth-comparator-r1-opt
python review/comparator_r1/historical_m2.py --source-root .
cd lean
lake build
python3 audit.py
python3 negative_controls.py
```

The Python campaign is an explicit manual command, not silently claimed to run in the existing Lean workflow. Its outputs include all sampled matrices/polynomials, coordinates, mutation counts and boundary witnesses. Full local evidence is retained in the accompanying conversation bundle.
