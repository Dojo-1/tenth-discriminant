# Phase300 — preregister composition of TWO nonintegral row attachments by an actual common orthogonal gluing lattice

**2026-11-13. BEFORE Phase300 code, experiments and results.** This is source-grounded mathematical research, not a claim of novel overlattice theory or a field discriminant improvement. DRAFT stacked on Phase299 #191 → Phase298 #190 → prior drafts. User forbids Work mode. Do not merge or alter main, source helpers, original primitive-lattice / full-field statements, 322^4 bound or PR #157.

## Recover the exact prior evidence and choose cases with no post-hoc fitting

The prior full ORIGINAL D163/J=S1/Q109/R40 consecutive-chain scan [Phase298-B exact original CI #43379240150](https://github.com/Dojo-1/tenth-discriminant/actions/runs/43379240150) recorded 38 complete cases. The FIRST two consecutive **nonintegral** stages are the ORIGINAL monomial row inclusions
```
L33=span(1,Z,...,Z^32) ⊂ L34=L33+Z^33 ⊂ L35=L34+Z^34,
```
whose Phase298-B finite cokernel image debts are **1,1**, with all old/intermediate Smith grades uncensored at precision16. The only SECOND such consecutive pair in that scan is L38⊂L39⊂L40 (also 1,1). Selection of these cases is **RETROSPECTIVE based on Phase298-B**, explicitly declared; no fresh source outcomes have been used for this preregistration.

D163 is a genuine class-number-one FIELD (classical Minkowski plus 2,3,5,7 inert), but the repository sampler is the ORIGINAL `Z[sqrt(-163)]` integer ellipse, not the maximal-order full two-coset lattice. R40/S=J1/Q109 is a low-jet original control, not a high-J field uniformity test.

## Paper-level two-step gluing identity [classical algebra, not novel]

Over R=Z5 with Q5 fraction field, take a primitive chain of **UNCHANGED original lattices** L0⊂L1⊂L2, each inclusion adding exactly one original row y1,y2, and original nondegenerate symmetric Gram in actual row labels

```
G2 = [[A,c1,c2],
      [c1^T,b1,e],
      [c2^T,e,b2]].
```

Assume BOTH rational orthogonal projections are nonintegral of exact denominator exponent1:
`t1=A^-1 c1 ∉ R^n, 5t1=a1∈R^n`,
and `t2=G1^-1 [c2;e] ∉ R^(n+1), 5t2=(a20,a21)∈R^n⊕R`.

Define **genuine elements of the unchanged original L2**:
```
k1=5 y1 − a1·old,
k2=5 y2 − a20·old − a21 y1 .
```
Since k1⊥old, and k2⊥L1, the sublattice
```
N=L0 ⊥ R k1 ⊥ R k2 ⊂ L2
```
is orthogonal, with index **25**, not an automorphic change of L2. The original L2 is recovered from N by a finite bilinear-isotropic gluing subgroup
```
Htot=L2/N  ⊂ D(N)=D(L0)⊕D(Rk1)⊕D(Rk2)
```
of order25. The classical overlattice theorem gives `D(L2) ≅ Htot^⊥/Htot`. This is a discriminant-form *span/overlattice*, not a fabricated canonical quotient map D(L2)→D(L1)→D(L0).

The exact integral-coordinate inclusion matrix from the orthogonal N basis to the ORIGINAL L2 basis is
```
B_N = [[ I_n,  -a1,    -a20],
       [  0,     5,    -a21],
       [  0,     0,       5]].
```
Thus `det(B_N)=25`, and `G_N=B_N^T G2 B_N=diag(A,m1,m2)`, with `m_i=(k_i,k_i)∈R`. The ORIGINAL determinant valuation is
```
v5(det G2) = v5(det A)+v5(m1)+v5(m2)−4.
```
The `−4` is index-SQUARED correction for p², not added determinant mass.

**The new structural distinction:** mod out the original old generators. Htot has presentation with generators u=[y1],v=[y2] and relations `5u=0`, `5v−a21*u=0`. Therefore:
- if `a21 mod5=0`, `Htot≅(Z/5)^2` (split);
- if `a21 mod5≠0`, `Htot≅Z/25` (cyclic, nonsplit).
Both have order25 but they carry different torsion extension data. This statement depends on the exact original row basis, but the abstract group type is invariant under unimodular reparametrizations of the same chain. The criterion is exact if a21 mod5 is known, even if all projection coefficients are computed only modulo5^16, provided old/intermediate Smith grades are <16 so every mod5 coefficient is determined by the exact Z5 solution.

The two *individual* H1,H2 are cyclic order5; their composition need not be the direct product. For bilinear isotropy, the generator cosets of y1 and y2 in D(N) have Gram self/cross pairings integral because they are ORIGINAL lattice vectors. Test the corresponding rational decomposition with a common denominator25 on the unchanged G2 (see below).

## Preregistered toy controls: same h1=h2=1 but different Htot group type

All are positive definite exact integer Gram blocks built over R:
```
Gcyclic = [[25,5,1],[5,10,0],[1,0,10]],
Gsplit  = [[25,5,0],[5,10,1],[0,1,10]].
```
For each the first old A=25/c1=5 gives t1=1/5 and a1=1. Direct exact rational inversion of G1 shows second t2 has one denominator5. Its scaled y1 coordinate a21 differs:
- cyclic: a21 = −1/9, a unit mod5 -> Htot≅Z/25;
- split: a21 = 5/9, divisible5 -> Htot≅(Z/5)^2.
Independent exact rational Fraction inversion / direct Schur must certify both t2 and a21, not merely the solver. Their full determinants are 2240 (v5=1) and2225 (v5=2). The source-independent toys must verify all B_N congruences and determinant relations and reject treating same group order25 as the same group.

A hostile toy where second projection IS integral, e.g. G=[[5,1,0],[1,5,0],[0,0,1]] with first nonintegral h1 but L1 Gram determinant unit mod5 and second orthogonal h2=0, must NOT pass a wrongly universal two-order5 theorem.

## Prospective original-source experiments: choose n33 and n38, NO group-type predictions

1. Freeze source exact blobs `research/phase206/source_probe.py` `3f954b59d9f86b06ad53667c869b5b24f2e6c7f6`, `research/phase298/class_one_d163_composition.py` `e8cae60a662ca59cade8acd741c2d5d4f4982d6a`, `research/phase297/minimal_transverse_repair.py` `22b0077a2424553021a4c9859f92f0fe3efc2fe7`, and Phase299 original gluing core `research/phase299/gluing_core.py` `dba83c3fd8a07734f0bc2a7ec6724c0362fbdf9a`. Only root source/original helpers are authoritative; never substitute normalized Frobenius or Smith columns for ORIGINAL trace B.
2. Reconstruct ORIGINAL D163 full `G40` by original `source_probe.gram` and independent source raw monomial j0 E/B trace; verify ALL1,600 original Gram entries mod5^16 (reuse frozen Phase298-B implementation) with original Q109/J1. Confirm old, first, final Smith grades uncensored at16 and the earlier two 1,1 image debts for n=33,38. DO NOT adaptively select any other n post-result.
3. For both selected n, solve the unscaled first and second original projection equations and REQUIRE they FAIL; solve the scaled equations `A a1=5c1` and `G1 a2=5[c2;e]` with the frozen tracked original Smith solver and verify ALL original equations modulo5^16. Report a21 modulo5 and Htot exact group type WITHOUT prior prediction. If a21=0 or nonzero, preserve the result. Build k1,k2 as actual original monomial observation-row combinations, check all old–k1, all (old+y1)–k2, k1–k2 source trace pairings vanish modulo5^16 and norms match G_N.
4. Check direct integral gluing matrix B_N in original row order and `B_N^T G2 B_N=diag(A,m1,m2)` on ALL (n+2)^2 entries modulo5^16; compute direct Smith sums of original A, G1, G2 (max grades <16), plus v5(m1),v5(m2) (must be <16). Require v5(G2)=v5(A)+v5(m1)+v5(m2)−4. If any m_i censored at16, state that rather than changing precision.
5. **Independently enumerate exact order25 subgroup cosets** of N in L2 using original quotient relations: in the last two coordinates u,v mod N, map `i*y1+j*y2` to rational-N coordinate residues `((5*i+a21*j) mod25, j mod5)` for i,j in0..4; check 25 UNIQUE cosets; verify addition modulo the relations and group type. Test each generator's order and the discriminant **bilinear isotropy** by representing y1 and y2 in N⊗Q5 with numerators over25, checking the rational numerator pairings agree with the ORIGINAL Gram modulo5^16, and all H generator self/cross pairings are integral. Do not mistake bilinear isotropy for even-quadratic isotropy.
6. Unimodular source-gauge check on one toy: change old basis with a unit shear/swap, and y2 by y2+y1, retaining the SAME chain. Recompute group type and original/full determinant valuations, and check no scalar count changes; a21 may transform but zero/nonzero mod5 group classification cannot change.
7. Contrast original D587 bad-first chain from Phase298: add original bad s4 first to old odd362 (first h1), then original safe s0,s2 (second image index0), so it DOES NOT supply two nonintegral stages. Record as a **negative applicability control**, not an invented h2 obstruction. The D587 original first-stage gluing remains Phase299-B; do not expand the source based on post hoc row choices.

**Stop** if any source hash drifts, either n33/38 is not double-nonintegral, any source pairings fail, the group-presentation/coset count fails, determinant identity fails, original Gram changes, group type contradicts independent toy arithmetic, or a zero/censored source result is improperly promoted. Preserve failed CI and repair only verified implementation errors.

**Evidence:** [P-paper, classical] nonintegral two-stage primitive orthogonal gluing and finite quotient presentation; [M after passing CI] exact source arithmetic on two genuine h1-original D163 nested row chains and two hostile toy types; [H] multi-stage nontrivial extensions, robust functoriality and uniform h1 field discriminator/cutoff; [R] additive gluing groups by default, canonical discriminant-quotient map, or extra original Gram valuation from index25.

No Work mode, no merges, external source/math review #50/#51 remains required.
