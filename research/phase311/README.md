# Phase311 — the inert-prime tendril: source kernel **versus** trace radical

> Two distinct ways for arithmetic information to become invisible.
>
> **First:** an original polynomial row may vanish in the residue-field evaluation.
>
> **Second:** an evaluation direction may survive but pair to zero with the entire surviving image under the original Hermitian trace form.

The earlier split-prime duality (Phase310) did not prove these are the same mechanism at an **inert** prime. This experiment uses the genuine inert extension \(\mathbb F_{25}\), with the original source and original pairing, and tests both mechanisms separately.

This is a stacked, unmerged research draft on Phase310's merged research branch. No change to \`main\`, the original tenth-discriminant theorem, or the reported \(322^4\) cutoff.

## The carrier and two distinct kernels

For an imaginary quadratic maximal order \(O=\mathbb Z[\omega]\) with \(\omega^2-\omega+m=0\), take inert prime \(p=5\). Then \(k=O/5O\cong\mathbb F_{25}\), and conjugation equals the 5th-power Frobenius on \(k\).

Let \(E\) be the original polynomial ordinary-jet evaluation matrix over \(k\), and \(P_\tau\) the involutive permutation of the **actual** conjugation-stable observation columns (within each original ordinary-jet layer). Polynomial coefficients and the exactly divided integral source-normalized rows obey

\[
\overline E=EP_\tau.
\]

The original Hermitian trace Gram, reduced modulo 5, satisfies

\[
\boxed{G=\mathrm{Tr}_{k/\mathbb F_5}(E\overline E^{\,T})=2EP_\tau E^T.}
\]

Unlike a Euclidean same-side dot product, this is the restriction of the ambient conjugate bilinear pairing to the image of **the actual source map**.

If \(n\) is the number of original rows, \(r_E=\operatorname{rank}_{k}(E)\) and \(r_G=\operatorname{rank}_{\mathbb F_5}(G)\), then

\[
\dim\ker(E^T)=n-r_E,\qquad
\dim\ker G=n-r_G,\qquad
\boxed{\dim(\operatorname{rad}(\operatorname{im}E^T))=r_E-r_G.}
\]

The first quantity is a **source kernel**; the last is a **pairing radical on surviving evaluations**. They have different mathematical meanings and must never be added to a valuation formula without constructing the corresponding integral filtration.

## Three original-source controls

The CI independently computes \(\mathbb F_{25}\) ranks using genuine extension-field Gaussian elimination and realifies the full field map into an \(\mathbb F_5\)-matrix with twice the expected rank. It checks every trace-Gram cell against the actual conjugate point permutation, in both the original and primitive row frames.

| Field | Source | Expected original \((r_E,r_G)\) | Expected primitive \((r_E,r_G)\) | h1? |
|---|---|---|---|---|
| \(D=163\) | Matched \(\rho21,R40,S=J1\) | \((25,25)\) | \((40,40)\) | Yes |
| \(D=187\) | Same matched parameters | \((25,25)\) | \((40,40)\) | No |
| \(D=203\) | Native \(\rho24,R50,S=J2\), full Q263 | \((50,38)\) | \((100,63)\) | No |

The table records **previously observed parent predictions**, not new Phase311 measurements, until the new CI verifies them. Each primitive basis is obtained by exact original integral row shears and division by 5 on precisely 15 (D163/187) or 50 (D203) rows, not a global unimodular gauge.

If verified, D203's 50 integral /5 source divisions contribute an index-square factor of \(5^{100}\), while its primitive **37-dimensional pairing radical** contributes at least one further factor of 5 per radical dimension. Thus the SAME original Gram has the finite lower bound

\[
v_5(\det G_{203})\ge 2(50)+37=137.
\]

