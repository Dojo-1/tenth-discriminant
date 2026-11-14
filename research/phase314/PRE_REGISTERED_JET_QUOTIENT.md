# Phase314 — preregistered wild second-jet quotient, original Gram and global convolution

2026-11-14 Europe/Madrid. This text precedes all Phase314 implementation and measurements. Base = Phase313 draft PR #205 head af1f0506e2314e46e497905e2d845c3ffc6a4af0. No main merge or altered reported 322^4 bound.

## Living question

Phase313 reconstructed the original D203 and h1 D163 primitive trace Grams from the 300 conductor25 signed ray counts plus 25 nonunit lift counts. Does the Gram see all of the wild information? What part survives h1 conductor50 convolution after the exact conductor2 suborder gate, and could it force any *independent* determinant valuation?

## A. Paper-level theorem target [P-paper]

Let k=F5, W=(F5)^2 additive. Its group algebra k[W]=k[U,V]/(U^5,V^5) with augmentation ideal J=(U,V). At each fixed signed tame residue c, the ALREADY EXISTING D203 source divided rows and both held-W ordinary jets, and the exact original D163 integer-order divided source, are affine k-linear in the wild coordinate w=(x,y). This follows from epsilon(z)=conj(c)*delta(z) and F25 conjugation being k-linear. The signed-pair trace Gram contribution G_c(w) is polynomial in (x,y) of total degree <=2. Its k[W]-linear extension annihilates J^3. Thus the entire 300 signed ray count map factors through 12 copies of k[W]/J^3, at most 12*(1+2+3)=72 F5 coordinates rather than 300. The 25 first-nonunit-lift classes u=z/5 have similarly affine evaluations and at most six F5 moment coordinates: at most 78 moment coordinates total. This does NOT say that all 78 are linearly independent, or that deeper 5-adic Gram digits are controlled by them.

The conductor50 group C3×C12×W has a 216-dimensional mod5 J³ quotient (3*12*6). The full h1 maximal-order norm-shell convolution descends to this quotient because J³ is a two-sided ideal. The original integer-order conductor2 selector is applied AFTER the convolution; selected suborder principal distributions do NOT themselves convolve.

## B. Frozen original-source coefficient and Gram experiment

1. For D203, each of 12 tame residues c and all 25 wild coordinates w, directly compute the signed pair-summed original primitive 100x100 Gram with held-W j0/j1 and exactly Phase307 original rows. Fit its six polynomial matrix coefficients in 1,x,y,x²,xy,y². Compare **ALL cells** at ALL 25 values, no sampling. Repeat D163 with exact original integer-order 40 rows after 15 /5 shears.
2. For each of 25 first-nonunit-lift values u, compute the actual original primitive Gram of one z=5u observation. Fit the six coefficients and compare all25 values, preserving the nonunit stratum explicitly.
3. Compress the real D203 Q263 300+25 count vector and h1 D163 original integer Q109 vector to 72+6 moment numbers. Reconstruct and check independently ALL original 10,000 and 1600 primitive Gram entries vs Phase313 and source oracle; recover ranks63 and23.
4. For each tame residue and EVERY wild w, verify all 8 third finite differences using field-coordinate basis increments e1 and e2 vanish as matrices, and verify at least one second finite difference is nonzero. Retire the claim if not.
5. Build two different NONNEGATIVE abstract count histograms differing by (g-1)^3 with equal total, linear and quadratic moments. Their actual Gram outputs must match. They are abstract formal spectra, NOT actual number fields or h1 ideal distributions.
6. Show 1,x,y,x²,xy,y² are linearly independent functions on the 25 wild points, proving J³ quotient dimension6 is the correct upper bound of degree-2 information.

## C. Frozen global convolution experiment

Using the ACTUAL D163 maximal-order Q225 radius21 full signed conductor50 900-ray distributions by norm n<=441, calculate 216 wild-second-jet moment coefficients for each shell prime to10. Implement and test closed moment convolution from multiplication of tame/conductor2 classes and addition of wild coordinates. For EVERY eligible coprime pair (expected 270), compare the SIX moment coordinates for every tame/conductor2 class against independently enumerated product norm-shell. Then apply the conductor2 selector on odd norms and add the real even-norm prime-to5 and nonunit strata. The resulting original integer Q109 unit/nonunit second moments must agree with the actual selected counts and produce the SAME original Gram. The exact omega norm41 and 1+omega norm43 outside the suborder, product norm1763 inside, remains a kill control against projecting before multiplication.

## D. Countermodels and theorem gap

Explore an abstract formal two-distribution system satisfying multiplicativity and total ideal counts but with different 1st/2nd wild moments, hence potentially different Gram images; such a model excludes a conclusion from convolution+total counts ALONE, not from all constraints of a real number field. Do not assert universal field impossibility.

## E. Narrow Lean target

Kernel-check two-variable quadratic third-difference cancellation (or simpler exact polynomial identity if necessary) and separately the six-coordinate convolution product law, without unverified axioms or admitted goals. The Lean theorem does not certify number fields, ray class groups, source rows or determinant valuations.

## Evidence and stops

[P] conditional algebraic polynomial/augmentation facts. [M after CI] finite full-source tests and all shell product checks. [H] a uniform h1-specific residual Gram valuation INDEPENDENT of existing valuationWeight. [R] the wild J³ layers affect the primitive mod5 Gram, or original suborder-selected ray counts themselves convolve. Stop on any source row, ordinary jet, nonunit lift, group product, conductor2 selection, Gram equality, J³ vanishing, or independent oracle mismatch. No altered v5=77/138 claims, no new discriminant cutoff, no physical quantum or intelligence claim.
