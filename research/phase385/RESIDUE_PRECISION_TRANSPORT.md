# Phase385.2 — A p-adic precision law for normalized ordinary source jets

**22 November 2026; elementary conditional theorem and exact bounded regression.** This note preserves Phase385's negative finding: residual Gram determinant valuations are NOT monotone under enlarging the original observation ellipse. It identifies a more productive object to measure than the scalar determinant.

## The exact source object

Fix integer D, odd inert prime p, rectangular rows (r,s), ordinary derivative order j, and an original pair-lattice sample a=(x,y) in Z² for z=x+y sqrt(-D). The repository's ordinary-Z derivative, W held fixed, is a polynomial with integer coefficients in x,y. Denote it by E_(r,s),j(a) in Z².

The explicit unimodular binomial matrix U replaces Z^r W^s with Z^(r-pk) W^s (Z^p-W)^k, where k_(r,s)=min(floor(r/p),S-1-s). Inert Frobenius and ordinary-jet divisibility give the integer coordinate factor

  P_i,j(a)=(UE)_i,j(a) = p^(k_i) F_i,j(a)

for every integer source point a. The underlying divisibility is already formalized in the existing InertFrobenius, FrobeniusJet, RectangularRowAction and RectangularGramFactor Lean modules. The new observation concerns the quotient's required input precision.

## Lemma: normalized-jet precision transport

Let P: Z² -> Z be an integer-coefficient polynomial with p^k dividing P(a) for every integer a. Define F(a)=P(a)/p^k. If

  a ≡ b (mod p^(k+m))

coordinatewise, for m>=1, then

  F(a) ≡ F(b) (mod p^m).

**Proof:** Integer polynomials preserve congruences. P(a)-P(b) is divisible by p^(k+m). Divide by p^k to obtain divisibility of F(a)-F(b) by p^m. QED.

For a finite family of original source jets with K=max_i k_i, a single modulus p^(K+m) suffices for every normalized row, sample and derivative order. The bound is sufficient, not necessarily minimal.

For the original integer-pair trace weights, define H_Q by summing over a in Q and derivative order j the outer products of normalized F_j(a) with the 2x2 metric diag(2,2D).

**Corollary:** H_Q mod p^m depends only on the histogram (including multiplicities) of source observations Q modulo p^(K+m), the normalized source polynomials, and the trace metric. Group the sum by residue class and apply the lemma. This is an exact compression opportunity for modular Gram calculations; it is NOT a claim that two ellipses of different radii have identical histograms.

## Mod-p sample classes are insufficient

For D=43,p=3, the normalized k=1 zeroth jet of Z³-W on real-axis points x is

  q_3(x)=(x³-x)/3.

At x=0,3,6, all source residues are zero modulo 3, but q_3(x) modulo 3 equals 0,2,1. Thus original source point counts merely modulo 3 cannot reconstruct the normalized Gram modulo 3.

At x=0 and x=9, source points agree modulo 9 but normalized quotients differ modulo 9 (0 versus 6). For this k=1 row, modulo 27 suffices to control the normalized quotient modulo 9.

In Phase385's D=43,p=3,R=7,S=3,J=3 source rectangle, K=2. Thus modulo 27 suffices for H_Q modulo 3 and modulo 81 suffices for H_Q modulo 9. The local script precision_jet_control.py checked 11,340 source-shift/row/derivative congruences under shifts of 27 modulo 3; shifts of 81 modulo 9 and both low-precision negative controls also passed. This is M (bounded exact tests), not a new Lean proof.

## Why this matters to Tao's arithmetic target

The production thin ellipse might admit a manageable residue-class histogram, permitting exact rank and higher Smith-layer studies without constructing the huge integer Gram. But **no general positive residual valuation follows**: Phase385's rho8 normalized Gram has extra valuation 14 while rho9 has zero, even though both support the same uniform 3^18 divisor and the second has more observations.

Next falsifiable theorem: identify the source residual histogram modulo p^(K+m) for the exact production radius and rigorously bound the rank of the corresponding normalized moment matrix, with source/maximal-order parity and actual field transport preserved. Reject any conclusion that substitutes Hasse derivatives, uses source residues mod p alone, or infers a global new discriminant cutoff from a finite test.

**Evidence:** P elementary polynomial-congruence/histogram lemma under the existing Frobenius divisibility; M 11,340 shifts plus independent 21x21 exact Gram tests; H uniform production-residue distribution and additional Smith valuation; R source modulo-p histogram as a complete normalized-jet invariant.
