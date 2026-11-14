# Phase313 — wild ray, honest bridge

> A local ring remembers how a point is lifted. An ideal class remembers whether its factors are principal. The ORIGINAL trace Gram is where these worlds meet.

Stacked research draft on Phase312. No changes to main, the field theorem, its integer-order matrix, valuationWeight or the reported cutoff \(322^4\). Every claimed arithmetic measurement requires exact-head CI, and external human peer review remains absent.

## The normalized wild coordinate

For inert \(p=5\), in \(\mathcal O_D=\mathbb Z[\omega]\), \(\omega^2-\omega+(D+1)/4=0\), define on LOCAL UNITS

\[
\varepsilon(z)=\frac{z^5-\bar z}{5}\bmod5,\qquad
\delta(z)=\frac{\varepsilon(z)}{\bar z}\bmod5\in\mathbb F_{25}.
\]

The division by \(\bar z\) is allowed only for units modulo5. The normalized quotient satisfies

\[
\delta(xy)=\delta(x)+\delta(y),\quad
\delta(-x)=\delta(x),\quad
\delta(\bar x)=\overline{\delta(x)},\quad
\delta(1+5u)=-\bar u.
\]

Consequently the signed ray UNIT group has an explicit isomorphism

\[
(\mathcal O/25)^\times/\{\pm1\}
\xrightarrow[\sim]{([z\bmod5],\delta(z))}
(\mathbb F_{25}^{\times}/\{\pm1\})\times(\mathbb F_{25},+)
\cong C_{12}\times C_5^2.
\]

All 600 local units and 300 signed classes were exhaustively checked for \(D=43,163,183,203\). When \(h_K=1\), this unit quotient identifies with the entire ray class group modulo25; in general, it is the kernel of the map to the ordinary class group.

The wild part is NOT semisimple in characteristic5:

\[
\mathbb F_5[C_5^2]\cong\mathbb F_5[U,V]/(U^5,V^5).
\]

