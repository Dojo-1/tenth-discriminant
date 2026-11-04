# Post-preregistration derivations: what survives an actually moving frame?

2026-11-04. Separate from the frozen preregistration commit 59933f9c. These are *new deductions and tests*, not retroactively preregistered predictions. The production 322 theorem remains untouched.

## P: exact combinatorial profile of the rectangular prime weights

The original row exponents are

    e_(r,s)(p)=min(floor(r/p), S-1-s)  (0<=r<R, 0<=s<S)

for odd Frobenius-prime row frames in the existing rectangular basis proof. Set n=R*S. Let c_j be the number of rows with exponent at least j. For positive integers j,

    c_j = max(R-p*j,0) * max(S-j,0).

Proof: e_(r,s)>=j exactly when r>=p*j and s<=S-1-j.

Let tau_k be the sum of the k *smallest* exponents (not largest). If m=n-k, then

    tau_k = sum_{j>=1} max(c_j-m, 0).

Proof: at level j, among the n rows there are n-c_j with exponent <j; selecting the k smallest includes exactly max(k-(n-c_j),0) rows with exponent >=j. Sum these level contributions.

When R >= p*(S-1), c_j=(R-p*j)(S-j) is decreasing for 1<=j<=S-1. Let t be the largest j with c_j>n-k. The resulting closed form is

    tau_k = t*R*S - (R+p*S)*t*(t+1)/2
                    + p*t*(t+1)*(2*t+1)/6 - (n-k)*t.

This expression is an *integer*: the consecutive-products divisible by 2 and 6 ensure exactness. At k=n it returns the existing full valuationWeight

    F(p) = R*S*(S-1)/2 - p*S*(S-1)*(S+1)/6.

The formula can be evaluated using integer binary search on t, in O(log S) time and O(1) large-integer storage, without materializing a matrix of dimension n.

## M: exact source-parameter profile at root 322, not a new bound

At D=322^4=10,750,371,856,
R=floor(D/4)=2,687,592,964;
S=floor(R/25)=107,503,718;
n=R*S=288,926,236,100,640,152.

For p=3, F(3)=14,909,109,270,883,882,320,543,235.
For p=5, F(5)=14,494,967,344,927,003,061,090,397.

The exact script [prefix_profile.py](prefix_profile.py) computed these with integers; the decimal ratios below are *display approximations*, not proof inputs:

| k as fraction of n | tau_k(3)/F(3) | tau_k(5)/F(5) |
|---|---:|---:|
| 1/4 | ~0.05909045 | ~0.05716769 |
| 1/2 | ~0.24051859 | ~0.23480383 |
| 3/4 | ~0.55134111 | ~0.54407463 |
| 1 | 1 | 1 |

The k<n profile is arithmetically nontrivial at enormous R,S even though the tiny R=4,S=2 pilot has tau_k=0 for k<8. This neither supplies a k-minor *geometric upper* nor improves the established scalar cutoff. H1 remains genuinely open.

The script exhaustively checks the closed form against sorted exponents for many small (R,S,p,k), and returns exact giant integer tau_k for the real source dimensions.

## P: unrestricted continuous frames erase geometric spectral shape

Let G,H be symmetric positive-definite n-by-n real matrices with det G=det H. Set

    U=H^(1/2)*G^(-1/2).

Then det U=1 and U G U^T=H. Therefore SL_n(R) acts transitively on the positive-definite matrices of a fixed determinant. Their individual eigenvalue lists are **not** invariants under arbitrary moving volume-preserving frames. Even allowing all GL_n(R) removes the determinant invariant as well.

**R (retired):** "a nontrivial spectrum in a moving SL_n(R) frame automatically reveals intrinsic new geometry." It can be a pure gauge artifact. A new geometric profile requires a fixed reference structure, a restricted gauge group, or *simultaneous* transport of a pair of forms.

## P: the simplest typed pair is already present in the original source

For fixed D,J,R,S and two positive-definite Grams G_thin and G_old built from their respective original sample supports, consider the *pair* (G_old,G_thin) acting on the same R*S-dimensional row module. Under simultaneous congruence by any U in GL_n(R), their generalized eigenvalues are unchanged:

    (U G_thin U^T)^(-1)(U G_old U^T)
       = U^(-T)(G_thin^(-1) G_old) U^T,

which is similar to G_thin^(-1) G_old.

If Q_thin subset Q_old, then G_old-G_thin is PSD, hence every generalized eigenvalue is >=1. Their product is det G_old/det G_thin. This gives a plural, frame-invariant **relative** spectrum without confusing it with the individual spectra under arbitrary real gauges.

**Small exact toy:** Q1={(1,0),(4,0)}, Q2=Q1 union {(2,0)}, ordinary rows 1,Z and J=1, yields G1=[[4,10],[10,34]] and G2=[[6,14],[14,42]]. The generalized eigenvalues of (G2,G1) are 1 and 14/9. The product 14/9 equals det G2/det G1=56/36. The one nontrivial eigenvalue encodes the rank-one geometric update; individual p-adic determinant valuations need not move monotonically.

**Important:** Although this pair is well defined, no existing arithmetic lower for the *old* Gram can be transferred to the *thin* one merely from PSD ordering. Both prime divisibility and geometry remain source-typed.

## Next decisive theorem target / stop rule

Try to prove in Lean the general k-minor divisibility of the exact integer Gram from the existing integral row diagonalization. Do not claim novelty: determinantal ideals and Smith invariants are classical, and the repository already has determinant-only integer transport in TransportCoherence.lean. Then seek a same-Q analytic k-principal-minor upper for the *actual* thin-ellipse row norms.

Stop/retire a claimed gain if it requires a continuously varying integer frame, claims spectral invariance under arbitrary SL_n(R) without a co-moving reference, changes the ordinary-Z derivative convention, or yields no improved exclusion beyond the current whole-determinant sandwich.
