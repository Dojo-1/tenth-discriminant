# Phase303 formal theorem targets and actual field-bridge obligations (NOT yet Lean-proved)

**13 November 2026.** These are exact proposed statements and proof sketches, NOT new Lean kernel certificates. They are meant to prevent a green CI badge, a reparametrization, or a finite-field rank computation being promoted to a tenth-discriminant theorem. The original field bound remains `|disc(K)| < 322^4`, with the lower 321^4 attempt still in separate draft PR #157. Source statuses follow [OBSERVED_MAXIMAL_ORDER_AND_FIELD_BRIDGES.md](OBSERVED_MAXIMAL_ORDER_AND_FIELD_BRIDGES.md).

## Target T1 — maximal-order trace and p5 localization [P-paper; Lean open]

Let `D=163`, `ω²−ω+41=0`, `R=Z[ω]`, and `R0=Z[sqrt(-163)]`. Define `φ(x,y)=(x−y,2y)`. Prove:

- `φ` is a multiplicative injective map from R0 to R preserving norm and trace pairing;
- determinant of the underlying Z-module map is exactly2;
- `Bω=[[2,1],[1,82]]` has `det Bω=163`;
- `Tᵀ Bω T=diag(2,326)` for `T=[[1,-1],[0,2]]`;
- localized at p5 the suborder inclusion is an isomorphism because 2 is a unit of Z5.

**Semantic gate:** This compares the TWO algebraic orders under the SAME element or literal finite support. It does NOT compare original Q109 with new full maximal support Q225; the latter gains 116 new points.

## Target T2 — Frobenius primitive-Gram Smith factorization [P-paper conditional; Lean open]

For odd prime p, integral observation matrix E with 40 row generators and integral nondegenerate trace metric B, assume the first25 rows are primitive in mod5 trace pairing. Suppose for r=25..39 an integral unimodular row operation makes rows E_r−E_(r−24) divisible5 and let Eprim be the resulting 40×m integral matrix with last15 rows divided5. Suppose `Gprim=Eprim B Eprimᵀ` is unimodular modulo5 AND its first25 leading block is also unimodular modulo5.

Prove the original `G=E B Eᵀ` has p5 elementary divisor profile EXACTLY `{0:25,2:15}`, and
```
 v5(det G)=30.
```
**Proof plan:** `U G Uᵀ=D Gprim D`, `D=diag(I25,5 I15)` and U unimodular. Schur-eliminate the first25 unit block over Z5. Its primitive Schur complement is unit mod5 because Gprim is unit; the lower 15 block is then 25 times a unit block, so exactly fifteen grade2 factors. The general determinant claim only needs Gprim unit, while the FULL Smith profile additionally needs the leading25 unit block.

**Semantic gate:** Eprim is a SATURATED EVALUATION superlattice, not the original polynomial row lattice. The original G's p5 exponent30 is **already the counted factor**. The identity does not create a new, independent number-field discriminant valuation or a universal bound.

## Target T3 — finite-field support and weighted trace rank [P-paper conditional; Lean open]

Let S⊂F25 be a finite Frobenius-stable subset, m:S→F5^× Frobenius-invariant, and choose n≥|S| polynomial rows 1,z,...,z^(n−1). Define
```
 G_ij = Σ_(z∈S) m(z) Tr_F25/F5(z^i (z^j)^5).
```
Prove `rank_F5(G)=|S|`.

**Proof idea:** The product over Frobenius orbits of irreducible minimal polynomials is separable and has degree |S|. The Chinese remainder theorem identifies F5[z]/I(S) with the full Frobenius-compatible function algebra on S, and polynomial monomials of degree <|S| span it. Finite-field trace is perfect on each factor; nonzero, Frobenius-consistent m is a unit weight, so the direct-product trace pairing is nondegenerate.

