# Phase101: actual even normalization and full closed original-Gram budget

The standalone theorem derives actual M(K)=4*sqrt(d)/pi for positive
squarefree d=1 or 2 modulo 4. It proves the closed count-kernel bound,
full normalized original-Gram weighted budget, domination by the scalar
cost at scale d, and the full scalar-budget consequence. No normalization,
counting or divisibility estimate is supplied by the caller.
[Human reconstruction](EVEN_NORMALIZATION_GUIDE.md).

## Scope and provenance

[Protocol](PHASE101_PROTOCOL.md) and [runner](run_phase101.ps1) registered at
`14dae7efb6b9f41092f4a1af3934597eb5514431` before source or execution.
Base: `cea92b0cc0e48d229379f48c1df9398d06d5c958`.
Final source SHA256:
`ca862eda8e0a8fb0f1c924d71b93ff4168c2c62e90a8fbb3e9370b1c0b43c9ba`.
First failed source SHA256:
`0ef960f72d4e2785c15fdb6b06ae81c0363206c8c76010d78e8bd5a8a056b064`.

Sixteen public theorem types, both definitions and all four controls were
fixed before the first invocation. The field degree/no-real-place and
actual discriminant identify the existing Minkowski formula. Generic
square-root and positive summation lemmas bound the count kernel. The
same original Gram retains radicand d while the count uses actual field
discriminant4*d. Comparing the closed costs is an inequality of real
formulas, not a field isomorphism or substitution of an odd field.

## Both full attempts, including the failure

| Attempt | Result | Seconds | Peak observed process working set, bytes |
| --- | --- | --- | --- |
| 1 | FAIL, incomplete final simplification | 94.426986 | 3309989888 |
| 2 | PASS | 49.0224752 | 3310727168 |

Cumulative143.4494612seconds, within1200seconds. Each invocation capped at
600seconds and8192MB per owned process. No resource stop, weaker target,
extra probe or limit increase. The exact command, from lean/, was:

```sh
lake env lean -j 1 ../research/ender_radius_bridge/Phase101EvenMinkowski.lean
```

The first actual_minkowski proof left `True ∨ Real.pi = 0` after numerical
normalization and ring normalization. The namespace and closure audits
correctly rejected the incomplete downstream proofs via sorryAx. This
was a failed run, not a checked theorem or an explicit source axiom.
The sole repair adds final `simp` immediately after `ring` in that proof.
No definition, statement, control or other proof changed. The complete
failed source/stdout/stderr/result remain in the archive. The second full
invocation passes with no sorryAx or nonstandard dependency.

Final namespace:23 logical declarations,21theorems including generated
auxiliaries, no runtime auxiliaries. Only propext, Classical.choice,
Quot.sound. All16public statements and both definitions are printed;
actual_minkowski and both full budgets have printed axiom lists. The
fresh final closure reaches57,646declarations and excludes58older inputs:
all52Phase100exclusions plus odd-specific ClosedKernel majorant/count/
budget and OddMinkowski normalization/count/budget. Generic summation and
scalar facts remain reusable; no old odd-field cutoff is a premise.

Four controls: actual Gaussian constant4/pi; d2actualdiscriminant-8 and
M=(4/pi)*sqrt2; log(n)/n domain rejection at1; exact half-axis log3/6cost.
They remain unchanged across both invocations.

## Recheck the saved record

```sh
python research/ender_radius_bridge/verify_phase101_results.py
```

This verifies both attempts, exact single repair, fixed types/definitions/
controls, caps/commands/hashes/axioms/exclusions, [eight raw files](PHASE101_RAW.zip),
[manifest](PHASE101_RESULTS.json) and1,553frozen prior files. It does not
execute Lean. Production/root/tools/pins/CI/certificates/earlier protocols/
verifiers/raw/reviews/ledgers and failed/stopped attempts are unchanged.
No new root build, whole-library audit or numerical campaign was run;
Phase100 remains the separate current production-check record. Historical
root-fixed verifiers remain frozen at accepted refs without weakening.

## Remaining work

Integrate the accepted proof, then combine its scalar budget with the
all-range determinant estimates. The even cutoff and arbitrary-field
transport remain open. No numerical candidate becomes a premise. No
new cutoff, full classification, novelty, optimality, external exact-head
CI or independent human review is claimed. Argon remains pending.
