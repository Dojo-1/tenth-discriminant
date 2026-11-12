# Phase282 — observed raw D403 modular ranks and their Hermite explanation

Recorded **after** the frozen [pre-registration](PRE_REGISTERED_RAW_HERMITE_RANK.md)
at \`d2e5b36\`. Executable source, fixed controls, and workflow were committed
at \`db06acc\`. The first [focused CI run 43190995784](https://github.com/Dojo-1/tenth-discriminant/actions/runs/43190995784)
**passed** on that implementation head. This note is post-result, not a
retrospective edit of the registered predictions.

## Precise finite result (M)

The original D403 trace source has R100, S=J4, the complete Q219 ellipse
rho40, rows \`Z^r W^s\` and ALL ordinary Z-derivatives (W fixed); E_raw has
400 rows and 1,752 original real/imag signed coordinate columns. There are
exactly three horizontal source layers y=-1,0,1, and each covers every x
residue modulo every tested prime. The metric B=(2,806) is **not used** in
this raw rank calculation and is not replaced by a Euclidean metric.

| p | type | effective ordinary jets t=min(p,4) | exact rank E_raw mod p | independent witness size | rank after forbidden j3 deletion |
|--:|--|--:|--:|--:|--:|
| 3 | inert | 3 | **27** | 27 (s=0) | 27 |
| 5 | inert | 4 | **60** | 60 (s=0) | 45 |
| 7 | inert | 4 | **84** | 84 (s=0) | 63 |
| 11 | split | 4 | **132** | 132 (split selectors) | 99 |

The source-blob hashes are asserted before calculation. Direct original
coordinate construction, independent exact integer ordinary-jet oracles,
truncated dual-number oracles, two modular rank algorithms, complete
ellipse/residue-class checks and explicit interpolation witnesses passed.
The j3 module vanishes at p3 because \`3!=0 mod3\`, but its legally
Frobenius-normalized p-adic quotient is a DIFFERENT object and can
recover nonzero information after dividing verified source factors.

## Paper-level proof (P-paper, not Lean; independently reviewable)

Set D=403, p in {3,5,7,11} and
\`A_p=F_p[u]/(u^2+D)\`. Each sample (x,y) gives
\`Z=x+yu,\ W=x-yu\` in A_p, and each ordinary jet is \`∂_Z^j\`
with W held constant. Taking coordinates in the Fp basis (1,u) is an
Fp-linear injection, even at a split prime because u^2+D defines an
etale two-dimensional algebra.

### Inert p = 3,5,7

Here \`u^p=-u\`, so every source node satisfies \`W=Z^p\`.
Substituting \`W=Z^p\` **after differentiation** commutes with the
ordinary Z derivative in characteristic p because \`∂_Z Z^p=0\`.
Thus the full original row \`Z^rW^s\` has exactly the same j-jet at
every source node as the univariate \`T^(r+ps)\` for every j<p.
All ordinary jets j>=p vanish identically, giving t=min(p,J).

The distinct residue nodes are
\`X_p={x+yu : x in Fp, y in {-1,0,1}}\`, of cardinality 3p.
Their monic vanishing polynomial is

\`Phi_p(T)=(T^p-T)*((T^p-T)^2+4D)\`,

because \`(x+yu)^p-(x+yu)=-2yu\`, hence the second factor vanishes
for y=±1 and the first for y=0. All 3p roots are distinct since
p is odd, p does not divide D, u is not in Fp and -1,0,1 are distinct.

For 0<=j<t<=p, the factorial j! is a unit in Fp. A univariate
polynomial f has vanishing ordinary jets through t-1 at every node
if and only if every node is a root of multiplicity at least t;
equivalently \`Phi_p^t | f\` over Fp. Therefore the kernel of all
original jets factors through the quotient \`Fp[T]/(Phi_p^t)\`,
which has dimension **3pt** over Fp. This proves the upper bound.
The original \`s=0, 0<=r<3pt\` rows include every monomial of degree
below 3pt because R=100>=3pt (27/60/84). Their evaluation is injective:
a nonzero polynomial of degree <3pt cannot be divisible by
\`Phi_p^t\`. This proves **rank(E_raw)=3pt**, not just a finite rank
coincidence.

### Split p=11

Pick the scalar component of the split algebra with \`u=2 mod11\`,
because \`2^2=-403 mod11\`. Original nodes satisfy \`z,w in F11\`
and \`w=z-2yu\`, y=-1,0,1, so they occupy three distinct affine lines,
each with all p=11 values of z. The other scalar component uses u=-2,
and its rows/ordinary jets are a permutation of the first component
under y↔-y; Q is symmetric in y. Therefore the entire two-coordinate
evaluation is determined by these **3pJ=132** scalar jet coordinates,
giving an upper bound.

Set \`T=Z^p-W\`. Since \`∂_Z(Z^p-W)=0\` identically in Fp[Z,W],
all its ordinary Z-derivatives of positive order vanish. On the
observed y-line, \`T(z,w)=2yu=c_y\`; the c_y are three distinct field
elements. Let \`L_y(T)\` denote the quadratic Lagrange polynomial with
\`L_y(c_z)=delta_(y,z)\`. Then each \`L_y(Z^p-W)\` selects exactly one
line for **every ordinary jet order**, without illegal differentiation
of W.

For each line, standard univariate Hermite interpolation at all
p distinct z values, with 0<=j<J=4<p, says that polynomials
\`H_y(Z)\` of degree < Jp=44 attain all desired scalar jet data.
Consequently the polynomials

\`F(Z,W)=sum_(y=-1,0,1) L_y(Z^p-W)*H_y(Z)\`

span all 3pJ scalar jet coordinates. The Z-degree of each term is
at most \`(2+J)*p-1=65 < R=100\`, and W-degree at most 2 < S=4.
So these are combinations of the **original rectangular rows**.
This proves the matching lower bound **rank(E_raw)=132**.

The regression explicitly expanded the 132 functions
\`L_y(Z^11-W)*Z^a\` (0<=a<44) into original (r,s) rows,
projected the original signed coordinates onto u=+2, checked that
off-line blocks were EXACTLY zero, and checked each on-line block
against every entry of the 44×44 ordinary Hermite confluent
Vandermonde. Both independent modular rank implementations reported
132; no generic-rank assumption was smuggled in.

## Boundary and prior-work accounting

- **The raw rank is not the Frobenius-normalized first grade.** Previously
  reported ranks of C0 modp are 90 at p3, 240 at p5 (Phase281), 331 at
  inert p7 (Phase277), and 132 at split p11. Dividing a source row
  by p^k is not an invertible mod-p frame change; it reveals deeper
  filtered information. Neither the raw rank nor these ratios determine
  the complete Smith index or primitive restricted pairing.
- **The old split p11 exact result remains prior work:** draft PR #167
  already recovered the *full* D403 p11 Smith index 838, primitive
  pairing residual 6 and exact v11(det original G)=1682.
- **A first-layer arithmetic bound is not a new proof gain.** If E has
  rational full row rank n, a raw modp rank r implies only
  \`v_p(det(E B E^T)) >= 2(n-r)\` for integral B via maximal minors;
  this is generally much weaker than the existing once-counted
  Frobenius and full Smith results. **Never add it** on top of
  those overlapping source factors.
- **No new class-number-one theorem:** D403 is intentionally outside
  the h=1 domain. These elementary finite-field rank arguments do not
  prove a uniform growing p-adic residual, improved D cutoff, or
  exclude a Landau–Siegel zero.
- **Independent human review remains open:** This is AI-authored
  paper-level algebra plus reproducible machine arithmetic. PR157's
  field-transport/analytic review #50 is not closed by this work.

## Next target, still H

Extend the collision-polynomial argument from first residue to the
\`p^k\` filtration **without changing the actual source**, with
explicit quotient/transport identities and a matched split negative
control. A genuine addition to the analytic lower bound would still
require a uniform, non-overlapping contribution after all existing
Frobenius/horizontal/factorial and evaluation-index terms are counted.
Do not reinterpret a first-grade rank identity as such a contribution.

**Merge gate:** exact-head focused regression, Markdown and whole-root
Lean/axiom/source audit must all pass. The mathematical rank theorem
is a paper-level reconstruction unless independently formalized.
