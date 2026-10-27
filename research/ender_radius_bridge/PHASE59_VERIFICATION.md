# Phase 59: registered conditional prototype

Registration `437001eebaec32998434e22ab7ba70c0d54c9283` precedes the prototype source and every build. The [protocol](PHASE59_PROTOCOL.md) fixed the actual-Gram conclusion, explicit count/kernel/weight inputs, controls and caps. The [short guide](EXCLUDED_PRIME_PROTOTYPE_GUIDE.md) explains what remains open.

Three complete builds, maximum 600 seconds / 8192 MB per process and 1200 seconds cumulative:

| Attempt | Outcome | Seconds | Change before next build |
| --- | --- | ---: | --- |
|1|FAIL|66.3803296|Make finite-set membership directions explicit; add finite-filter simplification.|
|2|FAIL|34.2828343|Add the existing singleton-filter simplification to fixed controls.|
|3|PASS|36.1702342|None; source frozen.|

Total 136.8333981 seconds, no resource stop. Both failed sources and raw outputs remain in `PHASE59_ATTEMPTS.zip`, with exact byte readback. The namespace audit rejected unfinished proofs through sorryAx in the failed builds. No such axiom or error remains in the accepted output. The recorded target is not weakened: all 11 complete theorem type prefixes, the four definitions and the audit/input-check tail are unchanged.

Final source SHA256:
`307ba7da9ba96bd5b7aa4437c8411b9632847e70e273fbf01c02dc6176f829d9`.
The result manifest seals the protocol, exact source, runner and all 12 archived raw files. The accepted audit is 36 logical / 32 theorem / 5 runtime, standard three axioms only. The three compiled closures are 48165 / 11176 / 48196, with none of the listed forbidden inputs.

Executed command from the repository root, three times within the registered campaign:

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File research/ender_radius_bridge/run_phase59.ps1 -Mode build
```

Its target command, in `lean`, was `lake env lean -j 1 ../research/ender_radius_bridge/Phase59Prototype.lean`. Pinned Lean 4.19.0 / Mathlib c44e0c8 were used. The runner's recorded campaign budget is now exhausted; it must not be reset to create another passing attempt.

Saved-evidence checks, not Lean reruns:

```sh
python research/ender_radius_bridge/verify_phase59_results.py
python research/ender_radius_bridge/verify_phase58_review.py
python research/ender_radius_bridge/verify_phase57_results.py
```

All pass. Production .lean files, root imports, tools, numerical certificates, pins and CI gates are unchanged. This source is a standalone research prototype. The existing pinned CI checks the production library; it does not replay this prototype unless its explicit target command is separately run. No permanent CI coverage, production-root integration or independent review is claimed for this addition.

The class-number-one cutoff remains 50 billion. No higher-class-number range, classification, novelty, optimality or Tao submission is established.
