# E39 / HK-035 — FULL ORIGINAL SOURCE CROSS-REPOSITORY COHERENCE

*19 November 2026 · composite Lake build; draft pending exact CI.*

## What this closes

HK-034 PR #33 demonstrated the crucial correction
    gpair(x,conjugate(y)) = positiveIntegerPairTrace(x,y)
on a faithful copied integer-pair D=1 source formula. But it
did not import the actual Tenth declaration in the HK package.

Both GitHub repositories use **the SAME Lean 4.19.0 toolchain**.
This branch introduces an isolated composite Lake workspace,
requiring exact local paths to the actual Tenth lean package and
a pinned HK-034 source commit aa322a93ed4b4f643378ead02ad05cb6423c62c6.
It does NOT alter either package's own lakefile or main branch.

## Four source-exact mathematical targets

1. Direct equality of HK GaussianInt arithmetic with Tenth's
   actual pairMul 1 on the exact underlying integer coefficients.
2. Direct equality of conjugation in the two packages.
3. Direct equality of HK gpair(x,gconj(y)) with the ACTUAL
   Tenth.integerPairTrace 1, retaining positive factor two.
   Negative control x=y=i exposes the wrong HK
   un-conjugated trace (-2) versus original positive trace (+2).
4. For arbitrary original finite Q, J, R, S, use the existing
   Tenth.integerDerivativeRow 1 (ordinary Z derivatives with W
   fixed) at EACH original q and j. Evaluate them using HK's
   positive-conjugated pair, and prove entrywise equality to
   Tenth.integerRectangularTraceGram Q 1 J R S across the
   COMPLETE rectangular R*S row index set. Equality of the
   actual determinant follows; no selected auxiliary minor.

## Evidence discipline and blockers

Only D=1 Gaussian coefficients are bridged; this is not a
general source-field equivalence for every squarefree D.
No prime valuations, extra p factors, stronger 307^4 bound,
new class-number theorem, or complexity result are inferred.

The composite build may expose actual Lake compatibility or
proof elaboration issues. Until exact-head two-repository
CI passes, these are H-level formal proof proposals.
Even a green composite build proves only the encoded
original arithmetic/tracing identity. It does not solve
the original thin-ellipse row-extraction task.

## Execution

Workflow: .github/workflows/e39-hk-original-source-bridge.yml
Composite project: research/bridge-project/lakefile.toml
Proof: research/bridge-project/OriginalSourceBridge.lean

The workflow checks out HK at a fixed SHA; dependency drift
must not be hidden by dynamic latest-branch resolution.

**Kill rule:** if the two packages cannot be compiled together
without altering their source algebra or permitted axioms,
do not claim cross-package verification.
