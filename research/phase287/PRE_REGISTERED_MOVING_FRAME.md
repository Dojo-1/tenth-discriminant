# Phase287 — preregistered symmetry-covariant, higher-dimensional moving-moving-frame lift

**Registered 12 Nov 2026 before the Phase287 executable experiment.** Prompt scope: preserve both symmetry and higher-dimensional constructs in a moving-moving frame with an *adiabatic* hypothesis. This is a **distinct exploratory mathematical model**, not a replacement for the original tenth-discriminant Gram or its proved/Lean-encoded field theorem. All proposed derivations and tests are AI-assisted, not independent human mathematical review. Standard Berry/Kato/Wilczek–Zee transport is prior art; the calculation below is a simple controlled instance and claims no novelty.

## Types and what moves

Let `K=Q(sqrt(-D))`, `D=19 or 403`, and `L=O_K=Z[(1+u)/2]` with u²=-D. Use the exact **index-two two-coset maximal order**, not merely Z[u]. Embed `z=x+y*u` as `v(z)=(x,sqrt(D)*y)` in R². The new CARRIER is `L direct_sum L` in R⁴, **not** the original source's 400-row trace Gram. The base parameter manifold is `B={(t,kappa,phi): t>0, 0<kappa<1, phi mod2pi}`, where t is Gaussian scale, kappa a coupling and phi the moving coupling direction.

Let `R_phi=[[cos(phi),-sin(phi)],[sin(phi),cos(phi)]]` and
`H_(kappa,phi)=[[I2,kappa*R_phi],[kappa*R_phi^T,I2]]`.
The coupled Gaussian for z,w in L is
`Q_(kappa,phi)(z,w)=[v(z);v(w)]^T H_(kappa,phi) [v(z);v(w)]`,
`Theta_(kappa,phi)(t)=sum_(z,w in L) exp(-t Q_(kappa,phi)(z,w))`.
The spectrum is `1+kappa` and `1-kappa`, each twice; hence Q is positive definite for |kappa|<1 and the two-band gap is `2*kappa` at kappa>0. At kappa=0 the Gaussian factorizes `Theta_0(t)=Theta_L(t)^2`; this is the matched tensor-product null control, not evidence for a novel higher-dimensional arithmetic mechanism. A coordinate rotation of v(z) is NOT generally an integral automorphism of L; phi moves the *analytic coupling kernel* while the arithmetic lattice stays fixed.

## Symmetry with correct domains

- Diagonal inversion `(z,w)->(-z,-w)` preserves Q for all phi, kappa. Noether C2 parity survives in the coupled source.
- Separate inversion `(z,w)->(-z,w)` maps kappa->-kappa, so the complete theta is an even function of kappa and its first derivative at kappa=0 vanishes.
- Factor swap `(z,w)->(w,z)` and simultaneous conjugation each map phi->-phi. They are **parameter-space equivariances**, not generally extra fixed-phi point stabilizers. When phi=0 or pi, they become fixed-parameter symmetries. Every listed transformation maps the actual full order lattice L² to itself.
- Real rotations R_phi do NOT act as integral source frame changes for generic phi. There is no claimed equality of Smith filtrations or class-number bounds.

## Moving eigenspace, connection and adiabatic gap [paper-level exact linear algebra]

For kappa>0 the + band projector and one orthonormal moving frame are

`P_+(phi)=(1/2)[[I2,R_phi],[R_phi^T,I2]]`,
`F_+(phi)=2^(-1/2)[I2;R_phi^T]`.

Let `J=[[0,-1],[1,0]]`. Then
`A=F_+^T dF_+=-(J/2)dphi`, so parallel transport on a full phi-cycle has
`Hol=exp(-integral A)=exp(pi J)=-I2`, a nontrivial real SO(2) geometric holonomy in a rank-two degenerate band. Under a different orthonormal gauge, holonomy changes by conjugation. This does not prove quantum tunneling or a topological Chern class. It is a classical Wilczek–Zee / Kato-type connection model.

One directly computable regularity check is
`||P_+(phi)-P_+(psi)||_op=|sin((phi-psi)/2)|`,
so `||dP_+/dphi||=1/2`. If kappa(s) >= kappa_0>0, the band gap stays >=2 kappa_0 under a smooth moving path. Actual *adiabatic tracking* requires an explicitly specified evolution equation, smoothness and a speed-versus-gap bound: a geometric projector alone is not a dynamical theorem. When kappa->0, the gap closes, so do not move through that point under an adiabatic label.

## Exact new angular discriminator [P-paper candidate]

Use the finite maximal-order norm disk `L_rho=O_K intersect {|z|<=rho}` with D19/rho5 (41 points) and D403/rho40 (479 points). Both are inversion and conjugation invariant. Fix t=ln2, making every finite Gaussian weight the exact rational dyadic `2^(-N(z))`. Define

