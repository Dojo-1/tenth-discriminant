# E35 — THE SOURCE JET, NOT THE AMBIENT KERNEL, OWNS THE PRIME FACTOR

**19 November 2026.** Research-only continuation of E34 and the
E31 negative control. No field cutoff is changed.

## New exact proof target

The actual source still uses:

- integerRectangularTraceGram Q D J 2 1, with its original
  rectangular two-row monomials 1 and Z;
- integerDerivativeRow D r s j q, ordinary Z-derivatives holding
  the conjugate factor W fixed;
- integerPairTrace D a b = 2 (a₁b₁+D a₂b₂), with the original positive
  trace and its factor of 2;
- exactly the original finite Q, derivative index range, and integer
  pair carrier.

Define the original second-row jet certificate:

    ∀ j in range J, ∀ q in Q,
       p | (integerDerivativeRow D 1 0 j q).1
    ∧  p | (integerDerivativeRow D 1 0 j q).2.

Then every original trace-gram entry with one such row gains at least
one p factor and its self-pair gains two. Applying the already
separate E34 two-by-two determinant theorem yields

    p² | det(integerRectangularTraceGram Q D J 2 1).

This is a universal conditional theorem for arbitrary finite Q, D, J
and integer p, but **only for the original TWO-row rectangular case**.
The strong hypothesis must be proved from the actual source. It is
not a general extraction theorem for an arbitrary n-row matrix.

## Matched positive/negative source controls

At D=25, J=1, R=2, S=1, the E34 support

    Qfive={(0,0),(5,0)}

satisfies the new jet certificate and yields the exact original Gram
determinant 100, hence 25 divides the determinant.

The E31 support

    Qunit={(0,0),(1,0)}

does NOT satisfy the premise, and its original Gram determinant 4
is not divisible by 5. The supports have the same cardinality, and
the ambient conductor-five frame has the same noninjectivity in
either case. Only the actual source jets distinguish them.

## Cross-research significance

- E24–E33: conductor kernel, nilpotent source and Gaussian prime
  labels remain typed *ambient arithmetic structure*.
- HK-034: any trace-gram bridge MUST use the positive conjugated
  form, not HK's un-conjugated gpair.
- E34/E35: prime-power determinant factors require actual source
  data with verified integrality and compatible row operations.
- Phase350 307^4: a separately full-root-checked research field theorem,
  still awaiting independent human reconstruction; this tiny two-row
  source proves no new endpoint.
- The corrected complexity/SAT frontier is unchanged; no new ETH or
  P vs NP claim follows from arithmetic kernel structure.

## Release gate

Source: lean/TenthDiscriminant/E35OriginalJetRowCertificate.lean.
Root import: lean/TenthDiscriminant.lean.
Focused workflow: .github/workflows/e35-original-jet-row-certificate.yml.

Do not mark P until exact-head Lean build, all three permitted axioms,
negative controls and full-root source-audit checks pass.
Kill any result requiring altered Q, changed jets, altered positive
trace or an auxiliary selected minor.

## Follow-up

Generalize source jet-row extractions to the full n-row original
rectangular matrix using an integer unimodular row operator and
diagonal prime-power factors. Prove the factorization with unchanged
column support and original B, and compare the resulting det lower
bound against the certified analytic upper on the SAME original G.