The prior exact Smith result \(v_5(\det G_{203})=138\) is a regression check, **not** deduced from the new rank computation. This 137 is not an independent additional contribution to the existing \`valuationWeight=45\` bound. In D163 and D187 the primitive pairing should be nondegenerate, yielding the already-known \(v_5(\det G)=30\).

The matched D163 and D187 profiles explicitly reject the assertion that **primitive trace nondegeneracy characterizes class-number-one**.

## Phase311-B — the one-dimensional secondary defect

The Phase311-A residue calculation gave rank 63 for the **primitive** 100-row Gram and therefore at least 37 positive 5-adic Smith exponents. This only guaranteed the original valuation lower bound 137. To resolve the difference with the earlier measured 138, we added **a separate preregistered derived-radical calculation**, not a new mathematical ontology.

Start with the original D203 evaluation at precision 5⁴=625 (necessary before **50 exact divisions** by 5), build the resulting primitive integral Gram modulo 5³=125, and perform *symmetric congruence* Schur elimination over the local rings:

```mermaid
flowchart TD
  O["ORIGINAL D203 100x1052<br/>ordinary jets, Q263"] -->|"50 exact shears and 50 divisions by 5"| P["Primitive 100x100 trace Gram<br/>mod 125"]
  P -->|"remove 63 unit directions"| R1["Residual 37x37<br/>entries divisible by 5"]
  R1 -->|"divide by 5; remove 36 units"| R2["Residual 1x1<br/>entries divisible by 5"]
  R2 -->|"divide by 5; final scalar is unit"| R3["No remaining radical"]
  R3 --> S["Primitive Smith 0^63, 1^36, 2^1<br/>exact v5(det)=38"]
  S --> G["ORIGINAL same Gram<br/>v5(det)=2x50+38=138"]
  G -. "must NOT add overlapping old weight45" .-> F["Uniform h1 bound still OPEN"]
```

The staged ranks are exactly **63, 36, 1**, with residual dimensions **100→37→1→0**. At the third stage no factor is censored. The original source's full **100×100 Gram factorization** is independently checked modulo 625, including the difference between integer-unimodular shears and non-unimodular /5 source divisions. A *separate* generic rectangular DVR Smith algorithm reproduces `{0:63,1:36,2:1}`; two nontrivial source congruences preserve the result. An off-diagonal-only symmetric unit block `[[0,1],[1,0]]` is a deliberate hostile test: a naive diagonal-only pivot algorithm would call it radical, but the correct odd-prime congruence exposes its units.

So the earlier reported original `v5(det G)=138` is now explained **without** a deep 5¹⁶ Smith computation: the finite staged calculation needs precision 5³ on the primitive Gram, after collecting the 5⁴ source digits required for exact division.

This is not a cohomological Bockstein, quantum tunnelling or a new global field bound; it is a genuine higher **DVR bilinear-form radical filtration**. Its proof obligations and stop rules were frozen in `PRE_REGISTERED_SECONDARY_RADICAL.md` after Phase311-A passed and *before* Phase311-B code.

## Phase311-C/D — 25 residue classes are enough for the original Gram mod 5

The **unnormalized original** polynomial/ordinary-jet source factors through the residue-class observation map. Count the number of genuine maximal-order observations in each of the 25 classes \(z\in\mathbb F_{25}\), call it \(m_z\), and reduce these multiplicities modulo 5. Let \(C\) evaluate the original polynomial rows once per residue \(z\) and once per original ordinary-jet order. Its **original** Gram modulo 5 is exactly

\[
G=\operatorname{Tr}_{\mathbb F_{25}/\mathbb F_5}
      (C\,\operatorname{diag}(m_z)\,\overline{C}^{\,T}).
\]

```mermaid
flowchart LR
  Q["Actual original maximal-order Q<br/>263 D203 or 537 D427 observations"] -->|"reduce each q mod 5"| W["25 multiplicities m_z<br/>in F5"]
  E["ORIGINAL monomial ordinary-jet rows<br/>R*S; NO /5 primitive normalization"] -->|"evaluate once per residue and jet"| C["Residue-jet matrix C<br/>25*J columns over F25"]
  W --> G["Weighted Hermitian trace Gram<br/>mod 5"]
  C --> G
  G --> R["Rank = J * nonzero residue weights<br/>IF C spans all 25*J columns"]
  R -. "not an integral primitive lift" .-> X["Cannot infer high 5-adic Smith<br/>or uniform class-one field bound"]
