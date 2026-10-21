Model: GPT-6.1 Sol (identification supplied by the user; exact runtime version not independently exposed).

# Phase 1 — blind referee report

Date: 2026-10-21. This report is frozen before reading repository content. Absolute repository root: `/home/runner/work/tenth-discriminant/tenth-discriminant`.

## Access record and limitations

**Exact list of repository files opened: empty.** No STATUS, LEDGER, REVIEW_BRIEF, tools, ledger directory, or git history was opened. The present file is the first repository file written. Shell commands checked installed executables/modules only.

The claimed Green paper, https://hexagonmath.org/pdf/2610.00311v2, could not be fetched: DNS lookup failure. **CANNOT-VERIFY** its Lemmas 3.1 and 5.1, their hypotheses, numbering, and page references. In particular, I will not pretend that reconstructing a possible Gram matrix verifies the actual paper.

The requested Tao posts and arXiv API could not be fetched, also because of DNS failures. An initial web search failed with HTTP 504; a subsequent search returned links but not primary-source lemma text or identifiable comment excerpts. Those summaries are not mathematical evidence.

## B1 — discriminants, representations, and a counting bound

Interpret “disc” as the fundamental discriminant of the maximal order of an imaginary quadratic field. An assertion about nonmaximal orders requires separate hypotheses.

Write the discriminant as -d, d > 8. Every nonreal algebraic integer has imaginary part of absolute value at least sqrt(d)/2, hence norm at least d/4. If a rational prime p ramifies and the class number is one, its prime ideal is principal, say (alpha), and N(alpha)=p. A real algebraic integer in an imaginary quadratic field is a rational integer, whose norm is a square. Thus alpha is nonreal, so p >= d/4.

If there are at least two ramified rational primes, take the smallest p. For an odd fundamental discriminant, d is squarefree, and d/p is an odd integer at least 5, so p < d/4. For an even fundamental discriminant with d>8, the smallest ramified prime is 2 and d >= 12, so 2 < d/4. Both contradict the preceding norm bound. A negative fundamental discriminant with a single ramified rational prime is -4, -8, or -D with D prime and D=3 mod 4: this follows directly from the classification of fundamental discriminants as squarefree delta=1 mod 4, or delta=4m with squarefree m=2,3 mod 4. Consequently d>8 forces d=D prime.

If D=7 mod 8, the defining polynomial of omega=(1+sqrt(-D))/2 is X^2-X+(D+1)/4 and reduces modulo 2 to X(X-1). Thus 2 splits. Principality would give norm 2; the bound D/4 <= 2 forces D<=8. Therefore D>7 forces D=3 mod 8.

For an unramified split prime p, its two distinct prime ideals of norm p are principal. Each has exactly two generators of norm p, because the only units for D>8 are ±1. These four generators are distinct: a shared generator would give the same ideal. Conversely, an element of norm p generates one of those two ideals. In the integral basis 1,omega, its norm is

    Q(x,y) = x^2+xy+((D+1)/4)y^2
           = (x+y/2)^2 + D*y^2/4.

There are therefore exactly four integer pairs representing p. None has y=0, since a prime is not an integer square. If y is odd, |x+y/2| >= 1/2; if y is even and nonzero, |y|>=2. Hence every such p >= (D+1)/4.

Put Y=floor(2*sqrt(t/D)). Pairing (x,y) with (-x,-y) and using four representations per split prime gives

    pi_split(t) <= (1/2) sum_{y=1}^Y (2 sqrt(t-D*y^2/4)+1)
                <= pi*t/(2 sqrt(D)) + Y/2
                <= pi*t/(2 sqrt(D)) + sqrt(t/D).

The second inequality uses that the decreasing nonnegative summand sqrt(t-D*y^2/4) has right-endpoint sum at most its integral from 0 to 2 sqrt(t/D); substitution y=2 sqrt(t/D) sin(theta) evaluates that integral as pi*t/(2 sqrt(D)). For t<(D+1)/4 the count is zero. For D>163 and t at or above that cutoff, the displayed bound is <2t/sqrt(D), since pi/2+1/sqrt(t)<2.

