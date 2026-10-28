# The coordinate bridge is now in the main library

[Read the mathematical explanation](COORDINATE_TRANSLATION_GUIDE.md):
one lattice has compatible integer, field and complex coordinates; moving
its samples preserves specified invariants. The odd chart has an explicit
index-two restriction. A checked counterexample shows the determinant
itself need not survive a shift unchanged.

Phase105 proved these facts in a bounded standalone attempt, preserving
both failures. Phase106 then moved the accepted proof unchanged into the
main library. Module build, full build, fresh dependency checks and whole
axiom audit all passed on their first invocation. See the
[exact integration record](PHASE106_VERIFICATION.md).

The class-number-one cutoff stays 50 billion. The next numerical advance
needs a justified upper estimate compatible with these operators.
Arbitrary even-field transport and independent human review remain open.
External CI and merge status are recorded per exact published head.
