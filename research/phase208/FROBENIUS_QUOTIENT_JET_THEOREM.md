# Phase208 — the integral Frobenius-quotient jet and residue-class rank lemma

**4 November 2026.** Registered as a *post-result follow-on* in [#151](https://github.com/Dojo-1/tenth-discriminant/issues/151) and audited in [#152](https://github.com/Dojo-1/tenth-discriminant/issues/152) **before** implementing the exact residue-class test. This is a paper-level derivation using classical commutative algebra and finite abelian groups, followed by bounded AI-authored exact checks. No claim of literature novelty, end-to-end Lean formalization, or new class-number-one field cutoff. The pre-existing [Phase152 Frobenius graph](../reverse_determinant/PHASE152_FROBENIUS_GRAPH.md), [Phase155 jet precision](../reverse_determinant/PHASE155_JET_PRECISION.md) and [old Frobenius divisor proof](../uniform_inert_valuation/PROOF.md) remain the cited internal prior art.

## Types, not an interchange of arithmetic fibres

Let \(O_D=\mathbb Z[u]/(u^2+D)\) with \(\bar u=-u\). Fix an odd rational prime \(p\) for which \(X^2+D\) is irreducible over \(\mathbb F_p\). Hence \(O_D/pO_D\cong\mathbb F_{p^2}\) and the finite-field Frobenius equals conjugation:

\[
z^p\equiv \bar z\pmod{pO_D},\qquad
q_p(z)=\frac{z^p-\bar z}{p}\in O_D.
\]

Let \(R,S,J\) be positive and \(Q\subset O_D\) a finite conjugation-stable set (the original ellipse is such a set). The old **unimodular integer** polynomial row change is
\[
k_{r,s}=\min(\lfloor r/p\rfloor,S-1-s),\quad
F_{r,s}(Z,W)=Z^{r-pk_{r,s}}W^s(Z^p-W)^{k_{r,s}}.
\]
For every original **ordinary** jet order \(j<J\), set the normalized evaluation entry
\[
c_{r,s,j}(z)=p^{-k_{r,s}}\,
\partial_Z^j F_{r,s}(z,\bar z).
\]
Its integrality had already been proved by the old Leibniz/Frobenius argument; the next identity gives an *additional, source-matched description*.

## Exact integral differential-polynomial identity [P-paper]

In \(A=\mathbb Z[Z,W,T]\), define the **integral derivation**
\[
\delta Z=1,\quad\delta W=0,\quad\delta T=Z^{p-1}.
\]
Put \(P_{r,s,j}:=\delta^j(Z^{r-pk}W^sT^k)\in A\).
Under the rational-ring substitution \(\phi:T\mapsto(Z^p-W)/p\), the maps commute:
\[
\phi(\delta f)=\partial_Z(\phi f).
\]
This follows by checking the three polynomial generators, especially
\(\partial_Z((Z^p-W)/p)=Z^{p-1}\).
Consequently **for every ordinary j, including j≥p**:
\[
\boxed{
c_{r,s,j}(z)=
P_{r,s,j}(z,\bar z,q_p(z))\in O_D.
}
\]
This does NOT replace ordinary derivatives with Hasse coefficients. The formal auxiliary \(T\) represents a **single divided Frobenius polynomial**, and \(\delta^j\) performs the original ordinary derivative. The old expansion/inertness premises are unchanged.

If \(z'\equiv z\bmod p^2O_D\), then \(q_p(z')\equiv q_p(z)\bmod pO_D\). Indeed, write \(z'=z+p^2t\), expand \((z+p^2t)^p\), and observe that the numerator difference is divisible by \(p^2\) (in fact its \(z^p\) term by \(p^3\)), so division by p leaves a multiple of p. It follows that every normalized ordinary source jet satisfies

\[
\boxed{
c_{r,s,j}(z')\equiv c_{r,s,j}(z)\pmod{pO_D}.
}
\]

## Conjugate-stable original sampling collapses observation channels [P-paper]

Let \(T_p(Q)=|\{z\bmod p^2O_D:z\in Q\}|\) (equivalently count coordinate pairs \((x\bmod p^2,y\bmod p^2)\)). The normalized integer-pair matrix \(C_{0,p}\) has \(n=RS\) rows and \(2J|Q|\) real/imaginary channels. Within each \(p^2\)-class, all normalized jet values agree modulo p.

Because \(Q=\bar Q\), classes come in conjugate pairs. A class fixed by conjugation has normalized value fixed by conjugation modulo p, so its imaginary channel vanishes (p odd). A nonreal conjugate *pair* contributes at most two real/imaginary channels across its two classes: the real columns are equal and the imaginary columns opposite. Thus a collection of \(T_p(Q)\) distinct classes contributes at most **\(J T_p(Q)\)** independent \(\mathbb F_p\)-columns, not the naïve \(2J T_p(Q)\).

\[
\boxed{\operatorname{rank}_{\mathbb F_p}C_{0,p}
\le J T_p(Q)\le Jp^4.}
\]

This is a **uniform, source-typed first-layer rank theorem** for the original Frobenius-normalized ordinary jets. No global novel theorem claim is made; paper proof is not a Lean certification or an external referee report.

If the original integer \(E_D\) has characteristic-zero row rank \(n\), then \(C_{0,p}\) also does (old row change and p-division invertible over \(\mathbb Q_p\)). Let \(F_p=\sum_{r,s}k_{r,s}\) be the **already counted** old exponent. The first Smith nullity of \(C_{0,p}\) is at least \(\max(0,n-JT_p(Q))\), and Cauchy–Binet with the ORIGINAL integral trace metric yields

\[
\boxed{
v_p(\det G_D)\ge
2F_p+2\max(0,RS-JT_p(Q)).
}
\]
This is an additive **subleading** arithmetic saving of order at most \(O(RS)\) for a fixed prime, not the still-missing \(O(R^2S)\) extra valuation.

## How to combine DIFFERENT Smith depths without double-counting [P-paper]

Treat the normalized integer source as a homomorphism \(C_{0,p}^{\mathsf T}:\mathbb Z_p^m\to\mathbb Z_p^n\). For any subset \(I\) of its original rows, coordinate projection induces a **surjection**
\[
\operatorname{coker}(C_{0,p}^{\mathsf T})
\twoheadrightarrow
\operatorname{coker}(C_{0,p}[I,:]^{\mathsf T}).
\]
Assuming full characteristic-zero row rank, these are finite \(p\)-primary modules locally. For each \(h\ge1\), surjectivity induces a surjection on \(p^{h-1}M/p^hM\), so the number \(\gamma_h\) of Smith exponents at least h satisfies
\[
\boxed{\gamma_h(\mathrm{full})\ge\gamma_h(\mathrm{subset}).}
\]
In particular one may combine the independently verified **FULL first layer** with a selected-subset **second layer**:
\[
v_p(\det G_D)\ge
2F_p+
2\bigl(\gamma_1(\mathrm{full})+
       \gamma_2(\mathrm{subset})\bigr).
\]
This adds two DIFFERENT levels of the full Smith filtration. It does **not** add nested k≥2 and k≥3 rank defects, nor the old \(2F_p\) twice, nor the restricted pairing's unverified radical.

## Frozen source checks [M] and what they do NOT establish

[The source-replay script](frobenius_signature.py) evaluates every original row and ordinary jet at every point of each frozen Q, with all integer channels, checks congruent-class equality and exact conjugate pairs, compresses columns to one per real residue and two per nonreal conjugate orbit, and computes the rank of that compressed matrix.

| Original source | p | \(|Q\bmod p^2|\) | Ceiling \(J T_p(Q)\) | Actual full normalized rank | First nullity |
|---|---:|---:|---:|---:|---:|
| D283,R70,S=J2,Q169 | 3 | 27 | 54 | 36 | 104 |
| D283,R70,S=J2,Q169 | 5 | 75 | 150 | 60 | 80 |
| D403,R100,S=J4,Q219 | 3 | 27 | 108 | 90 | 310 |
| D403,R100,S=J4,Q219 | 5 | 75 | 300 | 240 | 160 |

For the SAME original D403 positive Gram, Phase208's independently preregistered k≥2 subset p²-Smith checks found \(\gamma_2(\mathrm{subset})=116\) at p3 and 45 at p5. Therefore:

| p | Inherited old \(F_p\) | Full \(\gamma_1\) | Subset \(\gamma_2\) | Extra index lower | Original \(v_p(\det G)\) lower |
|---|---:|---:|---:|---:|---:|
| 3 | 570 | 310 | 116 | 426 | **1992** |
| 5 | 550 | 160 | 45 | 205 | **1510** |

Hence the SAME integral determinant is divisible by \(3^{1992}5^{1510}\). These are **conservative finite lower bounds**, not exact Smith exponents for the full 400-row source, not a uniform class-number-one theorem, and not a stronger cutoff than \(322^4\).

The predicted *uniform* geometric signature ceilings for these frozen ellipses are \(|Q\bmod9|=27\), \(|Q\bmod25|=75\) because only \(y=-1,0,1\) occur and each horizontal slice contains all \(p^2\) residues of \(x\). At \(D403\), this implies even without measuring full ranks \(v_3\ge1956\), \(v_5\ge1390\) when combined with the separately measured second-level subset. The actual measured ranks improve those numbers.

**Necessary next theorem for a competitive bound:** control third and deeper full Smith layers \(\gamma_h\) on a source family at production \(R,S,J,Q\), so that \(\sum_{h\ge1}\gamma_h=\Omega(R^2S)\); or prove an extensive family of exponentially small analytic Schur modes. The uniform *first-layer only* rank collapse remains \(O(RS)\) and cannot alone provide a fixed normalized saving. Do not promote finite results into a class-number-one proof.
