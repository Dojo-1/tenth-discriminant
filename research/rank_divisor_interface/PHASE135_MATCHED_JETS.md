# Phase135: the same original jets, before and after one inert-prime extraction

**30 October 2026.** [Issue #51](https://github.com/Dojo-1/tenth-discriminant/issues/51) · [PR #53](https://github.com/Dojo-1/tenth-discriminant/pull/53). This is a bounded, finite all-jet experiment (J=2), not a uniform number-theoretic theorem. The standalone [Rust implementation](phase135_ordinary_jet_pilot.rs) is intended to reproduce the exact integer formulas in the existing [IntegerTraceGram](../../lean/TenthDiscriminant/IntegerTraceGram.lean), [RectangularBasisMatrix](../../lean/TenthDiscriminant/RectangularBasisMatrix.lean), and [RectangularGramFactor](../../lean/TenthDiscriminant/RectangularGramFactor.lean), with no substituted samples, Hasse jets, or different trace pairing. Check exact-head CI before calling its recorded expectations measured [M]. No independent human review is implied.

## The frozen original object

Choose D=19, rho=5, R=4, S=J=2, and p=3. The *entire* integer ellipse is

    Q = {(x,y) in Z² : x²+19y² <= 25}, |Q|=21.

The field polynomial T²+19 remains irreducible mod 3 because -19 is the nonsquare 2 in F3, so 3 is inert in Q(sqrt(-19)); this inertness observation is independently elementary, and not needed to calculate the matrices. The original point-count hypothesis is 2(R-1)+(S-1)=7 < 21. No class-number hypothesis or Heegner list is an oracle for the finite experiment.

For the eight ORIGINAL row labels (r,s), 0<=r<4 and 0<=s<2, and for every original sample z=x+y sqrt(-19) and *ordinary* derivative order 0<=j<2, form the two integer coordinates of

    (d/dZ)^j [ Z^r W^s ] |_(Z=z, W=conjugate(z))
       = (r)_j z^(r-j) conjugate(z)^s.

The falling factorial (r)_j is zero for j>r. Write these real/imaginary integer coordinates in E, in row order i=2r+s: E is 8x84. Each (sample,j) coordinate pair receives the original quadratic trace metric B=diag(2,38); thus G=E B E^T is exactly the original integer Gram.

The checked rectangular basis matrix for (R,S,p)=(4,2,3) is the identity except for U_(6,1)=-1 (zero-based indices); the transformed row is Z³-W, not a replacement polynomial. Set Delta=diag(1,1,1,1,1,1,3,1). If and only if every transformed entry in row 6 is divisible by 3, C=Delta^(-1) U E is an **integral** matrix. The source's Frobenius congruence implies this here, including j=1. Let K=C B C^T.

## Exact expected finite results; pending checked CI

A standalone exact integer calculation predicted:

| Claim | Exact expected result |
|---|---|
| All transformed entries divisible by corresponding Delta entries | yes |
| rank(E mod 3) | 7 |
| rank(C mod 3) | 8 |
| U G U^T = Delta K Delta, entry by entry | yes |
| det(K) mod 3 | 2 |
| rank(K mod 3) | 8 |

If verified, these imply that **the original E loses rank mod 3 while its integral quotient C is full row rank at that SAME prime**. In this case the residual pairing is also nondegenerate, so the exact factorization det G = 3² det K has v3(det G)=2: *no positive extra residual valuation*. None of these conclusions generalizes to arbitrary Q,J,R,S without proof. In particular, the known inert-prime trace-metric example with C=[1,0,1,1] and B=diag(2,38,2,38) has C B C^T=42=0 mod 3 despite full row rank. Thus 'C has full rank mod p' is insufficient for a *general* 'det K is a unit mod p'.

The entire original ellipse has colliding residues at p=3: (-5,0) and (-2,0) both lie in Q, are distinct, and differ by (3,0). Nevertheless C may have full row rank. The collision prevents importing a theorem whose hypotheses demand **all nodes distinct**, but is not by itself a theorem of rank deficiency for a *different* normalized matrix.

Two registered negative controls are D=11 at p=3, where the Frobenius row quotient is not integral (the field polynomial splits at 3), and D=19, rho=1, where the original point-count guard fails. The script must reject both invalid promotions.

## The sharp coordinate collision condition (paper proof)

For every positive D and p, all pairs in the full Q are pairwise distinct modulo p **if and only if p>2rho**:

- If 0<p<=2rho, the two horizontal axis points (-rho,0) and (p-rho,0) lie in Q, are distinct, and are congruent modulo p. This direction is the new Lean target in PR #53.
- If p>2rho, every x and y coordinate of any sample lies between -rho and rho (because D>0). The difference between two coordinates therefore has absolute value <p; a multiple of p in this range is zero. Congruence in both coordinates forces equality.

The iff concerns the **selected free Z² coordinate chart** and the complete symmetric Q. For the index-two maximal order at odd fundamental discriminants, coordinate reduction in the chart can be transported to that order for odd p because 2 is a unit; at p=2 that step needs a separate integral comparison. An external proof may replace Q by a separated subset and change polynomial support, but then must rebuild BOTH its arithmetic divisor budget and its geometric upper bound. There is no new cutoff.

## Falsification and promotion

- **Kill:** any nonintegral quotient entry in the inert primary sample; rank(C mod 3)<8; det(K) mod3 not equal to 2; U G U^T != Delta K Delta at any entry; or passing an explicitly invalid split-prime / undersampling control.
- **Promote only the finite measurement:** Rust tests and exact-source CI succeed, all original integer formulas are matched, and a second independent reconstruction of critical entries is available. This is still not an independent mathematical referee and supplies no uniform residual divisor.
- **Further theorem only after a new preregistration:** prove an exact matrix-level normalization with controlled ordinary-to-Taylor factorial columns, distinguish the saturated determinantal ideal from the restriction of B to the row space, and establish a quantified range of admissible parameters. Do not double count the original p^(2F) dividend.

For [issue #50](https://github.com/Dojo-1/tenth-discriminant/issues/50), this experiment is a useful *local instrument* for the integral Gram and ordinary-jet semantics, but does not independently check the effective prime-tail estimate, the production radius/rectangle bounds or the field-discriminant endpoint. Keep the human reconstruction obligation open.
