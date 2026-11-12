# Phase285 — observed Noether disk-lens / finite-theta regression and boundaries

**Post-result:** written after the **focused exact-head** Phase285 CI success at implementation/workflow head `71291547`: [GitHub Actions 43218271242](https://github.com/Dojo-1/tenth-discriminant/actions/runs/43218271242). The predecessor code and protocol were separately committed. D19's toy numbers and D403 minor's expected prime valuations were **known before this CI implementation**, so this is reproduction of a declared control, not blind out-of-sample experimental novelty. All proof prose and checks were prepared with AI. The whole-repository Lean and Markdown workflows on this *new documentation head* must pass before merge.

## Exact object and source

The originally used sampled quadratic order is `Lambda_D = Z[u]`, `u^2=-D`, with `z=x+yu` and its conjugate `w=x-yu`. The **actual** original signed trace weight is 2 on real coordinates and 2D on imaginary coordinates. Monomials are `Z^rW^s`, ordinary `d_Z^j` holds W fixed, and j ranges 0..J-1. In D403, the entire original source has R=100, S=J=4 and 219 original ellipse points, giving 400 rows and 1752 channels. Phase285 **does not compute the determinant of that 400-row matrix**: it tests the original rows with (r,s) in {0,1,2,3}², a 16-row principal submatrix, using every original point and all four original derivative orders. Parity preservation is separately checked over all 400 labels and the legal old odd-prime Frobenius frame.

Let `Q0={x^2+Dy^2<=rho^2}`, `Qlens=Q0 ∩ {(x-1)^2+Dy^2<=rho^2} ∩ {(x+1)^2+Dy^2<=rho^2}`, and `Qplus=Q0 ∩ {(x-1)^2+Dy^2<=rho^2}`. Q0 and Qlens are inversion-stable; Qplus is intentionally not.

## Measured source-faithful finite observations [M]

| case | Q0 / symmetric lens / asymmetric points | 2-adic v(det) | 3-adic | 5-adic | 7-adic | 11-adic |
|:--|:--|:--|:--|:--|:--|:--|
| D19, two original rows 1,Z, J1, Q0 | 21 | 8 | 1 | 1 | 1 | 0 |
| D19, symmetric lens | 15 | 3 | 1 | 1 | 0 | 0 |
| D19, asymmetric | 18 | 2 | 3 | 0 | 0 | 0 |
| D403, original **16-row submatrix**, J4, Q0 | 219 | 56 | 7 | 1 | 1 | 0 |
| D403, same 16 rows, symmetric lens | 213 | 56 | 7 | 0 | 1 | 0 |
| D403, same 16 rows, asymmetric | 216 | 80 | 7 | 0 | 0 | 2 |

D19 exact 2x2 source Grams are `diag(42,640)`, `diag(30,356)`, and `[[36,18],[18,498]]`, with determinants **26880**, **10680**, and **17604**. In particular, the lens reduces determinant to **89/224** of the original yet *loses five 2-adic units*. For D403's 16-row minor, the lens reduces the determinant while **losing one 5-adic unit**, retaining the listed 2/3/7-adic exponents. Those claims refer to a specified finite minor only. They do not compare the actual full 400-row local Smith budget at the two samplings.

Across both symmetric windows, every selected even/odd cross-block Gram entry vanishes. At D403 the asymmetric control has **64 nonzero entries in the 8x8 even/odd rectangular cross block**. The original jets and the independently computed finite mixed-theta moments give the *same integer entry* for every tested pair. Their moment signatures of odd total degree vanish on the symmetric sources. The exact deleted-point Gram equals the difference `G(Q0)-G(Qlens)`, proving a constructive positive-semidefinite decomposition. Every selected determinant is positive.

## Paper-level identities and integral conservation [P-paper, not a new external theorem]

The central involution acts by `iota(Z,W)=(-Z,-W)`. Its invariant subring is

`Z[Z,W]^(C2) = Z[Z^2,ZW,W^2] = Z[A,B,C]/(AC-B^2)`,

and the original rectangular monomial lattice splits integrally into even and odd monomial-parity submodules. This is a genuine **integral** splitting: it does not invoke the rational half-projectors `(I+/-P)/2`, whose denominators would disrupt 2-adic accounting. Under inversion, ordinary j-jets acquire sign `(-1)^(r+s-j)`. Hence on Q=-Q, each even/odd cross Gram entry cancels and `det G = det G_even * det G_odd` for the *entire* original source whenever the determinant exists.

For odd p, the old integral Frobenius row `Z^(r-pk)W^s(Z^p-W)^k` expands into rows `Z^(r-ph)W^(s+h)`; their total exponent parity differs from r+s by `(1-p)h`, which is even. The existing old row normalization is therefore parity-compatible; **no new Frobenius valuation** is inferred from it. The p=2 parity argument fails and its behavior must be handled independently.

The **finite theta generating function** is

`Theta_Q(t,xi,eta) = sum_(z in Q) exp(-t N(z) + xi z + eta conj(z))`.

Its mixed xi/eta derivatives at zero are `M(a,b)=sum z^a conj(z)^b`. For original rows (r,s),(r',s'), the exact signed trace Gram has the coefficient formula

`G = 2 sum_(0<=j<J, j<=r,r') (r)_j (r')_j Re M(r-j+s',s+r'-j)`.

This is a finite algebraic identity verified entrywise, **not yet** a theorem connecting Gram determinants to Dirichlet L zero locations. It retains angular information through two independent exponent indices a and b. A scalar radial theta alone does not generally reconstruct these moments.

One possible sharper *finite-minor* analytic upper uses Hadamard-Fischer: for i,j in the same parity block, `det G <= (G_ii*G_jj-G_ij^2) * product_(k!=i,j) G_kk`. This is strictly below the uncorrected Hadamard product when `G_ij !=0`. Our regression computes the largest two-row correlation among the chosen 16 rows, not a competitive uniform upper for all 400 original rows.

## Maximal-order and infinite-theta transport remainder

Both tested squarefree D=19,403 satisfy D=3 mod4, so

`O_K = Z[u] disjoint_union ((1+u)/2 + Z[u])`, `u^2=-D`.

The absent coset begins at norm `(D+1)/4` for the displayed representative: **5 at D19**, **101 at D403**. It is not a remote radial tail that can be ignored. The full maximal-order Gaussian theta requires the separate half-shifted sum. When and only when class number one (or a separate ideal-class resolution) is established, one may use the Mellin relation to Dedekind zeta and ultimately `zeta(s)L(s,chi)`. A finite polynomial-moment identity alone does not supply such a statement, and the nontrivial angular moments require their own transport and error analysis.

**Missing proof obligations [H]:** (i) an explicit, verifiable Gaussian tail bound on each order coset, including angular weights, (ii) a precise angular-to-Hecke-character decomposition for the source moments, (iii) any nonoverlapping full-400-row determinant improvement and its original-analytic-upper comparison, (iv) independent review of PR157's source-to-field semantics.

**Negative results [R]:** smaller geometric window => larger p-adic divisor (false in D19 and the D403 16-row minor); even/odd splitting alone => better analytic constant (unproved); original order theta = maximal-order theta (false without the missing coset). No new cutoff, class-number classification or Siegel-zero exclusion is claimed.
