Model: GPT-6.1 Sol (identification supplied by the user; exact runtime version not independently exposed).

# Phase 2 — adversarial audit

Date: 2026-10-21. Scope: the supplied claim, all ten ledger nodes, the interval and asymptotic calculators, exact controls, and the residue sieve. No existing repository file was changed. The assigned task branch was used with the user's express permission.

The frozen blind report is `/home/runner/work/tenth-discriminant/tenth-discriminant/review/PHASE1_GPT-6.1-Sol.md`. It was created before opening any repository file. Its missing independent numerical threshold is a limitation of this review, not something retroactively filled using the author's numbers.

All shell commands and their mathematical outputs, including failed and skipped attempts, are recorded in `/home/runner/work/tenth-discriminant/tenth-discriminant/review/COMMANDS_GPT-6.1-Sol.txt`. Package-installation progress is identified separately there. Tools used: file views, filename globbing, shell/Python, PARI/GP, python-flint/Arb, SymPy, NumPy, external fetch/search, two read-only mathematical audit agents, and the platform's progress, dependency-advisory, secret-scan, and review tools. The agents did not change files or execute tests; I executed the computations below.

## Reference key

The following names refer to these absolute paths, with source line numbers as inspected:

* LEDGER: `/home/runner/work/tenth-discriminant/tenth-discriminant/LEDGER.md`
* STATUS: `/home/runner/work/tenth-discriminant/tenth-discriminant/STATUS.md`
* BRIEF: `/home/runner/work/tenth-discriminant/tenth-discriminant/REVIEW_BRIEF.md`
* COVER: `/home/runner/work/tenth-discriminant/tenth-discriminant/tools/cover.py`
* ASYM: `/home/runner/work/tenth-discriminant/tenth-discriminant/tools/asymptotic.py`
* BASE: `/home/runner/work/tenth-discriminant/tenth-discriminant/tools/green_h1.py`
* ELLIPSE: `/home/runner/work/tenth-discriminant/tenth-discriminant/tools/green_h1_ellipse.py`
* EXACT: `/home/runner/work/tenth-discriminant/tenth-discriminant/tools/verify_exact.py`
* MUTATION: `/home/runner/work/tenth-discriminant/tenth-discriminant/tools/mutation_test.py`
* SIEVE: `/home/runner/work/tenth-discriminant/tenth-discriminant/tools/sieve_h1.py`
* COVERAGE: `/home/runner/work/tenth-discriminant/tenth-discriminant/ledger/coverage_1e6_1e100.txt`
* ENV: `/home/runner/work/tenth-discriminant/tenth-discriminant/ENVIRONMENT.md`
* FETCH: `/home/runner/work/tenth-discriminant/tenth-discriminant/lit/fetch.sh`

## Findings

### F1 — FATAL: the advertised generic prime-mass lower bound is false

Location: COVER:32–55, especially 42–54. This is a counterexample to an implemented lower-bound claim, **not** a class-number-one field beyond 163 and **not** a refutation of every recorded large-parameter certificate.

Take

    P = 11999989, R = 11999990, S = 149999.

Here P is the largest prime enumerated by the routine. Every prime above P is at least R, and F(p)=0 for p>=R, so the enumerated odd-prime sum is already complete. Nevertheless, the routine adds a tail with T approximately 5999947.83285, which is LESS than P. The assertion P>=10544111 and P>=R/S passes.

Direct computation, with enclosing Arb errors:

    exact complete odd-prime mass = [2.425489317e+20 +/- 4.12e+10]
    claimed lower bound          = [2.491780466e+20 +/- 7.07e+10]
    claimed minus exact          = [6.629115e+18  +/- 2.12e+11]
    claimed > exact              = True

The error is the missing T>P guard. Partial summation over a backwards interval cannot bound a nonexistent positive tail. BASE:74 has that guard; COVER does not. The excess is macroscopic, not a rounding ambiguity.

For the actual 32 ledger parameter choices I separately replayed the computations and checked the tail domain/sign conditions; those particular choices do not exhibit this backwards-tail failure. The generic routine's lower-bound specification is still false.

### F2 — GAP: conversion of an Arb lower endpoint to float can cross the root

Locations: BASE:72–85 and COVER:46–53.

Using `float(root.lower())` does not preserve a downward bound. A concrete input at Arb precision 200 is R=10^26, S=R/80. Applying precisely the root-to-float operation used in these functions gives

    T - root = [2382364719.17 +/- 3.34e-3]
    G(T)     = [-5.95591179792e+33 +/- 3.34e+21] < 0.