**Negative control:** if some multiplicity m(z)=0 mod5 the resulting Gram can lose rank despite the same distinct residue support. Thus observation count and distinct-class count without multiplicities are incomplete evidence.

## Target T4 — norm/split-prime necessary h1 condition [P-paper classical; Lean open]

For squarefree D≡3(mod4), D>3, maximal quadratic order `Z[(1+sqrt(-D))/2]`, norm form `N(a+bω)=a²+ab+((D+1)/4)b²`, and h(K)=1:

For all rational primes `p < (D+1)/4`, prove p cannot split in K.

**Proof:** p split gives a prime ideal of norm p; class-one makes it principal and so N(z)=p. If b=0 N(z)=a² not a prime. If b≠0, N(z)=(a+b/2)²+(D/4)b²≥(D+1)/4 for odd b, and if |b|≥2 the lower bound is even greater. Contradiction. This is classical and independent of trace Gram G on any finite observation set.

**Counterworld:** D23: split primes2,3 below6; neither represented, so class number is not one. D163: all primes below41 are inert. The initial Phase303-C AI test had a wrong assertion omitting split3 in D23; it failed and was corrected with receipt preserved.

## Target T5 — source policy and impossibility of an actual known-h1 high-jet control

The original source `J(D)=⌊⌊D/4⌋/25⌋`. For the nine known h1 imaginary quadratic radicands, `D≤163`, so `J(D)≤1`. A source-faithful J≥2 requires D≥200, thus cannot be simultaneously a member of the classical list. This is a trivial arithmetic result conditional on the classical classification, NOT a proof of the class-number-one classification. Treat hypothetical h1 fields at D>163 separately from empirical actual h1 sources. One may define NEW high-J controls at D163, but that changes the original source-policy semantics.

## Target T6 — missing universal field/zero-free implication [H, not even a checked lemma]

A genuinely useful new tenth-discriminant theorem needs a statement of the form:

```
For ALL fundamental imaginary quadratic fields K
with h(K)=1 and discriminant size d≥D0,
the ORIGINAL source Gram (constructed uniformly in d) satisfies
property P(d), and P(d) contradicts an independently justified
arithmetic/analytic bound for all d≥D0.
```

The exact P(d) MUST be spelled out; candidates include an invariant determinant/Smith inequality, a norm-representation obstruction, or analytic control tied to zeta_K and Dirichlet L(s,χ). Merely being in a moving flag orbit with large `epsilon` is RETIRED as source of extra field mass (Phase302); fixed D163 maximal-order source v5(det)=30 is insufficient to constrain all d; the local order map at p5 says nothing about sampling Qfull vs Qeven; neither the class-number-one list nor finite tests substitute for a novel proof if the intended aim is a new method toward ruling out Siegel zeroes.

Existing Tao blog reports of stronger bounds/formal work are source-reported until actual proofs and kernel dependency closures are inspected; our integrated bound is not improved by Phase303. Novelty of any proposed new inequality is NOT checked.

## Actual proof-assistant implementation boundary

Before any Lean PR, inspect the live mathlib version, definitions of `NumberField.discr`, quadratic field ring of integers, ZMod/finite field trace, and applicable `Matrix.det` / Smith APIs; write the exact intended theorem statements and a separate source-to-field correspondence lemma. A trivial ring-coordinate matrix proof is feasible; a Lean theorem about a CUSTOM finite Gram alone is not a proof of a bound on `NumberField.classNumber`. Require `#print axioms`, no `sorry`/nonapproved custom axioms, and independent comparator review before upgrading evidence. Our current root Lean CI checks existing code and is NOT a Phase303 formal proof.

**Research next step:** independent exact (p,q)-half-integer maximal Gram and DVR Smith replay (preregistered F) is the best available near-term evidence against correlated implementation mistakes. After that, select ONE minimal T1/T2/T3 formalization with explicit Mathlib imports and a proof-to-field-type boundary. Stop expanding the number of flags if no new field-to-source implication is established.
