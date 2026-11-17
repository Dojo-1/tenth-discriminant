# Dedekind's quaternion field: relevance to the Tenth Discriminant Challenge

*17 November 2026 — a human-readable mathematical comparison, with explicit proof boundaries.*

## 1. The precise challenge

The field under study is an imaginary quadratic number field $E=\mathbb Q(\sqrt{-d})$, with $d>0$ squarefree. Write $\Delta_E$ for the **field discriminant** and $h_E$ for the class number. The research-branch Lean certificate currently establishes

$$
h_E=1 \quad\Longrightarrow\quad |\Delta_E|<313^4=9,597,924,961.
$$

See [Phase340: formal certificate](../phase340/VERIFIED_313.md). This is a checked internal bound, not a new classification or an independently accepted solution of the historical class-number-one problem. Public main remains unchanged.

## 2. Dedekind's field and the imaginary quadratic field are distinct

Dedekind's field is

$$
N=\mathbb Q\big(\sqrt{(2+\sqrt2)(3+\sqrt3)}\big).
$$

It is a **totally real Galois extension** with Galois group the quaternion group $Q_8$, and it is ramified only at 2 and 3. Its maximal abelian subfield is $\mathbb Q(\sqrt2,\sqrt3)$. See Peter Schmid, [Quaternion extensions with restricted ramification](https://www.impan.pl/shop/en/publication/transaction/download/product/83580), and [Quaternion lattices and quaternion fields](https://link.springer.com/article/10.1007/s00013-022-01816-z).

For a prime $p\nmid 6\Delta_E$, two independent-looking pieces of arithmetic data are available:

- The **Frobenius conjugacy class** $C_N(p)$ in $Q_8$, describing splitting in $N$.
- The **quadratic character** $\chi_E(p)=(\Delta_E/p)\in\{+1,-1\}$, describing whether $p$ splits or is inert in $E$.

The second character directly concerns the Tenth Discriminant Challenge. The first describes a fixed auxiliary number field; it does not by itself prove any property of $\Delta_E$.

## 3. A classical theorem gives a decisive negative control

**Proposition.** For every imaginary quadratic field $E$,

$$
N\cap E=\mathbb Q,
\qquad
\operatorname{Gal}(NE/\mathbb Q)\cong Q_8\times C_2.
$$

**Proof.** The intersection is a subfield of the quadratic field $E$, hence is either $\mathbb Q$ or $E$. The second possibility is impossible because $N$ is totally real and $E$ is imaginary. Both extensions are finite and Galois, so their compositum has direct-product Galois group. $\square$

**Consequence of Chebotarev.** If $C\subseteq Q_8$ is a conjugacy class and $\delta\in\{\pm1\}$, then the unramified primes satisfying

$$
C_N(p)=C,\qquad \chi_E(p)=\delta
$$

have natural density

$$
\boxed{\frac{|C|}{16}}.
$$

This follows from the standard Chebotarev density theorem for the degree-16 compositum; see [James Thorne's algebraic number theory notes](https://www.dpmms.cam.ac.uk/~jat58/antm2015/notes.pdf). It is a **paper-level application of classical theorems**, not a new Lean theorem.

For the singleton central classes $\{+1\}$ and $\{-1\}$, *each* quadratic splitting sign occurs with density $1/16$. For each two-element noncentral quaternion conjugacy class, *each* sign occurs with density $1/8$. Thus the quaternion sign **cannot, on its own, force splitting or inertness in the imaginary quadratic field**. Every combination occurs infinitely often for each fixed $E$.

This statement concerns asymptotic densities. It does not rule out a genuinely useful **effective** finite-prime estimate involving the discriminant $D=|\Delta_E|$, but such an estimate would have to be proved uniformly in $D$.

## 4. The moving frame that matters in the determinant proof

Let $G$ be the original integral Gram matrix of the ordinary-derivative evaluation system used in the discriminant argument. For an integral change-of-basis matrix $U$,

$$
G'=U^{\mathsf T}GU,
\qquad
\det G'=(\det U)^2\det G.
$$

If $U\in\mathrm{GL}_n(\mathbb Z)$, then $\det U=\pm1$ and the determinant and all of its prime-adic valuations are unchanged. That is a valid **unimodular change of integral basis**.

If $|\det U|>1$, the integral lattice has changed. Any change in determinant valuations must be accounted for by the corresponding index. In particular, moving from a nonmaximal order to maximal-order coordinates is not automatically a new divisor of the original Gram determinant.

This is the rigorous content of a moving frame that is relevant here: **which arithmetic quantities are invariant under legitimate changes of integral coordinates?** It is not a claim that a novel coordinate system removes a determinant obstruction or improves a discriminant bound.

## 5. What has been proved in Spin Woven Numbers

The [abstract quaternion shadow theorem](https://github.com/Dojo-1/spin-woven-numbers/blob/dev/SpinWoven/DedekindShadow.lean) identifies the quaternion products reachable from chosen prime conjugacy classes. The [moving-frame theorem](https://github.com/Dojo-1/spin-woven-numbers/blob/dev/SpinWoven/MovingFrameShadow.lean) establishes that this abstract reachability survives compatible invertible quaternion coordinate changes, including two successive changes. [SWN-25 verification](https://github.com/Dojo-1/spin-woven-numbers/actions/runs/44052792681) passed the Lean build, axiom audit and independent finite tests.

**That proof is about an abstract quaternion group.** It does not yet construct Dedekind's field inside Lean, identify the abstract classes with its actual Frobenius classes, or prove a new determinant valuation for the imaginary quadratic field.

## 6. The next necessary proof, if this is to advance the challenge

We need a new, nonredundant theorem of this form:

> Under explicit hypotheses on the imaginary quadratic field $E$, a verifiable arithmetic condition gives an additional prime-adic divisibility statement for the **same original ordinary-jet Gram determinant**, beyond the factors already proved, without double-counting any change of integral basis.

A successful bridge must specify which primes and which $E$, survive the Chebotarev negative control above, prove the extra divisibility in one compatible integral basis, and improve the established arithmetic-lower versus analytic-upper contradiction.

If no such theorem exists, the quaternion construction remains a useful **test of representation dependence and information loss**, but should not be credited with reducing the discriminant bound.

**Current evidence:** $313^4$ field theorem — Lean checked on the research branch; abstract quaternion moving-frame theorem — Lean checked; arithmetic Frobenius-to-original-Gram bridge — **open**.
