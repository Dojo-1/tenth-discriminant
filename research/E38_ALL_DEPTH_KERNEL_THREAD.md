# E38 — EVERY FINITE KERNEL IS NONZERO; THE COHERENT KERNEL IS ZERO

19 November 2026 · source-exact conductor tower · research draft.

## New theorem target (all depths)

The coefficient frame for the integral order inclusion at index two
sends b to 2*b. At observation depth n>=0 use the modulus 2^(n+1).

For EVERY n there is a nonzero lost residue:
    2^n is not 0 mod 2^(n+1),
    2*2^n is 0 mod 2^(n+1).

Nevertheless a coefficient a at level n+1 satisfying
    2a = 0 mod 2^(n+2)
already has
    a = 0 mod 2^(n+1).

Thus any coherent thread a_n satisfying BOTH
    2a_n = 0 mod 2^(n+1)
and
    a_(n+1) mod 2^(n+1) = a_n
must have every a_n=0.

This proves the elementary inverse-system kernel is a singleton
when encoded as compatible integer residue representatives.
No asymptotic approximation, scalar fit or invented geometric
transport is used.

At every depth an odd target residue (in particular 1) remains
outside the image of multiplication by two. The source-kernel
limit and missing-target obstruction must NOT be conflated.

## Scope boundary

The code states all-depth lemmas and a coherent-thread universal
property for the original integer coefficient observer.
It does NOT instantiate the full Mathlib p-adic integers,
derived inverse limits, higher sheaves or normalized valuations.

The established classical identification
    kernel(2 on Z_2)=0,
    cokernel(2 on Z_2) congruent to Z/2Z
requires a separate typed Z_2 proof if stated in Lean.
No ETH/P-vs-NP or field-discriminant improvement follows.

## Evidence controls

The E30 finite examples remain regression controls.
The E31 original-Gram falsifier remains active: ambient kernel
information alone gives no extra sampled Gram factor.
E32/E33 source nilpotent/cokernel exactness remains finite
and must not be identified with the inverse-limit tower.

Source: lean/TenthDiscriminant/E38CoherentKernelThread.lean.
CI: .github/workflows/e38-coherent-kernel-thread.yml.
Root import maintained.

Status [H] until exact-head focused/full-root Lean and axiom audit.
Do not promote from a finite sample or from the prose derivation.

## Next

Formalize the inverse-limit universal property in the typed
category of rings/modules, and separately show persistent
missing target via a compatible cokernel tower. Preserve the
transition maps, not just the cardinalities of finite fibers.
