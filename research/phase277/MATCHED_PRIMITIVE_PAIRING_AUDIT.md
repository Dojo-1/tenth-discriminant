# Phase277 — same-source primitive residual pairing, inert versus split

**11 November 2026. Status: [M] bounded exact computations; [P-paper] standard p-adic Smith/determinant identity; [H] extrapolation to large class-number-one production; no new Lean theorem.**

## Predeclared question and source

The user-facing Phase277 question was declared before the measurements: can the ORIGINAL production-shaped integer trace Gram have an additional primitive residual-pairing valuation after all known row/Frobenius and ordinary-jet factorial factors are counted **once**? Use a matched inert versus split control, not a surrogate matrix, a changed point set, or a pure real Gram.

The source is frozen at the already documented Phase206/208 specimen:

- Radicand D=403=13*31, D=3 (mod 4); this is a *squarefree radicand*, NOT asserted class number one.
- Complete support Q={(x,y) in Z^2: x^2+403*y^2 <= 40^2}, exactly |Q|=219.
- Original rectangular dimensions R=floor(D/4)=100, S=J=floor(R/25)=4.
- All rows (r,s) with 0<=r<100, 0<=s<4, ordinary derivatives d_Z^j (Z^r W^s), j=0,1,2,3, W HELD FIXED in differentiation.
- Both signed integer pair coordinates, so E is 400x1752 and the ORIGINAL trace metric is B=diag(2,806,2,806,...), not Euclidean diag(2,2).
- Matched primes: p=7 is **inert**, since (-403 mod 7)=3 is a nonsquare; p=11 is **split**, since (-403 mod 11)=4 is a nonzero square. Neither divides 2D. The Frobenius factor Z^p-W is therefore legally p-divisible for p=7 and ILLEGAL to divide out at p=11. A source witness at the latter prime is z=(-34,-1), giving (z^11-W) mod11=(0,9).
- Since every j<4<p, all j! are p-units at BOTH primes. No additional p-adic factorial valuation is available or double-counted.

No class-number-one assumption is made, and D=403 is far BELOW 321^4. This does **not** test the uniform theorem at the field-level threshold, but does test a necessary mechanism on an actual original-source Gram, not an invented surrogate.

## Typed decomposition and exact invariant

For a prime p not dividing 2D, let F_p be the sum of the old, already-proved Frobenius row exponents k(r,s)=min(floor(r/p),S-1-s) when inert. Set F_p=0 in the split control (no unjustified division). The old polynomial row change is integral and unimodular. After dividing those legally p-divisible rows, obtain C_0.

Now perform local Smith normalization *of C_0*, with unimodular row and column operations. Record the evaluation exponents a_i and obtain primitive C_prim of full rank mod p. Only THEN define the primitive residual trace pairing

  K_p=C_prim * B * C_prim^T.

With full row rank over Q_p and original integer trace B, the exact decomposition is

  v_p(det G)=2*F_p + 2*sum_i a_i + beta_p,
  beta_p=v_p(det K_p).

A unit from a unimodular row determinant does not change valuation. No factorial divisor is added separately. The source and the trace pairing remain unchanged.

**Important semantic distinction:** the radical of C_0 B C_0^T on the *first residue image* is NOT beta_p, and its dimension may vanish, emerge or change after evaluation-lattice saturation.

## Preregistered matched local controls: results

| Invariant | inert p=7 | split p=11 |
|---|---:|---:|
| F_p: old Frobenius row exponent sum | 530 | 0 |
| rank(C_0 mod p) | 331 | 132 |
| rank(C_0 B C_0^T mod p) | 305 | 132 |
| apparent restricted radical on first image | 26 | 0 |
| exact Smith exponents of C_0 | 0:331,1:5,2:4,3:23,4:37 | 0:132,1:66,2:44,3:44,4:44,5:44,6:26 |
| sum_i a_i: extra evaluation-lattice index | 230 | 838 |
| rank(C_prim mod p) | 400 | 400 |
| rank(K_p mod p) | 400 | 394 |
| primitive pairing Smith levels | 0:400 | 0:394,1:6 |
| beta_p | **0** | **6** |
| **exact v_p(det G)** | **1520** | **1682** |

Both exact determinant valuations come from exhaustive local Smith diagonalizations over sufficiently large p-power rings, plus the residual Gram Smith check through p^2. Neither uses floating-point acceptance, an invented determinant formula, or a class-number-one oracle.