`A=sum_(z in L_rho) x(z)^2*2^(-N(z))`,
`B=sum_(z in L_rho) D*y(z)^2*2^(-N(z))`.

The mixed sum `sum_(z) x(z)*y(z)*2^(-N(z))` vanishes exactly by conjugation. Define the frozen finite Gaussian coupled theta by the same formula with the sum over L_rho², and its normalized coupling curvature
`C_phi=(1/(4*t^2))*[d^2 Theta_(kappa,phi)(t)/d kappa²]_(kappa=0)`.
This is **not** a derivative of the original 400-row Gram.

By exact differentiation and the second-moment contraction,
`C_phi = (A²+B²)*cos(phi)² + 2*A*B*sin(phi)²`.
In particular
`C_0=A²+B²`, `C_(pi/2)=2AB`,
`C_0-C_(pi/2)=(A-B)²=(Re M_(2,0)(t))² >=0`,
where `M_(2,0)(t)=sum_(z in L_rho) z²*2^(-N(z))`. This is the first *nonfactorizing* direction-sensitive response; the first coupling derivative is zero under inversion. This gives a typed higher-dimensional link back to the existing finite angular theta moments. No originality claim.

## Frozen falsifiers / exact controls

1. Exact original D403 source helper still returns `rho40,R100,S=J4,Q219` (unchanged Z[u] integer disk). Frozen blob hash `research/phase206/source_probe.py=3f954b59d9f86b06ad53667c869b5b24f2e6c7f6`; original Q219 must equal directly enumerated integer coset. Build half-coset independently with odd numerator coordinates: D19 integer21+half20=41; D403 integer219+half260=479. All integer norms, both cosets inversion/conjugation-stable.
2. Use **only** `fractions.Fraction` dyadic weights and rational x,y for all finite moments. Freeze two test orientations phi=0 and pi/2 and kappa=1/3 for rational 4x4 matrix/projector spectrum checks. Do not silently use floating-point matrix factorizations.
3. Check `P_+^2=P_+`, `P_+P_-=0`, `P_++P_-=I`, `H=(1+kappa)P_+ +(1-kappa)P_-` at both frozen orientations. If any fails, STOP.
4. On the complete finite full-order disk at each D, compute A and B and the exact cross moment and require cross=0 and A != B (direction signal). Independently compute direct pairwise `C_0=sum_(z,w) [x_z x_w+D y_z y_w]²*2^(-N_z-N_w)` and `C_(pi/2)=sum_(z,w) D*(y_z x_w-x_z y_w)²*2^(-N_z-N_w)`; require exact equality to `A²+B²`, `2AB`, and gap `(A-B)²`.
5. Diagonal inversion and separate inversion controls must preserve/mirror Q as claimed at phi=0 and pi/2 for frozen sample pairs. Factor swap and conjugation must obey phi->-phi. A fixed-phi swap invariance at phi=pi/2 is **not** assumed or demanded.
6. Wrong source: ignore the half-coset and demand that the A/B moments **change**. Wrong separable model: kappa=0 has C as derivative of coupling perturbation but the Gaussian tensor itself factorizes and has no orientation signal. No claims of arithmetic gain from tensor products.
7. p-adic transport-negative control: `G=diag(4,4)`, rational det-one `U=diag(2,1/2)` yields `UGU^T=diag(16,1)`, both integer Grams and det16, but their 2-adic Smith exponent multisets are (2,2) and (0,4). Thus determinant preservation under GL_n(Q) does NOT preserve the p-adic Smith lattice. A generic R_phi moving analytic frame is not in GL_n(Z_p). This is a required safeguard.
8. Paper-level moving-moving gauge rule: for `G=F * G_tilde * F^T`, `Omega=F^(-1)dF`, `D G_tilde = dG_tilde + Omega G_tilde + G_tilde Omega^T = F^(-1)dG F^(-T)`; only a **p-integral unimodular** lattice-frame transport automatically preserves Smith factors.
9. Original full 400-row Gram remains unmodified; run only a fixed 4D higher-order theta control, not an unreviewed production source; CI <=15min, stdlib only. Stop on wrong-source/hash, point counts, exact angular identity, projector, symmetry, or p-adic counterexample failure.

## Status and non-claims

[P-paper] conditional exact linear algebra, symmetry equivariance, geometric connection, finite second-derivative identity, original lattice-vs-analytic-frame distinction. [M only after focused CI] finite rational D19/D403 two-coset angular and 4x4 matrix controls. [H] quantitative adiabatic dynamical error with a specified generator, nonfactorizing effects on a typed ordinary-jet trace Gram, higher-k lattice/window generalization, and any useful L-function or original determinant bound. [R] higher dimension by itself gives new arithmetic valuation; real moving frames necessarily preserve p-adic lattice; holonomy implies a class-number theorem or physical tunneling.

Root Lean CI and Markdown and focused exact CI must all pass before considering a merge. The 321^4 bound candidate PR157 and independent semantic review issue #50 remain separate.
