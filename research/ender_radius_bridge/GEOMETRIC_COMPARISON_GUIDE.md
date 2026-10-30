# One integer seen through a better geometric frame

The arithmetic derivation exposes prime factors in the original integer G.
Here we bound that SAME determinant from above. A different integral frame
improves the estimates; it need not preserve individual lengths or commute
with the prime-dependent frames. This is a reconstruction by the same
assistant, not a new independent review or a new kernel theorem.

## 1. Fix the geometry and retain the rounding

Throughout this page D>=450^4=41,006,250,000. Set t=D^(1/4), so t>=450,
and use the actual production choices

\[
R=\lfloor D/4\rfloor,\quad S=J=\lfloor R/25\rfloor,\quad
\rho=\lceil(13/25)t^3\rceil,\quad a=\lfloor\rho^2/2\rfloor.
\]

The samples Q are ALL integer pairs with x^2+D y^2<=rho^2, embedded as
z=x+i sqrt(D)y. The radius is an integer, not the half-integer campaign
radius. We have R>=D/5, S>=100, 25S<=R<=26S and

\[
(13/25)t^3\le\rho<(13/25)t^3+1\le(521/1000)t^3<R.
\]

The final inequalities use t>=450. For D=1 the claimed upper rounding
bound fails; it must not be silently extended outside the stated domain.

## 2. Two counting arguments, with different jobs

For the LOWER count, centered lattice cells have area sqrt(D) and every
point of a cell is within delta=(1+sqrt(D))/2 of its center. Rounding a
point in the disc of radius rho-delta therefore gives a center in Q.
When rho>=delta, covering that smaller disc gives

\[
\pi(\rho-\delta)^2\le |Q|\sqrt D.
\]

For q=3R+S, the bounds R<=D/4 and S<=R/25 give q<=0.76D. Since pi>=3.14,
sqrt(q sqrt(D)/pi)<=0.495t^3. The exact rational inequality
0.52-1.001*0.495-10/450>0 proves that our chosen rho satisfies
rho>=1.001sqrt(q sqrt(D)/pi)+10sqrt(D). Thus rho-delta exceeds
sqrt(q sqrt(D)/pi), and |Q|>q>2(R-1)+(S-1).

Distinct samples, R,S>=1 and J=S now supply the interpolation guards for
positive definiteness. Consequently detG>0. This is needed before logs.

For the UPPER count, each OFF-AXIS lattice point owns an inward cell inside
the original disc. These cells are disjoint up to boundaries and have area
sqrt(D). The axes are counted separately, giving the explicit bound

\[
|Q|\le n:=\pi\rho^2/\sqrt D+2\rho+2\lfloor\rho/\sqrt D\rfloor+1\le4D.
\]

The horizontal nonzero points contribute 2rho; the vertical axis includes
the origin. The last estimate follows from pi<4 and, with b=0.521,
n/D<=4b^2+2b/t+2b/t^3+1/t^4<4 for t>=450. Treating every axis point
as owning a full inward cell would be false. Squaring rho-delta when it
is negative would also invalidate the lower count.

## 3. Centering improves a uniform ceiling, not every value

Use the integer row family

\[
Q_{r,s}=Z^{r-m}W^{s-m}(ZW-a)^m,\qquad m=\min(r,s).
\]

Its binomial coefficient matrix T_a is lower unitriangular: the leading
term is Z^rW^s and all remaining labels decrease both exponents. Therefore
H=T_a G T_a^T has detH=detG. After W=conjugate(z), ZW=|z|^2 lies in
[0,rho^2], and integer centering gives

\[
\bigl||z|^2-a\bigr|\le\rho^2/2+1/2\le(13/25)\rho^2\quad(\rho\ge5).
\]

At the origin a centered observation can INCREASE. The proof uses this
uniform ceiling, never a claim that all observed values decrease.

For r>=s and j<=r, the complete ordinary Leibniz estimate is

\[
|\partial_Z^jQ_{r,s}(z,\bar z)|\le\rho^{r+s-j}B_j(h),\quad h=13/25,
\quad B_j(h)=\sum_{k=0}^s\binom{s}{k}(j)_k(r-s)_{j-k}h^{s-k}.
\]

Terms outside derivative support vanish through falling factorials. The
identity B_j(1)=(r)_j follows by differentiating Z^(r-s)Z^s. Hence h<=1
gives the old majorant without loss. More precisely, termwise factorial
comparison gives B_j(h)<=(r)_j(h+j/(r-j+1))^s: the denominator consists
of k factors each at least r-j+1, while (j)_k<=j^k.

When r>=9S and j<S, j/(r-j+1)<=1/8 and 13/25+1/8<=13/20. Every ordinary
jet of such a row therefore gains (13/20)^s. For r<s, direct differentiation
gives (r)_j W^(s-r+j)(ZW-a)^(r-j), which retains the old bound. Jets j>r
vanish because the Z-degree remains r. These cases include the origin.