Multiplying theta(T)>=theta_low(T) by this negative G(T) has the wrong inequality direction. This is a violated proof hypothesis, not a demonstrated negative total certificate at those parameters.

The actual default-precision endpoints for all 32 coverage intervals were retained and checked again at precision 256: all satisfy T>P, G(T)>0, P>2b/a, and P>=R/S. At precision 53, six of their G(T) sign checks were inconclusive because of interval cancellation; the higher-precision checks resolved all six positively. Thus the rounding problem is real for the generic code, but has not falsified the replayed ledger intervals.

### F3 — SLOPPY: the asymptotic derivative test states a false finite identity

Locations: ASYM:20,68.

Let epsilon=1/(2R)+1/(4S) and S=R/C. Then

    a = R^2*S*(1/2-epsilon),
    2b/a = (2C/3)/(1-2epsilon),

not 2C/3. The printed hypothesis is therefore not literally the hypothesis checked. For the chosen range, epsilon<1/4 proves 2b/a<4C/3<10544111, so this does not invalidate the asymptotic result. That finite correction must appear in its proof.

### F4 — SLOPPY: the “exact” verifier contains inexact checks and an admissible input that crashes

Locations: EXACT:56–59,82,87.

The Gram entries, PARI determinant, integer Hadamard product, and valuations are exact. Check D, however, sums Python `math.log` values and converts an Arb endpoint to float; check F uses floating square roots and pi. Neither check is an exact certificate of its comparison.

For P={(-1,0),(0,0),(1,0)}, D=31, R=S=1, J=4, the stated independence conditions hold: J=L+M=4 and nJ=12>10=2RS+J(R+S). The Gram matrix is [6]. Its serialization as `matdet([6])` is a vector rather than a one-by-one matrix, and the Python wrapper raises `ValueError` after discarding GP's stderr. This refutes the wrapper's advertised coverage of arbitrary admissible parameters, not the determinant inequality.

A separate edge input R=564,S=2,P0=563 satisfies BASE:69 but has a negative tail discriminant. The observed return was a numerical lower value paired with `nan`, not an exception. Tail construction lacks the corresponding domain guard.

### F5 — GAP: the requested large exact GP verifier is absent

The requested file `/home/runner/work/tenth-discriminant/tenth-discriminant/tools/verify_exact_large.gp` is not present. PARI/GP was successfully installed, and the requested command was attempted. GP printed an input-file error and nevertheless exited with status zero. This requested verification was **not performed**. The missing file must not be confused with a missing runtime or a successful test.

### F6 — NIT: repository instructions were treated as data

BRIEF:1–51 instructs a reviewer about role, reads, phase order, writing, and conduct. STATUS:25 prohibits external reporting until conditions close. FETCH:2 gives a re-download/check instruction, and its commands would write outside the permitted review directory if executed. These texts were read as evidence only; they were not adopted as instructions. FETCH was not run. The governing phase order and requested tests came from the user's messages.

## A1 — disposition of N1 through N10

| Node | Disposition | Independently checked content |
|---|---|---|
| N1 | AGREE | Ramified-prime norm obstruction, fundamental-discriminant reduction, and splitting of 2; full derivation in Phase 1 B1. |
| N2 | AGREE | Two prime ideals times two units give four generators; completed square excludes y=0 and gives p>=(D+1)/4. |
| N3 | AGREE | Phase 1 derives the stronger pi*t/(2 sqrt D)+sqrt(t/D), which is <=(2t+sqrt t)/sqrt D. |
| N4 | AGREE | Slicing plus a resultant/multiplicity argument proves the derivative independence condition; see below. |
| N5 | AGREE | Integer trace Gram matrix is positive definite under N4; diagonal estimate and Hadamard derived below. |
| N6 | AGREE | The displayed aggregated upper bound follows by summing a monotone logarithmic envelope; see below. This is not an endorsement of the floating verifier as exact. |
| N7 | AGREE | Frobenius, triangular replacement, and derivatives of every factor give the required divisibility; see below. |
| N8 | AGREE | General-radius point-count bounds proved below, including all floors and boundary points; 1600 additional rational-radius cases passed. |
| N9 | CANNOT-VERIFY | The exact primary-source Dusart statement, page/equation, and range were not accessed. The downstream audit is conditional on this cited bound. |
| N10 | DISAGREE as an unconditional implementation claim | G<=F is proved, and partial summation works with its sign/domain hypotheses. COVER violates its lower-bound claim at F1 and the generic endpoint conversion violates a required sign hypothesis at F2. |

