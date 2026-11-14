# Phase298 — preregister composition of original Gram-cokernel remainders

**13 November 2026, before any Phase298 implementation or measurement.** AI-authored mathematical research, external human verification outstanding. Stacked DRAFT above Phase297 #189 and its ancestor drafts. No Work mode, no merge, no changes to original D587 sampler, the 322^4 theorem or draft cutoff PR #157.

## Exact mathematical seed: composition must not sum valuation-like labels

Phase297 established from the complete ORIGINAL D587 n730 source with Q383/J=S5/trace B=diag(2,1174) that the FIRST 725 original monomial rows have Gram A; among the five actual NEW r145 original monomials, s=0,1,2,3 each have a Z5-INTEGRAL projection into the OLD 725, while s=4 has an exact order-5 coker(A) class. Full Gram v5 3924, old Gram v5 3855, Schur v5 69; these are historical observations, not prospective results.

We now examine genuine *nested original row modules* without ever changing the arithmetic lattice:

L0 = first725 original rows;
L1 = L0 plus ORIGINAL r145,s=0,1,2,3 (729 rows);
L2 = L1 plus ORIGINAL r145,s=4 (730 rows).

Also test the REVERSED order L0 ⊂ Lbad=L0 plus ORIGINAL s4 (726 rows) ⊂ L2, where the second stage adds the four original safe rows. The order matters to projections: do NOT assume that stagewise cokernel indices add to v5(det G) or even to each other.

### Elementary integral-split composition theorem [P-paper target]

Over a DVR R=Z5 with nonsingular symmetric Gram, use basis (L0,N1,N2):

```
G = [ A    C1   C2 ]
    [ C1^T B1   E  ]
    [ C2^T E^T  B2 ].
```

Assume **FIRST-STAGE INTEGRAL**: T1=A^-1 C1 ∈ Mat(R). Then an integral unipotent change of the FIRST TWO blocks gives Gram(L1) ∼ diag(A,S1), where S1=B1−C1^T T1 ∈ Mat(R), and it sends the later cross block [C2;E] to [C2; E−T1^T C2] (note sign and transpose). Therefore the SECOND-STAGE obstruction
```
eta_(1→2): N2 → coker(Gram L1)
```
decomposes under this actual integral frame as the PAIR
```
eta_(1→2)(n) = ([C2 n] in coker A,
                [(E−T1^T C2)n] in coker S1).
```
The second projection is integral iff BOTH components vanish. For a SINGLE N2 generator, the order of its coker image in the direct sum is **lcm** of component orders (over p-primary groups, p^max(h0,h1)), NOT product (p^(h0+h1)). If N2 has multiple generators, determine the GROUP generated jointly; do not add separate scalar indices without proving independent direct-product images. This theorem is conditional on *first-stage* integrality. If the first stage is nonintegral (bad-first chain), it does not apply; use actual enlarged Gram Smith directly.

The first-stage integral isometry is a `GL_(729)(Z5)` row-frame on the UNCHANGED original 729-generator lattice; no sublattice scaling is allowed in Phase298's production run. Its p-adic row map is not an arbitrary geometric gauge: every coefficient is solved on the SAME original trace Gram.

### Prospectively fixed exact experiments (unknown outcomes)

1. Freeze existing original source helpers and Phase297 implementation, including:
   - `research/phase297/original_schur_integrality_k16.py` blob `aa3678001c69a7235dca638638d2dab4c55b05b3`;
   - `research/phase297/minimal_transverse_repair.py` blob `22b0077a2424553021a4c9859f92f0fe3efc2fe7`.
   Their frozen parent guards must pass. Reconstruct original Eraw mod5^16 and verify all 800 original-source/ordinary-jet coordinates and original six-row Gram oracle, source rows R146/Q383 unchanged; no synthetic points or Frobenius-normalized rows substituted for original.
2. Construct A (725 old rows by same original parity 363/362), C1 (725×4) for unscaled original r145,s0..3, C2 (725×1) for unscaled original r145,s4, B1 (4×4) and E (4×1) using the original trace B and overflow-safe exact Phase297 three-digit method. Compute the genuine 5×5 new-new Gram including all s labels. Check full C2 parity (even/odd) cross pairings ZERO modulo5^16.
3. Solve *all* four original C1 columns `A T1=C1 mod5^16` using the pinned original old-Gram tracked Smith solver separately by parity. Require no denominators; check all 725×4 source-correct residues. Construct `S1=B1−C1^T T1` and `E'=E−T1^T C2` EXACTLY modulo5^16; verify symmetry and parity, and independently verify that the corrected original four NEW Eraw row vectors have Gram S1 and pairings E' with the final uncorrected s4 original row.
4. Run high-precision Smith on `S1` and `[S1|E']` to measure the **new Schur-cokernel** obstruction at the second stage, separately from the already-known original old eta(s4) of exact order5. **No preregistered prediction** for S1's Smith exponents, finite coker image debt or whether they are fully resolved by K16. If censored at16, report a finite lower diagnostic and leave exact order open. If resolved, compute the exact order of the one residual class and predict the composite class order as p^max(1,h_S1). Do not assert independence or sum the two indices.
5. Reversed original attachment order L0→Lbad=(old+original s4)→L2: the first-stage original eta has order5, so the integral-split composition lemma is **inapplicable**. Compute the *actual* original odd-sector 363×363 Gram of Lbad, its cross block with the original s0,s2 rows, and use capped K16 Smith to measure the second-stage image-index. Compare measured results against the split-first chain but do not force equal values; the old row lattices differ at stage1. Even original row sector stays old363 and s1,s3 are already integral. Guard n=363 within the original Smith implementation limit. No concatenating unfinished integer source lattices across different D.
6. Independent hostile toy A=[1], C1=[0], B1=[5], C2=[0], E=[1], B2=[2] gives first-stage integral and old component0 but residual S1=5, E'=1 carries order5; full positive-definite Gram. A second positive-definite toy A=[5], C1=[5], B1=[10], C2=[1], E=[2], B2=[10] gives T1=1 and S1=5, with two nonzero order5 components for the SAME new N2 generator, whose combined order is5 (NOT25). Verify full Gram positive principal minors and exact modular Smith images against these paper calculations. Both toy controls must fail any code that adds debt scalars as if independent.
7. Preserve the original old/full v5(det Gram)=3855/3924 and old Schur 69 as historical, and **do not** add either nested coker index or partial Schur valuation to these originals. Any optional nested `v5(det S1)` computed from a fully uncensored 4×4 Smith is a genuine nested determinant decomposition, not an additional factor.

**Stop rules:** stop if any original source/jet/metric guard drifts, any unscaled s0..s3 projection becomes nonintegral, `E−T1^TC2` fails independently checked source pairing, cross parity fails, a higher-level Smith is censored but claimed exact, or the hostile toys contradict the stated composition law. Preserve unexpected findings; no changing p,D,K,old/new labels or stage order post-result.

**Evidence:** [P-paper] conditional integral-split composition and direct-sum/lcm order lemma; [M after CI] exact D587 original nested lattice results. [H] arbitrary chains with nonintegral first stages and uniform h1-admissible field implications. [R] p-adic image-index increments as independent determinant valuations, automatic composition without integral-split hypothesis, and treating finite K zero as infinite integrality when Smith grades are censored.
