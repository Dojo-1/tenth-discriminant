# Phase181 follow-up — fixed extraction and transported normalization

*3 November 2026 · bounded exact arithmetic controls; **not** a new discriminant bound.*

The Phase179 rational half-shear and Phase181 normalized binary Smith filtration revealed a real distinction, but not a universal obstruction. A change of polynomial basis can leave the **original** integer Gram equivalent while changing a **residual** Gram computed with a fixed weighted normalization. Such a change is not necessarily information loss if the normalization is transported as part of the object.

## Freeze the original source

On the unchanged ordinary-Z-jet support, let the integer observation matrix be $E$, let the original trace metric be $B=2C$, and let $U$ be Phase162's monic unimodular integer row basis. Its checked source factorization reads

$$
UE=\Delta N,\qquad
\Delta=\mathrm{diag}(2^{k_1},\ldots,2^{k_m}),\qquad
H=NCN^{\mathsf T}.
$$

The source Gram remains $G=EBE^{\mathsf T}$, with exactly the original point support, derivative convention, column channels, and weights. The established binary exponent is counted once; H is its integral residual, not a replacement field discriminant.

For an integral row gauge $V$ with determinant $\pm1$, set $E'=VE$. There are two genuinely different normalization contracts.

## Contract A: keep the original extractor fixed

Keep $U$ and $\Delta$. Then

$$
N'_{\mathrm{fixed}}=\Delta^{-1}UVE
=KN,\qquad
K=\Delta^{-1} A\Delta,\qquad A=UVU^{-1}.
$$

Here $A$ is integral unimodular, but K may have rational entries. For the **entire extraction lattice** to be preserved, rather than merely the quotient on one particular E, require

$$
K\in\mathrm{GL}_m(\mathbb Z)
\quad\Longleftrightarrow\quad
2^{\,k_i-k_j}\mid A_{ij}
\quad\text{for every }k_i>k_j.
$$

Indeed $K_{ij}=2^{k_j-k_i}A_{ij}$. The divisibility conditions make K integral; $\det K=\det V=\pm1$ then makes its inverse integral. In this compatible case the residual Gram satisfies $H'=KHK^{\mathsf T}$ and all Smith factors and 2-primary cokernel layers agree.

This condition is **not necessary** for accidental equality of a particular Gram's Smith factors, nor for one specially divisible $N'_{\mathrm{fixed}}$ to be integral. It characterizes the *full weighted lattice stabilizer*.

## Contract B: transport the extractor with the basis

Move the extractor contragrediently: $U'=UV^{-1}$, keeping the diagonal extraction weights attached to the transported rows. Then

$$
N'_{\mathrm{moving}}
=\Delta^{-1}U' E'
=\Delta^{-1}UV^{-1}VE
=N.
$$

The normalized residual H returns *exactly*, even if the old fixed extractor was incompatible. This is a passive representation change, and the original filtered certificate is not intrinsically destroyed. The anchored comparison and the fully transported comparison answer different questions.

## Two exact falsification fixtures

Choose $U=I$, $\Delta=\mathrm{diag}(1,2)$, $N=2I$, $C=I$ and $E=\Delta N$. Both gauges act integrally on the **original** Gram and retain Smith factors $(8,32)$.

| Original gauge V | Induced K | Smith factors of fixed residual H' | Smith factors with moving extractor |
| --- | --- | --- | --- |
| $\begin{psmallmatrix}1&1\\0&1\end{psmallmatrix}$ | $\begin{psmallmatrix}1&2\\0&1\end{psmallmatrix}$ | $(4,4)$ | $(4,4)$ |
| $\begin{psmallmatrix}1&0\\1&1\end{psmallmatrix}$ | $\begin{psmallmatrix}1&0\\1/2&1\end{psmallmatrix}$ | $(1,16)$ | $(4,4)$ |

Both fixed-extractor quotients happen to be integral for this specially divisible N. The incompatible K nevertheless changes the residual Smith factors without changing the original Gram's integral equivalence class. A stronger claim that **every** original integral gauge preserves the fixed-extractor barcode is therefore **retired**.

The [executable exact control](phase181_filtered_gauge.py) adds 256 exhaustive 2x2 small shear/exponent cases, with no random oracle or floating-point tests.

## Source-matched D19 guard

The executable additionally targets the unchanged Phase181 D=19, R=8, S=4 historical six-point support. It reconstructs the Phase162 triangular monic U independently of the existing normalization routine, verifies UE=Delta N, and compares two integer shears in the U-coordinate frame:

- one admissible shear with coefficient 2 where $k_i-k_j=1$: the fixed quotient remains integral and the source residual Smith barcode must agree;
- one incompatible shear with coefficient 1: the fixed quotient must exhibit an odd-channel divisibility failure, while the **transported** extractor returns the original N exactly.

Unlike the standalone fixtures, this source-matched execution requires repository modules and their pinned dependency environment. Until a tracked exact-head run succeeds, it is a **test target**, not a confirmed source-level result. The translated/altered row basis is a gauge control, **not** a new admissible observation support for the field theorem.

## Evidence and stop rules

- **P (classical/paper):** the lattice-stabilizer equivalence and passive-extraction identity follow by elementary algebra, with their fixed-reference hypotheses explicit. Generic Lean formalization remains an open target.
- **M (local only):** 256 exact arithmetic compatibility cases and the two standalone Smith fixtures passed. Source D19 and GitHub CI are not yet promoted.
- **R:** unqualified gauge invariance of a *fixed* normalized residual, and the claim that a failed anchored comparison necessarily means intrinsic loss.
- **H:** source-specific compatibility as a generally useful tool to obtain uniform, non-double-counted residual 2-primary divisors for the actual thin ellipse. No such bound is presently proved.
- **S:** the Worldlet vocabulary is optional explanatory language; no geometric lift or complexity-theoretic theorem is inferred.

**Kill condition:** failure of source-exact ordinary jets, one changed trace weight, division by an unproved power of 2, a false original-frame inverse, failure of negative controls, or a source mismatch. **Stop:** do not add a harder ontology or improve a field endpoint based solely on a changing barcode; independently audit the original Gram and the source-specific logarithmic comparison first.

The actual-field result and its independent semantic reconstruction remain under [Issue #50](https://github.com/Dojo-1/tenth-discriminant/issues/50). The normalized-filtration target remains [Issue #99](https://github.com/Dojo-1/tenth-discriminant/issues/99). The separate Phase182 **375^4** numerical candidate is tracked in [PR #102](https://github.com/Dojo-1/tenth-discriminant/pull/102) and is not part of this appendix.
