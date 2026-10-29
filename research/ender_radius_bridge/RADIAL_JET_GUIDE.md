# Why recentering could improve the cutoff

**Status: the complete Phase118 ordinary-jet estimate is Lean-checked standalone.**
The integral operator is already published in [PR41](PR41_MERGE_RECEIPT.md).
The checked cutoff remains50 billion;48 billion remains the fixed candidate.

The invariant is an integer determinant. We can change the polynomial rows
by an integer matrix of determinant1 without changing that determinant or
its prime divisors. This gives freedom to choose observations that are
easier to bound on the same geometric region.

The new observations replace paired powers of Z and W by powers of ZW-a.
After W is set to conjugate Z, ZW is the squared distance from the origin.
Choosing a near half the squared radius centers this radial quantity.
On the whole disc it has size at most13/25 of the squared radius, including
the integer-rounding error. The origin is included: the observation ZW-a
there equals-a, so individual observations need not become smaller.

The hard point is differentiation. Each derivative can hit either the
unpaired Z powers or a centered radial factor. We must count every choice;
simply attaching a centering factor to the old derivative bound is false.
Already the derivative of ZW-a is W: its small centered factor disappears.

Write (n)_k=n(n-1)...(n-k+1), with value0 when k>n. For r>=s, the full
derivative majorant has coefficient

    B = sum_k choose(s,k) (j)_k (r-s)_(j-k) h^(s-k), h=13/25.

The checked elementary bound is

    B <= (r)_j (h + j/(r-j+1))^s, 0<=j<=r.

Its meaning: differentiation consumes some centering gain, at a controlled
cost. Descending-factorial splitting bounds each term, then the binomial
theorem collects them. This is a finite algebraic argument, without an
assumption that derivative choices are independent.

When j<S and r>=9S, that cost is at most1/8, leaving a factor at most13/20
for each paired power. All other rows retain their old uniform bound;
derivatives above the actual Z-degree vanish. No derivative column is lost.

Summing the row savings over the eligible rectangle gives at
least0.010 times the scale R^2*S, for S>=100 and25S<=R<=26S. That smaller
sufficient saving still targets48 billion. The stronger0.013 paper estimate
is a separate claim. The final scalar margin is only0.0001862561, so the
unchanged rounding and geometric guards matter.

Phase118 leaves the logarithmic upper bound
for the SAME original Gram determinant and the actual-field theorem to
compose and verify. The registered attempt includes negative controls,
fixed resources and preservation of every failed source; it is not itself
a new cutoff. [Exact verification](PHASE118_VERIFICATION.md) · [Protocol](PHASE118_PROTOCOL.md).
