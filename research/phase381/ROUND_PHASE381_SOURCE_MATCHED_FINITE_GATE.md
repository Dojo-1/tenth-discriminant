# Phase381 — source-matched finite gate for the analytic 652 endpoint

**22 November 2026 · AI-assisted research draft · stacked on Phase380 PR #300**

## Objective

Give Tao's conditional `ZF(7/8) => |D| <= 652` route a *short Lean-side finite finish* by reusing existing source-level class-number-one arithmetic. Do not replace the original trace-Gram determinant, conflate the squarefree radicand with the **actual fundamental discriminant**, or claim that a program proves Epstein's analytic continuation.

## Existing mathematical dependency (no new lemma assumptions)

The repository's pre-existing, reviewed-by-compilation source contains:

1. `ClassNumberInertBridge.smallPrime_nonsquare_of_classNumber_one`: for the odd maximal-order chart and odd prime `p < (d+1)/4`, `h(K)=1` forces `-(d : ZMod p)` to be non-square. It constructs a ring-of-integers quotient map and an element of norm `p` rather than asserting the ideal-to-element bridge.
2. `OddPrimeTwo.imaginaryQuadratic_classNumber_one_mod_eight`: for squarefree `d>7`, `h=1 => d % 8 = 3`, dealing separately with prime 2 and even maximal-order charts.
3. `FiniteSieveBridge.smallSieveCandidate_of_classNumber_one`: combines these with the eight base primes `[3,5,7,11,13,17,19,23]` to deduce the soundness of a decidable boolean sieve for the **actual number field**.
4. `QuadraticChartEquivalence.imaginaryQuadratic_discr_natAbs`: transports squarefree radicand `d` to **actual** `NumberField.discr` via `d` when `d%4=3`, otherwise `4*d`.

The full source already has an unconditional nine-field classification in `ClassNumberClassification.lean`. The alternative finite gate deliberately does **not** import that theorem or the 700-billion finite classification. Its value is a small explainable proof chain beneath an *external analytic cutoff*, not a new classification discovery.

## New, tightly scoped Lean targets

`lean/TenthDiscriminant/Phase381Finite653.lean` contains:

- `phase381_sieve_candidates_below_653`: exact kernel-decision goal
  `(List.range 653).filter smallSieveCandidate = [1,2,3,7,11,19,43,67,163]`.
- `phase381_classNumber_one_candidates_below_653`: use the existing global-to-local soundness theorem plus the finite equality; explicitly assume `d<653`.
- `phase381_actual_discriminant_candidates_below_653`: if the **actual** `NumberField.discr` has absolute value `<=652`, return the signed discriminant list `[-4,-8,-3,-7,-11,-19,-43,-67,-163]`.
- A deliberate false-positive control: `smallSieveCandidate 10987=true`, and the even-chart parameter control `smallSieveCandidate 58=false` (actual discriminant `-232` corresponds to radicand `58`).

**Local test actually run:** `python3 research/phase381/sieve_source_mirror.py`; it checks the complete 653-case output and the 10987 false positive. The first false positive above 163 (within 20,000) is `10987`: `10987 % 8 = 3` passes base primes, but `2^2+10987 ≡ 0 (mod 29)`, and the first-split-prime obstruction excludes its class number one. Thus `smallSieveCandidate` is only a necessary condition, never a general iff.

## What has and has not been checked

- **M:** local standard-library Python mirror passed its exact 653 inputs; Phase380's two distinct 199/190/9 checks also passed.
- **P (source inspection):** pre-existing Lean declarations for norm lifting, odd-prime nonresidue, prime-two modular restriction and source sieve soundness were inspected on main. This turn did not independently compile them.
- **H / pending CI:** compilation and axiom report for the new Phase381 Lean file. Neither `lake` nor `lean` is installed in the local runtime, so a GitHub Actions focused build is the only practical execution path available here.
- **A:** the analytic `ZF(7/8)` and Epstein/Poisson positivity bridge of Phase379. The finite Lean theorem does not establish either assumption.
- **Unresolved:** independent human source-to-field audit #50 of the original 322^4 / research 301-302^4 trace-Gram approach.

## Precise mathematical dependency graph

```
real quadratic zero-free ZF(7/8) [external]
    + Epstein/Poisson identity + rational bound [analytic bridge]
    ==> absolute fundamental discriminant <=652 [conditional]
                                           |
actual field class-number one ------------+
    |                                      |
    v                                      |
prime-two and odd-prime norm lifting      |
    |                                      |
    v                                      |
pre-existing boolean sieve soundness      |
    |                                      |
    v                                      |
653-case finite Boolean equality <--------+
    |
    v
radicands {1,2,3,7,11,19,43,67,163}
    |
    v
actual signed discriminants {-4,-8,-3,-7,-11,-19,-43,-67,-163}
```

**Do not reverse arrows.** Nine candidate discriminants do not imply a general zero-free region. Finite soundness does not prove positive class number for the nine survivors. The separately proved unconditional classification is a distinct proof and dependency chain.

## Reproduction

```sh
python3 research/phase380/split_prime_certificate.py
python3 research/phase380/verify_split_prime_witnesses.py
python3 research/phase381/sieve_source_mirror.py
cd lean
lake build TenthDiscriminant.Phase381Finite653
```

The last command must be reported as *not yet locally executed* until an actual build log is inspected.

## Next step

Close the new Lean build, then formally state the analytic assumption in its weakest correct shape: only **real** zeros of primitive quadratic `L(s,chi_D)` for `7/8 < s < 1`. Match the real quadratic character at its primitive conductor and prove the Dedekind `zeta_K = zeta * L(chi_D)` use. Do not import Masullo's unproved Hecke divisor statement or substitute an Ihara/ Selberg spectral gap.
