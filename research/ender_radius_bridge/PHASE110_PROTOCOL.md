# Phase110: passive polynomial, ordinary-jet and arithmetic-Gram transport

Base08bcddc72502b738f1ef19081c7a0e2ca9988542. Register before source or
Lean invocation. PR38 merged6c7e94c, exact source14b5446 passed full pinned
CI40718714733. This new target mechanizes the NEW semantic interface
identified by the user's transport/hardness question. It is not a replay
of105active-point shifts or stopped69/75targets. No new cutoff or
computational-hardness claim.

Four definitions, formulas frozen at first invocation:
translate a b F = outer Polynomial.taylor(C(-a)) of F.map(inner
(taylorAlgHom(-b)).toRingHom), for any CommRingA. This is the actual
bivariate polynomial F(Z-a,W-b), not a pre-defined shifted derivative row.
polynomialJet F j z = ordinary jth Z derivative of specializeF(conjz),
evaluated atz (Complex). W is independent during differentiation.
monomialRow r s = C(X^s)*X^r in Complex[W][Z].
polynomialGram P J F = original2*sumj<J sumz inP Re(jetFi*conj(jetFk)),
as real matrix indexed by Fin n; actual distinct shifted sample set used.

Sixteen main public theorem types: translate_zero,translate_add,
translate_inverse,translate_map(naturality for CommRing homomorphism),
derivative_translate,iterate_derivative_translate,specialize_translate,
jet_covariance(generic CommRing ordinary iterated derivatives at(w+b,z+a)),
conjugate_jet_covariance,monomial_jet_eq,transported_lattice_jet,
polynomialGram_translation,monomial_gram_eq,passive_integer_cast,
passive_det_cast,passive_translation_bridge.
The last constructs the same original integer Gram G fromQ,D,J,R,S and
polynomial Gram H at actual shifted lattice points with transported
monomial observables; proves H=G.cast, H.PosDef,0<G.det and the existing
p^(2*valuationWeight R S p) divisor ofG.det. Only original positivity/
count/depth/odd-prime/nonsquare guards; no supplied compatibility, jet
injectivity, real/complex matrix identity, determinant or divisibility.
transported_lattice_jet identifies actual differentiated transported
monomials with pairEval of ORIGINAL integerDerivativeRow at the old point.

Four fixed controls: passive24 versus active60 using same three points
D1,J1,R2,S1,vertical shift; real/complex rank distinction real det4 versus
explicit Hermitian det0; ordinary third derivative6!=1; W held fixed
(j1=0 and j0=1 at1+i for transportedW). Controls may reuse the existing
checked active counterexample, but fresh main roots must exclude it.
All20full public types/control data and four complete definition bodies
frozen at first run. Max2 proof-only repairs, private proof lemmas may be
added; no new data definitions/weaker types. Keep factor2,row order,
ordinary derivatives,W-held-fixed,point multiplicity,integer witness exact.

Three fresh closures: jet_covariance,passive_integer_cast,
passive_translation_bridge. Exactly58excluded roots from104 PLUS3EvenTwoClass
cutoffs,4EvenFieldTwoClass cutoffs,CoordinateTranslation.coordinate_translation_bridge,
shifted_gram_cast,shifted_posDef,shifted_valuation,shifted_gram_counterexample
(70total). Standard propext/Classical.choice/Quot.sound only; all20types,
four definitions,namespaceaudit and three root axioms printed; unresolved/
unsafe/forbidden roots rejected. Existing derivative-row/polynomial and
integer-cast/count/Frobenius lemmas allowed; no class-number assumption or
cutoff theorem used. Generic commutative-ring transport does NOT assert
jet separation/positive definiteness in finite characteristic.

Max3full standalone600s/8192MB perownedprocess,1200s cumulative. Stop any
internal/outer resource stop; no probes,replay,weaker target or changed
heartbeat/recursion/resource limits. Preserve all source/stdout/stderr/
result perrun,including failures and exact repairs. No standalone105replay.
Freeze production/root/tools/pins/CI,earlier protocols/raw/verifiers/reviews/
ledgers/certificates/failures. No rootbuild/wholeaudit/integration/publication/
CI/reviewer/Taopost here. Update current README61/STATUS/FORMALIZATION/
objectiveledger61/reply and a short human guide; save exact evidence verifier.