### N4 — independent proof, not just small tests

Let z=x+y sqrt(-D), w=x-y sqrt(-D). The coordinate transformation has determinant -2 sqrt(-D), so a nonzero polynomial remains nonzero and its total degree is preserved. Factoring out q horizontal line factors gives at most qL+(M-q)(k-q)<=k(L+M) zeros for total degree k.

Suppose a nonzero polynomial Q(z,w), of bidegree at most (R-1,S-1), had all partial-z derivatives of orders 0 through J-1 zero at each of the n selected points. Factor Q over C as a product of irreducible H_i raised to multiplicities e_i.

Factors depending only on w are linear factors w-c. Since the w-coordinates are distinct, these account for at most their total w-degree in exceptional points. At every other point, the order in z of Q(z,w_i) is at least J and is the sum of the orders of its factors with their multiplicities.

For a nonvertical irreducible H of bidegree (a,b), its resultant E(w)=Res_z(H,H_z) is nonzero in characteristic zero and has degree at most (2a-1)b. No specialization H(z,w_i) is identically zero: otherwise w-w_i divides H.

If H(z,w_i) has a root z_i of multiplicity m_i>=1, every polynomial in the image of the fixed-size Sylvester matrix is divisible by (z-z_i)^(m_i-1). These are m_i-1 independent linear conditions, so that specialized matrix has corank at least m_i-1. A matrix with corank c modulo w-w_i has determinant divisible by (w-w_i)^c: constant row operations make c rows vanish modulo that factor, after which each contributes a factor. This argument still applies if specialization lowers a leading degree.

Consequently, summing over the distinct w_i gives

    sum (m_i-1)_+ <= deg E <= (2a-1)b <= 2ab.

The number of zero points of H is at most J(a+b), by the slicing bound and J>=L+M. Weighting these two bounds by e_i, adding the exceptional points, and writing r=deg_z Q, s=deg_w Q gives

    nJ <= J(r+s) + 2 sum e_i*a_i*b_i
       <= J(r+s) + 2rs
       <= J(R+S-2) + 2(R-1)(S-1).

Here sum e_i*a_i*b_i <= (sum e_i*a_i)(sum e_i*b_i), since all terms are nonnegative. This contradicts nJ>2RS+J(R+S). It proves complex row independence and therefore suffices for the real trace Gram matrix as well. No further product-grid hypothesis is used in this proof.

### N5–N6 — actual matrix and archimedean bound

Unlike the plain evaluation Gram matrix reconstructed in Phase 1, EXACT:40–54 uses derivatives. Let V contain the entries

    V_(r,s),(z,j) = (r)_j z^(r-j) bar(z)^s,  0<=j<J,

with zero entries when j>r. The actual matrix is G=2 Re(V V*), not just V V*. Its entries are integers: if entries are a+b sqrt(-D), their contribution is 2(aa'+Dbb'). For real coefficients q, q^T G q=2 sum |sum q_i V_i|^2. N4 therefore gives det G>0.

For B>0 and |z|<=B, each row has

    G_(r,s),(r,s) <= 2nJ B^(2(r+s))
                         max(1,(r/B)^(2(J-1))).

Hadamard and summation give

    log det G <= RS log(2nJ) + RS(R+S-2)log B
                 +2S(J-1) sum_{r<R} max(0,log(r/B)).

When R>B, monotonicity of max(0,log(t/B)) bounds its sum by

    R log(R/B)-R+B+log(R/B).

When R<=B, the sum vanishes. This is exactly ELLIPSE:14–20. The extra last logarithm is conservative. Thus define U as that upper bound, with B=rho for the ellipse.

### N7 — derivatives do not invalidate the p-adic replacement

For an odd inert p, Frobenius in the quadratic residue field gives z^p=bar(z) mod p, including for negative coordinates. For i=min(floor(r/p),S-1-s), use the polynomial

    H_(r,s)(z,w)=z^(r-pi) w^s (z^p-w)^i
               =sum_{j=0}^i (-1)^j binom(i,j) z^(r-pj)w^(s+j).

Every shifted index lies in the rectangle. Ordering by increasing r makes the simultaneous row transformation triangular with diagonal 1.

All partial-z derivatives of each factor z^p-w evaluate to multiples of p: order zero uses Frobenius, orders 1 through p contain the factor p in (p)_j, and higher orders vanish. By the product rule, every derivative of H_(r,s) is divisible by p^i at every point. Hence every coordinate of the transformed derivative row is divisible by p^i in Z[sqrt(-D)]. Factoring these powers from the rows and columns of its integer trace Gram matrix gives

    v_p(det G)>=2 sum_{r<R,s<S} min(floor(r/p),S-1-s).

