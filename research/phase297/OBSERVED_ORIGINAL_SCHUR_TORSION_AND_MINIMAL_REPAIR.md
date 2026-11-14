# Phase297 — the exact transverse torsion remainder of the ORIGINAL D587 trace Gram

**13 November 2026 — post-result arithmetic ledger.** Pre-registered separately before each Phase297-A/B/C/D executable. All computations are AI-authored, exact modular arithmetic under frozen original source helpers, and reproducible through source-pinned GitHub Actions. No human-independent mathematical review and no new Lean theorem is claimed. **Stacked draft PR #189**, above unmerged Phase296 #188 → #186 → #185 → #184 → #183 → #182. No Work mode; no changes to actual-field PR #157 or original 322^4 research bound.

The user's intended bridge is a **symmetry-compatible integral transverse transport** between the moving-frame mathematics and the original trace Gram, while avoiding changes to the arithmetic lattice and avoiding repeated valuation factors. This Phase297 result is both a constructive answer and a precise obstruction: a **rational** orthogonal projection exists in the ORIGINAL D587 field, but an *integral* orthogonal projection on its unchanged 730-row lattice does NOT exist. The smallest arithmetic repair is an **index-five** transverse sublattice; the unavoidable torsion class must be retained as typed remainder if the original lattice is to remain unchanged. Those are different legitimate objects and must not be conflated.

## 1. The actual source and exact statement

Work within ONE quadratic field stress source, `D=587`, originally sampled as `Q=383` integer ellipse points at radius53, original row rectangle `R=146,S=J=5`, full `730` polynomial monomial rows `Z^r W^s`. All FIVE ordinary derivatives `∂_Z^j` keep W fixed; all real/imag channels use the ORIGINAL trace metric `diag(2,2D)=diag(2,1174)`. Nothing has been remapped to D583, and no extra or synthetic observation has been added. The original sample polynomial lattice and observed metric are not replaced by divided Frobenius rows or a primitive Smith-column basis.

The first725 original monomials `r<145` span `L_old`; the five new ORIGINAL monomials `r=145,s=0..4` span `N_new`. In the original row basis,

```
G_730 = [ A   C ]
        [ C^T B ],      A=G_725,  C=G(old,new).
```

Both Grams are nonsingular over Q (positive Gram of the original independent row evaluations). The rational orthogonal projection coefficients are `T=A^{-1}C`. A `GL_730(Z5)` unipotent Gram block diagonalization that preserves **this original row lattice** exists iff every column of C is in `A Z5^725`. The integral issue is NOT decided by positivity of a Schur complement or by the determinant of a coordinate transformation.

The historical **original-source** valuations are retained exactly (previous Phase292-C, not newly invented):

```
 v5(det A)         = 3855,
 v5(det G_730)     = 3924,
 v5(det Schur_5)   =   69 = 28 even +41 odd.
```

## 2. The cokernel map is the correct integral moving-frame obstruction [P-paper]

Define the **typed transverse pairing class** over `Z5`:

```
 eta: N_new=Z5^5  --->  coker(A)=Z5^725 / A Z5^725,
       t           |-->  [C t].
```

The condition for a fully integral orthogonalization is `eta=0`. If `eta≠0`, the nearest permitted integral transverse submodule is its KERNEL. The key exact sequence is

```
  0 ---> ker(eta) ---> Z5^5 --eta--> im(eta) ---> 0.
```

Here `eta` is not a guessed curvature/gerbe/sheaf obstruction; it is an exact, checkable **finite Gram-cokernel homomorphism**, derived from the same original sampled row/trace pairing. Calling it a higher geometric connection remains a separate [H/S] lift until such a connection is defined and related to eta. Its image is torsion, not an extra independent prime factor in the already-counted determinant valuation.

For finite K, `delta_K=log5 |im([A|C] mod5^K)/im(A mod5^K)|` is exactly the difference of capped Smith exponents. If positive, this proves a nonintegral projection. If zero, integrality is established ONLY when the original old matrix's Smith exponents are FULLY RESOLVED before K, because then `5^K Z5^725 ⊂ A Z5^725` and the modulo5^K cokernel equals the true Z5 cokernel.

## 3. Phase297-A, precision 5^9 — a clean null result with censorship [M]

