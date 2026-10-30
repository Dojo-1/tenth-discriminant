# Phase131: exterior-volume reconstruction of the same determinant

Base: published03cb58c25975ed638bebfa3bcc5b2a3152e9f452. Preserve that
source, PR45, every Lean file, all controls, pins and historical outcomes.
This cycle changes explanation and a separate reference comparator only.
It introduces no new cutoff, valuation exponent or formal theorem.

## Mathematical target

For original integer observations E and diagonal integer metric B, give the
exterior-power/Cauchy--Binet proof of the SAME det(E B E^t). From the actual
integral quotient identity U E=Delta Ehat, det U=1, show that every maximal
minor has a common p^F factor, hence the induced Gram norm has p^(2F).
Explain the squared lattice index only under row independence; retain the
wedge argument in dependent/zero cases. Explain why a unimodular frame can
change the Hadamard ceiling while preserving this exterior volume.

## One sealed exact comparator

Inputs are the immutable Phase123 archive, SHA256
e9a0b39a5924075e17b8da58a76f10123e758b6b0a379b5188eda0cc87e42ed6,
and the frozen five original points from phase123_two_sided_oracle.py.
Use EXACTLY the eight saved cases with J=1, (R,S) in {(1,1),(4,2)}, and
(D,p) in {(1,3),(19,3),(2,5),(1,7)}. Do not filter by determinant sign.

The archive contains G,U,K and exponents, not E. Therefore reconstruct E
in this NEW comparator via 2x2 integer multiplication matrices for x+yt,
not by calling/importing the old oracle or rerunning its 80-case campaign.
There are ten coordinate columns. Enumerate all maximal minors: ten per
one-row case and45per eight-row case,220in total. Use exact Fraction-based
elimination, then compare weighted sums of squared minors with the SEALED
detG/detK, and test each transformed/quotient minor's exact p^F factor.
Reconstructed original and quotient Gram entries must match saved G and K.
J=1 tests zero-order observations only; it does not replay all-order jets.

Fixed negative controls: omitting the square in Cauchy--Binet must change
at least one case; replacing2FbyFmust fail on a nonzero F>0case; a shear
must preserve determinant while changing the diagonal-product ceiling;
diag(p,1) must demonstrate rank loss on reduction, without contradicting
rank preservation between unimodular frames over the SAME residue field.
Record how many zero/nonzero minors and determinants actually occur.

One full invocation,60seconds,stdlibPython, no floating point, no parameter
search or repair/retry after execution. Static syntax checks are allowed
before invocation. On any mathematical, implementation or resource failure,
preserve all source/native logs and stop this cycle. Capture source, data,
stdout, stderr and native result. Verify saved evidence without replay.

## Reader delivery and evidence boundaries

Provide one concise exterior-volume note linked from the existing short
guide. Reconcile the evidence-layer page to the already completed PR45
proof/security runs, fixing the split table and stale integration backlog.
README/objective ledger remain61lines; all historical protocols/raw remain
unchanged. This is a second mathematical representation and code path by
the same assistant, NOT an independent human referee or a new theorem.
Any publication stays draft/unmerged and distinguishes old mathematical
source03cb58c from the new documentation/comparator revision.
