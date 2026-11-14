# Phase317 — BEFORE CODE: exact first nonrational norm fibre and the two 5-adic Smith slices

Date: 2026-11-14 Europe/Madrid. This preregistration is written BEFORE Phase317 scripts or CI. Branch created from Phase313-316 research consolidation commit f89e95435df59b832eb61e737c919cf264cb291d on research/phase312-fermat-ray-moments. Upstream Phase312/311 PRs remain draft. **No main merge and no change to the reported 322^4 discriminant cutoff.**

## Living question

We have an exact GLOBAL realizability obstruction in D163 at original integer-order norm164: 2 synthetic norm/conjugation-compatible signed conductor125 ray tags fail to be realized by the 4 exact integer generators; they change 363 entries of the same primitive 40x40 Gram modulo25 without changing it modulo5. Do those changes modify a *Smith digit* or merely matrix coordinates? And how much of the exact norm-D+1 fibre arithmetic is genuinely specific to class number one?

Two independent research lines follow. Keep them separate.

## A. The first nonrational norm fibre: an elementary universal theorem

Let D=4m-1>3, m≥2, and O'=Z[sqrt(-D)] with norm x²+D y². For the FIRST nonrational signed norm shell at n=D+1=4m:
  * y=±1 forces x=±1, giving exactly four nonrational integral solutions (2 signed classes).
  * y=0 contributes TWO additional rational solutions x=±2sqrt(m) IF AND ONLY IF m is a perfect square.
  * |y|≥2 is impossible as D y²> D+1.
Therefore there are exactly 4+2*[m is a perfect square] integer elements in the norm-(D+1) fibre, with signed classes 2+[m square].

Under h(K)=1 and D fundamental (squarefree D≡3 mod4), m MUST be prime: otherwise any rational prime p|m with p<m yields an ideal of norm p from the ring homomorphism O_K=Z[omega]→F_p, omega↦0 (minimal polynomial X²-X+m has simple root 0 modulo p). Since h1 every such ideal is principal, giving a generator norm p<m. The Phase316 small-norm form theorem forces any such generator to be an ordinary integer with SQUARE norm, contradiction since p is prime. This class-number-one=>prime m assertion is standard elementary number theory and is **NOT** a new discriminant bound. The field class-number-to-principal-ideal bridge is [P-paper conditional] and NOT automatically covered by the Phase316 Lean polynomial norm-form proof.

Strict controls:
  * h1 fundamental D7,11,19,43,67,163: m prime, exactly 4 norm-D+1 solutions.
  * h>1 fundamental D187: m47 prime, ALSO exactly 4 norm-D+1 solutions. Therefore that fibre alone is NOT a class-one detector.
  * fundamental D35: m9 square, exactly 6 solutions; if this control fails, the four-solution claim lacks a hypothesis and must be retired.
  * sample further squarefree D≡3 mod4 with nonsquare composite m if possible, to prove that "m nonsquare" is weaker than "m prime."
  * count signed ray residues only for 5-units; for p=5 divisor of D+1, report nonunit stratum and never invent ray tags.

## B. First TWO Smith layers of SAME original integer-order Gram mod25

The earlier Phase315 native D163 source is fixed:
D163, rho21, Q109, R40/S=J1, exactly15 original Frobenius25 row divisions and the native trace pairing. Phase316 synthetic norm-preserving trace-zero ideal-character twist preserves the ENTIRE original primitive Gram mod5 but changes 363 of1600 cells mod25, all arising at norm164.

For each 40x40 matrix A over Z/25, compute the invariant elementary divisor counts
  e0 = #{Smith exponents 0} = rank_F5(A mod5);
  e1 = #{Smith exponents 1};
  e≥2 = 40 - e0 - e1.
Find e1 by exact invertible pivot elimination over Z/25 on every unit pivot, then extracting the residual Schur complement divided by5 and taking rank_F5. Use independent integer residue arithmetic. This is a UNIMODULAR-equivalence invariant, not a spectral approximation.

Frozen checks:
  1. e0=23 on actual and synthetic A; verify every intermediate pivot is a unit and the entire residual is divisible by5.
  2. Check e0+e1+e≥2=40 and reconstruct the rank of A as an F5-linear map modulo5; compare against a second direct count of sizes of the kernel in (Z/25)^40 if computationally feasible through exact formula |ker(A)|=5^{e1+2e≥2}.
  3. Independently compare with an explicit integer 2x2 and 3x3 hostile matrix for which first and second Smith layers are known; include row/column permutation invariance and unimodular row/column shear invariance to reject a pivot-order bug.
  4. Compare actual original and synthetic Gram e1. DO NOT predeclare that they differ. If identical, report that 363 changed mod25 cells did not change first two Smith layers; if different, report a sharp countermodel that all earlier constraints fail to fix e1.
  5. Repeat the original matrix reconstructed from the exact norm164 tags ONLY; verify it matches the unchanged original. Removing the synthetic difference in that one fibre must restore all1600 entries.

## C. Lean (narrow) and mathematical frontier

Lean target: formalize the elementary norm-D+1 nonrational fibre restriction (if y≠0, then y²=1 and x²=1) for m≥2; separate existence of the four signed solutions. Optionally formalize the conditional six-versus-four count under m-square/no rational sqrt, only if proof compiles without opaque assumptions. Do NOT present this Lean statement as class-number-one=>m prime unless the ideal-theoretic implication is actually formalized.

Next decisive uniform theorem: obtain a h1-specific condition on TRUE globally realized norm-constrained ray supports that forces a residual Smith e1 (or higher) gain in the NATIVE large-field original Gram INDEPENDENT of inherited valuationWeight. A finite synthetic gauge difference is not enough.

[P] elementary norm-fibre conditional result and exact modular Smith algebra. [M after exact CI] bounded original D163 Smith comparison, h1/nonh1 numerical controls. [H] any uniform new determinant valuation, any change to reported bound. [R] "four generators implies class one" or "363 cell changes imply extra Smith valuation" without actual verification.

If any source, nonunit gate, pivot, four-vs-six control, original Gram or hostile Smith invariance fails: stop and preserve the failure. Keep Phase317 PR draft, upstream parent draft, main unchanged.
