# Phase386 — One extra p-adic digit suffices for normalized Frobenius jets

22 November 2026 · source-faithful research draft · no claim of a new tenth-discriminant cutoff.

**Primary objective:** retain Professor Tao's original tenth-discriminant/Siegel-zero challenge. Improve the mathematical *method* and its reproducibility without claiming novelty over the repository's historical higher-Smith work or substituting a more convenient Gram.

## Frozen source

Use the same objects as `lean/TenthDiscriminant/IntegerTraceGram.lean`, `RectangularRowAction.lean`, `RectangularGramFactor.lean`, `LatticeEllipse.lean` and `TunedRadiusFamily.lean`:

- Original order `A_D=Z[beta]`, `beta^2=-D`, `star(x+y beta)=x-y beta`.
- Original positive trace `Tr(v*star(w))=2(v_re*w_re+D*v_im*w_im)`.
- Original ordinary Z derivatives, with W fixed, at the **same** source samples `Q=ellipsePairs D (thinRadius D)`; `J=S` in production.
- Rectangular basis change `P_(r,s)=Z^a W^s(Z^p-W)^k`, with `k=min(floor(r/p),S-1-s)` and `a=r-pk`, and existing unimodular row matrix `U`.
- Prime p odd and **inert** in this source order; hence `z^p-star(z)` is divisible by p in BOTH integer coordinates for every z in A_D.

## 1. A stronger source-jet precision theorem (paper proof)

Set `delta(Z,W)=Z^p-W`. For each source evaluation z, define the integral Frobenius quotient `q_p(z)=(z^p-star(z))/p`. For every integer `1<=t<=p`,

`(d/dZ)^t delta(z,star(z))/p = ((p-1)!/(p-t)!) * z^(p-t)`, 

which is an integer polynomial in the source pair coordinates. At `t=0` the corresponding quotient is exactly `q_p(z)`; for `t>p` it vanishes.

The generalized **ordinary** Leibniz rule for `Z^a W^s delta^k` divides out `p^k` **one delta factor at a time**, leaving an integer sum of products of `q_p(z)` and the displayed higher-derivative factors. It is valid for every nonnegative `k`, *all* derivative orders `j`, and every actual integer sample, including `j>=p`. No Hasse derivative substitution is made.

If source pairs `z=z' (mod p^(m+1))`, then `q_p(z)=q_p(z') (mod p^m)`, because integer polynomial powers and conjugation preserve congruence and division by the KNOWN p factor loses exactly one digit in this argument. Every other factor is integral-polynomial in z and star(z), hence already agrees modulo p^m. Therefore

`(dZ^j P(z,star z))/p^k = (dZ^j P(z',star z'))/p^k  (mod p^m)`.

**Precision improvement:** modulo `p^m` the normalized source jets need **p^(m+1)** input precision, independent of k. The prior Phase385 sufficient bound `p^(k+m)` is still true, but it is grossly conservative for this *special Frobenius product*. For m=1 this means source residues mod p^2, not p^(max(k)+1). The test family and the exact product polynomial are essential premises; the statement is false for an arbitrary integer-valued quotient polynomial.

## 2. Exact histogram identity and finite Smith-rank corollary

Let `n=R*S` and let `F_Q` be the full normalized integer source jet-evaluation matrix, with `2*J*|Q|` scalar columns. The original integer Gram factorizes exactly as

`G_Q=U^{-1} Delta F_Q B_Q F_Q^T Delta (U^{-1})^T`, with `det(U)=1`, `Delta_ii=p^k_i`, so `det(G_Q)=p^(2*sum_i k_i)*det(H_Q)` and `H_Q=F_Q B_Q F_Q^T`.

The new theorem implies that modulo p each scalar column of F_Q at a fixed derivative order j and trace coordinate is **constant on source residue classes (x mod p²,y mod p²)**. There are at most `p^4` classes. Writing `h_c` for the EXACT count of points in class c,

`H_Q mod p = sum_(c,j) (h_c mod p) * F_(c,j) B F_(c,j)^T`.

Here F_(c,j) is an `n x 2` block, and B=diag(2,2D). Thus, if A is the number of residue classes with `h_c != 0 (mod p)`, then

`rank_(F_p)(H_Q) <= 2*J*A <= 2*J*p^4`.

Provided the **same source Gram** has nonzero determinant, the Smith decomposition gives

`v_p(det G_Q) >= 2*sum_i k_i + max(0, n - 2*J*A)`.

This is a *separate residual rank bound after the older Frobenius factors*, but **not a novelty or improved cutoff claim**: earlier repository Phases206–208 and 278–284 already investigate much deeper Smith layers, and any aggregate new prime mass must be compared against them and counted once. This bound uses the raw Frobenius-normalized matrix, not a fully primitive residual Smith matrix.

