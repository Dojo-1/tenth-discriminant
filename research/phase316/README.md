# Phase316 · the norm-preserving gauge the Gram still sees

> Same global ideal counts. Same full convolution. Same local norms and conjugation. Different second wild digit.
>
> The gap is now specific: actual global generator compatibility, not the vocabulary of grounding.

Stacked research **draft** on the consolidated Phase313/Phase315 branch. No change to main, the native field theorem, existing fixed original D163 valuation77 or reported 322^4 cutoff. Independent human mathematical review is still absent.

Two sequential preregistrations frozen BEFORE their corresponding code:
- PRE_REGISTERED_WILD_GAUGE.md
- PRE_REGISTERED_SMALL_NORM_RIGIDITY.md

## 1. Exact conjugate-prime valuation difference

For K=Q(sqrt(-163)), omega=(1+sqrt(-163))/2, omega²-omega+41=0. The principal conjugate primes P=(omega), Pbar=(1-omega) have norm41. Define the exact INTEGER ideal-valuation difference

\[
\nu(z)=v_P((z))-v_{\bar P}((z)).
\]

Then nu(xy)=nu(x)+nu(y), nu(conj(z))=-nu(z), nu(-z)=nu(z). Exact divisibility is checked on integer omega coordinates: omega divides a+b omega iff 41 divides a; baromega divides it iff 41 divides a+b. No reduced mod125 representation is used for ideal factorization.

The nonzero depth2 shift t=5(-1+2omega)=(20,10) mod25 is trace-zero, conjugation-anti-invariant and vanishes mod5. Define a **synthetic** conductor125 ray assignment

\[
\boxed{L'(z)=L(z)+\nu(z)t\pmod{25}}.
\]

It is multiplicative, signed-invariant, conjugation-covariant and preserves the SAME local norm modulo125, tame mod5 and conductor2 residues. Traceful t=5 is a hostile control that breaks norm and conjugation; zero t changes nothing. This is a compatible local ray assignment attached to EXISTING ideals, not the true principal-generator ray map of a new quadratic field.

## 2. All global ideal-shell constraints survive the twist

At held-out maximal-order radius60, the synthetic full conductor250 spectra retain the exact 1,440 independent ordinary ideal norm-shell counts and **59 genuine nonidentity coprime full 22,500-class ray products**. The native radius21 ball separately preserves 177 independent shell totals and 270 full coprime convolution equations. Conjugation and norm125 compatibility are checked across 1,720 unit generators; 84 have a changed second wild digit, and 1,344 exact prime-valuation product checks agree.

~~~mermaid
flowchart TD
  A["Actual h1 principal ideal norm shells"] --> B["Exact prime ideal valuation difference"]
  B --> C["Synthetic trace-zero wild second digit"]
  C --> D["Full conductor250 convolution preserved"]
  D --> E["Conductor2 selector AFTER multiplication"]
  E --> G["Same ORIGINAL integer-order Gram reconstruction mod25"]
  G --> M["Mod5 matrix exactly unchanged"]
  G --> H["363 mod25 cells changed"]
  H -. "not actual alternative field generators" .-> X["Missing actual global generator congruence"]
~~~

At the true original integer-order D163 source Q109/R40/S=J1, after the unchanged fifteen /5 source divisions, the synthetic ray spectrum reconstructs a primitive Gram which is IDENTICAL to the actual original Gram modulo5 (rank23), but **363 of its 1,600 entries differ modulo25**, first at (0,26) by 15 mod25.

This establishes a limited but substantial negative: full ideal-shell convolution, actual ideal counts, local norm congruences, tame and conductor2 residues, conjugation and signed invariance ALONE do not determine the higher-depth wild Gram. It DOES NOT prove that real globally realized ray generators are unconstrained, or exclude a genuine uniform class-one theorem.

## 3. The classical small-norm wall is also preserved

For any fundamental D=4m-1>3 and omega=(1+sqrt(-D))/2:

\[
N(a+b\omega)=a^2+ab+mb^2,\qquad
4N=(2a+b)^2+D b^2.
\]

If b is nonzero then 4N≥D=4m-1, and integrality forces N≥m. Every element of norm below m is therefore a rational integer of square norm. Under h(K)=1, EVERY integral ideal norm shell n<m consequently has precisely one ideal when n is a square and none otherwise; all rational primes p<m must be inert. This is classical arithmetic, not novel.

Test all such ideal shells for h1 D43 (m11) and D163 (m41), with h2 D187 (m47) as a negative: D187 has nonprincipal ideals of norms11 and17 even though its small-norm GENERATOR gap is identical. The synthetic D163 twist is zero on all rational integers and therefore preserves the exact ray classes, not merely the counts, of EVERY low norm shell fixed by h1.

In the original integer suborder, the first nonrational point is sqrt(-163) of norm163. The first point actually carrying the asymmetry between P and Pbar is 2omega=1+sqrt(-163) of norm164=4*41. The original-order conductor2 selector delays the synthetic perturbation to this sharp threshold.

## 4. Evidence and next minimal theorem target

- **P-paper:** norm-form completed square, low-norm rationality, and conditional exact ideal-character identities. Scoped Lean file Phase316SmallNorm.lean targets the quantified norm-form result, not class-number-one ideal theory. Its kernel check is separate.
- **M, after exact-head CI:** finite ray, convolution, conjugation, local norm, original Gram and small-norm hostile checks.
- **R:** any assertion that full h1 ideal counts, convolution, inert-small-prime rigidity and local second-depth norm/conjugation determine actual second-wild moments without global generator compatibility.
- **H:** a UNIFORM h1-only arithmetic constraint on ACTUAL principal generators in the native large-R,S,J integer-order source, forcing extra 5-adic Gram valuation beyond inherited valuationWeight.

The next step must distinguish coherent but synthetic local ray transports from actual globally realizable norm-limited generators. Matched h8 D183 and same-inert h2 D187 remain mandatory countercontrols. No main merge or new 322^4 claim.
