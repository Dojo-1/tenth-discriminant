# Phase269–270 — short finite inert-prime certificate up to 322^4

**Scope:** `163 < d < 322^4 = 10,750,371,856`. The proved `321^4` result remains a corollary.
**Evidence:** [P] exact closed Lean certificate at previously verified head `5447a51` relative to encoded definitions and standard axioms; [M] two independent-order integer enumerations; [H] independent human source/field reconstruction remains open in issue #50. Standalone C++/NumPy source defaults were synchronized to `322^4` after the last green Lean head, so all checks must be rerun on the current head before merge.

This is **not** a new unconditional class-number-one classification, a new Siegel-zero exclusion, or independent verification of PR #157's analytic `321^4` bound. The main branch already contains the nine-field classification and the merged `322^4` analytic bound. The new value is a small, separately reconstructed finite arithmetic certificate.

## Necessary arithmetic conditions

For a negative fundamental discriminant `-d` with `d > 163` and class number one, the odd chart has `d ≡ 3 (mod 8)` and every rational prime `p < d/4` is inert. Thus `-d mod p` must be a **nonzero nonsquare**. To overcount safely, the programs enumerate *every integer* satisfying these local constraints without requiring squarefreeness or primality.

The witness-prime condition is guarded by the **strict** inequality `4*p < d`. In the Lean statement the guard is written `4*p ≤ d`; on the restricted `d ≡ 3 (mod 8)` domain equality cannot occur for odd p.

## Two exact finite enumerations

Initial wheel: `W = 8*3*5*7*11*13*17*19 = 38,798,760`, with exactly `12,960` admissible residues. Every candidate below the bound occurs uniquely as `d = r + W*k` with `0 ≤ r < W`.

Below `322^4`, exactly **3,590,972** integers pass the initial wheel. Additional required nonsquare tests through p=109 reduce the candidates as follows:

```text
p:         23       29      31      37     41     43     47     53     59     61
remaining: 1717429   829089  401173  195269  95237  46513  22527  10809   5138   2469

p:         67    71   73   79   83   89   97  101  103  107  109
remaining: 1199  589  284  133   74   29   16    9    6    2    0
```

The last two integers are `585811843` and `1764959683`; they are excluded at p=109 by `41²+d ≡ 0` and `6²+d ≡ 0`, respectively. **Endpoint negative control:** `d=163` has a root at p=41 but is not excluded by that test because `4*41 > 163`.

Older `321^4` initial wheel count: 3,546,560. That interval is properly contained in the new interval; it is not silently replaced by a different arithmetic premise.

## Exact standalone reproduction

```sh
g++ -O3 -std=c++17 -Wall -Wextra tools/finite321_inert_sieve.cpp -o /tmp/finite322
/tmp/finite322
python3 -m venv /tmp/phase269-venv
/tmp/phase269-venv/bin/pip install numpy==2.2.6
/tmp/phase269-venv/bin/python tools/finite321_inert_sieve_numpy.py
```

The historical `finite321_` filenames are retained for link stability; both now default to `322^4`. Each implementation asserts every stage count. They use different enumeration orders but are AI-authored correlated witnesses, not independent human review.

## Formal CRT proof and exact-head receipts

`Phase269Finite321Data.lean` contains untrusted quotient-pattern literals and exact band widths at the `322^4` endpoint. `Phase269Finite321Sound.lean` proves wheel coverage, guarded-prime transport, small-interval control and quotient-bit retention. Nine full CRT subtree proofs `Phase269Finite321Seed00..08.lean` are combined by `Phase269Finite321Certified.lean`.

- `TenthDiscriminant.Phase269.finite322_certificate`: a CLOSED, bounded arithmetic certificate.
- `TenthDiscriminant.Phase269.finite321_certificate`: the narrower corollary.
- `TenthDiscriminant.Phase269.classNumber_ne_one_below_322_of_large`: field exclusion conditional on squarefree odd-radicand source, derived with the original inertness bridge.
- `Phase269Finite321Bridge.lean`: keeps a separate *conditional* bridge for audit transparency; its premise is now discharged by the other module rather than concealed.

Previously successful exact-head Lean verification for `5447a51`: [focused run 42902487281](https://github.com/Dojo-1/tenth-discriminant/actions/runs/42902487281), [whole-root run 42902487217](https://github.com/Dojo-1/tenth-discriminant/actions/runs/42902487217). Both ended success, along with the remaining 22 PR-head checks. They do NOT cover the subsequent standalone-script and documentation commits: newer exact-head checks are required.

**Promotion stop:** no merge until current-head finite regressions and full Lean/axiom/negative-control checks pass, the source/field semantics are reviewed, and the distinction from the separate `321^4` analytic PR and independent review issue #50 is preserved. A cancelled historical run is superseded by a successful later *exact-head* run; do not rerun stale heads merely to manufacture a green badge.