The same argument works modulo p^m for the Gram reconstruction with at most `p^(2m+2)` residue classes; a first-layer rank lower bound alone does not determine all higher Smith exponents.

## 3. An exact production-geometry test, not the production determinant

Choose `D=322^4+15=10,750,371,871`, a prime with `D mod4=3`, `D mod3=1` so p=3 is inert. Use **the actual repo parameter definitions**, not toy R,S:

| Object | Exact value |
|---|---:|
| `R=D//4` | 2,687,592,967 |
| `S=R//25=J` | 107,503,718 |
| `thinRadius=ceil((11/25)*D^(3/4))` | 14,689,950 |
| `max k` | 107,503,717 |
| `|ellipsePairs D thinRadius|` | 6,538,432,431 |
| Classes `(x,y) mod 9` | 81 |
| Classes with `h_c !=0 mod3` | 59 |

The exact source ellipse cardinality and 81-class histogram are computed by `y`-slicing and integer square roots; the program never allocates or enumerates 6.5 billion points. Only 283 y-slices are required. The universal full-`J=S` bound is

- `n=288,926,236,423,151,306` actual production row labels;
- `rank(H mod3) <= 17,415,602,316` from all 81 classes;
- `rank(H mod3) <= 12,685,438,724` from the 59 nonzero-weight classes;
- **conditional on nonzero det**, `v3(det H) >= 288,926,223,737,712,582` for this D.

The scalar normalization in `NormalizedComparison.lean` is **`comparisonScale(R,S)=R²*S`**. The extra `p=3` factor gives a normalized real log gain of just `(R-118)*log(3)/R² ~ 4.09e-10`. Even a favorable sum over all small eligible primes would not, by itself, bridge the current scalar comparison margin; the method is meaningful as an arithmetic/algorithmic transport result, not an immediate bound improvement.

The code computes **only five selected source rows and four derivative channels** of the actual production `Q`, and matches direct/histogram modular Grams on multiple finite ellipses. It does **not** compute the full production `n x n` Gram or infer its exact Smith profile. No hypothetical class-number-one property of the chosen D is assumed.

## 4. Bounded checks and hostile cases

`test_phase386.py` uses only Python standard-library arithmetic. It checks:

1. Exact original ordinary Z derivatives against an **independently written** quadratic-pair oracle, including `j>=p`, `k<=5`, and both mod3 and mod9.
2. Precision transport under source shifts by 9 (mod3) and 27 (mod9) for every small source row and selected high-k production rows, including `k=S-1`.
3. Split-prime D=19,p=5 **must fail** the inert normalization; source modulo3 alone **must fail** to recover the normalized first Frobenius quotient.
4. Exact source Q histogram reconstruction vs direct enumeration at D=43, radii 8,9,10,12, producing the older normalized Gram mod3 ranks `8,21,20,21` and agreeing modulo9.
5. Exact production radius and full point count by integer arithmetic, nonzero histogram size and inversion symmetry, 59 active weighted classes, and a selected five-row/four-channel modular Gram.
6. Code/mathematical rank bound and a comparison against the original `R²S` denominator. There is **no** experimental full-Gram determinant for production D.

## 5. Prior work, falsification and next gate

- **P (paper, conditional):** generalized Leibniz source-jet precision, class histogram factorization, first Smith-layer rank bound.
- **M (bounded exact):** source-jet reference implementation, 6.5b-point Q histogram computed by slices, small direct-Gram crosschecks, high-k probes.
- **A:** existing source Frobenius divisibility and unimodularity, and full production determinant positivity from the original interpolating geometry.
- **H:** full Lean formalization of the new p^(m+1) transport and matched source-type rank lemma; exact uniform extra Smith mass with non-overlap and enough normalized magnitude to change Tao's cutoff.
- **R:** Phase385 **heuristic** assumption that p^(K+m) is a *necessary* input precision; it is only sufficient. Any interpretation of the five-row/four-jet production probe as a proof of the full determinant is retired.

**Kill condition:** a single matched ordinary-jet source sample where normalized jets fail to descend modulo p^(m+1), or a mismatch between the histogram Gram and direct integer Gram on the same Q, terminates this precision claim. **Stop condition:** do not spin new hypercomplex architectures or advertise an improved field bound without an exact production-scale theorem whose gain survives the original `R²S` normalization and independent source-to-field review [issue #50](https://github.com/Dojo-1/Tenth-Discriminant/issues/50).

Other lines remain separate: externally checked Dirichlet-GRH interface; Masullo A15 still lacks angular-uniform zero-count/Weil positivity; MMF14 conductor saturation passed Lean; Selberg–Ihara's negative-index/positive-generator obstructions remain unchanged.
