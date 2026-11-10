# Phase269: bounded inertness sieve at the 321^4 cutoff

**Date:** 2026-11-10. **Status:** exact two-implementation computation (M); arithmetic-to-Lean certificate not discharged (H).

This is NOT a new unconditional imaginary-quadratic class-number-one classification. In fact, mainline already provides the stronger \`FieldClassification.field_classNumber_one_iff\` by an earlier, different large-cutoff and exact bitset route. It is also NOT independent verification of the original Gram/analytic derivation in PR #157.

## Mathematical input (class-number-one conditional)

If \(-d\) is a negative fundamental discriminant, \(d>163\), and its quadratic field has class number one, then:

- \(d\equiv3\pmod8\) (the prime 2 must be inert; d cannot be even);
- each rational prime \(p<d/4\) is inert; equivalently \(-d\bmod p\) is a **nonzero quadratic nonsquare**.

The strict inequality is essential. If p is split or ramified, class number one supplies an algebraic integer of norm p, contrary to the imaginary quadratic norm-form bound \(N(\alpha)\ge d/4\) for non-rational integers (rational norms are squares). Mainline's \`ClassNumberInertBridge\` and \`FiniteSieveBridge\` already formalize the relevant field-to-local implication.

## Exact computation and coverage

For the large interval \(163<d<321^4=10,617,447,681\), enumerate all
\(d\equiv3\pmod8\) satisfying nonzero nonsquare conditions at \(3,5,7,11,13,17,19\).
The wheel period is \(W=8\cdot3\cdot5\cdot7\cdot11\cdot13\cdot17\cdot19=38,798,760\),
with 12,960 permitted residues. Every \(d\) in the stated interval
satisfying the initial necessary conditions occurs uniquely as \(r+kW\)
with \(0\le r<W\) and a nonnegative integer k.
This is a larger search domain than fundamental discriminants; neither
squarefreeness nor primality is assumed in the computation.

Exactly 3,546,560 integers remain before the additional tests. Apply the
strict guarded nonresidue test to \(p=23,29,\ldots,109\) (all intervening primes).
The two independent enumerations agree on the survivor counts:

\`\`\`text
p:         23       29      31      37     41     43     47     53     59     61
remaining: 1696178  818872  396251  192895  94091  45960  22255  10671   5062   2437

p:         67    71   73   79   83   89   97  101  103  107  109
remaining: 1178  578  281  132   74   29   16    9    6    2    0
\`\`\`

At p=107 only d=585811843 and d=1764959683 remain; p=109 eliminates
both, witnessed respectively by \(41^2+d\equiv0\pmod{109}\) and
\(6^2+d\equiv0\pmod{109}\). At d=163, prime 41 does have a
root, but is intentionally NOT a required prime (\(4\cdot41>163\)).

### Reproduction

\`\`\`sh
g++ -O3 -std=c++17 -Wall -Wextra tools/finite321_inert_sieve.cpp -o /tmp/finite321
/tmp/finite321
python -m pip install numpy
python tools/finite321_inert_sieve_numpy.py
\`\`\`

Both terminate with PASS and assert all stage counts. The C++ implementation
needs only the C++17 standard library; the NumPy program enumerates by
different loop ordering. They are still correlated algorithmic witnesses,
not independent human mathematical review or formal proof.

## Lean boundary

\`lean/TenthDiscriminant/Phase269Finite321Bridge.lean\` provides the
sound **conditional** transport:

\`\`\`lean
hfinite : ∀ d, 163 < d → d < 321^4 → d % 8 = 3 →
   guardedPrimeTests d finite321Primes = false
\`\`\`

plus the implication that such a certificate excludes class number one.
It does **not** furnish hfinite, call the C++/NumPy programs from Lean, or
silently import the existing classification.

The smallest remaining proof task is a bounded, Lean-checkable CRT
bitset/quotient certificate for hfinite, with a full wheel-coverage and
interval-endpoint proof, using the existing \`ResidueMaskBridge\` and
\`QuotientFiberBridge\` machinery. If a source/primality/endpoint
translation fails, demote this proposal instead of closing the gate.

**Merge gate:** do not claim formally closed finite proof, independent
classification, or new cutoff from this draft alone. Keep independent
semantic review #50 and Phase268 exact-head CI separate.
