# Same boxes, different counting order

The prime weight is

    F(R,S,p)=sum_(r<R,t<S) min(floor(r/p),t).

Think of it as the number of integer triples(r,t,k) satisfying
r<R, t<S,1<=k<=t and pk<=r. The indices r,t describe monomial degrees;
k is a divisibility-weight level. None is the ordinary derivative order.
Changing which index we count first preserves the same finite set.

Fix a column height t and write C(t)=sum_(r<R)min(floor(r/p),t).
Raising that height by one adds precisely the rows r>=p(t+1):

    C(t+1)=C(t)+max(R-p(t+1),0).

This identity requires p>0 and works even when the new height does not
fit. Lean writes the last term as truncated natural subtraction.
If pt<=R, summing these increments gives

    2C(t)=t(2R-p(t+1)).

Now sum columns t=0,...,S-1. If the last threshold fits, p(S-1)<=R,
the exact original weight is

    6F(R,S,p)=S(S-1)(3R-p(S+1)).

The displayed polynomial is interpreted over the reals. It also handles
S=0 and S=1, where the weight is zero. Not all rows must be saturated:
the operation counts the partially filled rows too. This explains what
the earlier saturated-row lower bound left out.

## Why the guards matter

At p=0,R=4,S=2, the original weight is zero while the candidate polynomial
is24. At R=1,S=3,p=2, the last threshold does not fit: the original weight
is zero and the candidate polynomial is-30. These controls reject deleting
the hypotheses; neither proves that the chosen condition is sharp.

At R=8,S=2,p=2, F=6 and the new formula gives36=6F. The older
quadratic-floor expression, valid under a different quotient guard,
gives4 for F in this example and is already recorded as a false identity
without that guard. The two formulas have different hypotheses, with
some overlap; the new theorem does not erase that earlier negative result.

This is a simpler description of weights whose determinant divisibility
was already proved. It creates no new valuation exponent, prime input,
parity gain or discriminant cutoff. The current cutoff remains50 billion.
No novelty, optimality, independent human review or full classification
is claimed. [Lean source](../../lean/TenthDiscriminant/StaircaseExact.lean)
and [verification scope](PHASE57_VERIFICATION.md).