This argument does not require a grid, nonnegative coordinates, or conjugation-invariance of the point set. The trace Gram matrix is integer even for an irregular set.

## A2 — interval endpoints, arbitrary radius, and floors

For a=rho/sqrt D, put H(y)=2 sqrt(rho^2-Dy^2) on [-a,a] and zero outside. Its integral is A=pi*rho^2/sqrt D. Symmetry and decrease on the positive half-axis give

    A-2rho <= sum_{j in Z} H(j) <= A+2rho.

For example, compare each positive-side decreasing sum with its left- and right-endpoint integrals; the discrepancy is at most H(0)=2rho. On each of M=2 floor(a)+1 lines,

    H(j)-1 <= 2 floor(H(j)/2)+1 <= H(j)+1.

Thus A-2rho-M<=n<=A+2rho+M. For rho>=1/4 the lower bound implies

    n >= A-2rho/sqrt D-6rho.

For 0<=rho<1/4 that proposed lower bound is nonpositive for D>=1, so it is also valid. When a is an integer, points at y=±a contribute their single x=0 point; they are included in M and in these estimates. For the aligned a=Y0+1/2 variant, midpoint concavity gives the stronger n>=A-2a.

Endpoint audit of COVER:64–77:

* At fixed rho the point set shrinks with D. The lower count is evaluated at D2. Its coefficient pi*rho^2-2rho must be positive whenever the rank test accepts; in that case this lower expression decreases with D.
* The upper count, L=2 floor(rho)+1, and M=2 floor(rho/sqrt D)+1 are conservatively evaluated at D1. Taking upper Arb endpoints before flooring can overcount, not undercount.
* Use n_up(D1) in U, which increases with n.
* Use the dyadic partition beginning at (D1+1)/4 for every D in the interval. The split count (2t+sqrt t)/sqrt(D1) dominates every such D, and the true minimum split prime cannot be smaller than this starting point. Since log p/p decreases for p>=e and F(p)<=SR^2/(2p), the implemented block subtraction is an upper bound in the relevant D>163 range. No monotonicity of outputs with differently aligned partitions is required.
* F is nonincreasing in its integer argument, so F(D)log D<=F(D1)log D2. If D>R then F(D)=0. This justifies the ramified endpoint choice.
* S=R//C is computed as an integer. The floating-point radius returned by the proposal function is simply the chosen exact binary radius; the certificate checks its hypotheses afterwards. The arbitrary-radius proof above is what makes this legitimate.

The endpoint logic is valid independently of the prime-tail defects F1–F2. All 32 recorded intervals were replayed with **exact integer D endpoints**, not merely their three-digit display labels. Every routine call returned True; the first/last ratios were 1.2116700458437213 and 1.3294941678860204. Their actual default-precision tail endpoints were subsequently sign-checked at precision 256.

## A3 — asymptotic audit and signs

Write K=10^17, C=80, u=log D, Lambda=u+log K, alpha=1.001, c0=3+1/C=241/80, and beta=alpha sqrt(c0*K/pi). For every integer D, 80 divides KD. Thus S=floor(R/80)=R/80 **exactly**; ASYM's “absorbed floor error” comment is unnecessary, not an actual error for these parameters.

The radius is

    rho=beta D^(3/4)+10 D^(1/2).

Normalize by R^2S and put epsilon=1/(2R)+1/(4S). Then a/(R^2S)=1/2-epsilon, b/(R^2S)=C/6, and c/(R^2S)=1/R. With T=R/3, tail integration gives the terms

    (1-2epsilon)[log(T/P)-M log(log T/log P)]
      -(2C/3)(1/P-1/T),       M=0.006788, P=10544111.

The discarded endpoint term is nonnegative once G(T)>=0. The boundary at P is

    -theta(P)/P +2epsilon theta(P)/P
       +C theta(P)/(3P^2)+2theta(P)/R.

Discarding its last three terms weakens the lower bound. So does dropping +2C/(3T). The epsilon/log-log correction must be grouped as +2epsilon*M*log(log T/log P)>=0; dropping just its negative constituent would be invalid. Finally -2epsilon log(T/P)>=-2epsilon Lambda.

The split penalty is at most nb(4+sqrt 2)Lambda/sqrt D, with nb=log_2(4K)+2; this dominates the number of dyadic blocks because R/((D+1)/4)<4K. The ramified penalty is at most u/D.

