# Phase385 — Frobenius lower factor is stable; the residual pairing is not

**22 November 2026.** Research continuation under Tao's tenth-discriminant challenge. All comparisons are exact integers, using original `integerDerivativeRow`, rectangular monomial order, `integerPairTrace`, and `ellipsePairs` semantics. These are finite tests, **not** a new unconditional bound or an independent large-D analytic proof.

## Identity and object

Fix `D`, odd inert `p`, `R,S,J`, and ellipse `Q`. The original integer jet matrix `E_Q` has rows indexed by `(r,s)`, columns `(j,a,coordinate)` and metric `B_Q=diag(2,2D,...)`. Therefore `G_Q=E_Q B_Q E_Q^T`. Let `k_(r,s)=min(floor(r/p), S-1-s)` and let the *integer unimodular* basis matrix `U` send the `(r,s)` monomial to `Z^(r-pk) W^s (Z^p-W)^k`. Frobenius/ordinary-Z-jet divisibility supplies `U E_Q = Δ_p F_Q`, with `Δ_p=diag(p^k)`. It follows that

`det G_Q = p^(2 F(p)) det H_Q`, where `F(p)=sum k_(r,s)` and `H_Q=F_Q B_Q F_Q^T` is an integer Gram.

This identity is a source-independent reconstruction of the **already proved** `rectangularTraceGram_valuation_of_frobenius` path. The new experiment isolates `v_p(det H_Q)` and asks if it is transportable across nested source observation sets.

## Real Loewner monotonicity does NOT imply p-adic divisibility monotonicity

For `D=43`, inert `p=3`, `R=7`, `S=J=3`, one has `F(p)=9`, so the uniform source divisor has exponent 18. The ordinary-jet source ellipse cases give:

| Radius | # Q | v3(det G) | v3(det H) | rank(F mod 3) | rank(H mod 3) |
|:--:|--:|--:|--:|--:|--:|
| 8 | 35 | 32 | 14 | 21 | 8 |
| 9 | 45 | 18 | 0 | 21 | 21 |
| 10 | 51 | 19 | 1 | 21 | 20 |
| 12 | 67 | 18 | 0 | 21 | 21 |

All determinants are **positive** and exact integer determinants. `Q_8 ⊂ Q_9`, so the real matrices satisfy `G_9-G_8 ≽ 0`, and likewise `H_9-H_8 ≽0` as sums of weighted outer products of the additional normalized jets. Nevertheless the residual determinant valuation falls from 14 to 0. Thus no **radius-uniform extra exponent** follows from the uniform 18-factor; added observations may destroy the residual mod-3 radical. This is not an optimality theorem for the specific production thin ellipse.

At `rho=8`, mod-3 `H` has corank 13 but `v3(det H)=14`. Standard Smith theory therefore forces local invariant exponents `[0]×8 + [1]×12 + [2]×1`; at `rho=9`, all 21 exponents vanish. This explicitly exhibits a second p-adic Smith layer in a finite source Gram. Earlier I incorrectly guessed that residual valuation would always equal radical dimension; the case `D=19,p=3,rho=9,R=7,S=3` has residual valuation **2** but radical dimension **1**, refuting that first-layer-only conjecture.

## Two negative controls

**Split prime.** With `D=19,p=5,R=7,S=J=3,rho=9`, the transformed row factors `p^k` fail. The local Frobenius-conjugation assumption is necessary; the source test rejects that invalid implication. The exact Gram has `v5(det G)=1`, not the false claimed `2F(5)=8`.

**Hasse versus ordinary derivatives.** The original ordinary `∂_Z^p(Z^p-W)=p!` is divisible by `p`, but the Hasse derivative coefficient at order `p` is `1`. Thus replacing ordinary derivatives by Hasse derivatives would remove a load-bearing row factor at `j=p`. For `p=3`, `6≡0 (mod 3)` but `1≠0`.

## Higher residue dependence of normalized quotient jets

In the same source `D=43,p=3` test, points `0`, `3` and `6` on the real axis all reduce to residue zero mod 3, yet the normalized original Frobenius row 

`q_3(x)=(x^3-x)/3 mod 3`

returns `0,2,1` respectively. Hence the normalized quotient cannot be reconstructed from **only modulo-3 source sample classes**. The first quotient can depend on modulo-9 information, and a `p^k` quotient in general calls for up to `p^(k+1)` input precision. This is a useful hypothesis-generator for deeper Smith layers, not a proof of a uniform extra factor.

## Reproduction, provenance, gates

`python3 phase385_nested_source.py` is a standalone SymPy implementation using **binomial polynomial expansions**, not the previous direct quadratic-pair multiplication. The detailed accompanying scripts `ordinary_jet_multi_prime.py`, `normalized_radical.py`, and `nested_ellipse_arithmetic.py` provide a second formulation, derivative-row decomposition and nested-ellipse identity. Both implementations passed locally. The determinant is accepted only after an agreement between SymPy's domain-Gaussian and Bareiss methods. No floating-point tests, heuristic interpolation or external class-number oracle.

The original proof **already contains** generic Lean modules `InertFrobenius.lean`, `FrobeniusJet.lean`, `RectangularRowAction.lean`, `RectangularGramFactor.lean` and `BinaryNullTraceGram.lean`. This phase adds **M** (independently implemented finite regressions) and **P** (the elementary factorization/inertia consequences), not a new large-D Lean field theorem. `Phase384` and `MMF14` exact-head Lean builds passed separately. The source-to-field and production-ellipse review issue [#50](https://github.com/Dojo-1/tenth-discriminant/issues/50) remains open.

**Kill rule:** if the true production `Q`, ordinary derivative, Frobenius basis matrix or trace weight differs from these definitions, retract the comparison and replay it with corrected source objects. **Stop rule:** do not promote residual factors found on one finite ellipse into a uniform stronger discriminant bound without a theorem controlling the normalized Gram's higher Smith layers *on the exact production supports*. No merge or publication claim.
