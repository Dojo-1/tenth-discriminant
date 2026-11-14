# Phase278 — verification and limits

Base: `9c165b6eebf0fe366959bbafdc8c7d49a1f55f04` (merged Phase277).
Protocol: `19dd39b`, committed before implementing the checker.

**Paper result:** the guide proves a generic first-layer bound using
p-local row division, Gram congruence, a block-rank inequality and local
Smith form. This is not a new Lean theorem or novelty claim.

**M — sole finite trial:** `node research/phase278/safe_pairing_bound.cjs`
passed on Node v20.10.0, exit 0, elapsed 0.1331536 seconds under a
15-second external wall limit. No resource stop, stderr, retry, floating
point mathematical arithmetic or third-party dependency. Timing uses
the host clock; it is not a mathematical input.

| Control | Exact determinant | v3 | Safe first-layer bound |
|---|---:|---:|---:|
| Primitive isotropic line | 18 | 2 | 1 |
| Scaled isotropic line | 162 | 4 | 2 |
| Primitive plane | 32 | 0 | 0 |
| False-addition counterexample | 288 | 2 | 2 |
| Other scaled row | 288 | 2 | 2 |
| Both scaled rows | 2592 | 4 | 4 |

Each checks the two-sided Gram identity, residue ranks, exact separation
of twice the supplied lattice index from primitive pairing valuation,
and determinant/rank preservation under a determinant-one row shear.
The counterexample rejects additive double-counting; the primitive line
rejects identifying radical dimension with exact residual valuation.
A wrong metric changes that line's valuation from two to one.

These six matrices are abstract trace-metric models, **not original
ordinary-jet evaluation matrices**. The Phase277 panel calculations in
stdout are deductions from its published ranks, not fresh source ranks.
Phase206's p5 exact valuation 520 and unresolved p3 exponents were read
from its preserved checker, not rerun or independently remeasured.

**Saved evidence:** [RUN.json](RUN.json) records command, hashes, native
exit, timing and cap. [stdout.json](stdout.json) contains every result;
[stderr.txt](stderr.txt) is intentionally empty. The script SHA256 is
`5755ba0c0c36b39ddaa8946f74b7144fd4bd323af652c916b94f2efc2529fd0c`.
No failed invocation exists in this cycle. Prior failures remain untouched.

**Rizz review — one self-review, not an independent referee:** the guide
states the object, nonzero-determinant guard and residue ranks before the
formula; distinguishes a one-step divided matrix from a primitive one;
shows the counterexample numerically; separates paper, finite and Lean
evidence; and ends at the actual unproved production obligation. The
checker is dependency-free, uses exact BigInt arithmetic and explicit
fixed controls. No universal advantage is inferred from the finite run.

**Checks:** `node --check research/phase278/safe_pairing_bound.cjs` and
`git diff --check`. Existing Lean source, workflows, dependency pins and
historical evidence must have zero diff against the base (apart from the
new historical-status paragraph in `lean/FORMALIZATION.md`). Python and
Lean executables are not installed in this fresh Windows checkout. Local
whole-root replay was not attempted. Pinned project CI, if published,
must be reported on its exact new head; inherited green CI is not its result.

**Next R:** resolve the p3 primitive evaluation lattice at the SAME source
before assigning residual pairing mass. A later separately registered
attempt may address that finite problem; a uniform production theorem
and independent human reconstruction remain open. No new field cutoff,
classification or exclusion of Siegel zeroes follows from this cycle.
