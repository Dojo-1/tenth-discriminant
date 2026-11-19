# Phase351 — ORIGINAL THIN-ELLIPSE ENDPOINT AUDIT BELOW 307

*19 November 2026 · exact integer finite endpoints / independent scalar arithmetic · research-only.*

## Source and reason for this audit

In the Phase350 formally green 307^4 research branch, Phase342
establishes a conservative cell-area sufficient criterion and
contains the exact regression:

    32593*306 < 10000000 <= 32593*307.

The current proof's 307 parameter is thus partly tied to that
particular rational sufficient certificate. Failure at 306 of
this condition does NOT imply that the actual original
ellipse count fails.

Phase342's actual original source is:
    D >= 1, R=floor(D/4), S=floor(R/25),
    fourthRoot(D)=D^(1/4),
    thinRadius(D)=ceil((11/25)*fourthRoot(D)^3),
    Qthin=ellipsePairs(D,thinRadius(D)),

where ellipsePairs(D,r) is the set of exact integer pairs
(x,y) with x²+D*y²<=r² (the bounding-box convention is redundant
for D>0 and never changes the set).

The interpolating rank requirement is:
    card(Qthin)>2*(R-1)+(S-1).

## Independent frozen bounded instrument

The script research/oracles/phase351_exact_original_ellipse.py
checks only D=b^4, b=298,...,307, with exact integer radius
ceil(11*b^3/25) and vertical-slice counts:

    N(D,r)=sum_{-floor(r/sqrt(D)) <= y <= floor(r/sqrt(D))}
               (2*floor(sqrt(r²-D*y²))+1).

It uses math.isqrt on integers. The script does not enumerate
billions of points, replace samples, sample an ellipse with floats,
or infer cardinality from an approximate area.

For each b, the script prints R,S, the exact Q count, requirement,
positive surplus, whether the conservative Phase342
cell criterion holds, and a SEPARATE 65-digit Decimal evaluation
of Phase348 joint normalized lower's numeric formula MINUS
Phase347 normalized upper's numeric formula, at this exact D,R.

Key exact finite results:

    b     Qthin count       required        surplus
    298   4,796,721,297      4,021,936,709  774,784,588
    299   4,861,396,747      4,076,194,785  785,201,962
    300   4,925,304,253      4,130,999,997  794,304,256
    301   4,992,989,319      4,186,356,009  806,633,310
    302   5,058,469,573      4,242,266,501  816,203,072
    303   5,127,114,655      4,298,735,161  828,379,494
    304   5,194,250,777      4,355,765,695  838,485,082
    305   5,263,750,119      4,413,361,815  850,388,304
    306   5,332,671,893      4,471,527,249  861,144,644
    307   5,402,763,825      4,530,265,737  872,498,088

At b=302 the scalar lower-minus-upper expression evaluates
about +0.001640248469; at b=301 about -0.001013114144.
This is numerical *evaluation of formulae*, NOT proof that
they bound the original Gram at D=302^4 or all larger D.

## The falsifiable theorem candidate

The key missing result is a UNIFORM certificate of the
ORIGINAL source interpolation count for every integer
D >= (302)^4, using the original ceil-defined
thinRadius D and exact integer Qthin, not a bespoke
ellipse or interpolating statistic.

Potential method: a piecewise-rational inner polygon/
integer slice lower bound with sufficient floor error
control, or a strengthened cell-area estimate that
does not spend the 306–307 constant gap. Must work
for arbitrary integer D, not just perfect fourth powers.

Then all other source-to-field seams must be revisited
INDEPENDENTLY at any proposed smaller floor:
- Phase347 stronger thin/padded contraction with ceils,
  positivity and count majorants;
- same-source complete original ordinary-Z positive trace
  Gram and unchanged normalized upper;
- Phase348 joint binary/odd same-Gram lower with its
  dimension, tail and prime budget guards;
- Phase343 strict scalar gap for all D >= new floor;
- original odd/even maximal order and field-discriminant
  identification; no unapproved field assumption.

## Kill criteria, promotion and priority

If a proposed uniform count proof fails for any D in
its claimed range, retire the new count certificate.
If source-aligned lower/upper fail at any D, the
field-bound improvement is killed even if the count
and scalar expressions appear favorable.

The 307^4 theorem remains the strongest separately
full-root checked *research* theorem, awaiting human
semantic review. This Phase351 branch contains no new
Lean field declaration; it does not weaken axioms or
rename a source parameter to claim a bound.

Bounded M: finite exact integer counts at b=298..307.
Bounded numerical diagnostic: scalar formula margins at
those points. H: any proposed uniform >=302 statement.
