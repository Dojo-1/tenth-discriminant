# Reproducibility record

## Frozen object and workspace

- Requested target SHA: `39e9ce34d09ed9f990fab4b9ed5e3980cee64119`.
- Detached review worktree: `/tmp/tenth-discriminant-audit-wt`.
- Exact SHA observed in that worktree: `39e9ce34d09ed9f990fab4b9ed5e3980cee64119`.
- The original checkout was clean when checked and was not edited. Audit files and the generated `lean/lake-manifest.json` are in the detached worktree only.
- Linux x86_64; 2 visible CPUs; approximately 7.5 GiB RAM (6.0 GiB available at the time checked); no swap.
- Lean toolchain: `leanprover/lean4:v4.19.0`; executable reported Lean 4.19.0, commit `6caaee842e94`.
- Mathlib pin: `c44e0c8ee63ca166450922a373c7409c5d26b00b`.
- A generated `lake-manifest.json` pins that Mathlib revision and dependency revisions. It is untracked in the detached tree; it is not part of the frozen commit.

## Commands and outcomes

| Command/check | Outcome |
|---|---|
| `git -C /tmp/tenth-discriminant-audit-wt rev-parse HEAD` | Passed; printed requested SHA. |
| `lean --version` | Passed; Lean 4.19.0, commit `6caaee842e94`. |
| `lake update` | Failed while retrieving the Mathlib cache; the package sources and pinned revisions were cloned, but 6,641 cache downloads failed because `lakecache.blob.core.windows.net` did not resolve. |
| `getent hosts lakecache.blob.core.windows.net` | No address returned. |
| `curl -I --connect-timeout 8 --max-time 12 https://lakecache.blob.core.windows.net/mathlib4` | Failed: `curl: (6) Could not resolve host: lakecache.blob.core.windows.net`. |
| `timeout 180s lake build` | Exit 124 (timeout). It made progress through roughly 400 build targets, including Batteries, Aesop, and early Mathlib modules; it did not complete the project build. Elapsed time was bounded at 180 seconds. |
| `timeout 900s lake build` (incremental continuation) | Exit 124 (timeout) after the full 900-second bound. The last output was `[1209/1218] Built Mathlib.Algebra.GroupWithZero.Subgroup`; the project modules and requested theorems were not reached. |
| `lake build -j 2` | Failed immediately: this Lake version has no `-j` option. No proof check was performed by this command. |
| `python3 audit/sieve_oracle.py` from detached worktree | Passed: `200 masks reconstructed exactly; 92964 affine-root comparisons passed.` |
| `python3 audit/gram_control.py` | Passed: exact matrix `[[2, 6], [6, 24]]`, determinant `12`, independently reconstructed from integer-pair arithmetic and matching the source control. |
| `python3 audit/cutoff_margin.py` | Passed: exact rational margin `1909/312500000 = 0.0000061088`. This checks only the last affine comparison. |
| Static half of `audit.py` (its `project_coverage` and `source_code` functions run separately, without invoking Lean) | Passed: all 173 project modules reachable from the audited root; no `sorry`, `admit`, `axiom`, `native_decide`, or `unsafe` token found in source after comment stripping. This is not the compiled axiom audit. |
| `python3 audit.py` / `lake env lean Audit.lean` / `#print axioms` | Not completed. The full audit awaits the pinned Lean project build and required imports. |

The two source-build attempts consumed 1,080 seconds in total and both timed out without a Lean error in the project's code. The second attempt reused artifacts from the first and reached 1,209 built targets, but was still in foundational Mathlib modules. No successful project build is claimed.

Two sieve-script harness attempts failed before the final pass: first, the script was invoked from the original checkout (so its detached-worktree-relative path did not exist); second, its initial parser also matched the aggregate `phase36Entries` declaration. The script was corrected to run from the detached root and parse only `phase36Entry...` declarations, then passed all reported checks. These were harness/path errors, not mathematical mismatches.

Exact wall time for dependency cloning/cache retrieval and peak memory during compilation were not recorded. During the second build, a system snapshot showed 1.8 GiB used and 5.7 GiB available; this is not process high-water data. No clean-machine second build was performed.

## Prior-art artifacts

The following public source artifacts were fetched directly at pinned commits for comparison (none was built): Murphy `formalization/CN1/Main.lean`, `formalization/CN1/ChowlaSelberg/SevenEighths.lean`, `formalization/CN1/Finite/SplitPrime.lean`, `determinant/formalization/ELEM/Main.lean`, `determinant/formalization/ELEM/Divisibility/Main.lean`, and `determinant/formalization/ELEM/Endpoint/Comparison.lean` at `f0995bf604056a98f0af0d182ed152c6bd996419`; twinheterodox `companions/elementary/proof.tex` and `companions/elementary/verify_finite.py` at `95e8fe68da05790b99d828b5b6aff3f6dc479aa2`. GitHub repository and issue searches for Olivier's artifact returned no result; GitHub code search required sign-in.

## Independent sieve check

`audit/sieve_oracle.py` parses the serialized `QuotientPattern` values, verifies the listed prime moduli and modular inverses, independently computes every allowed bit from the root condition \(t^2+d\not\equiv0\pmod p\), and compares all 200 arbitrary-precision masks exactly. It then uses a fixed PRNG seed and boundary quotients/residues to compare mask bits with direct modular-root searches. The output is a reproducible measurement only; it does not prove full quotient or residue coverage.

## Reproducibility verdict

The source revision and Lean/Mathlib pins were identified. The finite mask oracle is reproducible and passed. A complete Lean build, theorem replay, project-wide axiom audit, and clean-environment reproduction remain unverified because the Mathlib cache host was unavailable and the source build had not finished.