```

A precise *surjective-pullback theorem* explains the observed equality. Assume \(J\le5\), the genuine original norm-ball observations are conjugation-stable, every residue class occurs, and \(C\) has **full column rank \(25J\) over \(\mathbb F_{25}\)**. Then the weighted Hermitian form on the residue-jet space has rank \(J\,t\), where \(t=\#\{z:m_z\not\equiv0\bmod5\}\). Pullback through a surjective \(C^T\) preserves its rank. The conjugation-stable original source makes the matrix Frobenius-fixed, hence its trace Gram is twice this form with the same rank over \(\mathbb F_5\).

**These hypotheses matter.** The code includes a non-surjective two-channel counterexample where both weights are nonzero but the pulled-back form has rank zero; it correctly REFUSES the equality without full column rank. For ordinary jets of order \(\ge5\), ordinary derivatives vanish modulo 5, and the active quotient uses \(J_{\rm eff}=\min(J,5)\), not an invented higher-jet rank.

The fully original-source results (including the new larger *non-h1* control) are:

| D | Original R,S,J | Q | Nonzero-weight classes | Rank(C) / 25J | Original rank(G) | Restricted trace radical |
|---:|---|---:|---:|---:|---:|---:|
| 163 (h1) | 40,1,1 | 225 | 25 | 25/25 | 25 | 0 |
| 187 (non-h1) | 40,1,1 | 205 | 25 | 25/25 | 25 | 0 |
| 203 (non-h1) | 50,2,2 | 263 | 19 | 50/50 | 38 | 12 |
| 427 (non-h1) | 106,4,4 | 537 | 17 | 100/100 | 68 | 32 |

D427 uses \(\rho=42\) and **all maximal-order observations** under the original numerical \(R,S,J,\rho\) parameter formula, rather than the original *even-order* source. A ramified ideal of norm 7 and the impossibility of principal norm7 when \(m=107\) prove it is non-h1. The direct original evaluator was checked on a declared 10×10 Gram submatrix; D163/D187/D203 were checked on every original Gram cell. All four actual residue-jet maps have full column rank.

For D427, the original-parameter **valuationWeight formula** is \(w_5(106,4)=586\), so its doubled *formula value* is 1172, while the first-level unnormalized Gram nullity floor is \(424-68=356\). This numerical comparison **does not itself prove that the old divisibility theorem applies to this particular maximal-order lift**, and certainly does not yield a stronger field cutoff. It is a negative design-space control, not a positive theorem.

The code also adds five copies of a *synthetic duplicate* actual observation: the Gram modulo 5 remains unchanged, while the integral observation source is different. Hence the residue-count compression is **not permitted** on the /5-divided primitive source, which depends on genuine higher \(5\)-adic digits. See `PRE_REGISTERED_RESIDUE_MULTIPLICITY.md`, honest post-result `PRE_REGISTERED_RESIDUE_RANK_THEOREM.md`, and `residue_multiplicity.py`.

## Types and provenance

- **Original D203 source:** unchanged Phase304 100×1052 coordinate evaluator, cross-checked against the independent Phase307 source evaluator; all 263 actual maximal-order observations, both original ordinary \(Z\)-jets.
- **Original D163/D187 source:** unchanged Phase304 matched half-integral norm-ball (converted exactly into maximal-order \(\omega\)-coordinates), with a different arithmetic power evaluator checking every original coefficient.
- **Finite field:** genuine inert \(\mathbb F_{25}\) (not \(\mathbb F_5^2\) treated as coordinatewise ring); field inverse identities and Frobenius conjugation checked.
- **Operator:** actual observation conjugation and Hermitian trace; \(EP_\tau E^T\) is not a Euclidean proxy.
- **Evidence:** [P-paper] conditional Hermitian radical decomposition, [M after CI] source ranks and countercontrols, [H] novel uniform h1 bound, [S] Worldlet vocabulary, [R] extra prime mass from adding overlapping valuations or a h1 diagnostic from the primitive radical.

## Reproduction and stop rule

Frozen prior-to-code plan: \`PRE_REGISTERED_INERT_TRACE_RADICAL.md\`. Source and hostile tests: \`inert_trace_radicals.py\` and \`test_inert_trace_radicals.py\`. CI: \`.github/workflows/phase311-inert-trace.yml\`.

A failed original-source entry, incorrect \(\mathbb F_{25}\) inverse, unequal direct/realified extension-field ranks, false conjugation permutation, or incorrect Gram trace forces correction rather than architectural escalation. The experiment cannot be merged into \`main\` or used to revise the original tenth-discriminant cutoff without an independently supported uniform field theorem.
