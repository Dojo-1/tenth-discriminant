# One determinant, two-sided arithmetic factor — independently readable

**29 October 2026. Scope:** mathematical reconstruction of the EXISTING determinant valuation, not an improved bound or a new theorem. Base: main 0bde1bf58893f1adf66bfded5eaf1a0f270c6dce. An independently written exact-integer oracle accompanies this note. The old failed attempts, the current 48-billion proof and its Lean files remain unchanged.

## The five objects, before changing coordinates

Let d>0 be squarefree and K=Q(sqrt(-d)). Its actual field discriminant is Delta_K=-d when d=3 mod 4, and Delta_K=-4d otherwise. The field discriminant is **not** our large jet determinant. The chosen observation order is A_d=Z[t]/(t^2+d), t=sqrt(-d). If d=3 mod 4, it has index two in the maximal order O_K=Z[(1+t)/2]; otherwise A_d=O_K. The class-number-one hypothesis lives in **O_K**, not automatically in A_d. The existing prime-lifting and field-chart lemmas supply that separate link.

Fix positive R,S and J, and a finite set Q of DISTINCT integer pairs (x,y). Identify q=x+yt and qbar=x-yt. For 0<=r<R, 0<=s<S, take the monomial f_(r,s)=Z^r W^s with W treated as an **independent, constant** symbol under differentiation in Z. The j-th ordinary jet is

    v_(r,s),j(q) = (r)_j q^(r-j) qbar^s     if j<=r; otherwise 0.

The falling factorial (r)_j=r(r-1)...(r-j+1) is NOT divided by j!. Write any v=a+bt in integer-pair coordinates and use the fixed positive integral trace pairing

    B_d(a+bt,c+et) = 2(ac+d*b*e).

The original N=RS by N integer matrix is

    G_ih = sum_(q in Q) sum_(0<=j<J) B_d(v_i,j(q), v_h,j(q)).

It has exactly these rows, points, derivative orders, and FACTOR TWO. Over R, B_d(v,v)=2|v|^2. Its determinant is a nonnegative integer; the separate strict point-count and jet-depth theorem makes it positive. Neither this G nor its determinant equals Delta_K.

## Why one inert p supplies p^(2F(p)): four checkable equalities

Take an odd prime p for which -d is a nonsquare in F_p. Thus A_d/p is the quadratic field F_(p^2), and for **each original integer pair** q, Frobenius sends q^p to qbar mod p. Equivalently both integer coordinates of q^p-qbar are divisible by p. In the global class-number-one application, the odd small-prime nonsquare property comes from the ACTUAL maximal-order ideal/norm bridge; it is not assumed from class number one without proof.

**1. Ordinary jets of H=Z^p-W.** At (q,qbar), H is p-divisible in each coordinate. Every positive ordinary Z derivative of H is p-divisible too: (p)_j Z^(p-j) for 1<=j<=p, and zero thereafter. A Hasse/divided derivative is NOT interchangeable: the p-th Hasse derivative of Z^p is 1.

**2. Integral unitriangular polynomial change.** For each row (r,s) let

    k_(r,s) = min(floor(r/p), S-1-s),
    b_(r,s) = Z^(r-p*k) W^s (Z^p-W)^k.

Expand it:

    b_(r,s) = sum_(0<=t<=k) (-1)^t binom(k,t)
                      Z^(r-p*t) W^(s+t).

All terms belong to the original rectangle; the t=0 coefficient is 1, and every t>0 term occurs at a strictly EARLIER row-major index. The explicit integer coefficient matrix U therefore has determinant exactly 1. This is an integer lattice basis change, not an arbitrary real change of basis.

**3. An integral middle K, not a slogan about rows and columns.** The ordinary product rule, applied to the k copies of H, gives p^k in both integer coordinates of **every** jet of b_(r,s). Hence the actual transformed jet table (obtained by applying U to the original integer table) can be written P W, where P=diag(p^k) and W consists of INTEGRAL pairs. Define the actual integral matrix

    K_ih = sum_(q in Q) sum_(j<J) B_d(W_i,j(q),W_h,j(q)).

By bilinearity, indexing the ORIGINAL samples (even if residues collide),

    U G U^T = P K P.

The shared diagonal is p^(2k)*K_ii. Separate row and column divisibility is insufficient: the one-by-one matrix [p] is divisible by p in its row and column but has determinant p, not p^2. The integral *quotient row* constructs what this false argument is missing.

**4. The exponent matches the existing arithmetic weight.** Take determinants:

    det(G) = det(U)^(-2) det(P)^2 det(K)
           = p^(2 sum_(r,s) k_(r,s)) det(K).

Substitute t=S-1-s, which permutes s=0,...,S-1 at every fixed r:

    sum_(r,s) k_(r,s)
      = sum_(r<R,t<S) min(floor(r/p),t) = F(R,S,p).

Therefore p^(2F(R,S,p)) divides the determinant of the **original** G. This is a divisibility statement even if det G=0; geometric positivity is a separate requirement for using its logarithm.

### Concrete witnesses / failure attacks