These are independent derivations, not appeals to the class-number-one classification. The algebraic ideal/norm correspondence and description of quadratic integer rings are used as foundational facts; primary-source page citations for them are **CANNOT-VERIFY** in this environment.

## B2 — zero counting and the change of coordinates

Let the horizontal lines be distinct, with at most L points on each of M lines, over a characteristic-zero field. Factor from a nonzero polynomial F of total degree k all its horizontal line factors. Suppose q of the selected lines are factors, with multiplicities counted only once here. Removing their factors reduces the degree by at least q. On each remaining selected line the restriction is a nonzero polynomial of degree at most k-q. Thus the number of zero points is at most

    q*L + (M-q)*(k-q) <= k*(L+M).

This proves the proposed coarse zero bound. It does not, on its own, prove any assertion about a parameter J whose definition has not been supplied. To prove injectivity for polynomials of degree <=k from this estimate one needs n>k(L+M), with a strict inequality. Equality does not suffice. For example, a point set contained in y=0 has a nonzero degree-one vanishing polynomial y; a large value assigned to an unrelated parameter J cannot repair injectivity.

Over C the matrix of (x,y) -> (x+y sqrt(-D),x-y sqrt(-D)) is

    [1, sqrt(-D); 1, -sqrt(-D)]

and has determinant -2 sqrt(-D), which is nonzero. It preserves nonzeroness and total-degree bounds under substitution. On real inputs its second component is the conjugate of its first, but conjugation on all of C is not a complex-linear map. The two-variable substitution just displayed is complex-linear; those are different statements.

**GAP P1-1.** “Hence J >= L+M suffices” is not established from the information supplied, because J and the further determinant argument are unspecified. The zero count is proved above; the remaining uses of the product grid in the actual Lemma 3.1 are **CANNOT-VERIFY**, not certified absent.

## B3 — independent p-adic row calculation

For this calculation take any finite set Z in Z[sqrt(-D)], not necessarily a rectangle or ellipse. Set A_(r,s),z=z^r*bar(z)^s for 0<=r<R, 0<=s<S, and G=A*A^*, with * the conjugate transpose. Let p be odd and inert, so sqrt(-D)^p=-sqrt(-D) modulo p and z^p=bar(z) modulo p, including for negative integer coordinates.

For each index let i=min(floor(r/p),S-1-s). Replace that row of A, simultaneously, by the row of values of

    z^(r-p*i)*bar(z)^s*(z^p-bar(z))^i
      = sum_{j=0}^i (-1)^j binom(i,j) z^(r-p*j)*bar(z)^(s+j).

Every shifted index lies in the rectangle: r-p*j>=0, r-p*j<=r<R, and s+j<=s+i<=S-1. In an order with r increasing, all j>0 terms use an earlier r; the transformation matrix is triangular with diagonal 1. Each new row is divisible by p^i in the integer ring. Applying the transformation and its conjugate transpose to G proves

    v_p(det G) >= 2 sum_{r=0}^{R-1} sum_{s=0}^{S-1}
                           min(floor(r/p),S-1-s).

Here the valuation is the inert prime's normalized valuation; if det G is a rational integer it is the usual v_p. If the point set is invariant under conjugation then each entry of G is a rational algebraic integer and hence an integer. Arbitrary point sets need not give rational-integer entries, although the ideal-divisibility calculation still works. A zero determinant satisfies a divisibility statement but cannot be used for a nonzero determinant lower bound.

Thus negatives and the shape of the set do not affect this particular row calculation. Agreement with the precise G and hypotheses of Green's actual Lemma 5.1 remains **CANNOT-VERIFY**.

## B4 — determinant comparison, and what has not been derived

