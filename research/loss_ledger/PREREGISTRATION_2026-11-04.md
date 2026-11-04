# Round 201 preregistration — valuation loss ledger and filtered Gram transport

**Date:** 2026-11-04 (Europe/Madrid). **Status:** PRE-REGISTERED, BEFORE exact Round 201 pilots. **Research branch:** research/round201-blueprint-loss-ledger, based on research/plural-moving-frame-prereg-20261104 at commit 8e3cb4cc779dbab89215d0d09289d82e3e18804b. **Provenance:** the user's guiding question is whether to seek a common foundation or a typed structure recording information lost between arithmetic and geometry. The specific experiment, definitions and tests in this document are an AI-assisted mathematical proposal. The uploaded paper is Oliver Lorscheid, *A unifying approach to tropicalization*, arXiv:1508.07949v4 (2 June 2022), PDF supplied by the user. No originality or external endorsement claimed.

## Decision

Prioritize a *faithful ledger of information loss under declared, typed maps*, while studying ordered blueprints as a possible common categorical language—not as a proven universal base for the real Gram and every p-adic sector. A base language alone does not make inadmissible transports valid. The mathematical test is whether the ledger yields an obstruction that scalar determinants and the existing fixed-prime row bounds cannot already detect.

## Frozen production baseline; continue independently

The production control is the **same original** integer ordinary-Z-jet trace Gram
G_D = integerRectangularTraceGram (ellipsePairs D (Tuned.thinRadius D)) D (Tuned.S D) (Tuned.R D) (Tuned.S D),
R=floor(D/4), S=floor(R/25), J=S, with W held fixed before the Z-derivatives and trace pairing B_D((a,b),(c,d))=2(ac+Dbd). The comparisonScale is exactly R^2*S. No new primes, surrogate Gram, replacement derivatives, support changes or swapped field charts.

The focused and whole-root 322^4 original field theorem compiled. On the exact PR #126 head cbc185af2220faac3154a89e06db8d2792f2a9bf, **22/22** GitHub checks succeeded (whole-root Lean proof checks run 41787273051 included complete project build, environment axiom audit and negative controls). PR #126 is still draft/unmerged at this preregistration; main at dc7e19eb still integrates 323^4. Independent mathematical semantic reconstruction in issue #50 remains open and is not resolved by CI. The exploratory research is NOT included in that production PR.

Prior preregistration: research/plural_moving_frames/PREREGISTRATION_2026-11-04.md at commit 59933f9c (before T1–T4) and Issue #127; exact pilots and derived tau_k bounds are inherited *evidence*, not predictions of this round.

## Literature boundary and precise interpretation

Lorscheid's ordered blueprints (Part 1, Definition 2.1 / section 2) have a monoid with zero plus a compatible subaddition relation. Section 7, especially Theorems 7.5 and 7.15, presents scheme-theoretic tropicalization as an extension-of-valuation moduli problem with base change and, under its hypotheses, bend relations. Section 12 recovers Maclagan–Rincón weights in a specified tropical scheme setting. These claims belong to that theory. Our integer Gram is not asserted to be an ordered-blue-scheme tropicalization, a new F_1 scheme or a realizable valuated matroid *as a whole family* without an explicit carrier and valuation map.

Known mathematical comparisons, not new: Smith normal form, determinantal/Fitting ideals, p-adic valuations, modular rank, tropical determinant inequality, Grassmann–Pluecker/valuated matroids. A fixed k-row submatrix of a rank-n Gram gives realizable Pluecker valuations across column subsets, but the collection of all rectangular minors for all row subsets is *not automatically one valuated matroid*. Full real spectra are not intrinsic under arbitrary GL_n(R) congruences.

## Declared objects and what each map forgets

Fix n>=1, prime p, G in Sym_n(Z) with G positive definite over R, so det G>0.

- E_p(G) = matrix (v_p(G_ij)) in (N union {infinity})^{n x n}, with v_p(0)=infinity. This remembers no unit residues/cancellation.
- t_p(G) = min_{sigma in S_n} sum_i v_p(G_i,sigma(i)) (tropical determinant from entry valuations).
- c_p(G)= v_p(det G)-t_p(G)>=0, a *coordinate-dependent cancellation defect*, not a frame-invariant metric. Values finite for SPD G.
- D_p(G) = (v_p(Delta_k(G)))_{1<=k<=n}, Delta_k = gcd of all k-minors, Delta_0=1. Delta_k>0 when G is nonsingular.
- M_p(G) = (rank_{F_p}(G mod p), its column matroid with labeled coordinates). Only the **rank** is invariant under arbitrary integral unimodular left/right frames; labeled matroid can change.
- K_{p,m}(G)=ker(G mod p^m : (Z/p^m)^n -> (Z/p^m)^n), h_{p,m}=log_p |K_{p,m}|. Counts and isomorphism class of cokernel are unimodular invariants; inclusions and reductions between different m must be explicitly typed.
- A geometric profile comprises the positive-real Gram form and, when comparing two *same-row* positive Grams, their generalized eigenvalues under simultaneous congruence. Real spectral shape alone is not invariant under arbitrary real frames.

For Smith data U G V = diag(d_1,...,d_n) with unimodular integer U,V and d_i|d_{i+1}, put a_i=v_p(d_i) in nondecreasing order.

**P (classical mathematical fact, not new Lean declaration):**
    v_p(Delta_k(G)) = sum_{i<=k} a_i.
    h_{p,m}(G) = sum_i min(a_i,m).
    h_{p,m}-h_{p,m-1} = #{i : a_i >= m}, m>=1, with h_{p,0}=0.
Thus the whole kernel-growth tower and the determinantal-divisor profile encode equivalent p-primary Smith information for nonsingular integral G. Rank modulo p records only #{i:a_i=0}; v_p(det G) records only sum_i a_i.

