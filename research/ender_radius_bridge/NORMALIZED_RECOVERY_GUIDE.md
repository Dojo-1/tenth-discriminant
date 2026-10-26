# A fixed gain that survives normalization

The recovered3/5 terms are now more than a strictly positive correction.
Lean proves they contribute at least3/50 after dividing by R^2*S, provided
S>=100 and25*S<=R<=26*S. Equivalently, for every real tail parameter I,

    raw budget/(R^2*S) + 3/50 <= recovered budget/(R^2*S).

The raw budget is the existing unclipped lower expression. The recovered
budget is the [certified proxy plus the exact3/5 terms](SMALL_PRIME_RECOVERY_GUIDE.md).
No original valuation exponent, observation or derivative is changed.

## Count the saturated part of the existing weight

For F(p)=sum_(r<R,t<S) min(floor(r/p),t), every row r>=p*S contributes
the full sum0+1+...+(S-1). The number of these rows is R-p*S, with natural
subtraction giving zero when there are none. Therefore, for p>0,

    2*F(p) >= (R-p*S)*S*(S-1).

The indices describe monomial-degree weights in the large row module;
t here is not the ordinary derivative order. This count is applied to
p=3 and5. It uses fewer saturated rows than one could count, deliberately
leaving room for a simple conservative bound.

The existing rational log2 certificate gives log3>=1 and log5>=1 through
logarithms of powers. No new prime-distribution estimate or table is used.
Since R>=25*S and S>=100, the recovered numerator is at least

    (2079/50)*S^3.

Meanwhile R<=26*S gives R^2*S<=676*S^3. The exact rational comparison
(2079/50)/676 > 3/50 proves the fixed normalized gain. This is not a claim
that3/50 is optimal.

## Checked limits

The p=0 control rejects applying the row-count formula without p>0.
The R=25,S=1 control has zero recovered gain despite satisfying the ratio
bounds, so dropping the lower-size assumption altogether would be false.
It does not show100 is necessary or sharp.

These estimates come from already proved prime weights, not an extra
contribution attributed to parity symmetry. The unchanged production
comparison still needs its tail, inertness/class-number and geometry guards
when applied to the actual Gram.

The current tuned rectangle falls in this ratio range under its checked
dimension guards. To prove a smaller discriminant cutoff, those guards
and the upper/lower comparison must be verified at a new endpoint. This
module proves no new endpoint; the stated cutoff remains10^11.

[SmallPrimeRecoveryGain.lean](../../lean/TenthDiscriminant/SmallPrimeRecoveryGain.lean)
contains the fixed gain and two boundary controls. The
[protocol](PHASE53_PROTOCOL.md) fixed the region and3/50 before execution.
No parameter search, new valuation, classification, novelty, independent
review, merge or Tao-submission result is claimed.
