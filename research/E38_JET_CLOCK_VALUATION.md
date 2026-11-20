# E38 — DERIVATIVE CLOCKS AND PRIME-POWER ROW FACTORS

*19 November 2026 · pre-registered finite exact-integer experiment. This is a
bounded arithmetic instrument, not a general theorem about number fields.*

## Object and original source (frozen)

Retain TenthDiscriminant.IntegerTraceGram's original ordinary
derivativeRow (holding W fixed), positive integer trace with factor
two, original finite support, and original rectangular row order.

The test family is deliberately narrow:
    D=25, S=1;
    p in {2,3,5};
    translation a in {-2,0,3};
    R in {2,3,4};
    J in {1,2,3};
    Q={(a+p*t,0): t=0,..,R-1}.

Precisely 81 cases. No hypercomplex interpretations, no source
resampling after results, no p-adic field completions.

## Prediction before inspecting results

The integral binomial basis change from Z^r to (Z-a)^r is a
lower-triangular U with unit diagonal (detU=1). At the actual
real source q=a+p*t, for original j-th ordinary Z derivative:

    derivative_j ((Z-a)^r)(q)
       = falling_factorial(r,j) * (p*t)^(r-j)
              when j<=r; zero otherwise.

For all original j in {0,..,J-1}, this forces
    e_r=max(0,r-J+1).
Thus every moved row has an original integer coefficient factor
p^e_r and, under the ACTUAL original positive Gram pairing,

    p^(2 sum_{r=0}^{R-1} e_r) divides det(G).

With K=max(0,R-J), the lower exponent is K*(K+1).

This is a specific theorem target, not a claim about arbitrary
non-real sources or arbitrary mixed Z,W ordinary jets.

## Independent bounded results (not a Lean theorem)

The separate pure-Python integer oracle in
research/oracles/e38_original_jet_clock_oracle.py passed all 81
frozen cases, using exact integer pair multiplication, powers,
ordinary derivatives, trace, and Bareiss determinant.
Each case checks:
- original entire Gram construction;
- integer lower-triangular U has determinant exactly 1;
- G' = U G U^T preserves its determinant;
- each transformed source jet (j,q,real/imag) has required p factor;
- original det valuation is at least 2 sum e;
- at J=1 the exact Vandermonde closed formula
      detG=2^R * p^(R*(R-1)) * product_{k=1}^{R-1} (k!)^2.

Exact same Q={(1,0),(6,0),(11,0)}, D=25,R=3:
    J=1: det G=500000, v5=6, lower=6
    J=2: det G=784400, v5=2, lower=2

Deeper jets reduce the *guaranteed source-extraction exponent* in
this particular real support; this is NOT a universal observed
monotone law for arbitrary source geometries.

## Predeclared negative controls and kill rules

- E36 fake V=diag(1,5) has det5 and is NOT a valid GL_2(Z)
  source row frame even if its terminal Gram equals that of U.
- E31 Qunit with ambient conductor kernel and detG=4 rejects
  kernel=>Gram prime divisibility without original source rows.
- If any source ordinary jet fails divisibility at the claimed
  exponent, kill the formula.
- If the original untransformed Gram determinant lacks the
  predicted p exponent, kill the formula.
- If any exact large source-to-field claim requires altered Q,
  nonunimodular U, modified derivatives/positive trace or a
  selected minor, reject that claim.

## Level and next proof

Evidence level M: finite arithmetic checks on 81 predetermined
instances. The elementary binomial derivative identity gives
a paper theorem candidate at H until formalized and reviewed.
CI for the Python script is separate from the heavy Lean root
build; a successful script is NOT Lean P.

Next candidate: a generic Lean source row-action theorem for
arbitrary R,J on real arithmetic progressions, linked to E37's
arbitrary-rank determinant certificate. The full thin-ellipse
Q with complex points and s>0 needs a new, explicit row
operator and arithmetic hypothesis. No 307^4 gain follows.
