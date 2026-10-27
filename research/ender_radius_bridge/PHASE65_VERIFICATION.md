# Phase65: parameter-prime-divisor loss

**Current integration:** the exact proof is now production-root reachable.
See [Phase67](PHASE67_VERIFICATION.md) for the combined local audit and pending
new-head CI. This original record describes the standalone execution; its
fixed-current-root verifier applies at its frozen source ref after new imports.
Use the Phase67 verifier for the current integrated tree.

**Standalone local proof and fixed controls PASS.** Protocol0d7392a precedes
all source and execution. Base9705cac; no production source, dependency pin,
numerical certificate or CI gate changed. This file is outside the root/CI.

The exact target uses the original valuationWeight, ExcludedPrime.mass and
actual ellipse Gram. Prime divisors of D have total mass at most
R*S*(S-1)*log D. The full Gram inequality requires a prefix-count B only
for the other excluded primes. No aggregate-loss premise is supplied.
Read the [human proof](PRIME_DIVISOR_LOSS_GUIDE.md).

## Registered execution

| Attempt | Result | Seconds | Interpretation |
|---|---|---:|---|
| 1 | FAIL | 33.2369437 | Product-cast normalization and explicit log_prod arguments were missing. The resulting sorryAx audit rejection is preserved. |
| 2 | PASS | 29.0058835 | Those two proof lines repaired; all9 public statements and5 controls unchanged. |

Total62.2428272s; per-attempt cap600s, total cap1200s, memory threshold8192MB.
No resource stop, third invocation, separate proof probe or old-campaign rerun.
The second run prints the actual full theorem and three axiom lists, then
checks13 logical declarations/13 theorems/0 runtime-only auxiliaries using
only propext, Classical.choice and Quot.sound. This is the new namespace
count, not a replacement for the whole production-library audit.

Controls cover S=1, prime divisors3 and5 of15, empty input, D=1, and failure
without the divisibility guard: T={3},R=4,S=2 has positive mass while log1=0.

The runner was invoked twice from the repository root:

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File research/ender_radius_bridge/run_phase65.ps1 -Mode build
```

The exact lake command, times, source SHA256 and process resource observations
are in PHASE65_RESULTS.json. PHASE65_RAW.zip preserves all8 source/log/result
files from both attempts. The final source is byte-identical to the second
snapshot. Protocol ancestry and unchanged types/guards are checked by:

```powershell
python research/ender_radius_bridge/verify_phase65_results.py
```

That command checks saved integrity; it does not execute Lean again.

No parameter-to-field-discriminant ramification identification, class/form
dictionary, four-representation theorem, arithmetic B, numerical cutoff,
classification, independent review or upstream acceptance is inferred.
PR32 doc-head CI40416976865 is separate and was live when this local result
was assembled; no new-head CI pass is claimed or old run interrupted.
