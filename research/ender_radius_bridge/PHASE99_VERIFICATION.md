# Phase99: the actual even prime count pays the original-Gram loss

Lean checks `EvenSplitPrimeBudget.actual_gram_budget` for positive squarefree
d=1 or 2 modulo 4, actual class number of EvenQuadraticField d at most two,
any finite P of odd primes <=L, L>=3, R,S>=1, d<=d2, and the existing Ender
radius condition. The result is

    mass(P,R,S) <= log(product of original Gram diagonal entries)
      + lossScale(R,S)*kernelCost(L,primeKernel,countBound d)
      + R*S*(S-1)*log(d).

The matrix remains rectangularTraceGram(ellipsePoints d rho), with its
ordinary derivatives and normalization unchanged. The count uses actual
field discriminant 4*d and actual M(K). No prefix bound, chosen family,
cardinality identity, slice estimate or local divisibility is assumed.
[Human explanation and operator](EVEN_WEIGHTED_BRIDGE_GUIDE.md).

## Preregistered scope and execution

[Protocol](PHASE99_PROTOCOL.md) and [runner](run_phase99.ps1) were committed at
`c02aaf9f82880442541ea1c929214df66237fc20` before source or execution.
Base: `a5cd1e3281c778ede1595c5065e29d0ca10834ef`.
Source SHA256:
`174ad6ed25744c53bbf312693c1c1eaf08c77a40c12af143c7a828be1758d985`.

The sole full invocation passed in 96.1654538 seconds, with observed peak
process working set 3,252,969,472 bytes. Caps: 600 seconds and 8,192 MB per
owned process. No repair, retry or resource stop. The exact command from
`lean/` was:

```sh
lake env lean -j 1 ../research/ender_radius_bridge/Phase99EvenSplitPrimeBudget.lean
```

Seven public theorem types, one countBound definition and five controls
were fixed at first invocation. Namespace audit: 11 logical declarations,
10 theorems including generated definition proof auxiliaries, no runtime
auxiliaries. Only `propext`, `Classical.choice`, `Quot.sound`.
Both main theorem statements and axiom sets are printed. The fresh final
closure reaches 57,514 declarations and excludes all 49 Phase98 inputs
plus the odd-field SplitPrimeBudget countBound, remainder_prefix_bound
and actual_gram_budget (52 exclusions). No odd-field counting or cutoff
result supplies the new bound.

The proof reuses the generic prime partition and summation machinery.
It feeds EvenClassAggregation.uniform_two_class_bound into
PrimeDivisorLoss.excluded_budget_without_divisors, so both estimates
refer to the original Gram with radicand d. The reusable partition facts
are field-independent; their odd-field count/budget theorems are excluded.

Controls cover the empty partition, d=1/p=5 square remainder, d=5/p=5
parameter-divisor exclusion, square root modulo two rejected by Admissible,
and one-column zero valuation. Production sources, root, tools, pins,
CI, certificates, earlier protocols/results/verifiers/reviews and all
failed/stopped attempts are unchanged. There was no new root build,
whole-library audit or numerical campaign: those are the separately
recorded Phase98 checks, not new Phase99 executions.

## Saved verification

```sh
python research/ender_radius_bridge/verify_phase99_results.py
```

This checks the full source, seven public types and definition, exact
command/caps, dependency/axiom reports, [four raw records](PHASE99_RAW.zip),
[manifest](PHASE99_RESULTS.json) and 1,538 frozen prior files. It does not
execute Lean. No negative proof attempt occurred; earlier failures remain
frozen, and the prime-two/one-column boundary controls are preserved.

## Remaining obligations

Production integration, actual M(K) normalization, an explicit closed
weighted bound and the final same-Gram even-field contradiction remain
open. No new cutoff, full classification, novelty, optimality, external
exact-head CI or independent human review is claimed. Argon's review
remains pending until received and tied to its covered version.
