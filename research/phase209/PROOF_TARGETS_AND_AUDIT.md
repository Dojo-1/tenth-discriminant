# Phase209 — divided-Frobenius depth and conditional 321^4 endpoint

> **Later status (10 November 2026):** This is the preserved **4 November preregistration and candidate analysis**. The subsequently checked [Phase267 actual-field theorem](../../lean/TenthDiscriminant/Phase267ActualField321.lean) proves the $321^4$ bound on the same original trace Gram; [focused](https://github.com/Dojo-1/tenth-discriminant/actions/runs/42820526500) and [whole-root](https://github.com/Dojo-1/tenth-discriminant/actions/runs/42820526708) CI passed at `4c3dc08`. Statements below about still-missing 321 bridges are **historical**, not current. Independent human review remains open.


**4 November 2026.** Three lines preregistered before this code: [operator #154](https://github.com/Dojo-1/tenth-discriminant/issues/154), [same-Gram column capacity #155](https://github.com/Dojo-1/tenth-discriminant/issues/155), and [321 threshold #156](https://github.com/Dojo-1/tenth-discriminant/issues/156). This draft is STACKED ON Phase208 PR #153, and does NOT change the integrated 322^4 field theorem. The uniform claims below are paper-level derivations, not fully formalized Lean proofs or independent human review.

## A — Exact original ordinary-jet depth [P-paper candidate]

Work in O_D=Z[u]/(u²+D), u-bar=-u. For an odd inert p, the already certified unimodular rectangular row is
$$
F_{r,s}(Z,W)=Z^{r-pk}W^s(Z^p-W)^k,\quad
k=\min(\lfloor r/p\rfloor,S-1-s).
$$
The extracted row factor p^k is ALREADY counted in the existing p=3,5 prime lower bound. Let A=Z[Z,W,T], with integral derivation
$$
\delta Z=1,\quad\delta W=0,\quad\delta T=Z^{p-1}.
$$
Substitution T=(Z^p-W)/p over Z[1/p] intertwines δ with the ORIGINAL ordinary derivative ∂Z holding W fixed. Inertness ensures q_p(z)=(z^p-bar(z))/p is an integer pair. Hence for EVERY ordinary j, including j>=p,
$$
p^{-k}\partial_Z^j F_{r,s}(z,\bar z)
=\delta^j(Z^{r-pk}W^sT^k)(z,\bar z,q_p(z)).
$$

Over Fp, the p-th iterate δ^p is a derivation by the p-binomial Leibniz rule. Its action on (Z,W,T) is (0,0,(p-1)!)=(0,0,-1), using Wilson. Therefore δ^p=-∂T modp and δ^(p²)=(-∂T)^p=0 modp. Back over Z, δ^(p²)(A)⊆pA. Apply this Z-linear operator repeatedly to get, for all f and all j,
$$
\boxed{\delta^j f\in p^{\lfloor j/p^2\rfloor}A.}
$$
Thus **every normalized original ordinary jet coordinate at depth j** has the new factor p^floor(j/p²) AFTER the old row p^k extraction. This is not a Hasse-derivative identity and is not a claim of literature novelty.

Finite tests in divided_derivation_probe.py check δ^p and δ^(p²) modulo p for 188 monomials and independently reconstruct normalized ordinary integer-pair derivatives at D19,p3 (j=9,18) and D23,p5 (j=25,50), including adjacent orders, plus the split D287,p3 failure. Generic proof remains a separate Lean obligation.

## B — EXACT original trace Gram, conjugate folding, and Cauchy–Binet [P-paper candidate]

The original IntegerTraceGram source uses an integer-pair jet evaluation and metric
$$
\langle (a,b),(c,d)\rangle_D=2(ac+Dbd).
$$
For the original complete ellipse Q, conjugation preserves Q and the real integer row transformation. A nonreal conjugate pair contributes two identical real columns and two opposite imaginary columns, yielding exactly **one real column of metric weight 4** and **one imaginary column of weight 4D** in the unchanged Gram. A real sample gives one column of weight 2. Therefore with N=|Q| there are exactly N effective integral columns PER derivative order j, not 2N; old row matrix U is unimodular.

Writing the old transformed and normalized evaluation C, the SAME integer Gram satisfies
$$
UG_DU^\top=\Delta_p\,C W C^\top\Delta_p,\quad
\det U=1,\quad \Delta_p=\operatorname{diag}(p^{k_{r,s}}),
$$
where W is the integral diagonal folded trace metric. Every C column at derivative depth j is divisible by p^floor(j/p²). Weighted Cauchy–Binet has no denominators: each term is the square of an n×n integral minor multiplied by integer weights. Thus the NEW additional valuation is **twice** the minimum total selected column depth, beyond the old 2F_p, F_p=Σk.

Let n=RS, J=S and assume the original Gram has full row rank (the original interpolation guard guarantees n≤NJ). If n=qN+r, 0≤r<N,
$$
\boxed{
W_p=N\sum_{j=0}^{q-1}\lfloor j/p^2\rfloor+
r\lfloor q/p^2\rfloor,\qquad
v_p(\det G_D)\ge2F_p+2W_p.}
$$
For a simple uniform lower, floor(j/p²)≥j/p²−1, and the sum of derivative indices among the first n available N-column groups is at least n(n−N)/(2N), since the exact difference is r(N−r)/(2N)≥0. Therefore
$$
W_p\ge n\left(\frac{n-N}{2Np^2}-1\right),\quad
\boxed{\Delta_p\ge\log p\left(\frac{S}{Np^2}-\frac1{Rp^2}-\frac2R\right).}
$$
The fixed-p gain can be O(R²S) because the number of required columns forces derivative depth proportional to S. This is NOT the previously retired trick of simply adding j! to old row p^k: it is new post-normalization divisibility proved via δ.

In divided_derivation_probe.py, the complete D19,p3,Q31,J10 original transformed 8-row Gram matched its conjugate-folded construction ENTRYWISE (64 entries). Removing one conjugate point changes the Gram. The companion weighted_capacity_321.py checks the exact min-cost, layer-count and conservative inequalities in 9,790 independently enumerated bounded parameter cases. These are correlated finite tests, not a substitute for a general Lean source identity.

## C — conditional exact 321^4 scalar endpoint

The integrated 322^4 proof already provides, at its existing hypothesis floor,
$$
L_0=(999997/1000000)\log D-57193/10000+\log2/4
\le\log\det G_D/(R^2S)
\le U_0=(4/5)\log D-1853/2000.
$$
NO 321 theorem follows until ALL old geometry/positivity/source/analytic/field interfaces have been reproved below 322^4 on the same Qthin.

For x=D^(1/4)≥321, R=floor(D/4), S=floor(R/25), rho=ceil((11/25)x³), the already accepted source-exact lemma ellipsePairs_card_le_upper_count gives
$$
N\le \pi\rho^2/\sqrt D+2\rho+2\lfloor\rho/\sqrt D\rfloor+1.
$$
Using pi≤22/7, rho≤11x³/25+1 and dividing by D:
$$
N/D\le (22/7)(11/25+1/x³)^2+
22/(25x)+3/x^4+22/(25x³)+2/x^6
\le 0.611198687<31/50.
$$
The last bound is a rational inequality at x=321 since every reciprocal decreases. Elementary integer rounding yields R≥D/5 and S≥D/101, so S/N≥50/(31*101) and 1/R≤5/D.

With existing Lean lower logarithms log3≥1098/1000, log5≥1609/1000, log321≥57714/10000, log2≥6931/10000 and safe upper logs log3≤11/10, log5≤161/100, a fully rational uniform bonus candidate is
$$
\Delta_{\rm rat}=
(50/(31\cdot101))(1098/9000+1609/25000)
-(5/321^4)[(2+1/9)(11/10)+(2+1/25)(161/100)]
=0.002976043351\ldots
$$
and the baseline gap at 321 is at least -3092821/1250000000=-0.0024742568. Thus the **conditional** total normalized margin exceeds 1/2000=0.0005. The exact rational endpoint and an ABSTRACT no-overlap theorem are in Phase209Scalar321.lean; source-specific Lean theorem, 321 source geometry, and actual-field transport are still missing.

The previously accepted source cell covering buffer also stays positive at x=321:
$$
(11/25-(1001/1000)(407/1000))321-10=462353/1000000>0.
$$
This exact number does NOT by itself reprove the source positivity/interpolation count in Lean at the new floor.

## P/A/M/H/S/R evidence ledger

**P-paper candidate:** characteristic-p derivation nilpotence and uniform derivative depth, exact source conjugate folding, Cauchy–Binet minimum, geometric/cardinality and rational inequalities. **P-formal only if new scoped Lean passes:** arithmetic scalar bridge and buffer, NOT the main substantive source theorem. **M:** bounded integer, symmetry, polynomial, capacity and negative-control tests, subject to exact-head CI. **A:** hypotheses of the abstract conditional scalar interface must be discharged with original source lemmas, never silently. **H:** full integrated 321^4 field theorem; lowering the 322-domain upper, lower, positivity, log and class-number bridges. **R:** folding mere p² residue classes, adding raw column j! atop old row factors, treating a finite test or scalar certificate as a field theorem.

**Strict stop rules:** no new actual-field endpoint and no merge before operator source Lean, Gram folding, weighted minor bound, original ellipse geometry/positivity, analytic upper and p=3/5+binary lower at 321-domain, exact-head Lake audit, and independent human meaning review #50 and comparator #51. Preserve any failed proof as a counterworld rather than changing Q, the denominator R²S, derivative convention or original p-divisors.
