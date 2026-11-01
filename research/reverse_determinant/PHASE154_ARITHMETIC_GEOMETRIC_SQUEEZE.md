# Phase154 — arithmetic meets geometry in the same determinant

**Canonical branch: main. Date: 1 November 2026.** [P-paper candidate] exact elementary bridge and explicit inequalities, pending independent mathematical reconstruction. [M] source-matched numerical/rational gates. [H] any new tenth-discriminant cutoff. [R] untransported triangular/Hasse or factorial "gains". This round does **not** replace the checked 47-billion actual-field bound or assert a Lean-verified 8b/5b theorem.

## The object

For odd squarefree D=3 (mod 4), put K=Q(sqrt(-D)) and m=(D+1)/4. Under the hypothetical class-number-one assumption every odd prime q<m is inert (the existing Lean ClassNumberInertBridge). Fix an inert **witness prime** p with p<m, and set R=p-1, S=J=floor(R/25), delta=sqrt(D+1)/2, A=sqrt(p sqrt(D)/3), rho=ceil(delta+A).

Use the ORIGINAL paired-integer ordinary partial-Z/W-held-fixed evaluation E_Q, not a Hasse, divided-power or transformed determinant, on Q={(x,y) in Z² : x²+Dy²<=rho², y>=0}; G_Q=E_Q B E_Q^T with B=diag(2,2D,...). The chosen witness p controls **rank and geometry**, while ALL odd mass primes q<R control valuations of the SAME positive integer determinant. The exterior-volume of E_Q at infinity and its q-primary divisors are two views of the same determinant line; this is an Arakelov-like interpretation, **not** a new arithmetic-intersection theorem.

## Frobenius rank plus covering (paper argument)

The lattice Z+i sqrt(D)Z has covolume sqrt(D) and covering radius delta. Its Voronoi cells give |Omega_D(rho)| >= pi (rho-delta)²/sqrt(D) >= (pi/3)p >p. If 2rho<p, all nodes and conjugates in Omega have distinct residues in the quadratic inert residue field.

On the characteristic-p Frobenius graph W=Z^p, the monomial section Z^rW^s restricts to T^(r+ps); R=p-1 makes all exponents distinct. For j<J<=p, ordinary partial-Z jets (W held fixed) agree with the first j ordinary T-derivatives because d(T^p)/dT=0 in characteristic p; j! is invertible for j<p. For each y>0 representative, its real/imag channels encode **both** conjugate roots. Hence a row kernel element would restrict to a nonzero polynomial of degree at most (R-1)+p(S-1)=pS-2 vanishing to order at least S at N=|Omega|>p distinct roots: contradiction. Thus E_Q has full rank over F_p and over Q. Since B is real positive definite, the SAME original G_Q is real positive definite and its integer determinant is positive.

The historical failure control p<R is still Z^p-W in the kernel of the graph-restriction map. The radius and residue-distinctness are essential, not decorative.

## The arithmetic/archimedean squeeze

The existing Lean theorem RadialCutoff.prime_mass_log_lower_of_det_pos applies to every support Q with positive integer det: under class number one and R<m,
  exactOddPrimeMass(R,S) <= log det G_Q.
