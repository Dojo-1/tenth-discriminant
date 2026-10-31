# Phase137 — integral Chebyshev moving frames, unchanged ordinary jets

**31 October 2026.** [Issue #51](https://github.com/Dojo-1/tenth-discriminant/issues/51) (transport) · [issue #50](https://github.com/Dojo-1/tenth-discriminant/issues/50) (human semantic reconstruction). Primary inspiration: [Tao's Gram/covolume exposition](https://terrytao.wordpress.com/2026/10/19/a-sketch-of-the-proof-of-non-existence-of-siegel-zeroes/) and [experimental tenth-discriminant challenge/comments](https://terrytao.wordpress.com/2026/10/20/an-experimental-ai-math-challenge-using-tenth-discriminant-bounds-to-explore-arguments-ruling-out-siegel-zeroes/comment-page-1/). The source field includes Green's derivative Gram determinant, auxiliary-prime, Poisson and split-prime refinements, and explicit requests for reconstructible comparisons. Classical Chebyshev minimax and unimodular frames are not claimed as discoveries. The *fitness for this exact ordinary-jet Gram* is the new question.

**Evidence:** [P] elementary paper identity for integer frames below (not yet separately Lean checked); [M-awaiting CI] finite 32-row Rust experiment; [H] uniform derivative-aware gain and proposed 46-billion target. The finite instance was explored BEFORE this note; it is an exploratory positive control, not blind preregistration. The **global conjecture** and its kill conditions are registered before any production-level proof/sweep. The existing strict 47.0b actual-field result and its arithmetic source remain unchanged.

## Monic integer radial polynomials: one original observation lattice

For the original rectangular monomials and m=min(r,s), [RadialOperator.lean](../../lean/TenthDiscriminant/RadialOperator.lean) uses Z^(r-m) W^(s-m) (ZW-a)^m, with a=floor(rho²/2). Its integer row operation preserves the original determinant and inert-prime divisor. Our variant preserves the **same** original E, Q, J, B and number field, and changes only the integer ROW frame.

Let rho≥1 be integer, L=rho², a=floor(L/2), e=max(a,L-a), and b=ceil(e²/4)∈Z_{>0}. Define:

    P_0(u)=1,  P_1(u)=u-a,  P_2(u)=(u-a)^2-2b,
    P_(m+1)(u)=(u-a)P_m(u)-b P_(m-1)(u)  for m>=2.

Every P_m is monic with integer coefficients. For row (r,s), define

    F_(r,s)(Z,W)=Z^(r-m) W^(s-m) P_m(ZW),  m=min(r,s).

Its expansion has leading term Z^r W^s with coefficient exactly one, with all lower terms among rows (r-m+t,s-m+t), t<m. Thus the row map H is lower unitriangular in the original row-major order, det H=1 over Z. For the exact original ordinary-jet observations E and factor-two trace B,

    E_new = H E;  G_old = E B E^T;
    G_new = H G_old H^T;  det G_new = det G_old.

The **exact moving-frame transport across local and real views** is also explicit. If the original inert-prime extraction is U_p E=Delta_p C_p with integral U_p, then E'=H E and integer H^{-1} give

    (U_p H^{-1}) E' = Delta_p C_p,
    (U_p H^{-1}) G' (U_p H^{-1})^T = Delta_p (C_p B C_p^T) Delta_p.

Thus the new row frame cannot lose the original p-integral quotient or alter its maximal-minor Smith valuations; the integer frame changes only which Archimedean diagonal estimates are convenient. U_p and H need not commute. This is a precise transport identity (paper linear algebra), not a sheaf or holonomy theorem and not an extra divisor.

The old Frobenius prime powers therefore divide the **same positive integer**. We have NOT inferred any new arithmetic divisor, altered the quadratic order, reduced Q, or substituted Hasse jets.

For m>=1, the Chebyshev identity gives

    P_m(u)=2*b^(m/2)*T_m((u-a)/(2*sqrt(b))).

For 0<=u<=L, |u-a|<=e<=2 sqrt(b), hence |P_m(u)|<=2 b^(m/2), whereas the old centered monic power has bound |u-a|^m<=e^m. This exponential-looking saving is for undifferentiated values ONLY. The production proof also includes ordinary derivatives with W held constant, and derivatives of P_m may eliminate or reverse the improvement.

## Finite positive and negative controls (explored before preregistration)

Freeze D=19, rho=5, R=8, S=J=4. The complete original ellipse Q has exactly 21 integer pairs and 2(R-1)+(S-1)=17<21, satisfying the original interpolation guard. E has 32 integer rows and 168 columns, with B repeating diag(2,38) at each unchanged point and ordinary derivative.

Here L=25, a=12, e=13, b=43:

    (u-12)^2 = u²-24u+144;    P_2(u)=u²-24u+58
    (u-12)^3 = u³-36u²+432u-1728;
                                  P_3(u)=u³-36u²+303u-180.

The preliminary exact-integer calculations predict (NOT yet CI certified): G_center[(2,2),(2,2)]=666616, G_new[(2,2),(2,2)]=378688; G_center[(3,3),(3,3)]=163129320, G_new[(3,3),(3,3)]=87348528. Of 32 rows, 12 diagonals decrease, 20 remain equal, none increase; log(product_new/product_old)≈-5.80382413464, product ratio≈0.00301599908. The [Rust pilot](phase137_chebyshev_frame.rs) computes the entire original integer observations using both polynomial-expansion and an independent Leibniz derivative formula. It checks E_new=HE, **every entry** of G_new=HGH^T, and all exact diagonals without floating-point operations except reporting the final log ratio.

**Necessary negative control:** no pointwise claim is licensed. At original node z=-4 and row (r,s)=(2,2), derivative j=0, the squared jet norm changes from 256 to 4900: the new polynomial is WORSE at that individual node. Only the sum over the original nodes and derivative slots happens to improve in this example. At large J, derivative amplification is a likely obstruction.

## An additional exact finite extremal question: Chebyshev is not the Sobolev optimum

This is a direct exercise in the practice of **refuting the strongest attractive statement**. The initial minimax intuition suggests that a Chebyshev basis should be optimal. But the actual objective is a finite positive *jet* Gram, not the uniform norm of an undifferentiated polynomial. On the original D=19, rho=5 complete ellipse, freeze r=s=2, a=12 and the monic one-parameter family

    f_c(Z,W)=(ZW-12)^2+c,   c in Z.

Because ordinary differentiation is with respect to Z holding W fixed, all j>=1 jets are independent of c for this particular row. Write u(q)=x^2+19y^2 for the actual 21 ellipse nodes. Exact integer sums give

    sum_Q (u-12)^2 = 1740,
    sum_Q 1 = 21.

With the original factor-two trace weights, the complete J=4 diagonal cost is therefore

    C(c)=666616 + 6960*c + 42*c^2.

The Chebyshev recurrence has c=-86 and C(-86)=378688. The **unique integer optimum** is c=-83 and C(-83)=378274 (further improvement of 414). For integer t=c+83,

    C(c)-C(-83)=6*t*(7*t-2) >= 0.

This inequality is elementary for all integers t; the [Rust source](phase137_chebyshev_frame.rs) exercises the formula on a broad interval and re-derives each cost from all original nodes and ordinary derivatives. Unlike the production conjecture, the *mathematical claim* has a short paper proof. It is a finite counterexample to the conjecture that a sup-norm Chebyshev choice minimizes the full discrete jet-Sobolev diagonal. The coefficient change is a unitriangular integral row shear and preserves the very same determinant and inert-prime divisor.

The deeper follow-up is to characterize, rather than merely optimize numerically, the **integer Sobolev projection defect**. Let G be the positive definite integer Gram on the same E, choose row i and earlier rows J, let A=G_(J,J), v=G_(J,i), c=G_(i,i). For k∈Z^|J|, the exact transformed diagonal is

    c(k)=c-2*k^T*v + k^T*A*k
        =c-v^T A^(-1)v + (k-A^(-1)v)^T A (k-A^(-1)v).

A is positive definite and invertible over Q, so this is a closest-vector problem in the ellipsoid norm A with **integer** k, not continuous Gram-Schmidt. The elementary complete-square identity gives an exact target and a falsification protocol. A uniform improvement still requires proof that the projection term beats the integral rounding defect, for enough production rows, with the original high-order jets in A and v. This is related to classical lattice/Gauss/LLL reduction and discrete Sobolev orthogonality; no claim of new general theory is made.

## Three genuinely falsifiable research questions

**Q1, highest priority [H]: Can a derivative-aware Chebyshev integer frame uniformly improve our PRODUCTION Hadamard bound by 43/10000?** For every admissible D≥46,000,000,000 and the unchanged Tuned.R D, Tuned.S D, Tuned.rho D, J=S and original full ellipse, seek:

    log(det G_D)/comparisonScale(R,S)
       <= (4/5) log D - 1649/2000 - 43/10000.

The currently checked production upper has NO final 43/10000 gain. The lower bound is unchanged:

    (999997/1000000) log D - 5739/1000.

**Exact conditional endpoint arithmetic:** if the upper conjecture and a fresh Lean-certified log(46,000,000,000)≥245519/10000 both hold, the lower exceeds the proposed upper by at least **1063443/10000000000 > 0** at and above 46b. This follows by exact rational algebra; it is NOT a proven 46b cutoff. D=46b is inside the existing Tuned parameter guard D≥41006250000. The full proof still needs an actual-field and parity composition on the unchanged field discriminant.

**Q2 [H]: Can an integer monic, derivative-weighted optimal frame beat the Chebyshev SUP-norm frame?** Minimize the exact product of original-jet row diagonals over monic integral P_m, not merely sup |P_m| over u∈[0,L]. The ordinary derivatives can reward very different integer polynomials. Specify bounded degree, coefficient bit lengths, rows, Q and derivative orders before a parameter search; compare with the original centered basis AND the Chebyshev recurrence. Avoid claims based only on low-derivative or changed-node tests.

**Q3 [H]: Can the p-adic Smith filtration and real diagonal cost be coupled without conflating them?** H∈GL_(RS)(Z) preserves every original determinantal divisor and actual det G, while changing the Archimedean Hadamard ceiling. Seek a proved joint cost function for a fixed integer E and B that detects when lower bounds from inert primes can coexist with a cheaper REAL frame. Do not infer extra residual p-adic valuation from real smallness or normalized modular rank.

**Secondary, lower priority [P/H]:** the current [EllipseCellArea](../../lean/TenthDiscriminant/EllipseCellArea.lean) uses (1+sqrt D)/2 as covering radius. Euclidean cell geometry gives sqrt(1+D)/2, a sharper elementary bound. BUT the existing chosen-radius inequality includes a 10 sqrt D margin; reducing the cell-radius estimate without retuning rho is unlikely to improve the endpoint. No cutoff gain is claimed from this isolated fact.

## Promotion and kill conditions

1. [M] **Exact-head Rust CI** must compile, check all 32×168 original observations by both ordinary-jet formulas, unitriangular H, all 32×32 Gram entries, 12/20/0 diagonal controls, and the **pointwise false-strengthening** negative control. Failures remain visible and must not be explained away.
2. [P] **General integer matrix theorem** can later be lifted into Lean, with a monic family, exact derivative row action, determinant-one H, and explicit unchanged integerRectangularTraceGram. The paper lemma alone is NOT Lean verified.
3. [H] **Production derivative bound** is killed by any correctly constructed admissible production counterexample or if the full bound including all j=0..S-1 cannot be certified. If the 43/10000 threshold fails, record its tightest honest bound rather than editing the conjecture retroactively.
4. **Global 46b promotion** needs all new uniform inequalities and the 46b log bracket in Lean, exact-head source/axiom/negative controls, the unchanged inert-prime mass and same-field return. #50 still requires external mathematical reconstruction; #51 remains open until genuinely compatible global transport exists.
5. **Stop** after this discrete frame test unless new evidence warrants a separate round. A polycosmic or hypercomplex metaphor does not earn a numerical exponent by itself.

The geometric language is operational here: radial fibers indexed by r-s, integer-polynomial transition matrices on each fiber, an Archimedean cost function, and p-local invariants that do **not** change under H. The movement of frames is real algebraic action, not a claimed holonomy theorem.

## Reproduction

    rustc --edition=2021 --test research/radial_chebyshev/phase137_chebyshev_frame.rs -o /tmp/phase137-tests
    /tmp/phase137-tests
    rustc --edition=2021 research/radial_chebyshev/phase137_chebyshev_frame.rs -o /tmp/phase137-pilot
    /tmp/phase137-pilot

[Exact-head CI workflow](../../.github/workflows/phase137-chebyshev-frame.yml). Neither a merge nor a communication to Professor Tao is authorized by passing these finite tests alone; both issues remain open.

## First exact-source CI receipt (post-registration, finite only)

[GitHub Actions run 41179952647](https://github.com/Dojo-1/tenth-discriminant/actions/runs/41179952647) on source SHA `91f1a4cfd4ef07b0d5673998e4ce32302198a881` completed with **4 Rust tests passed** using rustc 1.99.1. It executed the original-jet expansion, separate Leibniz formula, full 32×168 row relation, every entry of the 32×32 Gram congruence, signed trace-factor weights, the 12/20/0 diagonal criterion, and the *worse pointwise jet* negative control. Logged: `log_product_gain=-5.80382413464387`, `new_diag_product_over_old=0.0030159990776848942`. This verifies only the frozen finite instrument; the research note was committed later and no production inequality has been checked. The PR head must still be audited separately before a merge.