At d=19,p=3,R=4,S=2, row (3,0) changes from Z^3 to Z^3-W and k=1; every original ordinary jet is divisible by 3 and the same Gram has a factor 9. For Q={ (x,y): x^2+19y^2<=25 } there are exactly 21 points, J=2 and the strict positivity guard is 21>7. The independent integer oracle re-derives the original determinant, U, K and its exact factor 9. A larger d=19,p=3,R=7,S=3 control has F=9 and factor 3^18; another inert case d=3,p=5 gives 5^2.

d=2,p=3 is a split-prime counterexample to the local Frobenius premise: t^3 is NOT congruent to -t mod 3. This invalidates the displayed derivation's hypothesis; it is not a general claim that no determinant can happen to be divisible by 9.

## What geometric comparison preserves, and what it does not

For Q=ellipsePairs d rho (original integer pairs x^2+d y^2<=rho^2) with J>=S and |Q|>2(R-1)+(S-1), the real cast of **the same** G is positive definite. At the chosen radius, the geometric upper proof uses a second integer unimodular change T_a with a=floor(rho^2/2) and

    Z^rW^s -> Z^(r-m) W^(s-m) (ZW-a)^m,  m=min(r,s).

This is a different basis change from the arithmetic U, but it acts on the SAME original G: G'=T_a G T_a^T, det G'=det G. The samples, ordinary derivatives, and factor-two trace pairing are unchanged. Individual row norms and Hadamard diagonal factors ARE permitted to change. The claimed gain is a uniform diagonal bound, not a pointwise shrinking of every jet.

The checked radial estimate includes the origin, rounding, ordinary-derivative correction and point-count guards; rows r>=9S earn the squared factor (13/20)^(2s). Summing the log savings over eligible rows gives

    (R-9S)*S*(S-1)*log(20/13),

when R>=9S (otherwise the eligible set is empty). Hadamard then bounds this SAME determinant from above. Its arithmetic prime powers, along with positivity, bound the SAME determinant from below. The final normalized comparison, with all radius/aspect and field guards already discharged in the existing theorem, is

    0.999997 log(d)-5.739 <= log(det G)/(R^2*S)
                           <= 0.8 log(d)-0.823.

At d>=48,000,000,000, log(d)>=24.5813 gives a gap at least 0.0001862561 between the left and right scalars, a contradiction. The odd chart has |Delta_K|=d. The even chart has |Delta_K|=4d; its separate small-radicand argument and arbitrary-field equivalence are necessary and present in the existing proof. This audit does NOT assert those analytic/field lemmas have been independently reproved here.

## Transport and non-transport ledger

| Operation | Preserves | Changes or requires extra proof |
| --- | --- | --- |
| Field isomorphism | Actual field discriminant, ring-of-integers class number | Must construct equivalence, not just assert a quadratic generator |
| Selected maximal-order chart | Actual field after justified equivalence | Lattice index 2 in odd chart; actual discriminant 4d in even chart |
| Integral U or T with det=1 and both Gram sides | Integral row lattice, det G, prime factors, real rank/inertia | Individual rows, row norms, diagonal Hadamard product; not ordinary eigenvalues |
| Reduction mod p | G entries, det congruence, ranks of equivalent U-frames mod p | Absolute real rank may drop; repeated residues of distinct samples may NOT be deduplicated |
| Active translation of Q, fixed old monomials | Relative distances, point count | Original Gram may change: determinant 24->60 |
| Passive translation of points AND polynomials/jets | Original sampled jets, original Gram | Must move derivative/observable action compatibly: determinant 24->24 |
| Arbitrary hypercomplex/metric lift | Nothing automatically | Need typed algebra homomorphisms, faithful integer recovery and a determinant-preserving diagram |

### Verification is not reconstruction

- The frozen earlier 173-module inventory is not the present 202-module source. The inspected main review directory did not yield a completed Argon report; the user's described stop/failure is preserved as a separately reported obligation, not rewritten as success.
- Phase121 reports 202 imported reachable modules, 5,584 logical declarations, 4,772 theorems, 17,029 runtime auxiliaries, with only three standard Lean axioms. The current main HEAD also had two successful GitHub Actions runs. These confirm scope/versioned formal checks, **not independent human verification of the mathematical bridge**.
- The adjacent finite integer oracle is an independent CODE PATH, not an independent MATHEMATICIAN, and checks only the specified small cases. It must not be relabeled as closure of Argon's review.
- The user-described failed 47.5-billion attempt is not modified or retried. The present review did not locate its exact source-and-result receipt; no result for that attempt is invented.

**Smallest genuine open review obligation:** a mathematician must reconstruct the field maximal-order to inert-prime implication, the actual-jet U/P/K construction, and the same-G Hadamard comparison, checking every guard and index without relying on Lean's printed theorem names. An improved constant or a radial composition law is optional only after that succeeds.

**Source map:** IntegerTraceGram; RectangularBasisMatrix; RectangularRowAction; JetPower; InertFrobenius; RectangularGramFactor; GramDivisibility; RectangularValuation; ClassNumberInertBridge; QuadraticFieldChart; RadialOperator; RadialDetBound; RadialCutoff (all in lean/TenthDiscriminant). Current proof guide: FORTY_EIGHT_BILLION_GUIDE.md; field statement: lean/FORMALIZATION.md; integration record: PHASE121_VERIFICATION.md.
