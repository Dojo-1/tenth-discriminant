# E31 — THE GRAM DOES NOT OWE THE CONDUCTOR A FACTOR

*19 November 2026 · exact original-source negative control · draft until Lean CI.*

## The hypothesis we are deliberately attempting to kill

    If the conductor frame loses information modulo p,
    then p must divide the original integer trace-Gram determinant.

This unrestricted inference is false. An arithmetic ambient kernel is
not automatically a sampling-jet rank defect.

## The witness and exact original calculation

Take k=5, D=1 (source quadratic parameter D*k*k=25) and the original
integer sample support

    Q = {(0,0), (1,0)}.
    J=1, R=2, S=1.
    Original rows: 1 and Z.

Here ordinary derivatives hold the conjugate factor fixed. There is
only the j=0 channel, the original positive integer pairing retains
its required factor 2, and the entire original evaluation matrix is

    E = [[1,1],
         [0,1]].

All sampled source points have zero imaginary coordinate, so the
actual source trace pairing has B=2 I. Therefore

    G = E B E^T = [[4,2],
                   [2,2]]
    det(G)=4 > 0, and 5 does not divide det(G).

The index-five integral frame (x,y) -> (x,5y) maps Q to exactly Q.
E24's original-Gram transport theorem ensures the same matrix under
the correctly transported target D=1 presentation.

Meanwhile the local observer at modulus five sends both distinct
coefficient-pair residues (0,0) and (0,1) to (0,0):

    Frame_(5,5)(a,b)=(a,0) mod 5.

Consequently the local frame has a nontrivial kernel, but the actual
source original Gram determinant is 4, a unit modulo 5.

## Evidence and scope

- The exact two-by-two matrix was independently reproduced with an
  elementary integer arithmetic implementation, including matching
  D=25 and D=1 transported support calculations.
- E31 Lean source asserts the same matrix and determinant, the E24
  source-matched transport identity, a mod-5 kernel witness, and the
  failure of the unrestricted prime-divisibility implication.
- The proof is *not* certified by this note. Only exact-head Lean/root
  CI and allowed-axiom audit can promote the encoded theorem to P.
- This Q is deliberately tiny and does not satisfy the field theorem's
  large-ellipse and class-number hypotheses. The counterexample
  targets a proposed inference rule, not any proven field cutoff.
- No arbitrary resampling, auxiliary complex minor, p-adic valuation,
  changed derivative or reduced metric has been substituted.

## New requirement for any E32 determinant gain

To derive an actual p-power divisor of the original integer Gram,
the **original sampled jet image** must be shown to lie in a
certified p-divisible sublattice, or an equivalent original-source
unimodular row certificate must be supplied. An ambient conductor
kernel or a dimension count is insufficient. Measure the exact row
lattice, determinant and source reconstruction, then compare same
G under arithmetic and geometric bounds.

## Cross-research consequence

E29/E30 kernel towers and HK-032/HK-033 CRT reconstruction are
mathematically coherent. Their certificates cannot simply be
renamed original-Gram prime-mass savings.

**Policy:** Preserve the failed inference as [R]_arith (retired
shortcut); retain the constructive kernel/CRT lemmas as [P] only at
their respective exact successful heads.
