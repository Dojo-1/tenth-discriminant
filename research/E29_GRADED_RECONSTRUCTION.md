# E29 — THE FIBER THAT MOVES WITH THE CLOCK

*19 November 2026 · arithmetic-worldlet research · source-locked graded reconstruction*

> The modulus is not a clock painted on the number. It is the world in which a witness is asked to remain distinguishable.

## Exact source contract

The genuine E24 pair-ring embedding `(a,b) -> (a,k*b)` is injective over Z for k>0 but not surjective on the destination integer lattice for k>1. E28 proved explicit good and bad modular controls, while retaining original arithmetic pair operations. E29 proves a **general observer-level gate** for any `m k : Nat`:

```text
Frame_(m,k) : (ZMod m)^2 -> (ZMod m)^2
(a,b) |-> (a,k*b)

Function.Bijective(Frame_(m,k))
  ↔ ∃ u : ZMod m, u*k = 1.
```

This is equivalent to coprimality `gcd(k,m)=1` for positive finite m; the explicit `Nat.Coprime` theorem is still a future goal. The Lean statement is valid even at m=0 and m=1 under their standard ZMod interpretations. It is not a theorem about arbitrary prime ideals, number-field isomorphisms, or genuine geometric curvature.

## Typed information-loss fiber

```text
Lost_(m,k) = {d : ZMod m | k*d = 0}

Frame_(m,k)(a,b) = Frame_(m,k)(c,d)
  ↔ a=c ∧ (b-d) ∈ Lost_(m,k).
```

E29 proves the fiber is closed under zero, addition and negation, and that distinct future queries on a common observation fiber cannot factor through the current quotient.

At modulus 2, `k=2` destroys coefficient 1. At modulus 4, coefficient 2 is lost but 1 survives. At modulus 8, coefficient 4 is lost but 2 survives. At modulus 16, coefficient 8 is lost but 4 survives. These are exact Lean tests, not a fitted asymptotic law.

## An infinite ladder, not a flat scalar

For p prime and e=v_p(k), the classical size formula is

```text
|ker(x -> k*x on Z/p^n Z)| = p^min(e,n)
```

and the fiber groups interlock under the canonical reduction maps. **The general cardinality formula and coherent projective limit are paper-level results here, not formal E29 theorems.** More structure must be preserved than the scalar count (e.g. transition maps, original witnesses, prime labels and future-query actions).

For the full ring pair map, the real coefficient is unchanged, so these are imaginary-coefficient kernels. In arbitrary moving frames with non-diagonal or noncommuting local actions, the kernel must be typed on its source and target carriers, not conflated with a single Euclidean residual.

## Causal/complexity discipline

Do not infer any runtime advantage, novel ETH/P-vs-NP obstruction, field-discriminant improvement, or asymptotic complexity lower bound from this kernel. The same Boolean observer counterexamples already exist for elementary nongeometric quotient maps. A matched-null study would need to compare complete original-source reconstruction costs and certification behavior at equal compute.

## Cross-line continuation

- **E24–E28:** preserve ring operations and original integer sampling-set transport; do not swap the determinant by a convenient Gram.
- **HK-029–031:** query-dependent future reconstruction and moving prime labels; E29 supplies a parametric local modular test family.
- **307^4 field-bound draft:** remains separate and blocked by missing root-audit import coverage. E29 is not an arithmetic prime-mass gain.
- **p-adic worldlets:** conjectural replacement of a single local obstruction by a coherent inverse tower of residue witnesses, with precise original-source maps.
- **ACAF/negative controls:** test at m=2,4,8,16 versus m=5; falsify any alleged unconditional reconstructibility or scale-invariant feature.

## Evidence gates

Lean file: `lean/TenthDiscriminant/E29LocalUnitAndKernel.lean`.
Root import and focused workflow: `.github/workflows/e29-local-unit-kernel.yml`.
Any claim marked P must be attached to the exact successful CI head and permitted-axiom audit. Until then, this is a **Lean proof candidate**, not a completed theorem package.
