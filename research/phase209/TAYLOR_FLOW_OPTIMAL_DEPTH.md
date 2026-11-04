# Phase209-A · optimal ordinary-jet depth by integral Taylor flow

**Scope/evidence (4 November 2026).** The new stronger theorem was posted **before testing** as a separately registered follow-on in [issue #154](https://github.com/Dojo-1/tenth-discriminant/issues/154). The arithmetic here is a paper proof [P-paper; Lean unformalized], followed by correlated exact AI-authored checks [M]. The theorem does **not** assert a new class-number-one cutoff. It preserves the existing integer-pair ordinary-Z derivative source, the original monomial rectangle, all original complete-ellipse samples, the original p3/p5 Frobenius rows, and the unchanged integral trace Gram.

## Integral carrier, not a Hasse derivative

Fix a rational prime p and A=Z[Z,W,T]. Set
\[
\delta=\partial_Z+Z^{p-1}\partial_T,\qquad
\delta Z=1,\quad \delta W=0,\quad \delta T=Z^{p-1}.
\]
For an auxiliary indeterminate H, define a rational-polynomial algebra map
\[
\Phi_H:A\to\mathbb Q[Z,W,T,H],\quad
Z\mapsto Z+H,\ W\mapsto W,\
T\mapsto T+\frac{(Z+H)^p-Z^p}{p}.
\]
The two maps \(f\mapsto\partial_H\Phi_H(f)\) and \(f\mapsto\Phi_H(\delta f)\) are derivations *relative to the same algebra map* \(\Phi_H\), and agree on the three generators. Therefore they agree on A. Iterating, and evaluating at H=0, yields **ordinary Taylor**:
\[
\boxed{\delta^j f=j!\,[H^j]\Phi_H(f)}
\]
for every j≥0 and every f∈A. The ordinary factorial is PRESENT, never inverted in the integer source. No Hasse derivative substitutes for the original evaluation.

For prime p, \(\binom pa/p\) is an integer for \(1\le a<p\). Hence
\[
\Phi_H(T)=T+\sum_{a=1}^{p-1}
  \frac{\binom pa}{p}Z^{p-a}H^a+\frac{H^p}{p}.
\]
The **only** possible negative p-valuation in that expression comes from H^p/p. A product term of total H-degree j uses at most \(\lfloor j/p\rfloor\) such factors. As a consequence
\[
p^{\lfloor j/p\rfloor}[H^j]\Phi_H(f)\in\mathbb Z[Z,W,T].
\]
Since \(v_p(j!)=\sum_{m\ge1}\lfloor j/p^m\rfloor\), multiplying by j! proves the **optimal** uniform p-adic depth bound:
\[
\boxed{\delta^j(A)\subseteq p^{E_p(j)}A,\qquad
E_p(j)=v_p(j!)-\lfloor j/p\rfloor
=\sum_{m\ge2}\lfloor j/p^m\rfloor.}
\]
The older characteristic-p restricted-derivation proof gives only the first term \(E_p(j)\ge\lfloor j/p^2\rfloor\). The additional p³,p⁴,… terms come from the exact integer flow, not from a second independent source divisor.

## Sharpness — including the actual old Frobenius rows

Write \(j=pk+a\), \(0\le a<p\), \(k=\lfloor j/p\rfloor\). For \(f=Z^aT^k\), evaluating \(\Phi_H(f)\) at Z=T=0 gives exactly \(H^j/p^k\). Thus
\[
(\delta^j f)(0,W,0)=j!/p^k,\quad
v_p((\delta^j f)(0,W,0))=E_p(j).
\]
No larger guaranteed power can divide \(\delta^j f\) for **all** integral f. Moreover this is not merely an abstract polynomial witness: choose the ORIGINAL transformed rectangular source row
\[
r=j,\ s=0,\ k_{r,s}=\lfloor j/p\rfloor
\quad\text{when }R>j,\ S>j,
\]
and
\[
F_{j,0}(Z,W)=Z^{j-pk}(Z^p-W)^k.
\]
This source polynomial is monic of degree j in Z while holding W constant. Consequently its original ordinary \(j\)-th Z derivative is **exactly j!**, at every sample. AFTER factoring the old p^k, the normalized jet is exactly \(j!/p^k\) with valuation \(E_p(j)\). Since production has J=S<R, this row exists for every original jet order \(0\le j<J\). **The per-column depth bound is sharp even within the unchanged original source.** This does NOT imply the determinant lower is sharp: rows/columns may still have additional relations.

## Typed source substitution

For odd inert p in \(O_D=\mathbb Z[u]/(u^2+D)\), the finite-field Frobenius agrees with conjugation, so \(q_p(z)=(z^p-\bar z)/p\in O_D\). The old unimodular row polynomial \(F_{r,s}=Z^{r-pk}W^s(Z^p-W)^k\) is sent to the integral carrier \(Z^{r-pk}W^sT^k\). The chain rule intertwines \(\delta\) with ordinary \(\partial_Z\), including orders \(j\ge p\). Therefore **after** the old row factor \(p^k\) (counted once),
\[
\boxed{p^{-k}\partial_Z^jF_{r,s}(z,\bar z)
  \in p^{E_p(j)}O_D.}
\]
Each integer real/imaginary channel in the actual source has this valuation. There is no map between different D or p, and no claim that p-inertness is true for arbitrary D.

With exact conjugate-pair observation folding and the unchanged Gram, the *candidate strengthened determinant lower* has column weight
\[
w_p(j)=E_p(j)\quad\text{rather than merely}\quad\lfloor j/p^2\rfloor.
\]
The standard weighted Cauchy–Binet minimum would replace every old weight by \(w_p(j)\) once the full original source identity, row-normalization and integer diagonal folded metric are formally connected. This is a stronger **conditional** divisor; it must NOT be added to the old p²-derived weight because it already contains it.

## Falsification / provenance

The claim \(\delta^j A\subseteq p^{\lfloor j/p\rfloor}A\) is **false**: \(\delta^p T=(p-1)!\not\equiv0\pmod p\). A proposed stronger exponent than \(E_p(j)\) is also FALSE by the sharp original source row above. At j=p³ the full depth is p+1 whereas the earlier p² estimate gives p; at j=p² both give 1.

[Exact independent test](taylor_flow_precision.py) checks the integral δ monomial recurrence against independent rational-H Taylor coefficients and against original ordinary-Z transformed row derivatives at p=3,5 through orders 2p³; 176 bounded cases passed locally before the script was committed. These computations are not external mathematical verification, and a passing CI is not a proof of a universal statement.

**Next formalization:** (1) prove the ordinary formal-flow identity in pinned Lean for concrete \`Phase209DeltaCarrier.delta\`; (2) formalize the valuation of coefficients via the single nonintegral H^p/p term; (3) connect these to the full original normalized row matrix after \`Phase209WholeGramFold\`; (4) establish the weighted Gram minor divisor; (5) re-prove 321-domain arithmetic/analytic/field bridges before changing the 322⁴ endpoint. Human review #50 and independent source audit #51 remain open, PR remains draft.
