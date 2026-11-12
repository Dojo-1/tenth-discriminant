# Phase287-C — preregistered exact discrete gauge-holonomy replay

Registered 12 Nov 2026 **after** the focused Phase287 coupled-theta result and prior to Phase287-C implementation. This is a separate exact rational *discrete path-overlap* control inspired by the paper-level holonomy calculation, not a blind prospective prediction from Phase287's first protocol.

Keep H_(kappa,phi), the original full-order finite theta, the 400-row trace-Gram boundary and the existing source/code frozen. At angles phi_i=i*pi/2, i=0..4 (with phi_4=2*pi), let R_i be the corresponding integer 2x2 quadrant rotations and
`F_i=1/sqrt(2) [I2; R_i^T]`.
The 2x2 overlap **from old-band coordinates to new-band coordinates** is
`C_i = F_(i+1)^T F_i = (I2+R_(i+1) R_i^T)/2=(I2+J)/2`, `J=[[0,-1],[1,0]]`.

Exact rational predictions:

- Each `C_i^T C_i=I2/2`; its polar-orthogonal factor is `(I2+J)/sqrt2 = R_(pi/4)`.
- Ordered transport `C_3 C_2 C_1 C_0 = ((I2+J)/2)^4 = -I2/4`. Dividing by the positive polar amplitude `(1/sqrt2)^4=1/4` gives normalized closed-loop holonomy `-I2`, agreeing with `exp(pi J)` from the continuous connection.
- Under a **second periodic moving frame** `V_i=R_(m phi_i)`, m in {0,1,2,3}, the transported overlap is `C'_i = V_(i+1)^T C_i V_i`; the entire ordered product equals `V_4^T (C_3...C_0) V_0=-I2/4` because `V_4=V_0=I`. This is an explicit moving-moving gauge-covariance test, rather than an unchanged static frame.
- Negative: A nonclosed single C_i is a strict contraction and cannot be called a closed-loop holonomy. The misleading `V(phi)=R_(phi/2)` is **not periodic** (V_4=-V_0), so it cannot be used to gauge away the -I2 loop factor without including the endpoint transition.

Implement with standard-library `Fraction` and exact integer quadrant rotations, independent of the D19/D403 pairwise test. Require all four frames and at least four secondary windings, exact polar scale and normalized -I2. Do NOT claim a general non-Abelian holonomy group (all present 2x2 rotations commute), physical adiabatic evolution or class-number arithmetic.

If any equality fails, stop and report the failure, do not rewrite the prediction to match output. CI and merge gates remain exact-head focused/Markdown/root Lean plus honest paper/source review.
