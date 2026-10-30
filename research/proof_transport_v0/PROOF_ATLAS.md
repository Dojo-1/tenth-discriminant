# The same mathematical object, several noncommuting accounts

**Scope:** research proof-transport pilot at the new draft branch; no new tenth-discriminant cutoff or independently reviewed proof. The existing actual-field 47.5-billion theorem, original Gram, previously recorded failure and PR #45/#46 remain unchanged.

## A mathematical argument in ordinary language

Fix positive integer D, original integer-pair observations Q, row-major 0<=r<R, 0<=s<S, and ordinary derivative orders 0<=j<J (W held constant). In the chosen quadratic *order* A=Z[t]/(t²+D), evaluate

    v_(r,s)(z,j) = (r)_j z^(r-j) conjugate(z)^s

and use the two integer coefficients of every v as columns of E. With one diagonal (2,2D) block per sample/derivative, B is integral and positive definite. The original integer matrix is **exactly**

    G = E B E^T = integerRectangularTraceGram Q D J R S.

The maximal order of the quadratic field is a *different* object when D=3 mod 4. Field discriminant -D and det(G) are not interchangeable.

For odd p with -D nonsquare mod p, the quadratic residue Frobenius gives z^p=conjugate(z) mod p. Put k_(r,s)=min(floor(r/p), S-1-s) and replace Z^rW^s with

    Z^(r-pk) W^s (Z^p-W)^k.

Expanding the last factor produces the explicit lower-unitriangular integer matrix U_p in the **original** rectangular row index. Every ordinary derivative of (Z^p-conjugate(z)) is divisible by p, so the higher product rule produces p^k in both integer coordinates of each transformed jet, at each *original* point. This constructs, rather than assumes, integer quotient columns:

    U_p E = Delta_p Ehat,  Delta_p = diag(p^k).

Thus, with K_p=Ehat B Ehat^T integral,

    U_p G U_p^T = Delta_p K_p Delta_p
    det(G) = p^(2F(p)) det(K_p), F(p)=sum_(r,s) k_(r,s).

Equivalently, the exterior row volume omega=e_1 wedge ... wedge e_(RS) has omega=p^F omega_hat. Weighted Cauchy-Binet gives detG as the squared norm of omega. The two-sided factor p^(2F) is not an arbitrary doubling; it is the square of the integral row-volume factor. The exterior argument does **not** construct Ehat: the ordinary-jet theorem does that work.

Now apply the existing radial frame T_a (for monomial row (r,s) it implements Z^(r-m) W^(s-m) (ZW-a)^m, m=min(r,s)). T_a is lower-unitriangular, and T_a T_b=T_(a+b). As with U_p, detT_a=1. Mixed frames **need not commute**, yet either L=T_a U_p or L'=U_p T_a yields a congruence transform of the *same G* with det(L G L^T)=det(L' G L'^T)=detG.

They preserve integer determinant and the original guarded inert-prime divisor. They do **not** preserve each diagonal entry, Hadamard's row-length ceiling, a fixed ambient metric under arbitrary coordinate shears, or real rank across reduction to ZMod p. A scalar equality of determinants is therefore not equality of transported frames.

### An exact noncommuting witness (small enough to check by hand)

Choose R=5, S=2, p=3, a=1 and row index 8=(r,s)=(4,0). Then U_p sends Z^4 to Z^4-ZW, while T_a sends ZW to ZW-1.

Applying U first and then T **as the matrix product T U**, the row-8 expression is Z^4-ZW (because T itself fixes row 8). In the opposite order U T, it is Z^4-ZW+1. Consequently:

    (T_1 U_3)[8,0]=0,      (U_3 T_1)[8,0]=1.

The two path matrices are distinct, both unitriangular. Their commutator is a legitimate algebraic holonomy observable; do not assert a Riemannian curvature theorem or topological classification from this finite matrix fact.

### A bounded numerical witness (not the production determinant)

Take D=19, Q the five integer pairs (x,0) with -2<=x<=2, R=5,S=J=2,p=3,a=1. It is a valid direct finite Gram, but its cardinality **does not satisfy** the published sufficient interpolation point-count condition. Direct exact determinant computation establishes its own positivity.

    det G            = 112717121716224
    F(3)             = 2
    3^(2F)           = 81
    det G / 81       = 1391569403904

Diagonal-product Hadamard ceilings for this same finite G:

    canonical G      = 13015635040576930578432000
    radial T G T^T   = 2306514694562388295680000
    T U  route       = 1673467584363003985920000
    U T  route       = 1664348262452655575040000

The difference is **not** a better global inequality. The toy observation family is not the huge production Q; no asymptotic implication is inferred.

## Back to Lean, one claim at a time

