# Reverse determinant · one reading route (Phases 144–158)

This is the consolidated, **finite and exploratory** thread of the [Tenth Discriminant](../../README.md) project. Read it from the repository's **`main` branch**, not as five competing research branches. The original problem remains a same-integer arithmetic lower bound versus geometric upper bound on an ordinary-jet Gram, ultimately transported to an *actual* imaginary quadratic field discriminant.

**Evidence boundary.** The original mainline [strict 47-billion field-discriminant theorem](../../lean/TenthDiscriminant/TightRadialEndpoint.lean) is Lean-checked, still awaiting independent mathematical reconstruction ([#50](https://github.com/Dojo-1/tenth-discriminant/issues/50)). A stronger thin-ellipse field endpoint is discussed in *draft* [PR #62](https://github.com/Dojo-1/tenth-discriminant/pull/62): its exact-head Lean checks are separate from mathematical endorsement, and it must not be silently promoted by this branch merge. Phases144–158 do **not** assert a new number-field cutoff.

## What survives the round trip?

All experiments retain the **same original ordinary `∂_Z^j` derivatives with `W` fixed**, two integer coordinate channels and original positive trace weights. Let \(E_Q(D)\) denote the integer evaluation matrix of an observation support \(Q\), \(M_Q=\mathrm{im}_{\mathbb Z}E_Q\), and \(G_Q=E_Q B_Q E_Q^\mathsf T\). The finite metric and arithmetic outputs must not be confused: equality of integral column image does not imply equality of Gram determinants, an interpolation theorem for a new support, or the original prime-mass lower bound on that new Gram.

| Round | Exact finite result / paper identity | Read | Reproduce |
| --- | --- | --- | --- |
| **144** · Reverse determinant | A 6-point minimal integral-image witness for the fixed \(D=19,R=8,S=J=4,\rho=5\) ellipse; full/thin Smith factors and an exceptional \(2^{10}\) quotient for another support | [Dossier](PHASE144_REVERSE_DETERMINANT.md) · [#63](https://github.com/Dojo-1/tenth-discriminant/issues/63) | [Lattice scan](phase144_verifier.py) · [minimum-support certificate](phase144_minimum_support.py) |
| **145** · Ortho/anti/ambig | Real parity cross-coupling and nontrivial \(\mathbb Z/2\) integral gluing are distinct. The observed \(2^{10}\) jump arises from pure parity sublattices, **not** changed gluing; a nonzero SPD tangent commutator is **not** a measured loop holonomy | [Dossier](PHASE145_ORTHO_ANTI_AMBIG.md) · [#64](https://github.com/Dojo-1/tenth-discriminant/issues/64) | [Verifier](phase145_ortho_anti_ambig.py) |
| **146** · Moving integer frame | Exact unitriangular translation \(E_{Q+a}=T_a E_Q\), moving-grading invariance, typed translation-lattice quotients. A valid horizontal Newton support cap fails to trim at the proposed production floor | [Dossier](PHASE146_TRANSLATION_NEWTON.md) · [#65](https://github.com/Dojo-1/tenth-discriminant/issues/65) | [Verifier](phase146_translation_newton.py) |
| **147** · Prime-local adequacy | Eight exhaustive finite minimal support sizes, with a **7-primary** counterexample to checking just primes \(2,3,5\). Same sampling geometry can have different arithmetic minima | [Dossier](PHASE147_PRIME_ADEQUACY.md) · [#66](https://github.com/Dojo-1/tenth-discriminant/issues/66) | [Verifier](phase147_prime_adequacy.py) |
| **148** · Parameter chamber | For fixed same 21 nodes, \(D=17,\ldots,21\), **9** common points are sufficient and globally minimal. A 9-point support minimizes the **raw diagonal Hadamard** upper among all adequate 9-point supports. The fixed-coordinate matrix family has a separately typed universal column-congruence period **529,200** modulo a D-independent real-axis lattice | [Dossier](PHASE148_ARITHMETIC_CHAMBER.md) · [#67](https://github.com/Dojo-1/tenth-discriminant/issues/67) | [Chamber certificate](phase148_arithmetic_chamber.py) · [period certificate](phase148_fixed_lattice_period.py) |
| **149** · Positivity-first Lean interface | Factor the existing arbitrary-\(Q\) prime-mass logarithmic inequality through a direct positive-determinant hypothesis. Keep the original point-count theorem as a wrapper; new production positivity and analytic upper remain open | [Dossier](PHASE149_POSITIVITY_BRIDGE.md) | [Lean source](../../lean/TenthDiscriminant/RadialCutoff.lean) · [whole-root CI](../../.github/workflows/lean.yml) |

| **150** · Fourier minimal nodes | Unrestricted `ceil(R/2)` integer support exists for original `J=S≤R` ordinary jets, but the quantitative grid radius is too large for the discriminant argument | [Paper-level record #69](https://github.com/Dojo-1/tenth-discriminant/issues/69) | Independent Lean review remains open |
| **151** · Conjugation Worldlets | Exact `C₂` equivariant jet descent preserves the integral image; weighted orbit sum reconstructs the original Gram. Unweighted orbit descent gives a smaller positive Gram and a certified `O(RS)` gain bound; naive integral Fourier loses `2`-primary information | [Dossier](PHASE151_CONJUGATION_WORLDLET.md) | [Exact verifier](phase151_conjugation_descent.py) |
| **152** · Frobenius graph and Pareto geometry | Low-inert-prime no-collision theorem on the **unchanged ordinary-jet** rectangle, with an explicit conditional radius family and an exact D163 radius/support and analytic-upper Pareto frontier; the actual field cutoff remains open | [Dossier](PHASE152_FROBENIUS_GRAPH.md) | [Exact finite verifier](phase152_frobenius_graph.py) |
| **153** · Bertrand same-Gram budget | A conditional 25-billion **paper theorem target**: source-matched prime-mass and Hadamard envelopes close with positive rational-margin controls. The positivity-to-upper Lean bridge and independent review are still open | [Audit dossier](PHASE153_BERTRAND_CANDIDATE.md) | [Exact constants and edge tests](phase153_bertrand_budget.py) |
| **154** · Prime-window arithmetic geometry | A complete paper-level 8b Nagura candidate and a separately gated 5b Costa Pereira candidate: rank prime, mass primes and real trace metric act on one original integer determinant; no field cutoff promoted | [Dossier](PHASE154_ARITHMETIC_GEOMETRIC_SQUEEZE.md) · [#73](https://github.com/Dojo-1/tenth-discriminant/issues/73) | [Rational/endpoint tests](phase154_prime_window_budget.py) |
| **155** · Jet precision bridge | Directional Frobenius fat-point isomorphism for J≤p, full square quotient certificates at D163, ordinary-vs-Hasse factorial/prime-local counterworld, and sharp Fourier jet interpolation at p−1 real roots | [Dossier](PHASE155_JET_PRECISION.md) · [Lean factorial bridge](../../lean/TenthDiscriminant/JetPrecisionBridge.lean) | [Source-matched finite verifier](phase155_jet_precision.py) |
| **156** · Transport-relative Archimedean jets | Exact integral/PSD/prime-local determinant transports, 2-adic orbit-fold capacity, a fixed-frame counterworld, and a conservative **unproved** Nagura-only 6b field target | [Dossier](PHASE156_TRANSPORT_ARCHIM_JETS.md) | [Finite verifier](phase156_transport_archim_jets.py) |
| **157** · Archimedean π-tight jet radius | Using Mathlib's **3.14 < π < 3.15** to shrink the same original Frobenius-rank ellipse, tighten factorial 2-primary capacity, and pose a conservative Nagura-only **unproved 5b** boundary | [Dossier](PHASE157_PI_TIGHT_RADIUS.md) · [formal π bounds](../../lean/TenthDiscriminant/ArchimedeanPiWindow.lean) | [Same-source verifier](phase157_pi_tight_radius.py) |
| **158** · Walsh-inspired characteristic jets | **p** conjugate-closed roots suffice for the exact original ordinary-jet rank; with **p−1** roots rank is equivalent to an explicit `(S−1)×(S−1)` forbidden-coefficient obstruction, which can fail. D163 source/quotient tests; no new field cutoff | [Dossier and attributed sources](PHASE158_CHARACTERISTIC_JETS.md) | [Exact finite verifier](phase158_characteristic_jets.py) |

| **159** · Observation Gram continuum | Exact real Gram transport with integral lattice and prime-adic distinctions; source-matched D163 deletion controls, explicit p7/p11 counterworlds and full 2-adic valuation nonmonotonicity; **no new field cutoff** | [Mathematical dossier](PHASE159_OBSERVATION_CONTINUUM.md) | [Original-jet verifier](phase159_observation_continuum.py) · [2-adic Smith verifier](phase159_padic_gram.py) |

**One finite two-way obstruction.** For the 21 fixed points at \(D=17,18\), an exhaustive search of all \({21\choose8}=203,490\) supports shows no common 8-point support can preserve the integral image: every joint binary-rank candidate loses ternary rank at \(D=18\). A concrete 9-point support passes exact Hermite equality for all \(D=17,\ldots,21\). **The proof is finite/exhaustive and code-checked, not a uniform statement over fields.**

**One all-integer-parameter statement, with a different scope.** The D-independent eight-real-axis-column lattice contains the changes \(E_\Omega(D+529200)-E_\Omega(D)\) for **all integer D**, with \(\Omega\) frozen to the same 21 coordinate pairs. This follows from integer-valued polynomial finite differences after six exact evaluations, plus a nontrivial Smith exponent. It does **not** assert periodicity of the *varying ellipse* \(\Omega_D\), of the D-dependent trace metric, or of the arithmetic class-number assumptions.

## Reproduce on the one canonical branch

Python 3, SymPy **1.14.0**; exact integer and rational arithmetic is used for certificates. Log determinants in prose are approximations of exact integer values.

```sh
python3 -m pip install sympy==1.14.0
python3 research/reverse_determinant/phase144_verifier.py
python3 research/reverse_determinant/phase144_minimum_support.py
python3 research/reverse_determinant/phase145_ortho_anti_ambig.py
python3 research/reverse_determinant/phase146_translation_newton.py
python3 research/reverse_determinant/phase147_prime_adequacy.py
python3 research/reverse_determinant/phase148_arithmetic_chamber.py
python3 research/reverse_determinant/phase148_fixed_lattice_period.py
python3 research/reverse_determinant/phase151_conjugation_descent.py
python3 research/reverse_determinant/phase152_frobenius_graph.py
python3 research/reverse_determinant/phase153_bertrand_budget.py
python3 research/reverse_determinant/phase154_prime_window_budget.py
python3 research/reverse_determinant/phase155_jet_precision.py
python3 research/reverse_determinant/phase156_transport_archim_jets.py
python3 research/reverse_determinant/phase157_pi_tight_radius.py
python3 research/reverse_determinant/phase158_characteristic_jets.py
```

The single [reverse-determinant CI workflow](../../.github/workflows/reverse-determinant-finite.yml) runs these bounded verifiers on `main` when relevant files change. For the pre-consolidation exact Phase148 receipt, [Actions #41237057425](https://github.com/Dojo-1/tenth-discriminant/actions/runs/41237057425) passed at commit `df9a1e789efa40d709ab2ceb83f10514bc6ec56e`. The [Phase157 finite workflow](https://github.com/Dojo-1/tenth-discriminant/actions/runs/41319645008) passed on its exact source revision; the newly committed Phase158 tests require their **own** exact-head CI receipt. No finite pass promotes the proposed 5-billion field cutoff. Historical older receipts remain linked in the individual phase dossiers.

**Intellectual attribution.** The choice to seek a characteristic subset was inspired by [Miguel N. Walsh, *Characteristic subsets and the polynomial method*, ICM 2018](https://www.mathunion.org/fileadmin/ICM/Proceedings/uploads/ICM-2018-vol2-ver1-eb.pdf). The **p-root criterion and the p−1 coefficient matrix are elementary specializations proved/tested here, not results attributed to Walsh**; Ben Green's derivative determinant, Roelof van Dijk's finite-field method, Tao's challenge and the other participants are credited in [the root README](../../README.md) and [prior-art ledger](../../PRIOR_ART.md).

## The missing bridge

The candidate next theorem is **not** merely “find fewer points.” It is to construct original-ordinary-jet supports \(Q(D)\) on a legitimate parameter family with:

1. exact prime-local/Smith control of the same integral observation image and honest treatment of changed support,
2. an independent interpolation/prime-mass lower theorem applying to \(G_{Q(D)}\), **not inherited from \(G_\Omega\) by image equality**, and
3. a uniform inverse-Gram-free analytic upper for **that same integer \(\det G_{Q(D)}\)**.

A finite support minimum, moving frame, or p-adic periodicity does not discharge these obligations. Independent mathematical reconstruction and draft proof review remain separate [#50](https://github.com/Dojo-1/tenth-discriminant/issues/50), [#51](https://github.com/Dojo-1/tenth-discriminant/issues/51), [PR #61](https://github.com/Dojo-1/tenth-discriminant/pull/61), [PR #62](https://github.com/Dojo-1/tenth-discriminant/pull/62).
