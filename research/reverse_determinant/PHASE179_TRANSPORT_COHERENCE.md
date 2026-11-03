# Phase179 — What survives a change of mathematical world?

**3 November 2026 · proposed formal transport audit · no new discriminant bound.**

The source of this experiment is the Tenth Discriminant ordinary-$Z$-jet integer trace-Gram certificate: integer observation matrix $E_Q(D,J,R,S)$ on **the original lattice-pair support**, paired with the original trace weights $(2,2D)$. The field discriminant and class number are distinct invariants from its auxiliary $\det G_Q$.

[Phase156](PHASE156_TRANSPORT_ARCHIM_JETS.md) already distinguishes a moved PSD cone/order unit from a fixed-reference coordinate artifact. The earlier project had already proved source-specific passive translation, radial/arithmetic integer-frame determinant preservation and noncommutation in [ProofTransport.lean](../../lean/TenthDiscriminant/ProofTransport.lean) and [PassiveTransport.lean](../../lean/TenthDiscriminant/PassiveTransport.lean). This phase must **not claim those familiar facts as novel**, nor invent a higher-dimensional new object before testing the exact information that escapes a scalar.

## A typed transport contract

There are at least four *different* transformations. They should not be collapsed into the single label "transport":

1. **Integral gauge**: $U\in\mathrm{GL}_n(\mathbb Z)$, acting $E\mapsto UE$ and $G\mapsto UGU^{\mathsf T}$. The original integer source support $Q$ is unchanged. The Gram determinant, all its integral prime divisors, and the integral row-lattice equivalence are preserved. $\det U=\pm1$ is sufficient here.
2. **Rational gauge**: $T\in\mathrm{GL}_n(\mathbb Q)$. The determinant obeys $\det(TGT^{\mathsf T})=\det(T)^2\det G$. This is a *rational* metric statement; even when $\det T=1$, it need not preserve the *integral* lattice or the integer nature of the source Gram representation.
3. **Change of support**: $Q\to Q'$. This changes $E_Q$, may preserve the integer column image, and generally changes $G_Q$. Phase144–147 exhibit this difference in finite examples. Image adequacy and metric volume must be tested separately.
4. **Orbit descent / Fourier change**: conjugation representative reduction with signed channel and multiplicity data can reconstruct the original integral image; a naive sum/difference Fourier transformation is *not* a $\mathbb Z$-unit and can introduce 2-primary defects. See [Phase151](PHASE151_CONJUGATION_WORLDLET.md).

This is not a global "connection" or sheaf theorem. Each square needs a declared category, structure, forward map, return map (if one exists), and typed remainder. A numerical failure after transporting *only* $G$ but not the observable's grading $P$ is a gauge artifact, not intrinsic curvature.

## The determinant-one rational counterworld

Let
```math
H=\begin{pmatrix}1&\frac12\\0&1\end{pmatrix}\in\mathrm{SL}_2(\mathbb Q).
```
For any $2\times2$ rational matrix $G$,
```math
\det(HGH^{\mathsf T})=\det G.
```
Thus even the complete prime-valuation profile of this determinant is unchanged.

Yet $H\notin\mathrm{GL}_2(\mathbb Z)$. Let $L=\mathbb Z^2$ and $L'=H\mathbb Z^2$. An integer pair $(x,y)\in L$ belongs to $L'$ exactly when $H^{-1}(x,y)=(x-y/2,y)$ is integral, i.e. when $y$ is even. Therefore
```math
L\cap L'=\mathbb Z(1,0)\oplus\mathbb Z(0,2),\quad
L/(L\cap L')\cong\mathbb Z/2,\quad
L'/(L\cap L')\cong\mathbb Z/2.
```
Both covolumes agree, **both relative quotient groups are nontrivial**, and neither is determined by $\det H$.

For ANY $T\in\mathrm{GL}_n(\mathbb Q)$, the correct oriented relationship is
```math
|\det T|=\frac{[L:L\cap TL]}{[TL:L\cap TL]}.
```
The determinant collapses two index profiles to their quotient. In particular, the pair $(2,2)$ for the half-shear cancels to a determinant-one result.

**Reference correction:** $H:L\to L'$ is nevertheless an abstract isomorphism of $\mathbb Z$-modules. If one *also* transports the ambient reference lattice, then there is no intrinsic information loss. The two-sided index pair is a genuine defect only **relative to the anchored original integer coordinate lattice** required by the arithmetic certificate. A passive reparametrization and a proposed new matrix on a fixed source lattice are different tasks.

An even stronger false positive has BOTH integral positive-definite Grams:
```math
G_0=\begin{pmatrix}4&0\\0&4\end{pmatrix},\quad
G_1=HG_0H^{\mathsf T}=\begin{pmatrix}5&2\\2&4\end{pmatrix}.
```
Both determinants are $16$, hence all determinant valuations agree, yet their Smith invariant factors are respectively $(4,4)$ and $(1,16)$. Modulo 2 their ranks are $0$ and $1$, so no integral unimodular congruence between them exists. Equal integral Gram determinants do **not** imply identical prime-local module structure. This negative control is a classical, exact arithmetic fact, not a new difficulty theorem. This is the smallest decisive obstruction to taking "same determinant" as "same integral certificate." A determinant-one rational matrix can have an invisible *balanced denominator debt*.

