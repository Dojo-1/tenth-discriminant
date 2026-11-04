# T6 pre-execution amendment: correction to an overstrong preregistered claim

Date: 2026-11-04. This amendment is committed **after** T6 preregistration 55be9a07 and **before** any T6 code or run. It **does not edit** the original preregistration, which is preserved to expose the mistake.

**Retire item 4 as originally worded.** It predicted an *exact integer* Gram-product entry equal to -76 times the number of non-real nodes. That is false as a derivation: the identities Z^3=W, W^3=Z, derivative_1=0, derivative_2=0 hold **only after reduction modulo 3**, not over the integer quadratic order. The original f=Z^3 W^2+2W is not literally Z-W over Z[sqrt(-19)]. Therefore the trace identity is a congruence, not an equality of integers.

**Correct T6 test target:** for rho=5,6,7, compute the exact integer (0,1)-component of G(Q_rho)*v and assert that it is *congruent modulo 3* to -76*N_rho with N=(10,18,22), giving residues (2,0,2). Preserve the full integer values in output for auditing, without asserting their equality to the simplified modular expression.

This demonstrates a central information-loss lesson of Round201: a valid identity in a residue field must not be transported back to characteristic zero without a quantified p-adic remainder. The limitation is part of the research evidence and not a CI repair to be hidden.
