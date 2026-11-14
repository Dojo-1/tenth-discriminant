# Phase287-D — preregistered *dynamical* adiabatic leakage control

Registered 12 November 2026 AFTER Phase287 coupled-theta success and Phase287-C exact four-step geometric transport success, but BEFORE implementing the new finite-dimensional dynamical control. This is an AI-assisted derivation based on solvable two-level dynamics, not a theorem about the original trace Gram or physical quantum tunnelling.

## Specify an actual dynamical equation rather than using "adiabatic" loosely

Take the preexisting four-real-dimensional symmetric matrix
`H_(kappa,phi)=[[I2,kappa R_phi],[kappa R_phi^T,I2]]` with kappa>0. Complexify its 4-dimensional carrier for the **separate** toy Schrödinger evolution

`i*epsilon*dpsi/ds = H_(kappa,phi(s))*psi`, `phi(s)=Omega*s`, `s in [0,1]`.

This is a *chosen mathematical dynamics* on C⁴, not the original arithmetic sampling operator, and not an identified physical Hamiltonian. Let `W_phi=diag(I2,R_phi^T)`; then `H_phi=W_phi H_0 W_phi^T`. Setting `psi=W_phi chi` gives

`i*epsilon*dchi/ds=H_eff*chi`,
`H_eff=H_0 - i*epsilon*W_phi^T*dW_phi/ds
       =H_0 + i*epsilon*Omega*diag(0_2,J)`,
where J=[[0,-1],[1,0]].

J is real skew and has complex eigenvalues +/-i. In each helicity sector, iJ acts by a sign h in {+1,-1}; hence the two 2x2 EFFECTIVE Hermitian blocks are

`H_eff,h=[[1,kappa],[kappa,1+h*delta]]` with `delta=epsilon*Omega`.

Subtract the scalar center `(1+h delta/2)I` to obtain
`K_h=[[-h delta/2,kappa],[kappa,h delta/2]]`.
The exact identities
`K_h²=(kappa²+delta²/4)*I`,
`| <- | K_h | + > |²=delta²/4`,
where |+>,|->=(1, +/-1)/sqrt2 are the initial H0 band states, imply

`P_(+->-)(s)= [delta²/(4*kappa²+delta²)]
                 * sin²(s*sqrt(kappa²+delta²/4)/epsilon)`
for either helicity, with the SAME bound for any initial superposition in the + band:

`0<=P_leak(s)<=delta²/(4*kappa²+delta²)`.

For a complete phi-loop in s in [0,1], Omega=2*pi, this gives
`P_leak <= (pi*epsilon)²/(kappa²+(pi*epsilon)²)`.
Thus when kappa stays bounded away from zero and epsilon->0, the band leakage is O(epsilon²) for this **specified** constant-speed four-dimensional dynamics. Do NOT assert the same estimate for arbitrary time-dependent gaps or matrices.

## Fixed exact rational test before CI

Set `kappa=1/3`, `epsilon=1/12`, `Omega=1`, so delta=1/12 and the path is NOT a full circle. Freeze exact:

`L²=kappa²+delta²/4=65/576`,
`delta²/(4*kappa²+delta²)=1/65`.

A separate Python `Fraction` matrix oracle must:
- construct 4x4 real H_phi and moving W_phi at all FOUR quadrant rotations; verify H_phi=W H0 W^T;
- construct exact Wdot and W^T Wdot=diag(0,-Omega J) in every quadrant;
- form each h=+/- 2x2 K_h and check K_h²=(65/576)I and the + to - matrix element squared delta²/4, hence exact leakage upper 1/65;
- check delta=0 yields zero transition, while kappa=0 kills the **adiabatic band gap** and may NOT be promoted to an adiabatic theorem;
- separately preserve the original geometric holonomy -I2 and the distinction that the full-loop physical evolution contains dynamic phases and possible finite-speed leakage.

Use only fractions.Fraction, no numerical sine approximations or floating-point diagonalization. A completed exact algebraic CI test supports this bounded toy dynamics at [M]/[P-paper] but does not verify an experimental physical system or establish quantum tunnelling or a stronger tenth-discriminant bound. Treat root Lean, Markdown and all focused tests as merge gates. Failure of any frozen equality invalidates the dynamical result: do not silently alter parameters to pass.