## 4. From actual squared jets to the determinant

Let eta_(r,s)=(13/20)^(2s) for r>=9S and 1 otherwise. The actual diagonal,
including the original factor 2, satisfies

\[
H_{(r,s),(r,s)}=2\sum_{z\in Q}\sum_{j<S}|\partial_Z^j Q_{r,s}(z,\bar z)|^2
\le\eta_{r,s}\,2nS\rho^{2(r+s)}\max(1,r/\rho)^{2(S-1)}.
\]

Here (r)_j<=r^j and max(1,r/rho)^j<=max(1,r/rho)^(S-1). The factor S is
an upper bound on the derivative sum, not an exact constant-row identity.
H is positive definite by invertible real congruence. Its determinant and
diagonal entries are positive, so Hadamard and log monotonicity give

\[
\log\det G\le U_B-(R-9S)S(S-1)\log(20/13).
\]

The penalty counts R-9S eligible rows and sums 2s over s=0,...,S-1.
For C=R^2S, S>=100 and 25S<=R<=26S, its normalized size is at least
16*0.99*0.43/676>0.010; the logarithm input is log(20/13)>=0.43.
No factorial is divided out of the actual observations.

## 5. Check the baseline algebra, including its endpoint term

For f(x)=log(max(1,x/rho)), monotonicity and integration give
sum_(r<R)f(r)<=Rlog(R/rho)-R+rho+log(R/rho). The final logarithm is kept.
Summing the preceding row bounds WITHOUT the radial penalty gives exactly

\[
\frac{U_B}{C}=\frac{\log(2nS)}R+(1-S/R)\log\rho
 +\frac{2(S-1)}R(\log R-1)
 +\underbrace{\frac{2(S-1)}{R^2}(\rho+\log(R/\rho))}_{\epsilon}.
\]

The guarded production estimates are explicit. Write ell=logD and x=S/R:
logrho<=0.75ell-0.65, logR<=ell-1.38, ell>=24, x<=1/25,
ell/R<=1/9000, rho/R<=521/90000, and R>=100,000,000.
These follow from the radius/floor bounds, log2>=0.6931 and logu<=u-1.
For ell>=24, use D>=450^4>2^35 and 35*0.6931>24;
for example log(0.521)=log(1.042)-log2<=0.042-0.6931<-0.65.
Also logD/R<=10/t^2<=1/9000 by applying logu<=u-1 at u=sqrtD.

The count n<=4D and S<=D give log(2nS)/R<=(3+2ell)/R<=1/4000.
Since 0<=log(R/rho)<=ell, epsilon<=(2/25)(521/90000+1/9000)<1/1000.
All multipliers used to replace S-1 by S and x by 1/25 are nonnegative.
Therefore

\[
U_B/C\le0.75\ell-0.65+x(1.25\ell-4.11)+0.00125
\le0.8\ell-0.81315\le0.8\ell-0.813.
\]

Subtracting the checked radial saving gives the actual same-integer bound
log(detG)/C<=0.8logD-0.823 throughout D>=41,006,250,000.

## 6. What this closes, and what it does not

The arithmetic pressure on the SAME positive integer is
0.999997logD-5.739<=log(detG)/C. Its prime-power divisibility is reconstructed
in the [arithmetic guide](TWO_SIDED_ARITHMETIC_GUIDE.md). Its factorial-prime
mass and tail/recovery estimates are INHERITED inputs here, not independently
rederived by the rational check or by the geometric calculation above.
At the published 48-billion endpoint, the certified log lower bound 24.5813
gives the exact positive difference 0.0001862561. The coarser 24.58 fails.
The stopped 47.5-billion proof is not upgraded by any of these calculations.

Source map: [EllipseCellArea](../../lean/TenthDiscriminant/EllipseCellArea.lean)
for covering/positivity; [EllipseUpperCount](../../lean/TenthDiscriminant/EllipseUpperCount.lean)
for inward cells/axes; [RadialJetMajorant](../../lean/TenthDiscriminant/RadialJetMajorant.lean)
for every derivative; [RadialDetBound](../../lean/TenthDiscriminant/RadialDetBound.lean)
for the SAME determinant; [NormalizedComparison](../../lean/TenthDiscriminant/NormalizedComparison.lean)
for upperB_normalized; [TunedRadiusFamily](../../lean/TenthDiscriminant/TunedRadiusFamily.lean)
and [TunedAnalyticCutoff](../../lean/TenthDiscriminant/TunedAnalyticCutoff.lean)
for guarded production bounds; [RadialCutoff](../../lean/TenthDiscriminant/RadialCutoff.lean)
for recovered_normalized_lower and actual-field composition.

[Phase124](PHASE124_PROTOCOL.md) fixes ten rational-accounting checks; all
passed once. They check arithmetic displayed here, not analytic premises or
universal quantifiers. No new Lean theorem, cutoff or independent review.
