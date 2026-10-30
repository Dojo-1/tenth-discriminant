# Radial transport is an actual parameter action

**Integrated unchanged in this branch; all four local checks pass.** These laws concern
the original RadialOperator.matrix, all ordinary jets and the same Gram.
They do not follow merely from two matrices having the same determinant.

For a fixed rectangular row family, the integer matrices now satisfy

    T_0=I,   T_a T_b=T_(a+b),   T_a T_(-a)=T_(-a) T_a=I.

Why: fix r-s and put u=ZW. Each row is an unpaired monomial times u^m,
where m=min(r,s). Centering replaces u^m by(u-a)^m. Applying another center
replaces it by(u-a-b)^m. The formal proof expands the actual row action,
then extracts bivariate coefficients to identify the actual integer matrices.
The faithful object here is the coefficient encoding of rows, not a claim
that every rectangle gives an injective parameter representation.

The matrices act on every original jet column by integer linearity, so the
parameter law holds for all samples and derivative orders simultaneously.
For the Gram at parameter b, applying the actual matrix at a gives exactly
the original-sample Gram at parameter a+b. In particular a zero-sum parameter
loop returns the frame, jets and Gram, not just the determinant.

These are laws on each FIXED rectangle, including empty rectangles. They
do not identify row spaces of different sizes. If R=1 or S=1 every m=0,
so every parameter already acts trivially;zero sum is sufficient for return,
not a claimed necessary condition. The radial family commutes internally;
no commutation with the prime-dependent arithmetic frame is asserted.

This is an integer-linear observation action, NOT a ring automorphism.
At parameter3 and Z=0,W=1, separately movedZandW have product0, while the
moved productZW evaluates-3. The fixed formal negative control retains this.
Individual lengths may change. Neither the group law nor a loop supplies
new prime divisibility, a smaller cutoff or real-rank invariance after
reduction. Those require their own hypotheses and inequalities.

[Integrated actual Lean laws](../../lean/TenthDiscriminant/RadialAction.lean) · [Integration evidence](PHASE128_VERIFICATION.md) · [Registered scope](PHASE127_PROTOCOL.md)
· [Full verification](PHASE127_VERIFICATION.md). Same-assistant proof work,
not independent semantic review. Both failed elaboration attempts remain saved.
