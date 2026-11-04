# Post-registered T5: actual ordinary-jet integer trace Gram

Date 2026-11-04. **M (exact finite computation)**, not a general proof, and not part of the initial T1-T4 preregistration. Reproduce:

    python3 research/plural_moving_frames/original_source_small_pilot.py

This is deliberately closer to the project source than the arbitrary positive-definite 3x3 pilot: D=19, R=4, S=J=3, p=3, Q_rho={(x,y) in Z^2 : x^2+19y^2<=rho^2}. The ordinary Z derivative of Z^r W^s is evaluated at (Z,W)=(x+y sqrt(-19),x-y sqrt(-19)), with W fixed; each entry is summed with exactly the original trace pairing B_D((a,b),(c,d))=2(ac+19bd). No Hasse substitution, no surrogate Gram, no floating point.

The local Frobenius nonsquare condition is visible: -19 mod 3 = 2 is nonsquare. The original rectangular exponents for p=3 are e=1 at rows (3,0),(3,1), e=0 at the other ten rows, yielding tau_10=0, tau_11=1, tau_12=2. Thus the general algebraic partial-minor implication predicts 3^2 divides delta_11 and 3^4 divides delta_12=det, assuming the original row factorization.

Exact reproducible outcomes:

| Original radius | |Q| | dim G | det G positive | v3(delta_10) | v3(delta_11) | v3(det G) |
|---|---:|---:|---|---:|---:|---:|
| 5 | 21 | 12 | yes | 0 | 3 | 6 |
| 6 | 31 | 12 | yes | 2 | 5 | 8 |

This exceeds the predicted minima for k=11 and k=12 in both supports, while individual valuations change with the observation support. Both grami use the same ordinary derivative convention and original integer coordinates. The smaller support Q5 is included in Q6; PSD monotonicity holds from the sum-of-outer-products identity.

**Evidence boundaries:** This computation checks finite source fidelity and shows nontrivial partial-minor factors in a real original-jet model. It does not check the complete maximal-order class-number-one implication, any uniform D>=322^4 theorem, a k-minor Hadamard envelope, or an improved discriminant bound. General Cauchy–Binet determinantal-divisor transport remains P as an elementary mathematical derivation, but a *new Lean module* is still unproved.

**Next:** Give an exact integer proof of p^(2 tau_k) | delta_k(G) from the existing original Gram factorization, and compare with a same-source principal-minor upper. Do not claim a result beyond the current scalar certificate without a strict quantified gap.
