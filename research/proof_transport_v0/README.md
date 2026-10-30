# Proof-transport pilot (Rust + Lean)

This research directory is a bounded experiment for the actual integer derivative-jet Gram from the Tenth Discriminant, not a new discriminant bound or an independent mathematical review.

Start with [the registered protocol](PROTOCOL.md) and [the human-to-Lean proof atlas](PROOF_ATLAS.md). The Rust library implements, using checked \`i128\` and no external dependencies, the exact original ordinary jets, integer quadratic-order pair multiplication, actual arithmetic U_p and radial T_a binomial matrices, explicit integral quotient Ehat, Gram and its two-sided factor, determinant preservation, modular rank and negative controls.

The first fixture D=19,p=3,R=5,S=J=2,rho=2 was already explored during design; reproducing it does not make the code an independent proof or a held-out test.

Run (with the Rust toolchain installed):

\`\`\`sh
cargo test --offline --manifest-path research/proof_transport_v0/Cargo.toml
cargo run --offline --manifest-path research/proof_transport_v0/Cargo.toml --release
\`\`\`

All computations are exact in bounded \`i128\`. Overflow is a hard error, not wrapping. Dimension caps prevent pretending to materialize the production-sized matrices. The emitted Hadamard products are **finite** comparisons only, not universal bounds. The project-wide Lean build also imports the new \`TenthDiscriminant.ProofTransport\` module: \`cd lean && lake build\`.

Interpret outputs using [the evidence map](PROOF_ATLAS.md); PR status and exact commit-specific CI determine which statements are checked. Read [Phase131](../ender_radius_bridge/PHASE131_VERIFICATION.md) for a separate exterior-minor comparator and its limitations.
