# The integral radial frame is now checked

**Lean checks the universal operator bridge, standalone.** The quantitative
saving and 48-billion cutoff remain paper candidates; the published
class-number-one bound remains 50 billion. Integration and new CI are pending.

The original integer Gram determinant stays our common object. Replace
its polynomial row Z^rW^s by

$$Z^{r-m}W^{s-m}(ZW-a)^m,\qquad m=\min(r,s),\quad a\in\mathbb Z.$$

Expanding this expression gives its original row plus integer multiples
of earlier rows. Lean constructs that explicit matrix T, proves that its
diagonal is 1 and its determinant is 1, and constructs its integral inverse
using the adjugate. No invertibility premise is supplied by the caller.

The key commuting square is also checked. Applying T to the old sampled
ordinary jets equals directly differentiating the new polynomials, at
every derivative order. W is held constant while differentiating. The
identity is valid over any commutative ring; complex and integer-pair
versions use the same coefficients and row order.

For the actual new integer Gram H and original integer Gram G, Lean proves

$$H=TGT^{\mathsf T},\qquad \det H=\det G.$$

All points, derivative columns and the factor-two real trace remain.
The arithmetic and geometric estimates therefore concern the same integer.

The preserved structures have explicit scopes:

| Structure | Checked invariant |
| --- | --- |
| Integer row lattice | T has an integral two-sided inverse |
| Integer determinant | Exactly the original determinant |
| Prime-power divisor | The inherited odd-prime nonsquare divisor, unchanged |
| Real geometry | Exact cast and PSD for D>0; PD under the original count/depth guards |
| Reduction modulo a prime | det T=1 and equal Gram ranks, including p=2 |

Positive definiteness retains D>0,R>=1,S>=1,J>=S and the strict point-count
guard card(Q)>2(R-1)+(S-1). Divisibility retains its prime/nonsquare guards.
No general rank preservation by non-injective reduction is asserted.
The integer-pair chart is the original selected quadratic order, without
identifying it with every field's full ring of integers.

Individual row norms and polynomial multiplication are not invariants.
At the origin, ZW is 0 while ZW-3 is -3. This checked counterexample prevents
us from claiming that every actual observable got smaller. The geometric
candidate is a better uniform bound, whose proof remains separate.

The sharper parameter law T_aT_b=T_(a+b), including inverse T_-a, remains
paper/finite evidence in this cycle. The checked inverse is the adjugate.

The entire registered operator target passed after two proof-only repairs,
with unchanged 27 public statements and six definitions. The namespace
and all three fresh dependency checks pass; old cutoffs/classifications
are excluded. The failed first source is preserved.
[Lean source](Phase116RadialOperator.lean) ·
[Exact proof evidence](PHASE116_VERIFICATION.md) ·
[Quantitative candidate and remaining obligations](RADIAL_CENTERING_DERIVATION.md).
