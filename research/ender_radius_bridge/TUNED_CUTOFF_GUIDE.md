# From a promising radius to a universal cutoff

**Historical Phase42 checkpoint.** The separately registered Phase43
completion and current100-billion result are explained in the
[current proof guide](HUNDRED_BILLION_GUIDE.md). The failure/stop outcome
below remains unchanged.

Phase42 targets a direct100-billion analytic cutoff, not a consequence of
the finite classification. The new radius-family module compiled, but the
counted upper-envelope/field-composition target hit its registered600-second
limit. **No100-billion cutoff was accepted; the checked cutoff stays200
billion.** The unaccepted candidate is preserved outside the library in
[Phase42UnacceptedCutoff.lean](Phase42UnacceptedCutoff.lean). No retry or cap
increase is allowed within Phase42. Partial geometry verification is
separate and does not execute that unaccepted cutoff candidate.

The partial library's full root, fresh geometry-input check and compiled
axiom audit pass locally. The latter check explicitly confirms there is no
100-billion cutoff declaration in the library. [Results](PHASE42_RESULTS.json)
and [verification](PHASE42_VERIFICATION.md) distinguish these passes from
the failed and timed-out full-cutoff attempts; exact publication-head CI
has its own final PR28 record.

## The geometric insight

Keep the same integral trace-Gram determinant and its ordinary derivatives.
Choose a thinner monomial rectangle and a smaller sampling radius:

    R=floor(D/4), S=J=floor(R/25), t=D^(1/4),
    rho=ceil(.52*t^3).

This is a new auxiliary family, not a change to the frozen Ender campaign.
Shrinking the radius decreases complex size, but we must still fit enough
lattice points to make the determinant positive. That is the geometric
obligation; the successful one-point pilot did not prove it universally.

For D>=100000000000, Lean checks t>=500, R>=D/5, S/R<=1/25 and R<=25.1*S,
with actual integer floors retained. Hence `3R+S<=.76D`. Using pi>3.14,

    sqrt((3R+S)*sqrt(D)/pi) <= .495*t^3.

The original chosen-radius requirement is at most

    1.001*.495*t^3 + 10*t^2
      <= (.495495 + .02)*t^3
      < .52*t^3 <= rho.

The boundary strip costs `10/t` after normalization; t>=500 controls it.
This is why the radius cannot be shrunk just by changing a decimal in the
final inequality. Ceiling error is also paid: rho<=.521*t^3 on this
domain. At D=1 that upper-rounding claim is false, a retained Lean control.
The strict inertness guard remains R<(D+1)/4 in the odd chart; the inclusive
endpoint is rejected at D=163,p=41.

## Where the proposed improvement comes from

The Phase41 lower lemma exposes the price of thinning the rectangle:
normalized loss at most3.294+0.0448K when R<=K*S. At K=25.1, and using the
guarded `log R>=log D-1.4`, the new family has the checked lower envelope

    L/(R^2*S) >= .999997*u-5.820,  u=log D.

The remaining target is the counted upper envelope

    U/(R^2*S) <= .8*u-.813.

Its proof must retain the exact count-log, derivative and endpoint
corrections of the original upper_B. The intended accounting is

    .75*u-.65 + (S/R)*(1.25*u-4.11) + .00125
      <= .8*u-.81315 <= .8*u-.813.

This upper expression is a proof target at the checkpoint above, not a
newly accepted universal claim. The two proposed affine bounds separate
for u>=25.3; the exact scalar gap there is.0529241. They fail at u=25.
The endpoint logarithm follows from10^11=2^11*5^11 and checked log2/log5.
But scalar separation is not a cutoff until both universal envelopes and
all original guards reach the same positive integer determinant.

## Final bridge and verification boundary

If the remaining target passes, odd positive-squarefree D with D>=1e11
cannot have actual class number one. The existing generic maximal-order
argument at prime two handles the other parity chart; explicit field
equivalence and the actual field-discriminant identity then supply both
public bounds. Old700-billion and200-billion cutoff theorems, the final
iff, positive-case theorem and finite-answer certificates must not enter
the new proof's compiled dependency closure.

The [protocol](PHASE42_PROTOCOL.md) fixes this family and target, preserves
all failed attempts and caps resources. The first build failed only at an
unsimplified ceiling in the small-D rejection control; its repair makes
the positive-integer ceiling bound explicit without altering the control.
The repaired attempt built the radius-family module, then stopped at the
time cap without a completed upper/cutoff check. That is an incomplete
resource-bounded proof attempt, not a mathematical counterexample. Raw
failure/stop records are retained. No fresh numerical pilot was run.
Consult the final exact-head PR28 record for publication verification;
this phase establishes no smaller cutoff. No novelty, optimality,
independent human review, merge or external submission is claimed.
