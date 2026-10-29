# Monic radial centering: the complete paper argument

Status: PAPER CANDIDATE plus sealed finite exact checks. No new Lean
statement, verified all-D theorem, independent review or cutoff upgrade.
The published bound remains50 billion. This document states the proposed
uniform argument explicitly so that every bridge can be challenged.

## 1. The same integral observable lattice

Fix a positive integer D, nonnegative dimensions R,S,J and a finite set
of integer pairs Q.
Work in the free integer module with basis Z^r W^s, r<R,s<S. Define
m=min(r,s) and, for integer a,

$$Q_{r,s}^{(a)}=Z^{r-m}W^{s-m}(ZW-a)^m
 =\sum_{t=0}^{m}\binom mt(-a)^t Z^{r-t}W^{s-t}.$$

All terms stay in the SAME rectangle. Their row-major indices are
(r-t)S+(s-t)=rS+s-t(S+1). Thus the explicit coefficient matrix T_a is
lower triangular with diagonal 1; det T_a=1, also for empty rectangles.
For each fixed integer weight r-s, factor off Z^(r-s) or W^(s-r).
The remaining operation is polynomial translation in N=ZW on degrees
0..m. Translation composition gives T_a T_b=T_(a+b), hence T_-a is its
integer inverse. This proves preservation of the integral row lattice.
This is a change of observables, not movement of the sampled points.
It is an integer-LINEAR module automorphism, not a ring automorphism:
Z and W are fixed separately, but their product ZW is sent to ZW-a.
Coefficient reduction commutes with its integer matrix action; polynomial
multiplication and individual Euclidean row norms are not invariants.

Evaluate W as conjugate z AFTER taking ordinary Z derivatives. Both
ordinary differentiation and evaluation are linear. The entire sampled
jet matrix therefore transforms by T_a. For the original integer real
trace-Gram G, retaining its factor2 and both pair coordinates, the actual
transformed Gram is H=T_a G T_a^T. Consequently det H=det G over Int and
after the real cast. PSD is preserved, and PD is preserved because T_a
is invertible. Every determinant divisor is the SAME divisor of the SAME
integer. Reduction of T_aT_-a=I modulo ANY prime proves invertibility
there, so residue Gram ranks also agree. No C-to-finite-field map is used.

## 2. Centering a whole disc, including the origin

Let integer rho>=5, |z|<=rho, and a=floor(rho^2/2). Put
h=ceil(rho^2/2)/rho^2. For every N=|z|^2 in[0,rho^2],

$$|N-a|\le\lceil\rho^2/2\rceil=h\rho^2,
\qquad \tfrac12\le h\le\tfrac{13}{25}.$$

The last inequality follows from h<=1/2+1/(2rho^2) and rho>=5.
The actual row norm need NOT decrease: at z=0, ZW has value0 while
ZW-a has value-a. The estimate below concerns the old UNIFORM RADIAL
ENVELOPE, not pointwise domination by the old actual observable.

## 3. Every ordinary derivative term, with W held fixed

For r>=s, use Q=Z^(r-s)(ZW-a)^s. Leibniz gives, for0<=j<=r,

$$\partial_Z^j Q=
\sum_{\substack{0\le l\le\min(s,j)\\j-l\le r-s}}
\binom jl(s)_l(r-s)_{j-l}
Z^{r-s-j+l}W^l(ZW-a)^{s-l}.$$

The displayed restriction keeps every exponent nonnegative. Bounding each
factor on the disc gives

$$|\partial_Z^j Q(z,\bar z)|\le\rho^{r+s-j}B_j,
\quad B_j=\sum_l\binom jl(s)_l(r-s)_{j-l}h^{s-l}.$$

To bound B_j, choose uniformly a j-element subset of r positions, s of
which are marked. Let L count chosen marked positions. Counting subsets
shows B_j/(r)_j=E[h^(s-L)]. For k<=s,
E[choose(L,k)]=choose(s,k)(j)_k/(r)_k. Expand h^(-L) as
(1+(1/h-1))^L and interchange the finite sums. Since
(j)_k/(r)_k<= (j/r)^k, with zero numerator if k>j, for r>0,

$$\frac{B_j}{(r)_j}
=h^s\sum_{k=0}^s\binom sk(h^{-1}-1)^k\frac{(j)_k}{(r)_k}
\le \bigl(h+(1-h)j/r\bigr)^s.$$

