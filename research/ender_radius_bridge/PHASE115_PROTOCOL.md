# Phase115: monic radial centering, distinct paper-and-exact-check cycle

Base47563334e5374f15d490ece98a7ed1184a6822cd. Register before new code or
execution. Phase113 and Phase114 remain stopped: no replay, source repair,
parameter rescaling, dependency-partition proof or increased Lean limits.
This target changes the polynomial row basis, not the principal-block proof.
No Lean invocation or production/root/tool/pin/workflow change in this cycle.

## Fixed scientific target

For integer a and m=min(r,s), define
 Q_(r,s)=Z^(r-m) W^(s-m) (ZW-a)^m.
Expand Q=sum_(t<=m) choose(m,t)(-a)^t Z^(r-t)W^(s-t).
In original row-major order its integer matrix T_a is lower triangular,
diagonal1. Prove on paper T_a T_b=T_(a+b), inverse T_-a, full ordinary jet
linearity and H=T_a G T_a^T for the SAME original integer trace-Gram G.
Therefore determinant, lattice, prime-power determinant divisors and ranks
modulo every prime survive; PSD/guarded PD travel under the real cast.
No new arithmetic exponent, Hermitian replacement, ring map C->F_p,
rotational symmetry or sample/derivative omission.

At the ACTUAL production disc |z|<=rho, integer rho>=5, choose
 a=floor(rho^2/2), h=ceil(rho^2/2)/rho^2<=13/25.
For r>=s, bound the full ordinary jth derivative using
 B_j=sum_l choose(j,l)(s)_l(r-s)_(j-l) h^(s-l),
 with 0<=l<=min(s,j), j-l<=r-s.
Target B_j/(r)_j <= (h+(1-h)j/r)^s for 0<=j<=r,r>0.
For r<s retain all derivatives and prove no loss relative to the OLD
radial ENVELOPE (not the original actual row norm). For j>r jets vanish.
For J=S and r>=5S, get jet size<= (5/8)^s times the old termwise radial
envelope. All other rows retain the old envelope. Aggregate on the SAME
determinant: log det G <= upper_B - (R-5S) S(S-1) log(8/5).
For S>=100 and25S<=R<=26S target normalized saving>=13/1000.

Use unchanged production R=floor(D/4),S=J=floor(R/25),
rho=ceil(.52D^.75), old geometry valid for D>=450^4,
old normalized upper<=.8logD-.813 and recovered lower>=.999997logD-5.739.
FIXED candidate endpoint48,000,000,000: use factorization2^13*3*5^9,
log2>=.6931,log3>=1.09,log5>=1.609 and log(8/5)>=.46.
Verify the resulting rational affine separation at that endpoint and
monotone positive slope. No endpoint/centering/threshold search.
A paper argument and finite checks are NOT a checked cutoff. Full Lean
operator, quantitative bound, old-budget replacement, actual-field transport
and pinned CI remain required before upgrading the published50b bound.

## ONE sealed exact finite invocation

Pure standard-library Python, exact integers/Fractions, no floats or
imports/drivers of old campaigns. Cohorts:
 D1 points[(0,0),(1,0),(-1,0),(0,1)];
 D7 points[(0,0),(2,1),(-1,2),(3,-1)];
 D19 points[(0,0),(1,0),(2,0),(0,1),(1,1),(2,1)].
Rectangles(0,3),(3,0),(1,1),(4,3),(3,4),(6,2);
a in[-2,0,3], J in[0,1,4]:162cases, including empty/singular cases.
Independently multiply sparse bivariate polynomials then differentiate,
versus matrix action on original integer pair jets. Compare full H=TGT^T,
T_a T_-a=I, determinant equality, and mod3/mod5 ranks. For actual nonsquare
odd primes in[3,5] verify inherited original exponent directly when det!=0;
zero determinants have divisibility but no advertised positive lower bound.
Use a separate T_aT_b composition check with b=-1 in every rectangle.
For the same points/radius, test every j<J row norm against the full radial
envelope. Exact coefficient grid: r=1..48,s=0..min(r,8),j=0..min(r,12),
h=13/25. Check hypergeometric identity and bound; eligible S=1..8 check
r>=5S,j<S and s<S gives factor(5/8)^s. Include zero/s=0/j=r controls.

Reject mutations: missing factor2, ordinary->divided factorial substitution,
wrong sign ofa, dropping Leibniz terms, assuming rowwise ACTUAL norm always
improves, positive gain atS=1, ignoring the integer-rounding error in h,
and treating a singular determinant as a positive arithmetic lower bound.
These include recorded counterexamples to stronger false assertions.
Derive exact rational log enclosures using100positive atanh-series terms
and their explicit geometric tail; verify the fixed log bounds and endpoint
separation. These are reproducible rational calculations, not Lean proofs.

## Budget, evidence and stop rule

ExactlyONE combined invocation:120s/8192MB per owned process. No repairs,
repeats, pilot probes, parameter tuning or partial-success gate if any
assertion/resource limit fails. Source/data/stdout/stderr/native result
preserved. Success gate requires ALL162cases, all coefficient controls,
all mutation witnesses, fixed rational logs and candidate margin plus
complete paper derivation; it only authorizes a future formalization target.
Freeze every preexisting tracked file except current reader documents and
.agent task state. Read-only saved verifier checks raw hashes, protocol
ancestry, final verdict/completeness, exact endpoint margin and frozen Git
blobs; NEVER reruns the numerical trial. Commit a short readable guide,
paper derivation and exact results; update README/STATUS/FORMALIZATION/
objective ledger/reply. README and objective ledger remain61lines. No CI,
publication, merge, new reviewer or Tao posting in this cycle.