For the explicit Gram matrix in B3, let n=|Z| and |z|<=rho, rho>0. Each diagonal entry is <=n*rho^(2(r+s)). Hadamard gives, if the matrix is positive definite,

    log det G <= R*S*log n + R*S*(R+S-2)*log rho.

Writing F_(R,S)(p) for the double sum in B3, an integer nonzero determinant must satisfy

    2 sum_{p odd inert} F_(R,S)(p)*log p
       <= R*S*log n + R*S*(R+S-2)*log rho.                 (P1)

This is an independently derived necessary inequality, not the claimed improved Green upper bound. One must prove positive definiteness and control other primes before turning it into a contradiction.

For fixed S and R/p large, ignoring floor errors only as an asymptotic heuristic, put u=r/p. Then

    sum_{s=0}^{S-1} min(u,S-1-s)

grows linearly in u until u~S and then saturates at S(S-1)/2. For p much larger than R/S the leading unsaturated contribution is S*R^2/(2p), with truncation and floor corrections. Treating those corrections as uniformly negligible at p~R/S would be unjustified.

**GAP P1-2.** I have not derived the stronger archimedean determinant bound needed for a numerical D0, nor its optimizing parameters or its leading large-D constant. Green's source is unavailable, and the claim supplied does not define G, R, S, rho, or J sufficiently to recover that bound uniquely. I therefore report **CANNOT-VERIFY** a numerical threshold (including 200000), rather than invent one. There is no independent Phase 1 threshold or rigorous large-D asymptotic to compare in Phase 2. Equation (P1) is the exact comparison I independently obtained.

## B5 — circularity

The B1–B3 calculations above use neither L-functions, GRH, Siegel's theorem, ineffective constants, the Heegner/Baker/Stark classification, nor tables. This does not audit missing determinant estimates, the proposed residue sieve, Dusart's proof, or hidden inputs in the repository. A claim of no circularity for the complete argument would be premature.

## B6 — novelty and source searches

Requested direct targets:

* https://hexagonmath.org/pdf/2610.00311v2 — fetch failed, DNS.
* https://export.arxiv.org/api/query?search_query=au:Green+AND+all:Siegel&max_results=10 — fetch failed, DNS.
* https://terrytao.wordpress.com/2026/10/19/a-sketch-of-the-proof-of-non-existence-of-siegel-zeroes/ — fetch failed, DNS.
* https://terrytao.wordpress.com/2026/10/20/an-experimental-ai-math-challenge/ — fetch failed, DNS.

The successful search additionally suggested the longer October 20 URL https://terrytao.wordpress.com/2026/10/20/an-experimental-ai-math-challenge-using-tenth-discriminant-bounds-to-explore-arguments-ruling-out-siegel-zeroes/ . No primary content or comment permalink was verified. The search summary also conflated a hexagon identifier with an arXiv identifier; I do not adopt that conflation.

**GAP P1-3.** Novelty is **CANNOT-VERIFY**. No claim of priority, absence of an equivalent argument, or verified discussion in those threads is supported by these searches.

The attempted Dusart PDF URL ended in S0025-5718-99-01026-2 and failed DNS. Search suggested instead S0025-5718-99-01012-6, titled “The kth prime is greater than k(log k + log log k - 1) for k >= 2,” Math. Comp. 68 (1999), 411–415. Neither primary text was accessed; the numerical theta bound is **CANNOT-VERIFY**. This reference mismatch is an access-log correction, not a mathematical finding against the repository.

## Blind-stage disposition

No FATAL finding has been established. B1, the horizontal-line zero bound, the invertible substitution, the conditional row-divisibility calculation, and (P1) were re-derived. The actual Green lemmas, their stronger upper bound, a finite contradiction threshold, the sieve, Dusart's constant, and novelty were not verified. The GAP labels above describe missing verification/derivation in this review and the supplied abbreviated claim; they must not be confused with demonstrated gaps in a proof not yet read.
