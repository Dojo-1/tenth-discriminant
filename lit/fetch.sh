#!/bin/sh
# Re-download sources; verify with: sha256sum -c SHA256SUMS
cd "$(dirname "$0")"
curl -sSL -o green_2610.00311v2.pdf https://hexagonmath.org/pdf/2610.00311v2
curl -sSL -o kimura_2610.21511.pdf https://arxiv.org/pdf/2610.21511
curl -sSL -o banks_2610.15483.pdf https://arxiv.org/pdf/2610.15483
curl -sSL -o kerr_2610.21099.pdf https://arxiv.org/pdf/2610.21099
B=https://github.com/openai/math/raw/main/preprints
curl -sSL -o openai_siegel_2026-10-01.pdf $B/Uniform-exclusion-of-Landau-Siegel-zeros-October-1-2026/paper.pdf
curl -sSL -o openai_qrh_11-12.pdf $B/The-Quasi-Riemann-Hypothesis-October-5-2026/paper2.pdf
curl -sSL -o openai_qrh_7-8.pdf $B/The-Quasi-Riemann-Hypothesis-September-30-2026/paper.pdf
