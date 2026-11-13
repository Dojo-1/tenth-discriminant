# Phase311-C — post-B, pre-code inert residue-multiplicity compression

2026-11-13. The Phase311-A and B hosted experiments have already passed. This follow-up is preregistered **after** their evidence and **before** its own implementation. It has a deliberately narrow scope: the ORIGINAL, UNNORMALIZED ordinary-jet evaluation and original trace Gram mod5, not the primitive matrix after /5.

## Theorem target [P-paper]

Let p5 be inert, k=O_K/5=F25, and Q be a finite conjugation-invariant multiset of actual maximal-order observations. For each residue class z∈k define its **integer multiplicity** m_z = #{q∈Q: q mod5=z}, and reduce m_z mod5.

For integer-coefficient original monomial rows Z^r W^s and ordinary Z-derivatives j=0..J-1, evaluation mod5 depends ONLY on z=q mod5. Let C be the original evaluation on ONE representative of each residue z occurring in Q, repeated separately for the original jet labels; and let W diagonal contain the corresponding m_z mod5 in each jet.

Then the ORIGINAL Gram over F5 has EXACT compression

    G(original Q) mod5 = Tr_{k/F5}( C W conjugate(C)^T).

In particular, for 25 actually observed classes, if t is the number with m_z nonzero mod5, and J_eff=min(J,5) since ordinary derivatives of order≥5 vanish mod5, then

    rank_F5(G mod5) <= t * J_eff.

The original evaluation rank over F25 is computed using the classes with m_z>0 as integers (not those nonzero mod5); a source kernel and extra trace-image radical may both be present. This rank bound and the exact equality are unrelated to the full primitive 5-adic source until a separate integral lift map is supplied.

## Frozen controls

- D163 h1, D187 non-h1: same matched rho21/R40/S=J1/actual maximal-order norm ball, original Gram rank25 each, field E rank25; multiplicity compression must match all original Gram cells.
- D203 non-h1: native rho24/R50/S=J2/Q263, original Gram rank38 and E rank50, all 100x100 Gram cells matched to the frozen original Phase304 oracle.
- **New non-h1 larger parameter control:** D427=7*61 (squarefree, 3 mod4, p5 inert), native rho/R/S/J from the original Phase206 parameter formula (expected R106,S=J4), and ALL maximal-order norm-ball observations at that rho. Since 7 ramifies and cannot be represented by a principal norm< m107, D427 is not h1. Do not claim source h1 from any local computation. The original polynomial labels/ordinary-jet policy are unchanged, but the full maximal-order lift is explicitly identified; it is not the original even-suborder lattice. Predeclare no numerical Gram-rank outcome for D427.
- Independently check for D427 the first 10 source rows and first 10 columns of the exact uncompressed original j0..j3 trace Gram (from actual q) against compressed entries. For D203 check ALL rows against its original frozen source Gram.
- Verify every count m_z and its conjugate partner agree, all 25 F25 residue bins exist if claimed, and rank_G <= t*J_eff.
- Negative controls: five duplicate copies of one actual observation (a synthetic MULTISET not a new original source) leave mod5 Gram invariant but have different integral support, and a source row with an ordinary derivative of order ≥5 vanishes mod5. Reject treating these as an unchanged original source or as a primitive quotient statement.
- Do not use this compression to infer exact v5, new h1 field bound, nor add tJ rank deficiency to valuationWeight.

## Stop / kill

Any mismatched original Gram entry, source policy deviation, non-conjugation-closed set accepted as if original full Q, or incorrectly identified primitive projection retires the result. Benchmark speed only if independently measured with equivalent work; do not assert performance gain from compressed dimensions alone. Keep DRAFT, no main merge.
