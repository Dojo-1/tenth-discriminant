# Phase355 — 302⁴ scalar overlap gate, source-semantics explicitly OUT OF SCOPE

19 November 2026. **Pre-registered before Lean implementation.**

## Exact question

Can the unchanged Phase343 / Phase348 joint-lower scalar formula exceed the
unchanged Phase347 upper scalar formula uniformly for D>=302^4, without
replacing the original source Gram or inventing arithmetic factors?

Let R=floor(D/4), and define

  U(D)=(4/5)*log(D)-1923/2000,

  L(D)=(999997/1000000)*log(D)-57193/10000
       +log(2)/4
       +(4659/625000-16895455/(625000*D))
       +(6931/1000000-2/R)
       +(873747/250000000-40/R).

All constants are copied EXACTLY from Phase343Scalar307 and
Phase348JointLower307; changing any is forbidden.

## Prediction and rational instrument

1. Mathlib's pre-existing rational-series `checkPositiveLogBounds`
   with N=5, x=302, k=8 certifies
   `571/100<=log(302)<=572/100` exactly.
2. Monotonicity of log yields `22840/1000<=log(D)` for D>=302^4.
3. The pre-existing `log_two_rational_control` yields
   `6931/10000<=log(2)`.
4. Exact D>=302^4=8318169616, R>=100000000 imply
   `16895455/(625000*D)<=1/100000` and
   `42/R<=1/1000000`.
5. The resulting conservative **strict positive** rational margin is
   `318967/250000000 = 0.001275868`.

The Phase351 independent decimal diagnostic at D=302^4 is 0.001640248469.

## Mandatory negative controls

- The analogous `D=301^4` formula gap is NEGATIVE in Phase351's high-precision
  bounded oracle. No 301-domain theorem may be claimed from the same constants.
- The symbolic 302 scalar theorem must remain independent of any source
  determinant, prime or class-number assumptions.
- Even if scalar interval is empty, the actual 302-domain upper and lower
  inequalities for the SAME original positive ordinary-Z trace Gram must
  be established independently. This PR does NOT prove them.

## Evidence governance

H until fresh exact-head Lean and full-root transitive-axiom checks pass.
P relative to encoding if they pass. Phase350 307^4 field proof stays separate.
Independent number-theoretic semantic review issue #50 remains open.
