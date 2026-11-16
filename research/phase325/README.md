# Phase325 — Frobenius conjugacy classes of rational primes

**Branch:** `research/phase309-original-source-picard-minors`.
**Scope:** the conductor-125 ray-class fields `L/K` of
`K=Q(sqrt(-D))`, for `D=163,187,203`.
The Phase321/322/324 finite groups provide the coordinates;
standard class field and genus theory provide the interpretation as
Galois groups. These are different evidence layers.

## Arithmetic Frobenius and the two cases

For `p` a rational prime coprime to `5D`, let
`G=Gal(L/K)=Cl_125(K)` and
`H=Gal(L/Q)=G rtimes_sigma C2`. The action `sigma` is complex
conjugation on ray classes, **not** generally inversion.

If p splits in K, `(p)=P*bar(P)`, let `g=[P]` under the arithmetic
Artin map. The rational Frobenius conjugacy class is
`{g,sigma(g)}` (one element if fixed).

If p is inert, its rational Frobenius is in the nontrivial coset:
`Frob_p=g*sigma` for some `g in G`, with

```math
Frob_p^2=g\,\sigma(g)=[(p)]\in G.
```

The ray class `[(p)]` is the **square**, not the rational Frobenius
itself. Given `g`, conjugation by `h in G` transforms
`g*sigma` to `h*g*sigma(h)^{-1}*sigma`. Thus its conjugacy class
is determined by `g mod (1-sigma)G` and has size
`|(1-sigma)G|=|G|/|G^sigma|`. The squaring map on cosets factors
through the norm `g -> g*sigma(g)`.

## Exact finite group checks

| D | \u007cG\u007c | \u007cH\u007c | \u007cG^sigma\u007c | Size of one inert coset class | Classes per given Frobenius square |
|---|---:|---:|---:|---:|---:|
| 163 | 7500 | 15000 | 100 | 75 | 2 |
| 187 | 15000 | 30000 | 200 | 75 | 4 |
| 203 | 30000 | 60000 | 200 | 150 | 4 |

The norm image has exactly 50 elements: the signed rational units
modulo 125. The square of rational Frobenius does **not** identify
the complete rational Frobenius conjugacy class.

For `p=2`, all three quadratic fields have fundamental discriminant
`-D congruent 5 (mod 8)`, so 2 is inert. The signed rational ray
class of `(2)` has order 50, since 2 has order 100 modulo 125 and
`2^50=-1 (mod 125)`. Therefore

```math
\operatorname{ord}(Frob_2)=100,
\qquad f(2;L/Q)=100.
```

The numbers of primes above 2 in `L` are exactly 150, 300, 600,
respectively. These are algebraic consequences of Artin reciprocity
and the finite group arithmetic, not a computation of a defining
polynomial for L.

## Recovery of the *complete inert Frobenius class* using the
## maximal abelian quotient

There is a further mathematical observation: although the square loses
information, the **abelianization of H** retains enough information
to distinguish every conjugacy class in the nontrivial coset.

For an abelian G and involution sigma,
`H^ab = (G/(1-sigma)G) x C2`. Therefore
`|H^ab| = 2 |G^sigma|`, giving orders 200, 400, 400 in our fields.

Let `K_gen` denote the quadratic genus field of K. Standard quadratic
genus theory gives:

| D | K_gen | Degree of Q(zeta_125)*K_gen over Q |
|---|---|---:|
| 163 | Q(sqrt(-163)) | 200 |
| 187 | Q(sqrt(-11),sqrt(17)) | 400 |
| 203 | Q(sqrt(-7),sqrt(29)) | 400 |

The genus field lies in the Hilbert class field of K, which lies in
the ray class field L. The field `K(zeta_125)` lies in L since
its relative conductor divides `(125)`. Coprime discriminants
ensure that the genus fields are linearly disjoint from
`Q(zeta_125)` over Q.

