# From class lattices to a bound on the number of primes

**Checked locally in Lean:** the class counts now yield an actual prime
prefix bound. Assume actual class number h<=2 in the squarefree odd
chart. Let P be any finite set of primes p<=t with p!=2, p not dividing D
and -D square modulo p. Then

    card(P) <= (h/4)*(2*pi*t/sqrt(D)+4*sqrt(M(K)*t/D)+1)
            <= pi*t/sqrt(D)+2*sqrt(M(K)*t/D)+1/2.

Here t is natural and M(K) is the existing explicit Minkowski bound for
the actual field. Taking P to be all such primes up to t gives a count
function. There is no numerical certificate, supplied class count or
representation count in the theorem's hypotheses.

The proof joins the earlier pieces on the SAME ideal family. Select four
distinct labelled points for each prime. Their union U has card(U)=4*card(P).
For each class C, retain only points with that label and turn their values
into an actual finite subset of J_C. Projection is injective on this
fixed-class slice, and embedding into the ideal subtype preserves card.

Each slice consists of prime-normalized elements of norm magnitude at
most N(J_C)*t. Apply its checked full prime-point count. The class slices
partition U, so their cards sum to card(U). Writing A for the common area
term and B for the common boundary term gives

    4*card(P) <= h*(A+B)+2*(h-1).

The principal class contributes no axis points; every other class costs
at most two. For h<=2, 2*(h-1)<=h. Divide by four to obtain the displayed
bound. The earlier scalar accounting is now instantiated with actual
class-group slices, actual ideal elements and actual prime representatives.

Labels are essential. Two points with equal field value in different
classes are distinct labelled points. A control shows that forgetting
labels can change card2 to card1. Empty and absent slices, and the failure
of the axis-constant inequality at h=3, are also checked.

This is a COUNT bound. The next step is to carry it through the log(p)/p
weight and verify coverage of the excluded primes in the original Gram
argument, including the separate divisor budget. Field-parameter and
even-chart transport and a new discriminant cutoff remain open.

The failed first proof assembly and passing second run are preserved.
[Verification](PHASE81_VERIFICATION.md). The source is standalone and
outside production CI; the earlier integrated common-family checks remain
unchanged. No classification, novelty or independent human review is claimed.

Current update (Phase82): this exact source has now been integrated with
only its first import changed. Complete excluded-prime coverage and the
finite weighted budget are checked on the original Gram. The paragraph
above records the Phase81 checkpoint. A closed kernel estimate and new
cutoff remain open. [Current human guide](WEIGHTED_SPLIT_GUIDE.md).
