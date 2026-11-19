# E28 — THE CONDUCTOR REMEMBERS

*19 November 2026 · source-exact local residue worldlets · draft research*

## The actual source

E24-E27 transport the **original integer-pair quadratic algebra**, ordinary-Z derivatives, positive trace pairing, rectangular Gram and sample support along

```text
iota_k : A_(D k^2) -> A_D
(x,y) |-> (x,k*y)
A_D = Z[t]/(t^2 + D)
```

The inclusion is injective for positive k, but not lattice-surjective for k>1.
This new E28 file reduces those **same coefficient pairs** modulo m. It does
not substitute a different trace Gram or a selected p-adic minor.

## Local exact source identity

Let R_(D,m) = (Z/mZ)[t]/(t^2+D), presented by coefficient pairs.
The induced map is

```text
r_(m,k) : R_(D*k^2,m) -> R_(D,m)
(a,b) |-> (a,k*b)
```

and intertwines multiplication, conjugation and nested frame compositions.
The diagram from original Z-pairs to mod-m observations commutes.

As a module map on two coefficients its determinant is k mod m.
Therefore this map is an isomorphism of unital quotient rings **exactly if**
gcd(k,m)=1: inverse coefficients scale by the modular inverse of k.
For gcd(k,m)>1 it has a nonzero kernel. The general gcd equivalence is
paper mathematics in this round, **not** a new Lean declaration.

## The two finite original-witness controls (D=1,k=2)

**Good modulus 5:** multiplication by 2 is invertible modulo 5 with inverse
3. E28 proves both sided inverses and full bijectivity of r_(5,2).
Because multiplication is preserved, this is a ring isomorphism of the
**declared** modular pair rings.

**Bad modulus 2:** r_(2,2) maps both (0,0) and (0,1) to (0,0).
E28 proves failure of injectivity, and proves that the source ring
R_(4,2) has a *nonzero square-zero element* (0,1). Its imaginary
coefficient cannot be reconstructed by any decoder from the transported
pair alone. This is an honest typed information loss.

The example illustrates the familiar role of the conductor. The index
k controls which modular coefficient observers are faithful. This is
not a new theorem about all maximal orders or arbitrary number fields.

## Gaussian split primes — labels must move

At modulus 5, the Gaussian target factors 5=(2+i)(2-i) and the two
labelled probes are represented by a-2b and a+2b. Conjugation swaps
these probes rather than erasing them. E28 proves a concrete moving-label
identity and a distinct labelled-residue witness, complementing
Hardness Kernel HK-031. No general ideal or valuation API is claimed.

## The moving-moving-frame remainder

The correct invariant is a *typed reconstruction contract*: retain
coefficients, original support, index/conductor data, declared operations,
observer labels and the ability (or inability) to reconstruct future
queries. The mod-2 remainder is a nontrivial kernel/failure of decoding,
NOT an independently established geometric curvature or hardness signal.

## Cross-line gates

- **Tenth Discriminant:** this establishes no improvement of the published
  322^4 actual-field theorem. The draft 307^4 route separately requires
  a full-root source and axiom audit, source semantics and external review.
- **Hardness Kernel:** HK-029 through HK-031 form a research-only stack.
  This exact modular phenomenon is a candidate test object, not a proof
  of a new complexity lower bound.
- **Source equivalence:** positive original-jet-Gram preservation on
  image-transported finite Q does not assert equivalence after adding
  arbitrary destination lattice nodes.
- **Degeneracy:** the pair-algebra identities make sense at D=0, but D=0
  is the nonreduced dual-number algebra, not a quadratic number field.
- **Infinite towers:** Z[2^n i] intersection and the inverse system
  Z/2^nZ have different carriers, maps and limits; no infinite-limit
  statement was formalized by E28.

## Reproduction contract

```sh
cd lean
lake exe cache get
lake build TenthDiscriminant.E28ConductorResidue
lake build
python3 audit.py
python3 negative_controls.py
```

Exact focused workflow: `.github/workflows/e28-conductor-residue.yml`.
The Lean file ends with explicit `#print axioms` declarations.
**Until exact-head CI is green, E28 remains a proposed Lean proof file, not
a certified Lean result.** Its branch is deliberately separate from main.

## Next discriminating stages

1. Formalize the gcd(k,m) equivalence with Mathlib's ZMod units, including
   the nontrivial kernel at bad moduli and a total forward ring equivalence
   at good moduli.
2. Move from pair presentations to genuine ideals of Z[i], valuations and
   the local structures of nonmaximal orders; test the conductor prime 2.
3. Transfer into the one original integer trace-Gram source only through
   exact witness/provenance-preserving maps.
4. Test whether local ideal certificates, as opposed to mere trace
   equivalences, contribute a new source-locked arithmetic lower estimate.
5. Retain the current 307^4 proposal as draft until its root audit passes.

*An invariant is not merely what remains numerically unchanged. It is what
can be reconstructed, with its witnesses, after the world itself moves.*
