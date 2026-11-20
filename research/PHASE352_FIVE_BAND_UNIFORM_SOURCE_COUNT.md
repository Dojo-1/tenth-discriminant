# Phase352 — FIVE BANDS INSIDE THE ORIGINAL INTEGER ELLIPSE

*19 November 2026 · uniform analytic proof proposal, separate exact test oracle.*

## Fixed object: nothing was resampled

In the unchanged Tenth Discriminant integer lattice, let D>0,
t = D^(1/4), r = ceil((11/25)*t^3) = Tuned.thinRadius D,
Q = ellipsePairs D r = {(x,y) in Z² : x²+D*y² <= r²}.
Let R=floor(D/4), S=floor(R/25).
The original strict interpolation criterion is

    card Q > 2*(R-1)+(S-1).

The previous Phase342 sufficient cell-area argument requires the
conservative inequality 32593*t >= 10000000, first assured
at fourth-root 307. This sufficient inequality is NOT an
equivalent condition for the original count.

## Rational inner-polygon witness

For i=1,..,5 set c_i=2i/25, and
beta_i=(43,40,36,30,18)_i /100.
All five exact integer checks hold:

    10000*(beta_i²+c_i²) <= 1936,

equivalently beta_i²+c_i² <= (11/25)², because
the integer values betaNumerator²+(8i)² are
(1913,1856,1872,1924,1924) <= 44²=1936.

Define vertical integer bounds Y_0=0,
Y_i=floor(c_i*t), and horizontal integer half-widths
X_i=floor(beta_i*t³). For each band
Y_(i-1) < |y| <= Y_i and |x| <= X_i:

    x² + D*y²
      <= (beta_i²+c_i²)*t^6
      <= (11/25)²*t^6
      <= r².

Therefore EVERY band consists of original integer Q points.
Bands are disjoint, and we safely omit the entire central
row y=0. The exact count has the following rigorous lower
expression:

    card Q >= 2 * Σ_i (Y_i-Y_(i-1))*(2 X_i+1).

For t>=274 all factors below are positive, and the elementary
floor bounds imply:

    Y_i-Y_(i-1) > (2/25)*t - 1,
    2 X_i + 1 > (2 beta_i)*t³ -1.

Since Σ_i beta_i=167/100:

    card Q >
       (334/625)*t⁴
       -(167/25)*t³
       -(4/5)*t+10.

Meanwhile, because R<=D/4 and S<=D/100,

    2*(R-1)+(S-1) <= (51/100)*t⁴ -3.

The difference between the displayed geometric lower bound
and the displayed interpolation upper is

    (61/2500)*t⁴ -(167/25)*t³ -(4/5)*t +13.

Multiply by 2500 and factor the leading terms:

    t³*(61*t-16700) -2000*t+32500.

For t>=274, 61*t-16700>=14 and
14*t³-2000*t+32500>0. Thus the lower count
strictly exceeds the unchanged original interpolation
requirement for EVERY D>=274^4.

This argument works for arbitrary integer D (and the real
fourth-root t), not merely D=b^4. It uses exact integer
regions and floor error margins. It is a SHORT PAPER
derivation here, **not yet a kernel-checked Lean proof**.
The missing formal step is a Mathlib Finset cardinality
lemma for these five disjoint original source subregions.

## Reproduction and evidence

research/oracles/phase352_five_band_source_geometry.py
uses ONLY exact integer comparisons of fourth powers.
It computes the original non-fourth-power ceiling radius
without floating roots and checks 110 deterministic inputs,
including near b^4 transitions and random D up to 600^4.
Every case must satisfy:

- all five outer band corners belong to the original ellipse,
- the exact five-band count exceeds the exact original
  interpolation requirement,
- the direct original source count exceeds the band count.

This is independent finite M evidence; it does not replace
the uniform paper argument or provide independent human review.

## Crucial semantic and theorem boundaries

This is a new sufficient ORIGINAL-SOURCE count certificate,
not a new geometric substrate, non-Euclidean solver,
prime-power valuation, actual class-number-one field theorem
or change in the existing trace Gram.

To improve the 307^4 endpoint, we also need all uniform
307-domain arguments reproved at a smaller floor:
- the original thin-radius 17/20 contraction and padded
  cardinality majorant (without source substitution),
- exact positivity of the original same-Q ordinary-Z Gram,
- source-locked arithmetic lower and Hadamard upper,
- the scalar strict gap for all D in the new domain,
- odd/even maximal-order field/discriminant transport,
- independent semantic review of every assumption.

If any of these fails, there is no field-bound improvement
even though this standalone count claim survives.

## Precise Lean next-step

Introduce and prove (at the ACTUAL source definition):

    theorem five_band_original_ellipse_interpolation
      (D : Nat) (hD : 274^4 <= D) :
      2*(R D-1)+(S D-1)
        < (ellipsePairs D (thinRadius D)).card

under the real-fourth-root definition already used in
Phase342. First isolate a general cardinality lower
lemma for five disjoint integer band rectangles. Audit
both strict inequalities and all ceil/floor transports.

**Evidence label:** H for the uniform proof pending Lean
and outside source semantic review; M for the bounded
110-case exact arithmetic oracle. Earlier 307 root theorem
remains P relative to encoding, not externally reviewed.
