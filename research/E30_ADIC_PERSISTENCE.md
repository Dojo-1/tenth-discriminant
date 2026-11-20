# E30 — THE KERNEL THAT DISAPPEARS, THE TARGET THAT DOES NOT

*19 November 2026 · source-locked finite adic clock counterworld*

## A precise falsifier for scalar residual narratives

Consider multiplication by 2 on each coefficient-observer world Z/2^nZ.
At n=1,2,3,4 the finite source kernel has **exactly two elements**:
```text
K_n = {0, 2^(n-1)}  in  Z/2^n Z
|K_n| = 2.
```
The source kernel therefore looks perfectly stable to a scalar count.
But the actual transition `K_(n+1) -> K_n` induced by reduction is
**the zero map**: both its source elements reduce to zero.

E30 encodes exact universal finite witnesses for 4→2, 8→4 and 16→8;
it also forbids lifting the nonzero mod-2 source ambiguity to a
compatible kernel element modulo 4.

This is an explicit negative control: constant finite kernel cardinality
does **not** imply a nonzero persistent inverse-limit witness.

## Opposite behavior of the target remainder

At every tested depth, the target coefficient 1 is *not* in the image
of multiplication by 2. Its observation is compatible under every
natural reduction. Unlike the ephemeral source-kernel witness, the
missing target coset persists.

Classical paper-level generalization:
```text
ker(2 : Z_2 -> Z_2) = 0
coker(2 : Z_2 -> Z_2) = Z/2 Z.
```
For any prime p and e>0:
```text
|ker(p^e : Z/p^n Z -> Z/p^n Z)| = p^min(e,n).
lim_n ker(p^e mod p^n) = 0.
coker(p^e : Z_p -> Z_p) = Z/p^e Z.
```
The general infinite-limit and cokernel statements are **not** claimed
as Lean-verified by E30. They are independent mathematical arguments
whose carriers and bonding maps must be defined before formal promotion.

## What the finite Lean file proves

- Exact constant kernel cardinality at moduli 2,4,8,16.
- Actual reduction maps of original residue representatives.
- All tested higher-level source kernels collapse to zero on reduction.
- No compatible nonzero lower-level source ambiguity at the next level.
- Missing target 1 at all tested levels.
- Compatibility of this target observation under clock reduction.

The source of all examples is E29's genuine coefficient-pair frame,
not a substitute Gram or an abstract numerical surrogate.

## Negative inference controls

A stable count is not a nonzero invariant element.
A finite noninjectivity certificate is not proof of infinite-limit
noninjectivity.
A source kernel and a missing-target cokernel are differently typed
objects and may have different persistence.
A classical p-adic limit does not imply an improved class-number-one
field-discriminant cutoff, ETH lower bound or solver speedup.

## Cross-branch integration

- E24-E27: exact index-k integral source embedding and original source Gram.
- E28: local residual good/bad modular transport.
- E29: general invertibility gate and observer fibers.
- E30: compatibility maps and source/target asymmetry across clocks.
- HK-032: two labelled good-prime observers recover the entire Gaussian
  coefficient world modulo 5 even where a scalar trace cannot.
- 307^4 candidate: source-bound investigation and independent semantic
  reconstruction remain entirely separate.

## Proof status and promotion rule

`lean/TenthDiscriminant/E30AdicPersistence.lean` contains finite Lean
theorems plus explicit `#print axioms` calls; the pinned
`.github/workflows/e30-adic-persistence.yml` is the focused gate.
Do not present E30 as formally verified until exact-head CI is green.
Do not claim the infinite p-adic statements as Lean theorems from these
finite tests.

*The remainder is not a number detached from its clock. It is an object
with arrows, compatible witnesses and a provenance history.*
