# Review the new bridges by trying to break their hypotheses

Target commit69010f4e5d2e0adc44c70932d20583e669b7b7c2 in this repository.
Review only the five obligations below, reading source before author guides.
Working proof sources must match that commit; verify before relying on them.
The requested conclusion is an adversarial finding or an explicit bounded
absence of findings, not confirmation of the project narrative.

## Claims and fixed obligations

1. **Conjugation and rationality.** In
   `lean/TenthDiscriminant/ImaginaryQuadraticRepresentation.lean`, reconstruct
   why an abstract totally complex quadratic number field admits the
   asserted nonidentity conjugation operator, and why a square of a nonzero
   anti-invariant element belongs to Q. Check quadratic normality and the
   whole Galois group, rather than assume one involution always has rational
   fixed field. Check the dimension-independent projector statements against
   their actual types. Explain what would fail in a larger field.
2. **Normalization and transport.** Trace the nonzero/pure-imaginary/strict
   negative-square step, rational denominator clearing, positive squarefree
   factorization and all divisions. Read
   `lean/TenthDiscriminant/QuadraticGeneratorBridge.lean` and verify that the
   constructed equivalence transports actual class number and actual field
   discriminant. Distinguish the field discriminant from a scaled polynomial
   or order discriminant. Decide whether the final public abstract-field
   bound has an undisclosed root/isomorphism premise or a circular finite
   answer input in these new wrappers. Do not re-prove the inherited100b core.
3. **Sign sectors and sample symmetry.** Read
   `lean/TenthDiscriminant/CentralSymmetry.lean`. Re-derive how ordinary
   derivatives and the original factor-two integer pairing transform under
   simultaneous sample negation. Check cancellation, origin, arbitrary J,
   zero derivatives, generic finite samples and the positive-D ellipse
   instance. Verify the singleton mixed-entry control. Does the theorem
   really refer to the original Gram and preserve a thin rectangle?
4. **Arithmetic compatibility and guards.** Read
   `lean/TenthDiscriminant/ParityCompatibility.lean` plus the reached
   rectangular basis/row-action definitions. Check active-term bounds,
   natural subtraction, original row-major labels, oddness, empty rectangles
   and the actual coefficient matrix. Verify that both concrete commutation
   statements use the same sign operator. Check the p=2,R=3,S=2,row4,col1
   mixing control and whether the integer-sector interpretation is valid.
5. **Public claim boundaries.** After your derivations, read
   `research/ender_radius_bridge/CONJUGATION_BRIDGE_GUIDE.md`,
   `CENTRAL_SYMMETRY_GUIDE.md`, `PARITY_COMPATIBILITY_GUIDE.md`, current README,
   STATUS and lean/FORMALIZATION. Identify claims stronger than exported
   theorems, missing assumptions, outdated current frontiers or misleading
   quantitative/review assertions. In particular, block structure alone is
   not a stronger valuation or strict Hadamard saving, and no new cutoff,
   general classification announcement, novelty or human review is claimed.

## Evidence boundaries

Local compiled input/axiom checks exist in Phase46/47/49/50 artifacts.
They may help locate claims after source derivation, but passing checks
are not a substitute for mathematical semantics. Prior AI reports are
not coverage of these additions. CI40227162534 is separate and may still
be live. No review assertion may use its eventual outcome without observing it.

For every finding give severity (FATAL/GAP/SLOPPY/CANNOT-VERIFY), exact
file/line evidence, a mathematical trigger or counterexample, and effect on
the public theorem or documentation. For each of five obligations give a
verdict and scope label: RE-DERIVED, SOURCE-TRACED or CANNOT-VERIFY. Do not
inflate a source trace into a complete re-proof. List inherited arguments
and checks not performed. If none is found, say "No contradiction established
in these bounded checks," with limits. Independent human or model-family
review is not established by a fresh process.

Read-only, no delegation, no edits, no rebuild or experiment,30-minute cap.
Return your first report. Do not message other chats or post externally.