The [Lean module](../../lean/TenthDiscriminant/TransportCoherence.lean) targets the universal rational determinant rule, source-exact integer-unimodular determinant/divisor transport, and a proof that this half-shear is **not** the rational cast of any integral matrix. The independent standalone $2\times2$ arithmetic oracle checks the intersection and both indices, but does **not** by itself establish a universal lattice theorem in Lean.

## Fourier loss and metric compensation are different

For
```math
F=\begin{pmatrix}1&1\\1&-1\end{pmatrix},
\qquad \det F=-2,\qquad
\mathbb Z^2/F\mathbb Z^2\cong\mathbb Z/2,
```
the fixed-metric congruence multiplies a Gram determinant by four, not one:
```math
\det(FGF^{\mathsf T})=4\det G.
```
Modulo $2$, $F$ has rank one.

**Type distinction:** $\det(FGF^{\mathsf T})=4\det G$ describes a *row-frame congruence*. Phase151's genuine source counterworld acts instead on the observation/jet **columns** $E'=EF$, yielding $G'=EFBF^{\mathsf T}E^{\mathsf T}$ if the metric B is fixed. These expressions have different carriers and may not be identified. Only the *channel metric* compensation $B'=F^{-1}BF^{-{\mathsf T}}$ makes $E'B'E'^{\mathsf T}=EBE^{\mathsf T}$. The toy 2×2 formula is a diagnostic, not a silently substituted source Gram.

But using the *contravariantly transported* metric $B'=F^{-1}BF^{-{\mathsf T}}$ gives $FB'F^{\mathsf T}=B$ over $\mathbb Q$. In the explicit toy with the original channel weights $B=\mathrm{diag}(2,38)$, even $B'=\begin{psmallmatrix}10&-9\\-9&10\end{psmallmatrix}$ remains integral. **This does not promote $F$ into $\mathrm{GL}_2(\mathbb Z)$.** Integrality of a compensated metric is not integrality of its witness transport.

## Original-ordinary-jet D=19 matched control

Use only the previously source-matched six-point support $Q_6$, $D=19,R=8,S=J=4$, the original ordinary derivatives and $B=\mathrm{diag}(2,38,\ldots)$. Under integer translation $T_2$,
```math
E_{Q_6+(2,0)}=T_2 E_{Q_6},\qquad
G'=T_2GT_2^{\mathsf T},\qquad\det G'=\det G.
```
Transporting the parity grading as $P'=T_2PT_2^{-1}$ must preserve the exact ratio
```math
\frac{\det\bigl((G+PGP^{\mathsf T})/2\bigr)}{\det G}.
```
Holding $P$ fixed while moving $G$ changes that ratio and is an intentionally invalid comparison. The D=19 $(+2,0)$ translated support is **outside** the original ellipse: this is a representation/gauge negative control, **not** an admissible new source for the field bound.

The [executable test](phase179_transport_coherence.py) uses (i) an independent $2\times2$ oracle, and (ii) the original Phase140/144 ordinary-jet evaluator cross-checked against the distinct Phase147 parameterized evaluator. It prints no invented runtime benefits. The mainline finite workflow must run it alongside historical regressions.

## World and provenance

The broader use of integral module/cokernel data is established mathematics. [Fink–Moci, *Matroids over a ring*, JEMS 18 (2016)](https://doi.org/10.4171/JEMS/600) formalizes module-valued matroid information that includes what ordinary rank discards. We do **not** claim that arithmetic matroids, Smith forms, determinant lines or module transport are invented here. Our bounded research contribution is a *source-typed* audit of these mechanisms on this ordinary-jet certificate.

## Evidence and next promotion gates

- **P (pre-existing)**: integer source-Gram factorization and guarded prime divisibility, translation/passive-polynomial identities, the checked $\lvert\mathrm{disc}(K)\rvert<377^4$ declaration relative to its definitions/axioms.
- **P (proposed, not yet promoted)**: the new generic congruence and rational-shear Lean declarations until focused pinned Lean and whole-root axiom/source/negative-control checks pass.
- **M**: exact bounded $2\times2$ and source-matched D=19 controls *only once their exact-head CI is green*.
- **R**: "det(T)=1 guarantees integral witness equivalence"; "a Fourier compensation automatically preserves integral lattices"; "fixed-grading parity after a gauge move diagnoses intrinsic geometry."
- **H**: a typed, resource-aware hardness invariant across multiple regimes; any uniform support selection with improved analytic upper; any strengthened field cutoff from this experiment.
- **S**: "Worldlets", "holoportation" and "polycosmic" as names for the typed architecture. No claim of sheaf cohomology, quantum hardware, actual closed-loop holonomy or a physical mechanism.

**Complexity/hardness gate:** even an integral isomorphism need not preserve an operational resource budget if constructing or applying the forward/inverse map expands bit lengths, oracle access or witness complexity. Any proposed complexity-theoretic hardness transport must state efficient forward, return and certificate maps, task correspondence and matched resource costs. Algebraic frame invariance alone is not a hardness equivalence. A change in D creates a new family member, not automatically a coordinate change of one underlying field.

**Kill condition:** any code or theorem purporting to infer integral equivalence from rational det-one, any misidentified source Gram, or any failure to reproduce the exact 2-primary counterworld. **Stop condition:** do not design a richer general geometry until this first square and its negative controls pass and a nontrivial further obstruction can be identified without changing definitions.

Keep [independent semantic reconstruction #50](https://github.com/Dojo-1/tenth-discriminant/issues/50) open. Existing formal actual-field results do not become externally accepted because this transport demonstration passes.