The previously formalized chain puts the exact-source rawPrimeMassLower(R,S,FirstEnderInterval.tailBudget) below that prime mass. The source-head checked theorem RadialDetBound.integer_log_upper_of_posDef supplies the **inverse-free analytic upper** of the same original Gram when positivity is supplied independently; the older point-count guard was only sufficient, not necessary. The new Lean criterion RadialCutoff.classNumber_ne_one_of_posDef_budget_gap was committed in [85f8ce0](https://github.com/Dojo-1/tenth-discriminant/commit/85f8ce0f7e0eca7cf66b1cd3f73391c52101e863) to close the logical lower-vs-upper square, but its exact-head whole-root CI must be checked independently.

Write L for the rawPrimeMassLower and U=enderUpperB(R,S,S,rho,4D). Under D>=8b and p>5m/6, R>10^9, S>40m, 25S<=R<=26S, t=D^(1/4)>298. The exact source-normalized expressions give:

(1) Uniform lower: L/(R²S) >= log R - 4.411. A sufficient bound on all discarded terms is
  3/2 + 1/(10^9-1) + 15/30000 + 1.791 + (2*9893)/10^9 + ((25+25/(40m))/3)*0.134281 < 4.411.
This uses C=FAC+I-LIN<1.791, C_s=SQ+I<0.134281, ERR<9893, log(R-1)>=log R-1/(R-1), and log R<=sqrt R.

(2) Geometry: delta/A<1.9/t, 1/A<4/t³, so rho<=A(1+1/150). Similarly rho/R<1/200. A simple bounding-box count yields |Q|<=4D. In particular,
  log rho <= (1/4)log D+(1/2)log R-(1/2)log 3+1/150+1/(2R).

(3) Upper: using S/R<=1/25, rho<R and the displayed log-rho bound, plus a count and derivative-endpoint remainder <0.001,
  U/(R²S) <= 0.24 log D+0.56 log R-0.595.
The constants are deliberately conservative, with log3>1.09.

(4) Difference:
  (L-U)/(R²S) >= 0.44 log R - 0.24 log D - 3.816.

## Prime intervals: two distinct corridors

**Primary lighter input, Nagura (1952).** The classical prime interval theorem supplies p in (5m/6,m): apply the original (x,6x/5) interval theorem at x=5m/6>25. Hence log R>log D - log(24/5)-1e-6. For D>=8b, log D>22.8 and log(24/5)<1.57. The RHS in (4) exceeds
  0.2*22.8 - 0.44*1.57 - 3.816 - 1e-6 = 0.053199.
This is a complete **proposed paper-level exclusion argument** for odd fundamental D>=8b once the general rank, covering, source and external prime theorem steps have undergone independent semantic reconstruction. It is NOT yet a Lean field result.

**Stronger external input, Costa Pereira (1989), cited by Panaitopol (2001).** A prime exists in [x,258x/257) for x>=485492. Take x=257m/258. For D>=5b this supplies p>=257m/258 below m. Now t>265, delta/A<(7/4)/t, 1/A<4/t³, rho/R<(6/5)/t*(1+2/10^9)+3/t²+5/t⁴<1/200; the SAME L,U envelopes still hold. Since log R>log D-log(1032/257)-1e-6, log D>22.3 and log(1032/257)<1.4, (4) is >0.027999. This **5b candidate** adds an external number-theory input not reconstructed from the original primary proof, so its independent verification gate is strictly stronger. Do not silently replace Nagura with it.

## Finite controls and status

The verifier [phase154_prime_window_budget.py](phase154_prime_window_budget.py) runs the same original Lean-derived L/U functions as Phase153, with rational gates independent of sampled D and explicitly labelled *pseudo-prime endpoint probes*. At D=8,000,000,003 and p/m just above 5/6 it records L≈16.824122782, U≈16.762818927, gap≈+0.061303855; the Nagura-worst-ratio D5b control is negative (≈-0.033501013). The stronger Costa endpoint at D5b gives ≈+0.045628. These numbers do not themselves certify the universal field statements.

The same-source checks include full Phase144–153 regressions, earlier source-correspondence from Phase153, and exact rational constants. Existing field cutoff on main stays 47b until the Frobenius rank, covering lemma, uniform inequalities, external prime interval and final odd/even field bridge have been proven and independently reviewed. No equivalence to the rival 331 bound or claim of novel Arakelov theory is made.

**Provenance and prior art:** [Nagura, Proc. Japan Acad. 28 (1952), 177–181](https://doi.org/10.3792/pja/1195570997); [Costa Pereira, Acta Arithmetica 52 (1989), 307–337](https://doi.org/10.4064/aa-52-4-307-337); [Panaitopol, Notes Number Theory Discrete Math. 7(4) (2001), 111–114](https://nntdm.net/volume-07-2001/number-4/111-114/). Classical results are prior art; this source-specific synthesis has not been checked for novelty.
