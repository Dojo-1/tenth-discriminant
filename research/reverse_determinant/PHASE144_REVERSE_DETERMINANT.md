# Phase144 — reverse determinant: the integral-image stratum beneath Gram volume

31 October 2026. **Evidence [M]: exact finite integer experiment; [P]: standard lattice/Cauchy–Binet implications; [H]: proposed uniform extension.** No production cutoff, Lean proof, or independent peer review is asserted. PRs #61/#62 and the established strict 47-billion theorem are untouched.

## Frozen objects and the mathematical interface

Use the **original ordinary jets** from Phase140: $D=19,\rho=5,R=8,S=J=4$, rectangular monomial rows $(r,s)$, $Z$-derivatives $j=0,1,2,3$ with $W$ fixed, both integer coordinates of $x+y\sqrt{-19}$, and the positive trace weights $B=\operatorname{diag}(2,38,\ldots)$. For each finite set $Q$, $E_Q$ has $32$ rows and $8|Q|$ columns and $G_Q=E_Q B_Q E_Q^\mathsf T$.

Define $C_Q=\mathbb Z^{32}/\operatorname{im}E_Q$ and $d_Q=|C_Q|$ when full row rank holds. Cauchy–Binet and the maximal-minor content imply $\det G_Q=d_Q^2 H_Q$ with $H_Q$ a positive integer primitive weighted Plücker norm. For $Q'\subseteq Q$ there is a **canonical surjection** $C_{Q'}\to C_Q$ with kernel $\operatorname{im}(E_Q)/\operatorname{im}(E_{Q'})$. Unlike the row lattices embedded in distinct ambient $\mathbb Z^{8|Q|}$ spaces, these **column images** lie in one fixed $\mathbb Z^{32}$ and can be compared exactly.

## First discriminating result

Take the original 21-point norm ellipse $Q_\mathrm{full}=\{x^2+19y^2\le25\}$ and the 19-point nested ellipse $Q_\mathrm{thin}=\{6x^2+95y^2\le125\}$, deleting only $(\pm5,0)$.

The two exact modular Hermite normal forms **are identical**, and their complete Smith lists are also identical:

- Smith factors: $1^{\times8},2^{\times8},4,12^{\times3},24^{\times8},144^{\times4}$.
- Index $d_\mathrm{full}=d_\mathrm{thin}=2^{56}3^{19}=83749764955012576535642112$.
- The canonical kernel of $C_\mathrm{thin}\to C_\mathrm{full}$ is **zero**.
- $\log\det G_\mathrm{full}\approx530.285191202$; $\log\det G_\mathrm{thin}\approx512.666684184$; decrease $\approx17.618507018297$, consistent with the earlier independently implemented Phase140 exact-Gram pilot.
- $v_3(\det G_\mathrm{full})=39$, $v_3(\det G_\mathrm{thin})=38$. Since $v_3(d)=19$ in both, the guaranteed $3^{38}$ divisor is wholly accounted for by $d^2$, and the extra factor of 3 in the full ellipse is **primitive metric residue**: $v_3(H)$ changes from 1 to 0.
- $\operatorname{rank}_{\mathbb F_2}(E)=8$ and $\operatorname{rank}_{\mathbb F_3}(E)=17$ for both.

**Correction:** this specific thinning does not produce a new arithmetic quotient. It improves the real determinant within one and the same integral column-image stratum.

## Exactly bounded stratification tests

For all 10 antipodal pairs, delete $k=1,2,3$ pairs, always retaining $(0,0)$. Each candidate has an **independently checked nonsingular square original-jet witness**: eight real nodes (one real channel per jet) when available, otherwise four nonreal nodes on one horizontal line. The determinant of that witness supplies the valid multiple for SymPy's modular Hermite algorithm; reusing a witness after removing its points would be invalid.

| Removed pairs | Points left | Configurations | Same Hermite form | Changed image |
|---:|---:|---:|---:|---:|
| 1 | 19 | 10 | 10 | 0 |
| 2 | 17 | 45 | 44 | 1 |
| 3 | 15 | 120 | 111 | 9 |

The unique 17-point exception removes the pairs $(1,-1)$ and $(1,1)$ (i.e., all four $(\pm1,\pm1)$ observations). It remains rationally full rank, but the **relative** Smith factors of its inclusion into the full column lattice are $2,2,2,2,2,2,4,4$. Therefore the canonical quotient is $(\mathbb Z/2)^6\oplus(\mathbb Z/4)^2$ of order $2^{10}$. Its rank mod 2 drops from 8 to 6 while its rank mod 3 remains 17. Notably, $v_3(\det G)$ rises to 43 despite the determinant decreasing; the residual metric valuation can move in either direction.

For the 120 cases with 15 points, the index-ratio histogram is: unchanged 111; $2^{10}$ in 6 cases; $2^{12}$ in 1; $2^{14}$ in 1; $2^{26}$ in 1. There is no claim that powers of 2 remain the only exceptional factors outside these cases.

## Evidence, boundary, and next question

The original sufficient interpolation cardinality guard is $17<|Q|$. The exact 17- and 15-point samples above can violate this guard while retaining full rational rank **and** the entire original column image. The guard is not an optimality criterion.

This **does not** imply a new uniform discriminant upper bound. Finite image stability, primitive metric volume, a uniform interpolation theorem, and the production prime-lower hypotheses must be kept separate. A meaningful next [H] target is to characterize a *uniform family of compact ordinary-jet supports* generating the original integral column image while permitting a determinant-independent metric upper bound. Counterworld: this stability is a finite small-$D$ accident or its construction consumes the intended gain.

**Executable reproducer:** [phase144_verifier.py](phase144_verifier.py), consuming unchanged [Phase140 source](../ellipsoid_trimming/phase140_exact_trim.py). Uses exact integer arithmetic and SymPy modular HNF/Smith; printed natural logarithms are presentation-only. No new PR or branch merge is authorized by the finite tests themselves.