At p=7, use precision 7^6 on the old-normalized source; maximum further Smith exponent is 4, leaving two reliable p-adic digits for the primitive Gram. At p=11, use precision 11^9 on the unnormalized original E; maximum exponent is 6, leaving three p-adic digits. Every original row operation is applied to a separate copy of the original source, while column operations are applied only to the working Smith matrix. Division is checked coordinatewise BEFORE each row is normalized. The final C_prim has full rank 400 mod p.

For p7, beta=0 because the primitive Gram is nondegenerate mod 7. For p11, the primitive Gram has exactly six elementary divisors of valuation one and **none of valuation >=2**, so beta=6. The resulting exact original determinant valuations are

  v7(det G)=2*(530+230)+0=1520,
  v11(det G)=2*(0+838)+6=1682.

This is a *finite measurement*, not a new asymptotic lower bound.

## Independent known-answer and hostile controls

- **Historical exact oracle:** D=19, R=8,S=J=4,rho=5,Q21, 32x168 original E is rebuilt with PURE PYTHON integer pair multiplication, and the actual 32x32 Gram determinant is computed using exact Bareiss elimination. Local Smith reconstruction matches the exact determinant valuations at p3 (inert: 39), p5 (split: 4), p7 (split: 0), reproducing prior Phase205 results without invoking the new D403 source builder.
- **Independent expansion:** one builder uses the binomial expansion of (Z^p-W)^k; the other uses an independently organized truncated dual-number convolution for selected first/middle/last original rows across ALL 219 points and BOTH channels. They share some arithmetic helpers and remain correlated model-authored controls, not independent human review.
- **Gauge stability:** row permutations preserve finite source ranks. A small Smith toy diag(1,p,p^2,1) preserves the levels under integral row and column shears.
- **Original metric sensitivity:** at p7 the actual trace B produces first-layer Gram rank 305, while the incorrect Euclidean B produces rank 303. Wrong-metric observations are intentionally not admitted.
- **Original ordinary j3:** removing the fourth jet drops the p7 source rank 331 -> 252 and the split p11 rank 132 -> 99. A Hasse/low-order replacement would change the source.
- **Invalid split division:** the split p11 Frobenius witness (0,9) mod11 prevents assigning the inert p11 k(r,s) factor.
- **p^2 truncation before saturation:** p7 levels (0:331,1:5,>=2:64), split p11 (0:132,1:66,>=2:202). The deeper bands are never falsely called exact level two.

The two GitHub source-check programs and a separate pure-Python exact reference are versioned with this note. Exact-head CI is **required before merging** and before reporting GitHub verification. Source/oracle checks are correlated; the known-answer D19 path supplies an independently derived integer determinant check.

## Falsification, interpretation and stop rule

**Retired [R]:** the proposed primitive residual bonus at inert p7 is NOT present. A first-residue-image radical of dimension 26 cannot be counted in addition to the evaluation index; after saturation the primitive residual beta7=0. Also retired is the claim that *inertness alone*, at finite production-shaped parameters, forces beta_p>0. Split p11 has beta11=6; the split example does not satisfy a class-number-one hypothesis.

**Strongest result [M]:** an exact finite p-adic decomposition of ONE 400x1752 original source at two matched primes, with correct original B and full saturations. At p7, all v7(det G) arises from the known Frobenius row factors and an additional **evaluation-lattice index**, not a primitive pairing determinant. At split p11, the primitive pairing contributes six.

**Still open [H]:** a uniform residual prime-mass gain for actual D>=321^4 under the formalized class-number-one hypotheses and SAME original thin ellipse/row-frame production source. Neither the p7 negative example nor the p11 split measurement settles it; D403 is far below that domain and its class-number-one premise is false. The huge production dimensions are computationally inaccessible to this finite matrix probe.

**Next bounded discriminant test:** at another small squarefree D with a different production row/ellipse profile, independently reproduce the same source normalization, using fixed inert/split primes and a control that changes D without changing its interpretation. A universal claim must be rejected if it fails at a permitted D; do not infer asymptotic nonvanishing from three examples.

**Explicit mathematical scaling gate:** to help the analytic Siegel-zero problem, prove a same-source, non-double-counted uniform sum of extra prime exponents large enough after normalizing by R^2 S to affect the conductor-scale log(D) coefficient. A fixed finite list of positive beta_p(D) cannot supply such a conclusion without an additional growing-depth theorem.

**Merge gate for this negative experiment:** the exact-head focused Python regression, whole-root CI, file scope, and an honest note of the negative result must pass. Integration of these finite controls does not satisfy independent analytic review issue #50 and must not be used to merge the separate 321^4 field-theorem PR #157.
