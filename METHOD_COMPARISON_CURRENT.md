# A source-aware comparison, 26 October 2026

**A smaller cutoff and a lighter hypothesis are different achievements.**
This selected comparison distinguishes our checked result from external
source claims. It is not an exhaustive ranking or an independent replay
of another repository.

## Source freshness update — 30 October 2026

The checked direct h=1 bound in this repository is now **actual |discriminant| < 47.1 billion** ([merged PR #48](https://github.com/Dojo-1/tenth-discriminant/pull/48), [exact-head full CI](https://github.com/Dojo-1/tenth-discriminant/actions/runs/41087748526)); the 50-billion row below is the **26 October historical snapshot**, not the current publication. [PR #49](https://github.com/Dojo-1/tenth-discriminant/pull/49) proposes, but has **not yet proved**, 47.0 billion on the same integer Gram. The independent-reader review is [issue #50](https://github.com/Dojo-1/tenth-discriminant/issues/50).

Tao's [public challenge discussion](https://terrytao.wordpress.com/2026/10/20/an-experimental-ai-math-challenge-using-tenth-discriminant-bounds-to-explore-arguments-ruling-out-siegel-zeroes/comment-page-1/) now includes participant-reported cutoffs such as 570, 565 and 331, and a separately reported 7/8 zero-free-region-based Lean route. These are **participant reports**, not results independently replayed in this work. A fair comparison must align the meaning of D or q, external theorems, original determinant versus selected minors, finite completion, independent human review, and exactly which artifacts were kernel-checked. We should not treat the numerical ranking as proof-method ranking.

### 30 October primary-source comparison: why the determinant definition matters

Two additional **source-reported** developments change the mathematical
comparison, without independently verifying any external proof here.

- [DrMurphyIsIn's determinant route](https://github.com/DrMurphyIsIn/tenth-discriminant/blob/main/determinant/README.md) reports a **kernel-checked class-number-one classification** and a direct cutoff q<2^15, using the auxiliary inert-prime nonvanishing argument and the norm of a selected maximal derivative minor. It reports two-kernel (Lean/nanoda) checking and matched tampered controls; this review has NOT replayed them. Its closure reportedly excludes L-functions, though Mathlib measure/integral machinery remains. That is a genuinely relevant comparator to our **positive trace Gram of all original observations**, but they are different integer objects. A separate 7/8 zero-free-region route in that repository reports q<=652.
- [DualverseAI/rStation's 331 draft](https://github.com/dualverse-ai/tenth_discriminant/blob/main/README.md) reports **D<=331** by tightening the exact degree and vanishing-order information in a determinant rank proof, with supporting code and a polished working draft; this is a source report, not a replay or Lean certificate established here. Its separate small-prime completion returns the familiar D<=163. Keep the analytic cutoff distinct from the finite endgame.

A precise possible interface, rather than a numerical transplant: their selected
maximal-minor nonvanishing modulo an auxiliary inert prime implies full row
rank over that residue field; on the **same actual observation matrix** this
would imply characteristic-zero row independence and positivity of our
positive trace Gram. But it does **not** by itself preserve the original
lattice-point set or make the rank guard cheaper. Conversely the original
Gram has a weighted Cauchy–Binet decomposition as a sum of squares of
maximal minors; importing a bound for one chosen minor is NOT automatically
an upper bound for their sum. The former is a potential typed bridge, the
latter a necessary obstruction. A source-checked, same-parameters comparison
of ranks, radii and row counts is a future experiment [H], not an achieved
sharper theorem.

**Present task order:** finish [Phase133 PR #49](https://github.com/Dojo-1/tenth-discriminant/pull/49)
without moving the Gram, invite the bounded [independent arithmetic/geometry
review #50](https://github.com/Dojo-1/tenth-discriminant/issues/50),
and only then consider an auxiliary-prime port as a newly registered method.
Our 47.1-billion bound is kernel-checked on its own exact head, not claimed
competitive in raw constant. The other works' authors report stronger
bounds and verification; no independent reproduction here.

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

## 30 October: exact-rank comparison, a transport with remainder

The [Chung/Dualverse 331 working draft](https://github.com/dualverse-ai/tenth_discriminant/blob/main/bound-331/latex/intro.tex)
reports that retaining *individual degree and vanishing-order estimates* in the
auxiliary-prime rank proof improves its earlier cutoff 498 to **331**.
[Its exact rank criterion](https://github.com/dualverse-ai/tenth_discriminant/blob/main/bound-331/latex/rank.tex)
tracks the layerwise coefficient degrees D_m, the degree bound B_e and
the vanishing multiplicities mu_e; the proof reduces a polynomial
relation modulo an **auxiliary inert prime**, then compares the total
multiplicity of a nonzero one-variable polynomial with its degree.
The reported parameter improvement includes triangular exponent shape
K=17. [Its determinant comparison](https://github.com/dualverse-ai/tenth_discriminant/blob/main/bound-331/latex/comparison.tex)
uses a chosen nonzero maximal minor, nodewise derivative column blocks,
and Meixner/Schur-type singular-value bounds. We inspected these *source
descriptions*, **not** the full proof, code execution, or referee record.

Our method has the original **rectangular** exponent grid and a full
positive trace Gram G=E B E^T. There is one mathematically honest shared
interface: IF their mod-p nonzero minor were proved for our **very same E,
same original sample points, same ordinary derivatives and same prime**,
then full row rank mod p would imply characteristic-zero row independence,
and positivity of our real G would follow. But their *parameters and E
are not presently the same*, so the implication is only a conditional
typed interface, not a usable imported proof. A nonzero selected minor
also does not give an upper bound on the **sum of squared minors**
in Cauchy–Binet: the full Gram determinant has extra terms. Nor does
reducing the node count preserve the old integer G; if a future
experiment chooses a new node set Q, it must reconstruct BOTH
arithmetic p-adic divisibility and geometric positivity/upper estimates
for that explicitly new integer.

**Falsifiable next experiment [H]:** fix an identical observation type
(E,Q,J,R,S) and compare the original point-count positivity certificate
against an auxiliary-prime nonzero-minor witness. Require an exact map of
sample/derivative indices and the full mod-p rank implication, then
measure how much (if any) smaller a valid sample set becomes without losing
the other proof obligations. Kill the candidate if the sample types cannot
be matched, the necessary auxiliary prime is unavailable, or any new
cutoff relies on bounding a sum of minors by one chosen minor.
This is more consequential than merely ranking numerical constants, but
currently supplies **no stronger theorem**.