Their composita have degrees equal to `|H^ab|`, so they are the
**maximal abelian subfields of L over Q**.

On the coset `G*sigma`, the quotient `H -> H^ab` is injective
*on conjugacy classes*. Hence, for **inert** unramified p, the full
Frobenius conjugacy class is uniquely labelled by the abelian
characters of `Q(zeta_125)*K_gen`:

- **D163:** `p modulo 125`, given the already-known inert sign
  `(-163/p)=-1`.
- **D187:** `(p modulo 125, (17/p))`, given `(-187/p)=-1`.
- **D203:** `(p modulo 125, (29/p))`, given `(-203/p)=-1`.

Here `(d/p)` is the Kronecker symbol, so the labels include p=2.
This gives an explicit *conjugacy-class label*, not automatically a
coordinate representative `g` in Phase322's selected generators.

**Exact finite discriminating witnesses:**
- D163: inert p=2 and 127 have the same label `(2)`, hence the
  same rational Frobenius conjugacy class.
- D187: inert p=2 and 2377 have the same rational residue class 2
  modulo 125, hence the same `[(p)]) square, but their real genus
  signs `(17/p)` are +1 and -1; they lie in distinct conjugacy classes.
- D203: inert p=2 and 3877 similarly have residue 2 modulo 125,
  but genus signs `(29/p)` are -1 and +1; the classes differ.

The program checks primality, splitting signs and finite degree
identities. The underlying identification with the maximal abelian
subfield is a **mathematical class-field-theoretic deduction**, not a
Lean theorem or a computational reconstruction of L.

These labels classify **inert** Frobenius classes. For split primes,
the abelian quotient in general loses the distinction between classes
`{g,sigma(g)}`; the ideal-aware Phase321 coordinates remain needed.

## Exact local Artin polynomials, without a global Euler product

For an induced two-dimensional irreducible representation
`pi_chi=Ind_G^H(chi)` with `chi != chi circ sigma`, define

```math
P_{p,\chi}(T)=\det(1-T\pi_\chi(Frob_p)).
```

For unramified split p, with `g=[P]`,

```math
P_{p,\chi}(T)
=(1-\chi(g)T)(1-\chi(\sigma(g))T).
```

For unramified inert p,

```math
\operatorname{Tr}(\pi_\chi(Frob_p))=0,\quad
\pi_\chi(Frob_p)^2=\chi([(p)])I_2,\quad
P_{p,\chi}(T)=1-\chi([(p)])T^2.
```

These are local characteristic-polynomial identities and are checked
using *exact modular rational character phases*, not complex floats.
The inert polynomial is independent of which of the 2 or 4
square-compatible conjugacy classes actually occurs.

Do **not** upgrade these identities to a global L-value estimate,
a zero-free region, a uniform Chebotarev error, a same-Gram valuation
gain, or a 315^4 discriminant theorem. Each would require an
additional theorem with appropriate quantifiers and evidence.

## Files and verification

- `frobenius_conjugacy.py`: finite conjugacy classes of the nontrivial
  coset, square-fiber counts and split/inert local phase checks.
- `test_frobenius_conjugacy.py`: adversarial exact tests.
- `abelian_frobenius_labels.py`: inert congruence/genus labels.
- `test_abelian_frobenius_labels.py`: exact primality, Kronecker and
  degree-matching controls.
- `.github/workflows/phase325-frobenius.yml`: focused CI.

Reference mathematics:
- J.S. Milne, *Class Field Theory* (Frobenius and reciprocity):
  https://webusers.imj-prg.fr/~christophe.cornut/M2/Ref/Milne_CFT.pdf
- Number-theoretic genus fields and class-number-two examples:
  https://www.kurims.kyoto-u.ac.jp/~kyodo/kokyuroku/contents/pdf/0971-2.pdf
- Artin local determinant factors:
  https://kskedlaya.org/ant/chap-artin.html