| Human obligation | Exact theorem in the inherited repository |
| --- | --- |
| Integer coordinates, original ordinary jets and metric | \`IntegerTraceGram.integerDerivativeRow\`, \`integerRectangularTraceGram_det_cast\` |
| Guarded Frobenius in the selected quadratic order | \`InertFrobenius.integerPair_frobenius_of_nonsquare\` |
| Binomial frame is integral and unimodular | \`RectangularBasisMatrix.rectangularBasisMatrix_det\` |
| The same matrix acts on the **actual** integer jets | \`RectangularRowAction.rectangularBasisMatrix_integerDerivativeRow_action\` |
| Integral quotient witnesses and shared pivot | \`RectangularGramFactor.rectangularTraceGram_basis_factor_of_frobenius\` |
| Exact exponent and determinant divisor | \`RectangularValuation.sum_rectangularBasisExponent\`, \`GramDivisibility.pow_dvd_det_of_unimodular_gram_factor\` |
| Actual radial frame, ordinary jets, same Gram | \`RadialOperator.gram_congruence\`, \`gram_det\` |
| Additive radial action, inverse and same sample Gram | \`RadialAction.matrix_add\`, \`matrix_neg\`, \`gram_add\` |
| **New:** either mixed-frame order preserves det(G) | \`ProofTransport.radial_arithmetic_same_gram_det\`, \`arithmetic_radial_same_gram_det\` |
| **New:** either mixed-frame order retains inert divisor | \`ProofTransport.radial_arithmetic_inert_divisor\`, \`arithmetic_radial_inert_divisor\` |
| **New:** order matters, with an exact two-entry control | \`ProofTransport.two_frame_noncommutation_control\` |
| Negative controls for split p and Hasse differentiation | \`ProofTransport.split_prime_frobenius_control\`; inherited \`JetPower.hasse_derivative_negative_control\` |

The global field bridge is elsewhere and remains unchanged: \`ClassNumberInertBridge\` supplies the guarded local condition from actual class number one; \`RadialCutoff\` supplies the SAME integer's analytic bounds, and \`EndpointCutoff.totallyComplex_degree_two_classNumber_one_discriminant_bound_47_5b\` states the complete actual-field theorem. The canonical classification uses its own 700-billion finite endgame.

**Mathematical survival at every transport:** \`source object -> actual operation -> destination -> named invariant -> guard -> failure control -> Lean declaration\`. Do not replace the arrows with a generic assertion of "equivalence".

## Ortho / Anti / Ambig: a prototype governance, not another numerical dimension

The 360×360 toroidal mesh is an address book for two loop directions; mathematical fibers over its cells are the different, typed local views. It is not a construction of 129,600 independent proof dimensions. A nonzero matrix commutator records path sensitivity and may serve as a research observable, but our **new** Lean theorems are only integer-frame invariance results.

- **Ortho:** compare arithmetic factorization, exterior-volume argument, Gram congruence and geometric Hadamard, with explicit distinct dependencies. Multiple expositions by the same assistant are still *correlated* witnesses.
- **Anti:** test split/ramified primes, derivative conventions, wrongly fixed ambient metric, and rank across different fields. A failing premise is an active boundary, not a failed desired theorem.
- **Ambig:** retain alternative frames, their guard sets, and unresolved \`[R]_formal\` obligations without a single combined score or auto-promotion.

To move from this pilot toward a better bound for Tao's challenge, the missing theorem has the precise shape

    forall D >= D0, suitable Q(D), R(D), S(D), a(D), ...
      log(det(original_G(D))) / (R(D)^2*S(D))
        <= old_upper(D) - delta(D)

with explicit \`delta(D)>0\` and source-level matching to the exact prime-mass lower bound. No such uniform improvement is established here. The mathematical bottleneck remains a better **uniform ordinary-jet majorant on the same determinant**, not an exotic holonomy word.

## Evidence and return paths

- **P (inherited):** source definitions and formalized theorems at \`ebf5743\`, supported by their recorded exact-head CI, subject to the stated semantic-review limitation.
- **H until CI:** new \`ProofTransport.lean\` theorems; code presence alone is no proof.
- **M only after Rust CI:** the bounded integer pilot. Its fixture was discovered before registration, so its successful reproduction is a regression result, not independent validation.
- **S/H:** toroidal/hyperbolic/Clifford governance and its proposed link to improved mathematical search.
- **[R]_formal:** independent human semantic reconstruction of the inherited analytic prime-mass/tail assumptions and complete theorem.
- **[R]_transport:** any proposed coordinate change with missing metric, integral quotient, or real-to-mod-p rank bridge.

A mathematician should be able to read the first two sections without Lean. A Lean reviewer should be able to open one named declaration for every essential step. Neither can be replaced by a visually persuasive controller or CI alone.