Its augmentation ideal \(J=(U,V)\) has \(J^9=0\), \(J^8\ne0\) and graded dimensions \(1,2,3,4,5,4,3,2,1\). Multiplicative characters taking values in \(\mathbb F_{25}^{\times}\) cannot detect the wild part. This is standard modular group algebra, not physical quantum entanglement or a new cohomological theorem. See [Sharifi's class field theory notes](https://math.ucla.edu/~sharifi/notes/algnum-ch07.html) and [background on elementary abelian group algebras](https://doi.org/10.1016/j.jalgebra.2016.06.002).

## A genuinely global class-number-one constraint

Let \(P_n(c,w)\) count PRINCIPAL integral ideals of norm \(n\), prime-to5, tagged by the signed tame/wild conductor25 class of a generator. When \(h_K=1\), every ideal is principal and unique factorization OF IDEALS gives, for coprime \(m,n\),

\[
\boxed{P_{mn}=P_m*P_n}.
\]

The first wild moment \(B(n)=\sum\delta(z)\), square moment \(C(n)=\sum\delta(z)^2\), and Hermitian moment \(H(n)=\sum\delta(z)\overline{\delta(z)}\) satisfy corresponding Leibniz identities, e.g.

\[
B(mn)=A(m)B(n)+A(n)B(m),\qquad A(n)=\sum_{c,w}P_n(c,w).
\]

For each \(D=43,163\), both class number one, hosted finite checks verified **353** independent norm-shell total ideal counts, **720** full 300-component coprime convolution identities and **2160** first/second mixed moment identities for \(mn\le441\). The normalized first moment is not forced to vanish by sign symmetry: \(B(4)=3\bmod5\).

In \(D=183\), class number eight, \(\operatorname{Norm}(\omega)=46=2\cdot23\), but there is no element of norm2 or23. Thus \(P_2=P_{23}=0\), while \(P_{46}\) contains TWO principal ideals. Nonprincipal ideal classes can cancel in a product. This explicit obstruction is invisible to their isomorphic inert local completions.

## Exact transport to the SAME original Gram

Phase312 proved that primitive polynomial rows and ordinary held-W jets depend modulo5 on

\[
(1,\varepsilon(z),\overline{\varepsilon(z)})
=(1,\bar z\,\delta(z),z\,\overline{\delta(z)}).
\]

A principal ideal's signed ray tag determines contributions from BOTH generators \(\{z,-z\}\). When \(z=5u\), no unit ray tag exists; the correct separate stratum is the first lift \(u=z/5\bmod5\), since \(\varepsilon(z)=-\bar u\). These two disjoint sources define a linear map of \(\mathbb F_5\)-modules

\[
\mathcal L:\mathbb F_5^{300}\oplus\mathbb F_5^{25}
\to\operatorname{Sym}_N(\mathbb F_5)
\]

with the original row and jet labels fixed.

~~~mermaid
flowchart TD
  A["Global principal-ideal norm shells"] -->|"h=1: coprime convolution"| B["300 signed tame/wild ray classes"]
  B -->|"delta and both generator signs"| C["Original primitive source rows and ordinary jets"]
  N["5-divisible observations: z/5 mod5"] --> C
  C -->|"unchanged Hermitian trace"| G["SAME primitive Gram mod5"]
  G --> P["Actual higher 5-adic Smith filtration"]
  P -. "uniform h1 theorem still missing" .-> H["Non-overlapping global Gram mass OPEN"]
  X["D183: nonprincipal factors norm2 ×23 become principal at46"] --> B
~~~

The original D203 maximal-order \(Q263,R50,S=J2\) source has **127 principal unit ideals in 82 populated ray classes** plus **9 nonunit observations**. Those counts reproduce ALL **10000** original primitive Gram cells and rank63. Dropping either the wild coordinate or nonunit lift classes changes the result.

Even more importantly, the exact D163 \(h=1\) ORIGINAL INTEGER-ORDER source (not the maximal-order substitute) uses the integral embedding

\[
x+y\sqrt{-163}=(x-y)+2y\omega.
\]

Its \(Q109,R40,S=J1\) primitive source after 15 exact divisions is reconstructed using **50 principal unit ideals in 35 ray classes** and **9 nonunits**. All **8720** original primitive source coordinates and **1600** actual original primitive Gram entries match. The primitive rank over \(\mathbb F_5\) is 23.

This closes a finite global ray-spectrum-to-SAME-original-Gram bridge. It does not force any extra rank defect under h1 without new arithmetic estimates on these counts.

## Exact p-adic filtration and negative controls

The D203 original Gram splits EXACTLY into two 50-row sign-parity blocks. The primitive 5-adic valuations are 18 and20, totaling38; adding the already-verified 50 exact source divisions recovers the unchanged original valuation138. This splitting does not add new factors.

For the D163 ORIGINAL INTEGER-ORDER Gram, the primitive Smith profile obtained through precision \(5^6\) is

\[
\operatorname{Smith}_5(G_{\mathrm{prim}})
=\{0^{23},1^7,4^{10}\}.
\]

Thus

\[
v_5(\det G_{\mathrm{original},163})
=2(15)+7+4(10)=\boxed{77}.
\]

A wholly separate arbitrary-precision EXACT INTEGER determinant over \(\mathbb Z\), using SymPy DomainMatrix rather than modular Smith or Schur reductions, gives even/odd original block valuations **37** and **40**, determinant units \(4,3\bmod5\), and the full original v5=77 with unit2 modulo5.

The strongest countercontrol uses **identical integer observation geometry**. Fields D163 (\(h=1\)) and D183 (\(h=8\)) have the same ORIGINAL integer-pair Q109 at matched radius21: \(y=0,-21\le x\le21\), and \(y=\pm1,-16\le x\le16\). The original Grams agree mod5 and both have measured exact full determinant valuation **77** with even/odd valuations 37/40. D183's R40 is deliberately matched, not its native parameter choice. Therefore these local and finite determinant fingerprints **do not characterize class number one**.

## Evidence contract and remaining theorem

- **[P-paper]** normalized wild-log product law, signed unit-group decomposition, class-one ideal-convolution implication, parity orthogonality and conditional determinant index-square factorization.
- **[M, after exact-head CI]** exhaustive 300-class enumerations, bounded h1 and h8 norm shells, exact original ray-to-Gram mappings, primitive Smith and independent full integer determinants.
- **[H]** a uniform theorem forcing extra non-overlapping primitive Gram valuation from the class-one ray convolution for the SAME large-\(R,S,J,\rho\) integer-order field source.
- **[R]** local tame/wild data, rank23, or valuation77 as a class-number-one diagnostic; treating wild ordinary Fourier characters as sufficient; adding the new floors to the old valuationWeight blindly.

The missing theorem must show that the class-one convolution plus the **native norm cutoff** constrains the ray distribution so that the image under \(\mathcal L\) has a residual \(5\)-adic defect independent of the existing valuationWeight. No such uniform implication has been proved. The reported cutoff \(322^4\) remains unchanged.

Source code and adversarial tests are in this directory. Preregistrations record the order of A–G before each implementation. The narrow Lean Phase313WildRay proofs only cover principal-unit polynomial identities and elementary sign-pairing algebra; they do not certify ray class groups, local inverses, any exact 40×40 determinant or the uniform field theorem.
