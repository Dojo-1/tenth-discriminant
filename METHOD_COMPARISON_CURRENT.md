# A source-aware comparison, 26 October 2026

**A smaller cutoff and a lighter hypothesis are different achievements.**
This selected comparison distinguishes our checked result from external
source claims. It is not an exhaustive ranking or an independent replay
of another repository.

| Route | Cutoff / scope | Load-bearing input | Evidence inspected here |
|---|---|---|---|
| Our determinant route | Actual field discriminant <50 billion for h=1 | Original Gram, nonsquare-prime divisibility, elementary factorial/tail estimates | Merged cutoff; integrated bridge at b4cff27 passes pinned CI40403267176, including final controls. No QRH input. |
| Murphy: Chowla–Selberg at7/8 | Reports d<=652 for h=1 | Fixed zero-free region for Dirichlet L-functions | Author reports checked closure including the zero-free theorem; we have not replayed it. |
| Murphy: sum over ideal classes | Reports d<=4777 for h<=2 and a finite completion | Same zero-free input, class partition and explicit analytic estimates | Pinned HCN.Main statements/proof terms and documentation inspected; no checker replay here. |
| Murphy: determinant bands plus analytic closure | Reports d<565 | Arb bands[565,652] and the QRH-based theorem above652 | Reproduction instructions inspected; neither band code nor proof rerun here. This is a hybrid closure. |

External sources are frozen at
[`DrMurphyIsIn/tenth-discriminant@f0995bf`](https://github.com/DrMurphyIsIn/tenth-discriminant/tree/f0995bf604056a98f0af0d182ed152c6bd996419):
[HCN explanation](https://github.com/DrMurphyIsIn/tenth-discriminant/blob/f0995bf604056a98f0af0d182ed152c6bd996419/hcn/README.md),
[formalization and pins](https://github.com/DrMurphyIsIn/tenth-discriminant/blob/f0995bf604056a98f0af0d182ed152c6bd996419/hcn/formalization/README.md),
[actual statements](https://github.com/DrMurphyIsIn/tenth-discriminant/blob/f0995bf604056a98f0af0d182ed152c6bd996419/hcn/formalization/HCN/Main.lean),
and [hybrid reproduction scope](https://github.com/DrMurphyIsIn/tenth-discriminant/blob/f0995bf604056a98f0af0d182ed152c6bd996419/comparison/REPRODUCE.md).
Their documented pins are Lean4.34.1/Mathlibd13f23b7/openai-mathadc7f124;
ours remain Lean4.19.0/Mathlibc44e0c8. These are not drop-in imports.

## A useful bridge, with a guard to preserve

The external class partition uses ideal representatives with Hermite bases,
not a completed reduced-form library. Its documented leading coefficient
bound is a<=(2/3)sqrt(d). Our proposed reduced-form counting argument uses
a<=sqrt(d/3). The first bound is larger; copying the former dictionary
into the latter estimate without changing its error coefficient would
be invalid. [Inspected class-partition source](https://github.com/DrMurphyIsIn/tenth-discriminant/blob/f0995bf604056a98f0af0d182ed152c6bd996419/hcn/formalization/HCN/Statements/ClassPartition.lean).

The external analytic proof also retains a nonprincipal zero-row term.
That is related mathematical context, not the same inequality as our
[checked axis accounting](research/ender_radius_bridge/TWO_CLASS_AXIS_GUIDE.md).
It was inspected after that local proof; no priority claim is made.

Our old [prior-art note](PRIOR_ART.md) is a21October snapshot. Its absence
claims must not be read as current. The broader comparison objective stays
partial: source inspection and author-reported checks do not constitute
independent semantic or build verification. Tao's [challenge](https://terrytao.wordpress.com/2026/10/20/an-experimental-ai-math-challenge-using-tenth-discriminant-bounds-to-explore-arguments-ruling-out-siegel-zeroes/)
welcomes different approaches, including numerically weaker bounds.

## 28 October source refresh

The accessible [twinheterodox v0.7.0 release](https://github.com/twinheterodox/tenth-discriminant/releases/tag/v0.7.0)
states q<570. The suggested q<480 remains unverified; latest-release
metadata was unavailable. No competing proof/code is imported here.
[Public-comment provenance and scope](research/ender_radius_bridge/SOURCE_REFRESH_20261028.md).

Our higher-class-number additions are separate: arbitrary odd fields with
h<=2 have actual discriminant<2^50; the integrated canonical even-chart
bound is actual discriminant<2^52. Arbitrary even-field transport remains
open. These do not improve the separate h=1 bound of50billion. The user
requests coordinate and literal-shift compatibility proofs before drawing
new conclusions from transformed frames; no determinant invariance or
cutoff gain is assumed. Original frozen source comparisons above retain
their dates and evidence scope.
