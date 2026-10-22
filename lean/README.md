# Lean formalization — partial, build status pending

This is a new formalization layer, not a completed proof of the tenth-discriminant claim.
At base commit 6ac874fb9e7b9f282a5a1f7a64638668bba5c91d the repository had no Lean files or Lake project.

Lean 4.19.0 and Mathlib commit c44e0c8ee63ca166450922a373c7409c5d26b00b are pinned deliberately; no claim to the newest toolchain is made.

## Current scope

* `Arithmetic`: principal-form lower bound, strict cutoff, exact valuation-weight endpoint regressions and the finite sum-of-minima identity.
* `Radial`: weighted-moment correlation core and 9/25 two-row scalar bound, derivative-multiplier inequality and normalized pair-gain ceiling.
* `Coverage`: a sound exact interval-stitching checker and negative controls; it does not certify Arb values.
* `Envelope`: positivity propagation with explicit antitonicity and endpoint assumptions; it does not discharge those assumptions for Ender.

## Not yet formalized

The connection to actual quadratic fields, discriminants and class groups; small-prime inertness; the derivative Gram construction and its integrality, nonvanishing and inert-prime divisibility; ellipse counts and interpolation; the complete factorial/Legendre prime-mass inequality; conversion of Arb records to kernel-checkable inequalities; the full CRT sieve and reduced-form/class-group correspondence; the all-D analytic envelope with its instantiated constants; the derivative-row/moment bridge and full Fischer product.

These are obligations, not assumed axioms or hidden theorem parameters. In particular there is no Lean theorem here asserting that class number one implies D <= 163.

## Run

```sh
lake update
lake exe cache get
lake build
python3 audit.py
```

Build success is necessary, not sufficient: compare each declaration's hypotheses and conclusion with its source ledger. No self-authored proof/test pair is called independent mathematical review.
