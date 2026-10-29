# Why keeping row correlations can tighten the squeeze

**Paper argument only: the Phase114 formalization failed its checks.**

The object stays the same: an integer matrix G built from ordinary polynomial
jets. Geometry bounds det G from above; prime arithmetic forces divisors of
that same integer. A coordinate change is useful only when we track which
part of this comparison it preserves.

## The geometric move

A diagonal bound measures every row separately. A block bound keeps some
correlations between rows. For a positive-semidefinite real matrix A,

    det A <= product of determinants of its actual principal blocks.

Here is the proof in four steps. Within each principal block, choose an
orthonormal eigenbasis. Combine these changes into one block-diagonal
orthogonal matrix U. The full matrix becomes U^T A U: it is still PSD and
has the SAME determinant. Apply the ordinary diagonal Hadamard bound to
this full transformed matrix. Within each block its diagonal entries are
the block eigenvalues, whose product is the original block determinant.

The off-block entries need not vanish. Cross-block entries are retained throughout the full-matrix calculation. Empty blocks contribute 1; singular blocks are
allowed. This is the classical Fischer inequality, not a novelty claim.

## Which rows belong together?

Our row indexed by (r,s) is Z^r W^s, with W evaluated as conjugate Z only
AFTER differentiating in Z. Its jth ordinary derivative contributes
(r)_j z^(r-j) conjugate(z)^s. Group rows by the INTEGER label r-s.
For two rows (r,s), (t,u) in the same group, r+u=t+s. Their product with
complex conjugation is therefore a real multiple of a power of |z|^2.
Summing gives the exact cross entry

    2 sum_(j<J, j<=r, j<=t) (r)_j (t)_j M_(r+u-j),
    M_n = sum_(z in P) |z|^(2n).

No symmetry of P is needed. Origins and negative labels remain present.
Different labels can have nonzero cross entries. Every diagonal retains
ALL its own derivatives, including columns unmatched by another row.
Ordinary derivatives carry falling factorials: at 1, the row (2,4) with
J=3 has diagonal 2*(1^2+2^2+2^2)=18.

## Where arithmetic stays anchored

The orthogonal eigenbases can have nonintegral entries. They are auxiliary
REAL coordinates for an upper-bound proof. They do not automatically
preserve the integer lattice, Smith form or residue kernels.

Instead we keep the exact cast identity A=G mapped from Int to Real.
Under the original positivity guards and odd-prime nonsquare condition,

    p^(2*valuationWeight) <= det G <= product of moment-block determinants.

The first inequality uses positive integer det G and its proved divisor;
the second estimates its exact real cast. Neither branch silently changes
the determinant. This is the useful local-to-global bridge: a common
integral object supports both reductions and real geometric estimates.

## What would actually lower the cutoff?

This block inequality alone does not supply a numerical improvement.
We still need a uniform quantitative upper estimate for the blocks at the
ACTUAL production radius and parameters, then an all-range contradiction
with the arithmetic lower estimate. The stopped Phase113 finite annulus
experiment cannot stand in for that proof. The published h1 bound remains
50 billion; full classification, optimality and independent human review
are not claimed.

## Verification boundary

The Phase114 outcome and exact commands are recorded separately in
[the verification report](PHASE114_VERIFICATION.md). Research source and
local standalone checking are distinct from production integration and CI.
The first failed source, every repair and all terminal logs are preserved.
[Registered target and limits](PHASE114_PROTOCOL.md).
