# BEAN — class number one with no split-prime counting

**Theorem (candidate; see review limitations below).** If -D is a fundamental discriminant and K = Q(sqrt(-D)) has class number one, then D <= 163.

**The whole input from h = 1** is Rabinowitsch's elementary fact: every prime p < (D+1)/4 is inert.
No split-prime or representation counting, no L-functions, Siegel zeros, GRH/QRH, Heegner/Baker/Stark, or class-number tables.

**Argument.** Take R < (D+1)/4, so every odd prime up to R is inert. Evaluate Green's derivative Gram determinant on the
lattice points of Z[sqrt(-D)] in the norm ellipse |z| <= rho. Frobenius at the inert primes makes det G divisible by
prod p^{2F(p)}; Hadamard bounds det G from above. The ellipse lowers the archimedean side by (1/4) log D, which is exactly
what allows R < D/4. For large D the inert-prime mass log R beats the archimedean term (3/4) log D.

**Certificates.**
| range | method | file |
|---|---|---|
| D >= 1e36 | one monotone inequality (slope 15/64) | tools/asymptotic_bean.py |
| [7e11, 1.04e36] | 257 contiguous Arb interval certificates, min margin 1.0009 | ledger/coverage_bean.txt, tools/bean.py |
| [92, 7e11) | CRT sieve (Rabinowitsch residue conditions), 8 s, survivors: 163 only | ledger/sieve_bean.txt, tools/sieve_crt.py |
| D < 92 | reduced-form enumeration | ledger/finite_h2.txt |

**Inputs:** Green's lemmas (ledger N4–N7, independently re-derived by GPT-6.1), ellipse count (N8, re-derived), Hadamard,
Dusart 2010 (theta(x) >= x(1-0.2/ln^2 x), x >= 3 594 641, primary checked), Rabinowitsch (elementary).

**Credits.** Green (determinant); twinheterodox, van Dijk (the route family); Kyle Pratt (disk interpolation; CRT sieve idea,
Tao comment of 20 Oct); J. Vilela (norm-ellipse evaluation set; the seed of this route).
**Novelty:** in the thread snapshot of 21 Oct, the inertness of all p < D/4 is used only for the computational sieve; no entry
found that uses it as the sole analytic input to the determinant. "Not found", not "confirmed".
**Trade-off:** analytic cutoff ~7e11 (vs 570 for counting routes), in exchange for removing the split side entirely.

**Continuation (Ender / Formic).** The BEAN audit found gaps in the written all-D bridge and a mismatch in the saved finite-range artifact; see `review/BEAN_AUDIT.txt`.
The factorial/Legendre continuation removes Dusart: 250 intervals from 7e11 to 1e36, an explicit monotone asymptotic envelope
(margin 7.84016 at 1e36), and a fresh full CRT run with sole survivor 163. Derivation and limitations: `ledger/ender.txt`.
Formic supplies exact local, mutation and coverage checks, not a formal proof.