Preregistered at commit `d7108a8c`; [focused original-source CI #43375032425](https://github.com/Dojo-1/tenth-discriminant/actions/runs/43375032425) SUCCESS.

- Built and verified ORIGINAL Eraw modulo5^9 from the frozen divided Frobenius generator by **reversing its UNDVIDED integer-unitriangular polynomial transformation**. The source's division powers were undone BEFORE computing the Gram. 600 exact independent `jet` real/imag coordinates, 36 independent exact original mixed-moment Gram entries and all 133,225 original even×odd parity cross-pairings were checked.
- Original Gram sectors are **old even363→new even2** and **old odd362→new odd3**; the full old/new row counts 725/730 are unchanged.
- The capped Smith profiles of original old A and [A|C] agree in BOTH sectors modulo5^9; `delta_9(even)=delta_9(odd)=0`.
- But **63 even and62 odd old Gram directions are censored at grade>=9**. Therefore this first zero did NOT prove an integral projection, and the subsequent deeper test was not fitted to a hoped-for outcome.

Hostile positive-definite toy controls show why a Schur determinant cannot substitute for this image/cokernel test: `A=[10],C=[2],B=[2]` has full Gram determinant16 and NONintegral projector 1/5, while `A=[10],C=[5],B=[10]` has an integral 5-adic projector 1/2. No universal monotonic p-adic Schur valuation statement is assumed.

## 4. Phase297-B, precision 5^16 — COMPLETE original cokernel [M + P]

After the inconclusive K9 result, separately preregistered at commit `ae04e06a`, choosing **K=16 in advance**, and retaining the SAME field/rows/observations. [Exact high-precision CI #43375446953](https://github.com/Dojo-1/tenth-discriminant/actions/runs/43375446953) SUCCESS.

The program evaluates the ORIGINAL source Eraw mod5^16 from frozen Phase292 helpers, then replays **EVERY** original Eraw matrix element mod5^9 against Phase297-A, verifies 800 independent integer original-jet coordinates and 36 independent original Gram entries, and checks original full even×odd orthogonality mod5^16. To prevent int64 overflow, the weighted Gram is computed using a base5^6 three-digit decomposition with 128-channel bounded chunks, and arbitrary-precision Python integers are used for the K16 Smith elementary divisors. The hostile Smith controls and exact K9 replay both passed.

**Original old even Gram Smith profile:**
```
{0:63, 2:15, 3:47, 4:63, 5:47, 6:10,
 7:5, 8:50, 9:13, 12:20, 14:30}   (sum=1930).
```

**Original old odd Gram Smith profile:**
```
{0:62, 2:15, 3:48, 4:62, 5:48, 6:10,
 7:5, 8:50, 9:12, 12:20, 14:30}   (sum=1925).
```

**FULLY RESOLVED:** All old Smith exponents are ≤14, strictly below16. Thus this **finite** computation captures the exact old 5-adic cokernel. Adjoining original cross columns changes:
- **Even:** no old elementary factor whatsoever; `delta_16(even)=0`. This **PROVES** that both even original new-row projections are integral over Z5; the prior script's generic `if_zero_still_open` fallback does not apply after confirming max exponent14.
- **Odd:** precisely ONE elementary exponent **14→13**, leaving all others untouched; `delta_16(odd)=1`. This **PROVES** a nontrivial image of order5 inside the exact old odd Gram cokernel.

Consequently

```
  im(eta) ≅ Z/5 Z,
  5 T ∈ Mat_(725×5)(Z5),    T not∈Mat_(725×5)(Z5).
```

There is **exactly one** p5 denominator power, not 0 and not an unbounded or multiply counted index.

## 5. Phase297-C — an independent original-Gram dual functional [M, P implication]

Preregistered separately after B at commit `4eea98d1`. [Explicit original-source dual CI #43375859310](https://github.com/Dojo-1/tenth-discriminant/actions/runs/43375859310) SUCCESS.

Using a tracked integral left Smith row transform only as a proof search device (never moving the original B), it constructs a **362-component original odd-old-row functional** `ell mod5^14` satisfying

```
 ell A_odd = 0                       mod5^14   (ALL 362 columns),
 ell C_odd = (0,0,4*5^13)           mod5^14
                for r=145,s=(0,2,4).
```

The latter is nonzero, so `C_odd` cannot be contained in `A_odd Z5^362`. The vector is deterministically losslessly encoded in the CI output, with exact self-decoding and all original-Gram pairing checks. Its compressed compact-JSON SHA-256 is

`b09bb9c1a2e40772932c25f8edf984898d2ed3606d7e689e135dab554504815b`.

Additionally, an independent full K16 image check proves `5*C_odd` is in the old Gram image (including all three new odd columns) and that every even new column already is in its old image. Thus the odd cokernel's image has **exact order5**, not just at least one denominator.

Since `ell` defines a nonzero homomorphism on the image group of order5, its restriction to `im(eta_odd)` is injective. The original new odd `s=0,2` classes vanish, while **s=4 generates the entire order5 image**. The original even new `s=1,3` classes also vanish. Therefore, in the original five generator basis,

```
eta(t0,t1,t2,t3,t4) = t4 mod5   (after choosing the generator eta(e4)),
ker eta = {(t0,t1,t2,t3,t4)∈Z5^5: t4∈5Z5}.
```

This is the precise **symmetry-typed transverse lattice remainder**. No scalar proxy can replace the actual parity and generator structure.

## 6. Phase297-D — CONSTRUCT the minimal integral transverse return [M + P]

Preregistered before execution at commit `25907fd7`. [Full source-to-Gram constructive CI #43376290535](https://github.com/Dojo-1/tenth-discriminant/actions/runs/43376290535) SUCCESS.

**The minimal admissible sublattice** of the original full row lattice is

```
L' = L_old ⊕ ker(eta)
   = span_Z5{ ALL 725 old original monomials,
              Z^145 W^0, Z^145 W^1, Z^145 W^2, Z^145 W^3,
              5 Z^145 W^4 }.
```

It has **index5** in the actual original 730-row arithmetic lattice L. This inclusion is NOT a GL_730(Z5) automorphism of L; the base changed by the specified index and that exact debt must remain visible. The index is minimal among p-adic sublattices of the five new directions allowing integral orthogonal projection because ker eta itself has index5.

The program recomputes Eraw at p16, tracks BOTH the row/column Smith transforms U,V as integral modular linear solvers for the ORIGINAL old Gram A, verifies `U A V = diagonal` entry-by-entry, tests U,V mod5 invertibility, and solves `A T=C'` modulo5^16. Here C' is the original cross-block with **only the s=4 new-row cross column multiplied by5**. The code rejects the unscaled s4 column with an actual divisibility witness in grade14, and solves all four remaining original new-row columns unscaled. Every old Smith grade is fully resolved (<16), which guarantees an exact Z5-integral lift exists; the printed finite coefficients are one deterministic p16 solution, **not unique canonical coefficients modulo p16**.

It assembles the full 725×5 projection coefficient matrix T in ORIGINAL row order, preserving inversion parity. The CI then reconstructs the five ACTUAL corrected original observation-jet row vectors and confirms:
- **ALL 725×5=3,625 original trace-Gram cross pairings vanish modulo5^16**;
- the full 5×5 transverse Gram is symmetric and agrees with the original-source Schur formula in all25 entries modulo5^16;
- exactly one original generator `Z^145 W^4` is scaled by5, and all the other729 original generators are not scaled;
- no Frobenius, source Smith COLUMN or synthetic-sampler change has been smuggled into the metric;
- positive and negative integral/nonintegral Gram controls pass.

The deterministic SHA-256 of the chosen JSON row-major matrix of 725×5 coefficients T mod5^16 is

`5bd8994090188feb7817bf6f6c0a194f5f0c4b48339baac2810641f2f389ee57`.

Over Z5, the resulting integral **UNIPOTENT** row-frame transformation of L' has determinant1, while the inclusion `L'→L` has determinant5. Since a row scaling by5 multiplies the corresponding Gram determinant by 5², the typed determinant ledger is:

| Object | v5(det old A) | v5(det full Gram) | v5(det Schur) | Even / odd Schur v5 |
|---|---:|---:|---:|---|
| ORIGINAL full D587 L | 3855 | **3924** | **69** | 28 / 41 |
| MODIFIED index-five sublattice L' | 3855 | **3926** | **71** | 28 / 43 |

These are two **different lattices**. The extra 2 in the index-five Gram is not an improvement or additional factor for the original source. Adding `+1` for the cokernel obstruction, or `+2` for L', to the ORIGINAL v5(det G730)=3924 would **double-count/change the research object**.

## 7. What has been closed, and what has not

**Closed [P-paper + finite M]:** The original D587 five-row transverse projection is **not integral** on the unmodified full arithmetic row lattice; its exact original-gram cokernel obstruction is `Z/5` carried by the new odd `(145,4)` generator. The smallest modification of the transverse lattice which permits integral orthogonalization is the index-five kernel. An explicit 725×5 projection is computed modulo5^16 with all original source/trace/jet and symmetry gates. The source and metric remain original within that test, except for the **explicitly declared and costed lattice modification**.

**Still not closed [H]:** The originally requested **no-arithmetic-lattice-change** return of an arbitrary higher-dimensional observable to the actual original D587 trace Gram by such an integral *orthogonal* projection: it is obstructed, not constructed. One may retain the torsion remainder `eta` as an additional typed datum, use a NON-orthogonal compatible integral frame, or accept the index-five repair; each option is a different mathematical demand. A higher-dimensional sheaf/worldlet/adiabatic geometric transport that preserves the source and proves a UNIFORM contribution across genuine class-number-one-admissible discriminants remains open. Both the D583/D587 stress fields are not class-number-one, so no tenth-discriminant cutoff follows from the Phase297 exact finite result.

**Evidence:** [P-paper] finite Smith index and exact p-adic cokernel capture once max old exponent<K; dual functional obstruction; index-five kernel and unipotent Schur block splitting; determinant index-square law. [M] four source-pinned, preregistered, exact modular original D587 CI experiments with a direct functional, a fully original 725×5 reconstructed Gram solver, hostile controls and deterministic digests. All AI-authored and correlated; external independent math/source-to-field review #50/#51 is still required. [R] finite K9 null implies integral, an abstract primitive isometry is the original row gauge, matching modulo5 raw jets transports divided Frobenius rows, and an altered-lattice determinant adds valuation factors to the original Gram.

**Next smallest theorem target:** Develop the `eta` *transport-with-remainder* interface over **nested original row additions for multiple genuinely h1-admissible sources**, preserving both the original Gram and source integer row lattice. Specify composition of cokernel homomorphisms and their exact-sequence maps across successive attachments rather than assuming p-adic Schur monotonicity. Only prove a new field cutoff if a uniform h1-specific arithmetic inequality survives independent human/source-to-field verification. No Work mode and keep the draft stack unmerged.