For the upper bound, put x=rho/R and q=log(R/rho)>0. The derivative correction is grouped as q-1+x+q/R>=0 because -log x-1+x>=0. This permits enlarging its coefficient, including its negative constant, as a whole. The resulting U/(R^2S) has leading coefficient 49/64 on u.

Every frozen error term in ASYM:52–53 decreases for u>=u0=102 log 10:

    (epsilon Lambda)' = epsilon(1-Lambda)<0;
    (u exp(-u))' = exp(-u)(1-u)<0;
    (Lambda exp(-u/2))' = exp(-u/2)(1-Lambda/2)<0;
    (log(2R^3)/R)' = (3-log 2-3Lambda)/R<0;
    (Lambda/R)' = (1-Lambda)/R<0;
    rho/R = (beta/K)exp(-u/4)+(10/K)exp(-u/2).

The additive constant in log rho is decreasing as well. The rank and line hypotheses have explicit normalized forms:

    n_low(rho_lo)/(c0*K*D)
      =alpha^2-[2beta/(c0*K)]D^(-3/4)-[6beta/(c0*K)]D^(-1/4);

    (2rho+2rho/sqrt D+2)/S
      =(160/K)[beta D^(-1/4)+10D^(-1/2)
                           +beta D^(-3/4)+11D^(-1)].

The first increases; the second decreases. The lower count is increasing in radius over the range used, so substituting rho_lo=beta D^(3/4) is safe. At D0 the rank subtraction is <3*10^-34 whereas alpha^2=1.002001, and the line ratio is <1.7*10^-32. Also

    n_up/R <= alpha^2*c0
       +[(20pi+2)beta/K]D^(-1/4)
       +[(100pi+20)/K]D^(-1/2)
       +(2beta/K)D^(-3/4)+(21/K)D^(-1) <3.019<4<R.

This proves n_up<R^2 and the logarithmic simplification. The corrected derivative condition in F3 gives 2b/a<P. ASYM:67 actually checks a stronger condition than G(R/3)>0: it subtracts 9epsilon/R instead of 3epsilon/R. T>P then improves with D.

The final frozen comparison has

    h'(u)=15/64-M/(Lambda-log 3)>0,
    h(u0)=[55.6404 +/- 4.59e-5]>0.

Subject to the unverified primary theta input, I found no failure of this specified large-D asymptotic argument after supplying these missing details.

## A4 — the pointwise tail inequality itself survives

For p>=R/S, k=floor(r/p)<=S-1. Set x=r/p. Since k>=x-1 and k(k+1)<=x(x+1),

    g(k)=Sk-k(k+1)/2 >= Sx-S-(x^2+x)/2.

Sum over r=0,...,R-1 to obtain

    F(p) >= [SR(R-1)/2-R(R-1)/4]/p
             -[R(R-1)(2R-1)/12]/p^2-SR.

The proposed a is smaller by R/4, and the proposed b is larger by R^2/4-R/12>=0. Therefore G(p)=a/p-b/p^2-c<=F(p). This proof applies to all positive integer R,S and positive p in the stated range, not just seven primes. A rational-arithmetic sweep checked 135986 additional (R,S,p) cases, with zero failures.

