# A positive scalar margin worth proving

The registered numerical test found a positive margin at D=2^50.
This is a candidate proof target, not a new class-number cutoff.

The checked odd-chart bridge bounds one original determinant above by
geometry plus two arithmetic costs: counted split primes and primes
dividing D. Divide everything by the existing positive scale R^2*S.
For the fixed family R=floor(D/4), S=floor(R/25), L=R, the existing
class-free scalar lower and upper envelopes leave

    0.199997*log(D) - 4.926.

The parameter-divisor payment is at most log(D)/25. The remaining
split-prime cost can be conservatively bounded by the candidate expression

    H(D) = (4/sqrt(D)+1/fourthRoot(D))*(2+u*(1+u)) + 1/3,
    u = log(D).

This replaces pi by simple safe bounds and log(3) by2, while keeping
the constant payment separate. The tested remaining margin is

    m(D) = 0.159997*log(D) - 4.926 - H(D).

The test evaluated exactly 18 preregistered powers of two, at 100 and 200 digits with
outward enclosures. It kept every negative sample. Both precisions agreed:

| Scalar sample | Enclosed margin, rounded here | Meaning |
|---|---:|---|
| 2^48 | -0.21520 | This conservative envelope does not separate here. |
| 2^50 | +0.07191 | First positive sample in the sealed grid. |
| 2^52 | +0.34423 | A further positive sample, not an all-D proof. |

There were 7 negative and 11 positive samples at each precision, none
unresolved. All eight controls passed at each precision, including a
mutation that omits the constant payment. The enclosures at 100 digits contain
those at 200 digits. These are deterministic numerical intervals,
not statistical confidence intervals or independent implementations.

No field was tested for class number two. Powers of two are scalar
arguments for this envelope; they are not the squarefree odd parameters
of the field theorem. Nothing here establishes a result between samples
or beyond the last sample, or the smallest possible endpoint.

The next proof must establish the conservative majorization in Lean,
control it for EVERY D beyond an endpoint, and compose the actual
prime-mass lower bound with the diagonal upper bound under all guards.
General-field/even-chart transport remains separate. The checked
class-number-one cutoff is still 50 billion.

[Execution and evidence](PHASE85_VERIFICATION.md) preserve the complete
grid, controls, source, negative results and the missing memory observation.
