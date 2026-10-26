# Why Ender's chosen radius has enough lattice points

**Status:** complete elementary mathematical proof of the geometric count;
Phase 18 also checks the cell-area inequality and chosen-radius count in
[`EllipseCellArea.lean`](../../lean/TenthDiscriminant/EllipseCellArea.lean).
This note concerns only point
counting, not determinant divisibility, the analytic contradiction, or class
numbers. It keeps the original Ender parameters and certificates unchanged.
The older horizontal-slice proof is in `review/PHASE2_GPT-6.1-Sol.md:172-186`;
the cell argument below is a shorter independent derivation of the same lower
bound and the chosen-radius guard.

## 1. A lattice-cell lemma with all boundary cases

For an integer `D >= 1` and real `rho >= 0`, set `s = sqrt(D)` and

    E(D,rho) = {(x,y) in Z² : x² + D*y² <= rho²},   n = |E(D,rho)|.

Write `delta = (1+s)/2`. For every `rho >= delta`,

    n*s >= pi*(rho-delta)².                                      (1)

For `rho < delta`, the corresponding lower bound with
`max(rho-delta,0)²` is the trivial `n*s >= 0`.

**Proof.** For each pair `(x,y)`, center a half-open rectangle of width `1`
and height `s` at `(x,sy)`:

    [x-1/2,x+1/2) × [s(y-1/2),s(y+1/2)).

These rectangles partition the plane, have disjoint interiors, and each has
area `s`. Every point in one is at distance at most
`sqrt(1+s²)/2 <= (1+s)/2 = delta` from its center. If a point lies in the
closed disk of radius `rho-delta`, the center of its rectangle has norm at
most `rho` by the triangle inequality; hence that center belongs to
`E(D,rho)`. Therefore the disk is covered by the `n` rectangles associated
with `E(D,rho)`. Comparing areas gives (1). The disk boundary and half-open
cell ties do not affect area. A center with norm exactly `rho` is retained
because the ellipse inequality is non-strict. This also retains negative
coordinates and the origin. ∎

The lemma proves Ender's inherited all-radius lower estimate:

    n >= pi*rho²/s - 2*rho/s - 6*rho.                         (2)

For `rho >= delta`, expand (1). Since `s >= 1` and `pi < 4`,

    pi*(1+1/s) < 4+4/s <= 6+2/s.

Dropping the nonnegative `pi*delta²/s` term gives (2). For
`0 <= rho < delta <= s`, the right side of (2) is at most
`rho*(pi-6-2/s) <= 0`, so (2) follows from `n >= 0`; at `rho=0`, the
origin in fact gives `n=1`. No integral approximation or unproved
monotonicity in `D` is used.

## 2. Ender's radius clears the rank count directly

Let `R,S` be natural numbers with `q = 3R+S > 0`. Suppose `rho` is an
integer satisfying Ender's chosen-radius lower condition

    rho >= 1.001*sqrt(q*sqrt(D)/pi) + 10*sqrt(D).             (3)

Put `beta = sqrt(q*s/pi)`, which is positive. Because `s >= 1`,
`delta <= s`. From (3),

    rho-delta >= 1.001*beta + 9*s > beta.

Using (1) and `s > 0`,

    n*s >= pi*(rho-delta)² > pi*beta² = q*s,

so **`n(D,rho) > 3R+S`**. This avoids the `D >= 10^36` error-budget
calculation for the count alone. It does *not* remove that threshold from
Ender's separate determinant upper/lower comparison.

For a finite certified interval `[D1,D2]`, `tools/ender.py:58-63,72-86`
selects one integer radius at `D2` and checks that it lies above (3) with
`D=D2`. For every integer `D1 <= D <= D2`,

    E(D2,rho) subseteq E(D,rho)

because `y² >= 0`. Thus `n(D,rho) >= n(D2,rho) > 3R+S` with the same
`R,S,rho`. The inclusion and its cardinality consequence are checked in
`LatticeEllipse.lean`. Phase 17 also checks in Lean that (1) and the exact
radius guard imply the strict endpoint count and actual-Gram positivity;
Phase 18 checks the cell-covering proof of (1) in `EllipseCellArea.lean`.
For the
universal part, Ender defines the exact
ceiling of the right side of (3) at each integer `D >= 10^36`, so (3)
holds by construction.

This is stronger than the count required by the existing Lean interpolation
theorem: when `R,S >= 1`, `3R+S > 2*(R-1)+(S-1)`. At `J=S`, the new
`ellipseTraceGram_det_bounds_of_ender_guard` transports an *established*
upper-endpoint count to positivity and Hadamard for the actual trace-Gram
matrix. Phase 18's `ellipseTraceGram_det_bounds_of_ender_radius` now supplies
that count from the radius guard, without an area or point-count premise.

## 3. What this does not close

The historical finite Arb certificates and all-D determinant envelopes were
not rerun or strengthened here. A passing `radius_for` comparison validates
its returned integer relative to an Arb enclosure; the derivation above
explains why that lower condition suffices mathematically. Lean now checks
the disk-area proof using **closed** cells and finite-union subadditivity;
boundary overlap does not affect the upper bound. Phase 17 checks the formal
connection from real inequality (3), assuming (1), to `ellipsePairs`
cardinality; Phase 18 supplies (1), so its public count theorem has no
area premise. The same Gram matrix is identified with an integer matrix, and
Phase 16 derives its strict-small-prime valuation from class number one
in the squarefree `D≡3 (mod 4)` chart. The analytic comparison,
certificate interpretation and final classification still need their
own end-to-end audit. No full classification follows from this note.
