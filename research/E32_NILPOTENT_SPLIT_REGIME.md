# E32 — THE SOURCE HAS A NILPOTENT; THE TARGET HAS TWO PRIMES

*19 November 2026 · concrete, source-typed local-algebra regime change*

## Not a coordinate change

In the E24 quadratic pair algebra, let A_D = Z[t]/(t²+D),
represented faithfully by original integer coefficient pairs.

Use D=1 and k=5:

    A_25 = Z[5i] embeds in A_1 = Z[i].
    iota_5(a,b)=(a,5b).

Now reduce both *different orders* modulo five.

    Source: (Z/5)[t]/(t²+25) = F5[epsilon]/(epsilon²).
    Target: (Z/5)[t]/(t²+1) = F5 x F5,
            because t²+1=(t-2)(t+2) mod 5.

The source has a nonzero square-zero element epsilon=(0,1).
The target has no nonzero square-zero element. The actual induced
conductor frame sends epsilon to zero.

This is a **typed algebraic regime difference**: even though the two
orders span the same rational field, their finite modular reductions
have incompatible nilpotent structures. A bare Euclidean/trace metric
or frame determinant cannot reverse this loss.

## New Lean candidate

Module: lean/TenthDiscriminant/E32RegimeNilpotentSplit.lean.

It targets exact statements about the ORIGINAL E28 residueMul and
residueFrame definitions:

1. Source D=25 mod 5 has an explicit nonzero square-zero coefficient.
2. Target D=1 mod 5 has no nonzero square-zero coefficient (exact finite check).
3. The source nilpotent maps to zero.
4. The E28 frame preserves the declared multiplication.
5. **No zero-preserving, square-compatible injective map**
   from the source residue pair algebra into the reduced target can exist.

Even without assuming addition or unit preservation, the fifth
statement follows from the first two, so it is a strong obstruction.

Until an exact-head Lean run and root axiom audit pass, these are
proof candidates. The external ring identifications with dual
numbers and F5 x F5 are classical paper mathematics; the module
proves their decisive finite algebraic invariants directly, not
a general ring equivalence using Mathlib's Ideal API.

## Bridges and countercontrols

- HK-032: two split-prime probes at the **Gaussian target** can
  reconstruct its coefficient pair modulo 5. That does not reconstruct
  a source dual-number epsilon already killed by iota_5.
- HK-033: source-exact Bézout witnesses establish comaximal Gaussian
  target factors; they are not transferred to the nonmaximal order.
- E29/E30: modular reconstruction criteria and finite kernel towers
  distinguish recoverable ambiguity from missing target witnesses.
- E31: the original sampled ordinary-Z-jet trace Gram may remain
  determinant 4 even as the conductor-five local algebra map loses
  its nilpotent coefficient. Do NOT infer additional det factors.
- Phase350: the 307^4 field theorem is a separately source-checked
  research branch; this nonfundamental conductor example is not an
  eligible input to its large squarefree-field proof.
- No nonzero differential curvature, new sheaf cohomology, ETH/P-vs-NP,
  number-field classification, or measured speedup is claimed.

**Next authorization gate:** a formal adapter to HK-032's Gaussian
prime-labelled target and the exact original sampling-jet module,
without changing any source carrier silently.
