# Phase139 — Original ordinary jets as graded radial and angular moments

**31 October 2026.** The object is frozen: the complete ellipse \(Q_{D,\rho}=\{(x,y)\in\mathbb Z^2:x^2+Dy^2\le\rho^2\}\); all rectangular monomial rows \(Z^rW^s\), all ordinary \(Z\)-derivatives with \(W\) fixed, and the original integral trace metric with weights \(2,2D\). The identities do not change observations or increase the established inert-prime divisor.

**Status:** elementary exact algebra [P, paper argument, not separately Lean formalized]; finite implementation [M, exact-head Rust CI]; proposed uniform estimates [H]. No new tenth-discriminant bound.

## The explicit bridge

For \(z_q=x+i\sqrt D\,y\), \(n_q=z_q\bar z_q\), define mixed moments
\(M_{a,b}=\sum_{q\in Q}\operatorname{Re}(z_q^a\bar z_q^b)\)
and radial moments \(\mu_k=\sum_{q\in Q}n_q^k\).

The ORIGINAL positive trace Gram satisfies

\[
G_{(r,s),(t,u)}=
2\sum_{\substack{0\le j<J\\ j\le r,t}}
r^{\underline j}t^{\underline j}M_{r-j+u,\ s+t-j}. \tag{1}
\]

This follows directly by multiplying the two original ordinary jets and taking twice the real part. The difference of moment exponents equals
\((r-s)-(t-u)\), **independent of j**.

Write \(d=r-s,\ e=t-u\), \(\ell=|d-e|\), \(k_j=\min(r-j+u,s+t-j)\). Define the *signed angular power moment*

\[
H_{\ell,k}=\sum_{q\in Q} n_q^k\operatorname{Re}(z_q^\ell).
\]

The exact cross-fiber form is

\[
\boxed{G_{(r,s),(t,u)}
=2\sum_{\substack{0\le j<J\\ j\le r,t}}
r^{\underline j}t^{\underline j}H_{\ell,k_j}.} \tag{2}
\]

Within one fiber \(d=e\), let \(m=\min(r,s)\), \(n=\min(t,u)\). Then \(H_{0,k}=\mu_k\) and

\[
\boxed{G^{(d)}_{m,n}
=2\sum_{\substack{0\le j<J\\ j\le r,t}}
r^{\underline j}t^{\underline j}\mu_{|d|+m+n-j}.} \tag{3}
\]

So the full original fiber is a factorial-weighted Hankel–Sobolev moment matrix. Signed angular moments, indexed by the one integer \(\ell\), carry the cross-fiber information. Odd \(\ell\) vanish by \(q\mapsto-q\), consistent with [existing Lean parity](../../lean/TenthDiscriminant/CentralSymmetry.lean); even \(\ell\) can be positive or negative.

## The one-dimensional ellipse-slice formula

For \(Dy^2\le\rho^2\), define \(X_y=\lfloor\sqrt{\rho^2-Dy^2}\rfloor\) and
\(S_m(X)=\sum_{x=-X}^X x^m\). Pure integer binomial expansion yields

\[
\boxed{
H_{\ell,k}=\sum_{Dy^2\le\rho^2}
\sum_{h=0}^{\lfloor\ell/2\rfloor}\sum_{v=0}^{k}
(-D)^h\binom{\ell}{2h}\binom{k}{v}
y^{2h}(Dy^2)^{k-v}S_{\ell-2h+2v}(X_y).
} \tag{4}
\]

This evaluates angular moments through finite *one-dimensional integer power sums*, without introducing floating-point angles or a reduced node set. It is a change of computational representation, not a stronger inequality by itself.

The [standalone Rust source](phase139_original_moments.rs) independently reconstructs **every entry** of the original \(32\times32\) Gram at \(D=19,\rho=5,R=8,S=J=4\) using direct ordinary jets, the mixed-moment formula, the radial specialization, and the slice formula. [Exact-head run #41187477536](https://github.com/Dojo-1/tenth-discriminant/actions/runs/41187477536) passed all **five tests**.

Exact finite controls:

    (mu0,mu1,mu2,mu3)=(21,320,6396,135416)
    H_(2,0)=-60; H_(2,1)=-1584; H_(4,0)=3356
    G_{1,Z^2}=[[42,-120],[-120,15520]]
    det(G_{1,Z^2})=637440.

The j=0-only shortcut would report diagonal 12792 instead of 15520: a **failed derivative-omission hypothesis**. A determinant-one real shear with coefficient \(-20/7\) orthogonalizes this two-row Gram without changing its integer determinant; the new rows are not asserted integral or p-locally normalized.

## Conjecture portfolio [H], with failure conditions

**A. Moment-majorant conjecture.** Starting from (4), obtain explicit **determinant-independent** bounds on sufficiently many signed \(H_{\ell,k}\) throughout the unchanged production parameters \(D,\rho,R,S,J\). Use them to certify a determinant-one *real* frame and a whole-Gram upper through **every** ordinary derivative. The frame need not be integral for the Archimedean upper, but the p-adic lower stays on the ORIGINAL integer Gram. Kill an alleged improvement if the bounds require the determinant being bounded, omit high derivatives, or silently assume angular cancellation.

**B. Spectral-coupling conjecture.** Bound the spectrum of diagonal-normalized same-parity fiber blocks via (2), and translate this into a **strict improvement over the existing certified production upper**, not merely the unoptimized diagonal product. If all normalized eigenvalues exceed \(\delta_R>0\), then the total normalized block saving is at most \(\log(1/\delta_R)/R\). A constant target \(43/10000\) therefore requires exponentially small eigenvalues or equivalent aggregate concentration. The opposite possibility—that signed angular moments cancel too strongly, leaving too little coupling—remains a live counterworld.

**C. Certified rational-frame lemma target.** For any two-row positive Gram \(a=G_{jj}>0,b=G_{ij}\), the real shear \(t_*=b/a\) minimizes the other diagonal; using a computable rational \(\tilde t\) costs exactly \(a(\tilde t-t_*)^2\). Can interval estimates of \(a,b\) from (4) deliver *computably specified* rational shears with provable cumulative savings at production scale? A single pair's finite gain disappears under \(R^2S\) normalization. Kill claims that rely on an oracle for unknown full-Gram entries.

The earlier [Phase137](../radial_chebyshev/PHASE137_PROTOCOL.md) **conditional** 46-billion proposal needs an additional \(43/10000\) normalized geometric saving against the *already certified upper envelope*, and a new checked log certificate. Neither is available; the strict verified 47-billion theorem is unchanged.

## Semantic and prior-art boundaries

General discrete Sobolev orthogonal polynomials, generalized Hankel–Sobolev moment matrices and Hessenberg/long recurrence theory predate this study. Relevant sources: [2005 discrete Sobolev orthogonal polynomial algorithms](https://doi.org/10.1016/j.cam.2004.12.003); [2024 Gauss–Borel Sobolev moment treatment](https://doi.org/10.1007/s13324-024-00883-5); and [2023 generation via Hessenberg inverse eigenvalue problems](https://doi.org/10.1007/s00211-023-01379-3). The value to test is the applicability of their machinery to *this unchanged ordinary-jet integer Gram*, not priority over those established theories.

[Issue #50](https://github.com/Dojo-1/tenth-discriminant/issues/50) still requires independent mathematical reconstruction of the actual-field theorem. Formulae (1)–(4) offer a human-sized semantic test, not a referee result. [Issue #51](https://github.com/Dojo-1/tenth-discriminant/issues/51) still requires an analytically uniform, p-integrally compatible bound; finite moment identities do not close it. No external submission or new field cutoff is claimed.
