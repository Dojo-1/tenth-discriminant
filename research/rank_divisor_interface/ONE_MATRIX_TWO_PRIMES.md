# One observation matrix, two prime roles

**Phase134 preregistration, 30 October 2026.** [Issue #51](https://github.com/Dojo-1/tenth-discriminant/issues/51).
This is an elementary conditional matrix observation with a direct written
proof, not yet a Lean theorem or a result improving our 47.0-billion cutoff.
The starting point is the **unchanged** integer ordinary-jet observation
matrix E and its original positive diagonal trace metric B.

## Lemma: prime extraction forbids same-prime modular full rank

Let E be an n by m integer matrix, n<=m, and p a positive prime. Suppose

    U E = Delta Ehat,
    U in GL_n(Z), det U=+1 or -1,
    Delta=diag(p^k_1,...,p^k_n),  k_i>=0,
    Ehat in Z^(n by m).

Set F=sum_i k_i. For any n-element choice I of E's m columns, restrict
the matrix equality to those columns and take the determinant:

    (det U)(det E_I)
       = det(Delta) det(Ehat_I)
       = p^F det(Ehat_I).

Since det U is a unit, p^F divides **every** maximal minor det E_I.
If F>0, all those minors vanish modulo p and E mod p has row
rank strictly less than n. This conclusion is purely integral linear
algebra. It does not require p to be inert; inertness is part of the
*number-theoretic proof of the assumed extraction*.

Therefore a prime that appears in a nontrivial two-sided row
extraction for this SAME E cannot also be used to exhibit a
nonzero maximal minor of E modulo that very prime. A different
auxiliary prime q is not ruled out by this lemma.

When B is the same original positive diagonal trace matrix, the
positive Gram G=EBE^T obeys the Cauchy--Binet identity

    det G = sum_{I, |I|=n} (det E_I)^2 * prod_{j in I} B_jj.

Every term is nonnegative in the real embedding, so one nonzero
minor implies positive det G. However a uniform upper bound on
*one selected minor* is NOT a uniform upper bound on the whole
sum. The existing p-adic two-sided factorization of G proves a
divisor of det G even when the sum's p-adic terms might otherwise
cancel; preserve the integral metric and the actual block factor two.

## Exact negative and positive controls

(A) Let E=diag(3,1), U=I, Delta=diag(3,1), Ehat=I.
Here F=1 at p=3; E mod 3 has rank one, so a same-prime full-rank
certificate is impossible. With B=diag(2,2D), D>0,

    G = diag(18,2D),   det G = 36D.

At q=5, E mod 5 *does* have full row rank. Both facts coexist:
prime q can witness nonvanishing while prime p forces the divisor.

(B) Let E=[1 1] (one row) and B=I_2. Each selected
one-column minor has determinant 1, but det(EBE^T)=2. Bounding
a chosen minor by 1 does not upper-bound the whole Gram by 1.
This is the concrete failure of the naive selected-minor transport.

(C) If F=0 (all k_i=0), the lemma supplies no rank
obstruction. If n>m, there are no n-by-n minors at all.
The prime and dimension guards are essential.

## What a genuine bridge would require [H]

1. Keep the actual number field, the SAME E, B, all original
   monomial labels, ordinary derivative orders, trace metric,
   lattice observations, radius and sampling cardinality fixed.
2. Identify which p in the inherited prime-power budget have F(p)>0.
   Any proposed modular rank witness at such p is *killed*.
3. Find a different auxiliary q with a **noncircular**, independently
   proved admissible range and inertness (if inertness is needed for
   the candidate rank proof). Establish full row rank of the
   **unchanged E** over the required residue field.
4. Transport full row rank to characteristic zero and the positive
   trace Gram. Then compare the auxiliary-prime existence cost
   with the current interpolation point-count proof; quantify what
   actually becomes better. A new observation E' requires rebuilding
   **both** the divisibility and geometric bounds; old cutoffs do
   not automatically transport.
5. Formally prove the all-minors lemma and matched negative controls
   in a separate Lean experiment before any claim of a more efficient
   proof or improved cutoff.

The simple conditional lemma has a transparent paper proof. Its
relevance to a better tenth-discriminant estimate remains *hypothetical*
until the rank witness, exact matrix compatibility and quantitative
advantage are established. No claim of originality: the algebra is
standard and the question is whether it can usefully connect these
two existing proof architectures.

Related: [current verified 47.0b theorem](../tight_radial_v1/PHASE133_VERIFICATION.md),
[method comparison](../../METHOD_COMPARISON_CURRENT.md),
[independent human review](https://github.com/Dojo-1/tenth-discriminant/issues/50).