**P (elementary tropical inequality):** v_p(det G)>=t_p(G), with potential strict inequality from cancellation. The defect is presentation-dependent; it is NOT automatically a valuation of a determinant polynomial tropicalization in the full ordered-blueprint/bend sense.

**Loss ledger, no false scalarization:** for a declared projection P and declared admissible gauge equivalence ~, consider its fiber F_P(q) = {[H]_(~): P(H)=q}; the projection is lossy on a domain precisely when some fiber has at least two distinct classes. The actual equivalence relation must be stated: for integer-structure claims use integral unimodular equivalence, not GL_n(R) congruence. Do not define a universal "loss entropy" without a finite model.

## Predicted exact finite tests (frozen BEFORE execution)

**T0 (cancellation defect counterworld):** p=3,
    A=[[1,1],[1,4]] and B=[[1,1],[1,10]].
Both are SPD, every entry has 3-valuation zero, t_3(A)=t_3(B)=0, but det A=3 and det B=9; therefore c_3(A)=1, c_3(B)=2. Entrywise tropical data alone does not determine determinant valuation. These matrices have no claimed quadratic-source provenance.

**T1 (rank+det insufficiency):** p=3,
    C=diag(1,3,27), E=diag(1,9,9).
Both SPD, both det=81=3^4, both mod-3 rank 1. But Delta_2(C)=3 and Delta_2(E)=9, so (a_i)=(0,1,3) vs (0,2,2). Kernel growth h_{3,1}=(2,2), h_{3,2}=(3,4), h_{3,3}=(4,4). This separates distinct fibers under the coarse invariant (det, modular rank).

**T2 (frame-counterworld):** integral unimodular U=[[1,-1],[0,1]] sends A above by congruence to [[3,-3],[-3,4]], preserving det=3, Smith determinantal divisors and all h_{3,m}, while reducing the naive cancellation defect from 1 to 0. Hence c_p is not intrinsic and must be tracked with its presentation/frame.

**T3 (same-original-source regression):** import the existing *unmodified* test gram from research/plural_moving_frames/original_source_small_pilot.py for D=19, R=4,S=J=3,p=3, rho=5 or 6. Check mod-3 ranks through exact finite-field Gaussian elimination. For rho=5, existing v3(Delta_10)=0 implies rank=10; for rho=6, v3(Delta_10)>0 implies rank<=9. Both must satisfy original pointwise-row upper bound rank <= R+p*(S-1)=10. Real positive definiteness must coexist with this modular rank deficit. No uniform D>=322^4 inference.

**T4 (representation gate, not automatically a successful implementation):** explicitly exhibit the determinant/minor polynomial relation in a named ring with generators. Compare two coordinate presentations: entries only versus entries plus minor symbols and defining relations. If a proposed ordered-blueprint map or bend recovers v_p(det), identify its actual valuation extension, chosen monoid and subaddition; merely adding det as a generator and reading its value is tautological, not discovery. Do not claim to have implemented Lorscheid's full scheme theory with a small Python script.

## Hypotheses, counterhypotheses and falsification

H0: an explicit typed *forgetful/recovery tower* E_p -> (rank, incidence) plus D_p/K_{p,m} and geometric reference correctly diagnoses which data are lost without assigning an arbitrary scalar. T0–T3 and an exact proof of the SNF formula are minimum acceptance; observed failure or gauge mix-up retires the current proposed maps.

H1: a SOURCE-EXACT filtered inequality for the original thin Gram (e.g. lower bounds on v_p(Delta_k) from the existing integral row factorization paired with genuinely frame-controlled geometric upper constraints) yields an exclusion not obtained from the current scalar determinant envelope. Accept only if a strict new numerical threshold is certified on the original Q, ordinary jets and field chart; otherwise mark **unproved or empirically unhelpful**, not a new number-field theorem.

H2: a concrete blueprint/bend construction retains a relation essential to the exact determinant/Pluecker valuations that an entrywise tropical projection loses. Accept only with named carrier, valuation and commutative diagram, plus an adverse example; if it just records additional coordinates by fiat, report no substantive reconstruction advantage.

Counterhypothesis: all useful constraints already reduce to determinantal ideals/Smith/cokernel computations and no novel geometric obstruction is obtained; the F_1/blueprint language is conceptually clarifying but technically redundant here. Retain that negative conclusion if tests support it.

## Separation of evidence and workstreams

- P = classical proved deduction with stated hypotheses or compiled Lean theorem in its own scope; M = exact bounded finite pilot; H = open hypothesis; S = conceptual analogy; R = refuted shortcut. Do not silently promote.
- Source discrepancies R_sem; lack of typed congruence/valuation map R_transport; uncompiled theorem R_formal; missing strict discriminant gain R_emp.
- Preregister T0–T4 before creating their scripts or running CI. Keep tests / results in subsequent commits to retain temporal separation.
- Continue original PR #126 integration and independent #50 semantic review as a separate workstream. Do not merge #126 merely because its 22 GitHub checks passed unless source semantics are independently assessed.
- Stop Round 201's claim to improved field bound after finite counterworlds and one attempted same-source minor inequality if every gain is a frame artifact, a re-encoding of the scalar determinant, or an inadmissible map.

## Independent follow-up obligations

For a meaningful external maths review: reconstruct why ordinary Z derivatives with W fixed yield an integral row factorization; check inertness/class-number-one assumptions in the maximal order; check binary and odd-prime aggregation once; confirm real positive-definiteness of the exact original Gram; and separately check K (totally complex quadratic number field) to abs-discriminant return. Ordered blueprints do not absolve those obligations.

User learning target: explain, without relying on AI formulas, why equal determinant and equal rank mod p still permit distinct p-power kernel growth.
