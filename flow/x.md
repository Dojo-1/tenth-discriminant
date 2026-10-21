# x — the whole argument (every step present; status per obligation)

Let K imaginary quadratic, D = |disc K|, h = h(K) <= H assumed. O_K = Z[w], covolume sqrt(D)/2.
Rows v_{r,s}, 0<=r<R, 0<=s<S: derivatives d^j/dz^j (z^r zbar^s), 0<=j<J, at all z in O_K with |z| <= rho.
G = Gram matrix with entries sum tr(alpha * conj(beta)) in Z.

O1  independence: points on M lines (fixed coefficient of w), <= L per line; J >= L+M and nJ > 2RS+J(R+S)
    => det G > 0.                               [h=1 proof (N4, GPT-reviewed) is lattice-independent]   BRUTE 22 cases on O_K (composite, even discs); proof restatement pending
O2  count: A - 2rho - M <= n <= A + 2rho + M, A = 2 pi rho^2 / sqrt D.                                   BRUTE (22 cases)
O3  upper: log det G <= U(R,S,J,n,rho)  (Hadamard; unchanged).                                          DONE (N5,N6)
O4  p-adic: odd p with chi(p) = -1: Frobenius z^p = zbar mod p on O_K => v_p(det G) >= 2F(p).          BRUTE (22 cases, up to 3 ramified primes)
O5  split count: sum over the h reduced forms of reps of p equals 4 for split p (Dirichlet: r(n) = w sum_{d|n} chi(d), w=2),
    so #{split p <= t} <= (1/4)[h 2 pi t/sqrt D + sum_f (4 sqrt(a_f t / D) + 1)], a_f <= sqrt(D/3).  BRUTE: reps==4 on 17 discs, h<=19; bound loose 5-17x
O6  ramified: at most omega(D) <= 1 + log2(h) primes divide D (genus theory: 2^{omega-1} | h); worst case = smallest primes.  GUESS (implemented)
O7  prime mass: exact sum p <= 1.2e7 + Dusart tail (guarded, review F1/F2).                            DONE
O8  interval certificates on [X(H), 10^K] and asymptotic closure.                                       OPEN
O9  finite range D < X(H): class numbers computed directly.                                            OPEN

## step 1 result (exploratory point thresholds X(H); falsifier vs PARI passed)
H=1: 1.42e4 · H=2: 6.6e4 · H=3: 1.55e5 · H=5: 4.3e5 · H=10: 2.39e6   (true max D with h<=H: 163, 427, 907, 2683, 13843)