This is a finite counting identity and product inequality; no independence
assumption or probabilistic limit theorem is used. The case r=s=0 has
its sole nonzero derivative at j=0 and is checked separately.

For r<s, Q=W^(s-r)(ZW-a)^r, so the derivative is exactly
(r)_j W^(s-r+j)(ZW-a)^(r-j) for j<=r. Its magnitude is bounded by
(r)_j rho^(r+s-j) h^(r-j), at most the old radial envelope.
Every jet with j>r vanishes in both cases, because deg_Z Q=r.

Now set J=S. For r>=5S and j<S, j/r<=1/5 and r>=s for every s<S.
Hence h+(1-h)j/r<=13/25+(12/25)/5=77/125<5/8. Thus ALL derivative
columns of every such row obey the old envelope times(5/8)^s.
Every other row keeps the old envelope without a multiplicative penalty.
In particular s=0 and S=1 supply no positive claimed gain.

## 4. A smaller upper bound on the same determinant

Let n be the number of samples. The old rowwise majorant is

$$K_{r,s}=2nJ\rho^{2(r+s)}\max(1,r/\rho)^{2(J-1)}.$$

Indeed (r)_j<=r^j and the sum over j<J is at most J times the largest
corresponding radius ratio. The transformed diagonal is at most K_(r,s),
and for r>=5S it is at most(5/8)^(2s) K_(r,s). Hadamard applies to H,
whose determinant equals det G. If the original guards give PD, every
transformed diagonal and det G are positive, so logarithms are legitimate.
The old aggregation of log K remains valid at the SAME production radius:
when R>rho its monotone integral bound on sum_r log(max(1,r/rho)) is
R log(R/rho)-R+rho+log(R/rho). Thus

$$\log\det G\le U_B-(R-5S)S(S-1)\log(8/5).$$

This step needs no general Fischer theorem or dependent partition identity.
It does require formalizing the explicit T_a action and transformed row
majorants; finite numerical comparisons cannot discharge those obligations.

For S>=100 and25S<=R<=26S, use R-5S>=20S, S-1>=.99S,
R^2<=676S^2 and log(8/5)>=.46. With the unchanged scale R^2 S,

$$\frac{(R-5S)S(S-1)\log(8/5)}{R^2S}
\ge\frac{20\cdot.99\cdot.46}{676}
=\frac{2277}{169000}>\frac{13}{1000}.$$

## 5. Fixed candidate endpoint and inherited guards

The unchanged production parameters are R=floor(D/4),S=J=floor(R/25),
rho=ceil(.52D^.75). Existing geometric helper statements apply for
D>=450^4=41006250000. They give the original upper envelope
.8logD-.813 and the raw lower envelope .999997logD-5.820.
The existing strong recovery lemma adds.081 under S>=100,25S<=R<=26S.
Those floor guards hold already throughout this geometric domain.
Therefore the recovered lower envelope is .999997logD-5.739.

Important formal boundary: the named fifty_normalized_lower WRAPPER in
the repository assumes D>=50b. It cannot be invoked at48b. A new proof
must compose normalized_lower (domain450^4) with the existing strong
recovery lemma and reprove the floor guards. No earlier cutoff theorem
is a premise of this paper comparison.

The proposed radial gain changes the upper envelope to .8logD-.826.
At the FIXED endpoint48b=2^13*3*5^9, the rational logarithm bounds
log2>=.6931,log3>=1.09,log5>=1.609 give logD>=24.5813.
The recovered lower minus proposed upper is at least

$$.199997\cdot24.5813-4.913
=\frac{31862561}{10000000000}=.0031862561>0.$$

The slope .199997 is positive, so this affine separation persists for
larger D. Strict inertness, rank/count guards and prime masses are the
old ones; the determinant remains their original integer. Arbitrary-field
discriminant transport and the even-field case still need explicit
composition in a new formal theorem. This document supplies no such
checked theorem and does not upgrade the published50b bound.

## 6. Evidence boundary

The one sealed exact trial checks162 small matrix cases,4,910 coefficient
cases and3,516 eligible cases, with nine planted false-claim witnesses and
rational log certificates. Those finite checks support the implementation
and challenge the paper formulas; they do not prove their universal
quantifiers. See PHASE115_VERIFICATION.md. No stopped phase was replayed,
no failed Lean artifact repaired, and no new Lean/CI run occurred here.