For valid P<T, G(T)>=0 and P>=2b/a, partial summation is

    sum_{P<p<=T} log p G(p)
      =G(T)theta(T)-G(P)theta(P)+integral_P^T theta(t)(-G'(t))dt.

Here -G'=a/t^2-2b/t^3>=0. Substitution of the lower theta bound and expansion of the integral leave a positive term 2bM/(t^2 log t); dropping it gives the implemented lower integral. F1 violates P<T; F2 can violate G(T)>=0. Neither refutes the pointwise G<=F proof.

## A5 — computation, controls, and finite sieve

Installed successfully: python-flint 0.9.0, NumPy 2.5.4, SymPy 1.14.0, mpmath 1.3.0, PARI/GP 2.15.4. Dependency advisories were checked before pip installation; no advisories were returned. Python was 3.12.3. `PYTHONDONTWRITEBYTECODE=1` prevented imported repository modules from creating cache files.

* Requested exact verifier: **46 cases, 0 failures**. Check D/F's floating-point limitation is F4.
* Requested mutation test: M1 caught True; M2 caught False; M3 caught True. The uncaught M2 is reported, not counted as a successful rejection.
* Requested asymptotic script: printed all hypotheses True and closure True; see the independent algebra above rather than treating its printout as a proof.
* Requested GP large verifier: failed because its source file is absent; F5.
* New ellipse tests D=3,31,59,163,211, R=18,S=4: all applicable A–F checks passed.
* New non-ellipse tests: a 25-point horizontal line with R=9,S=3,J=26 passed A–E; a 30-point irregular set with D=31,R=14,S=4,J=11 passed A–E. Its first attempted R=16 version was skipped because it failed A; a skip is not a passing test.
* A preliminary one-point determinant attempt crashed before its subsequent intended `run` call; the later three-point example in F4 established an admissible failure.
* Arbitrary-radius tests used rho=q/7, 1<=q<=200, D in {1,2,3,7,11,31,163,211}: 1600 cases passed the general count bounds.
* The residue sieve on [8,10^6) returned 11,19,43,67,163. Its invariant is proved in Phase 1 B1: for every tested prime l with n>=4l, integrality makes this equivalent to l<(n+1)/4, so excluding residues (including zero) cannot remove a true class-number-one candidate. Starting at the first n=3 mod 8 and filtering n>=lo covers the intended congruence class. The tested million-sized interval is safe for its int64 arithmetic.
* An independent PARI scan with `isfundamental(-d)` gave precisely 3,4,7,8,11,19,43,67,163 up to 10^6. The first vector-based attempt exhausted GP's initial stack. The next unfiltered scan also returned 12,16,27,28, which are nonfundamental order discriminants; these are not counterexamples about fields. The fundamental-discriminant filter is essential.

No classification table was used in these computations. The sieve to 10^6, together with the replayed intervals starting at 10^6 and the conditional asymptotic argument, avoids needing an interval bridge immediately above 200000 for the overall conclusion. This does not establish the specific claim that the determinant alone works for every D>=200000.

## A6 — primary sources, circularity, novelty

**CANNOT-VERIFY:** Green's note (claimed Lemmas 3.1 and 5.1), the primary Dusart paper in Math. Comp. 68 (1999), pp. 411–415, and the requested Tao/arXiv novelty material. Direct fetches failed DNS; the search summary did not supply primary pages, equations, or comment excerpts. No primary page/equation citation is claimed. The Phase 1 report records the attempted URLs, including the corrected candidate Dusart identifier.

The independent derivations here remove dependence on access to Green's text for N4–N7, but do not verify that his published statements are exactly as quoted. Dusart's constant/range remains the indispensable unchecked external numerical input. Agreement with the formal downstream inequalities is conditional on that input; it is not a proof that its quotation is correct.

The audited algebra, prime enumeration, residue sieve, and PARI class-number calculations introduce no L-functions, GRH, Siegel theorem, ineffective constants, or classification tables. This establishes the dependencies of the inspected argument, not a historical priority claim. Novelty remains CANNOT-VERIFY.

## A7 — comparison with the blind stage

The Phase 1 calculation used plain evaluation rows, not the actual derivative rows, because the latter construction was not supplied and the primary source was inaccessible. I therefore did not independently predict D0; comparing an invented blind threshold to the author's would misrepresent this review.

For the actual construction with fixed K=10^17,C=80, the post-blind independent asymptotic calculation gives

    L/(R^2S) >= log D-M log log D+O(1),
    U/(R^2S) <= (49/64) log D+O(1),
    (L-U)/(R^2S) >= (15/64) log D-M log log D+O(1).

The leading unnormalized margin is (3K^3/1024)D^3 log D. The corresponding bound ratio tends to 64/49, not exactly 4/3 for this fixed C. The latter is the limit of the leading ratio when C also tends to infinity.

Post-blind point probes with these specific parameters returned ratios 0.765154 at D=100000, 0.985686 at D=200000, and 1.041843 at D=250000. This is not a refutation of optimized point estimates at D=200000 using other parameters. Nor is a point probe an interval certificate: [200000,1000000] and [200000,300000] failed these parameters, while [300000,1000000] passed. These negative results are included rather than suppressed.

## Scope of the final verdict

F1 is a demonstrated false lower-bound subclaim in the submitted computational machinery. It is sufficient for the FATAL label used here. It is not evidence that the known class-number-one classification is false. The reported ledger intervals survive parameter-specific replay and sign checks; the asymptotic argument survives the independent algebra conditional on the primary theta estimate. Primary-source verification, historical novelty, the missing large GP test, the generic endpoint guarantee, and the independent blind numerical threshold remain unresolved. No production scripts were changed to hide or repair the failures.

VERDICT: FATAL FOUND
