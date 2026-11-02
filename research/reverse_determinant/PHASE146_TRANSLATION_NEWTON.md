# Phase146 — Up/down integer translations, moving grading, and Newton-fiber support

31 October 2026. **[P-paper]** classical binomial, Newton finite-difference and integral-index statements, derived for the *original ordinary* Z-jet convention. **[M]** finite exact integer experiments, bounded D range and matched controls. **[H]** uniform production compression and any improvement of the actual discriminant bound remain open. **[R]** the strong fixed-six-point all-D speculation is false. No Lean claim, no holonomy measurement, and no PR or merge.

Source lineage: [Phase140 original ordinary jets](../ellipsoid_trimming/phase140_exact_trim.py), [Phase144 image/cokernel](phase144_verifier.py), [six-point minimum certificate](phase144_minimum_support.py), [Phase145 ortho/anti/ambig](phase145_ortho_anti_ambig.py). The [Phase146 exact verifier](phase146_translation_newton.py) imports the prior sources unchanged and checks an independently parameterized implementation against the *exact original source* at D=19. Traces retain $B_Q=\operatorname{diag}(2,2D,\dots)$ and both real/imaginary integer observation coordinates.

## The integer moving frame is an exact automorphism, not a renamed point cloud

Let $F_{r,s}(Z,W)=Z^rW^s$ ($0\le r<R,\ 0\le s<S$). Derivatives remain **ordinary partial $\partial_Z^j$ with $W$ held fixed**, $0\le j<J$. For integer real-axis translation $a$, introduce the unitriangular integer polynomial-row operator

$$
(T_a)_{(r,s),(u,v)}
=
\begin{cases}
{r\choose u}{s\choose v}\,a^{r+s-u-v}, & u\le r,\ v\le s,\\
0,&\text{otherwise}.
\end{cases}
$$

For **every** $D>0$, finite pair set $Q$, and dimensions $R,S,J$, the ordinary-binomial identity gives, with matched column order,

$$ E_{Q+(a,0)}=T_aE_Q,\quad
G_{Q+(a,0)}=T_aG_QT_a^{\mathsf T},\quad
T_aT_b=T_{a+b},\quad \det T_a=1.$$

Thus determinants agree and $C_{Q+(a,0)}\cong C_Q$ as abstract abelian groups. **The fixed-coordinate image need not be equal**: it is $T_aM_Q$. In the frozen $D=19,R=8,S=J=4,\rho=5$ example, the known [Phase144] $Q_6$ and $Q_6+(1,0)$ both lie inside $\Omega_{19,5}$ and both generate $M_\Omega$. Consequently $T_1M_\Omega=M_\Omega$ exactly. This follows from inclusion plus equal covolume; the verifier also checks identical HNF and directly checks $H^{-1}T_1H$ integral unimodular.

## Ortho/anti gauge compatibility is distinguishable from fixed-frame artefacts

Let $P_{(r,s)}=(-1)^{r+s}$ and $\Pi_P(G)=\tfrac12(G+PGP^{\mathsf T})$ for an involution. For an arbitrary invertible $T$, transport **both** the Gram and its grading: $G'=TGT^{\mathsf T}$, $P'=TPT^{-1}$. Then exactly

$$ \Pi_{P'}(G')=T\Pi_P(G)T^{\mathsf T},\qquad
\chi_{P'}(G')=\log\frac{\det\Pi_{P'}(G')}{\det G'}
=\chi_P(G).$$

Here $T=T_a$ for integer translations or $T=T_{-c}$ for rational centering. In the latter case the determinant identity is still exact **over $\mathbb Q$**, but there is no automatic integral-lattice transport: denominator effects must be tracked, especially at $p=2$.

**Measured [M]**: with the six-point support, $\chi_P(G)\approx19.995899166040$. Translating by $a=2$ leaves the determinant unchanged; using the **old** grading $P$ instead yields $\chi_P(G_{Q_6+2})\approx61.054717175$, whereas transporting $P_2=T_2PT_{-2}$ restores exactly the original ratio. This $a=2$ test deliberately leaves the radius-five sampling ellipse. It is a **pure gauge negative control**, not an admissible improved support.

## A genuinely inverse-free analytic upper by rational centering [P-paper + M]

For any real/rational centre $c$, use the unitriangular row basis $(Z-c)^r(W-c)^s$. It has determinant one, so the **same original** integer Gram determinant is unchanged by its congruence, even when the row matrix is only rational. The exact diagonal becomes

$$
g_{r,s}^{(c)}
=2\sum_{(x,y)\in Q}\ \sum_{j=0}^{\min(r,J-1)}
(r)_{\underline j}^2
\big((x-c)^2+Dy^2\big)^{r+s-j}.
$$

For positive definite $G_Q$, Hadamard gives the rigorous upper

$$
\log\det G_Q \le \sum_{r,s}\log g_{r,s}^{(c)}
\le \sum_{r,s}
\log\Big[2|Q|\sum_{j\le\min(r,J-1)}
(r)_{\underline j}^2 (\rho_c^2)^{r+s-j}\Big],
\quad \rho_c^2=\max_{(x,y)\in Q}[(x-c)^2+Dy^2].
$$

Nothing invokes the unknown inverse Gram, and neither upper assumes divisibility of a *different* Gram integer. The choice of centre is geometrical and explicit.

Frozen $Q_6$, $D=19$ [M]: moving $c=0\to-\tfrac12$ lowers $\rho_c^2$ from $23$ to $85/4$; the **exact-diagonal** logarithmic Hadamard upper drops $580.46012919\to577.86796190$; the weaker **radius-only** upper drops $606.96047266\to596.21055438$. The determinant stays fixed, $\log\det G_6\approx424.34264224$. The current upper remains too loose to imply a new production bound. In particular a rational *row frame* is allowed as an analytic upper, but must not be used to claim integral valuation transport to a new sample support.

## A typed arithmetic boundary remainder [P-paper + M]

For $M=\operatorname{im}_\mathbb Z E_Q\subseteq\mathbb Z^{RS}$ of full rank, define

$$ \Delta_{+}(M)=(M+T_1M)/M.$$

This finite abelian group is exactly the **translation-image closure defect**. $\Delta_+(M)=0$ iff $T_1M\subseteq M$; unimodularity of $T_1$ and equal finite covolume then imply $T_1M=M$.

If $Q$ is a union of contiguous horizontal integer fibers, the global test reduces to the **rightmost boundary** of each fiber. All translated columns at interior points already belong to $M$; only each missing right-neighbour's entire ordinary-jet block needs integral membership. For antipodally symmetric $Q$, $PM=M$ and $PT_1P=T_{-1}$, so $\Delta_+(M)\cong\Delta_-(M)$; this is exact transport of a typed quotient, not a curvature claim.

Exact [M] scan for $\rho=5$, $R=8$, $S=J=4$:

| $D$ | Points | $|\Delta_+(M)|$ | Nontrivial Smith factors |
|---:|---:|---:|---|
| 17 | 21 | 1 | — |
| 18 | 21 | 9 | 3, 3 |
| 19 | 21 | 1 | — |
| 22 | 17 | 1 | — |
| 23 | 17 | 16 | 2, 2, 2, 2 |
| 24 | 17 | 256 | 4, 4, 4, 4 |
| 25 | 13 | 1,474,560,000 | 4, 4, 4, 4, 20, 20, 120, 120 |
| 26 | 11 | 1 | — |

All $D=1,\dots,26$ were tested, and translation instability occurred precisely at $D=18,23,24,25$. The verifier checks the boundary-membership test against the full HNF conjugation test and independently computes the relative Smith factors of the enlarged lattice $\operatorname{im}[H\ \ T_1H]$. It does *not* prove that these are the only exceptional parameters for other $\rho,R,S,J$.

## Counterworld: fixed six-point image preservation is not uniform

The known Phase144 six-point set lies in the radius-five ellipse when $D\le21$. For the complete integer sweep $D=1,\dots,21$, its integral image equals the full ellipse image **only** for $D=3,4,6,10,12,16,19$. Nearby exact relative indices: $D=13:16$; $D=17:1296$; $D=19:1$; $D=21:112$. This falsifies the strong claim that one literal six-point support works for every admissible $D$. The scan includes nonsquarefree/even $D$ as *ordinary-jet matrix controls*, not as hypotheses for the class-number theorem.

A universal statement still survives: $T_a$ gives an exact polynomial row transport for every parameter. The assertion that a chosen compact support generates the same integral image is **additional arithmetic content** and has its own typed failure group.

## The Newton-fiber lift: a valid universal image theorem with a production barrier

Every fixed $(r,s,j)$ real/imaginary ordinary-jet coordinate, as a function of the *integer horizontal coordinate* $x$ at fixed $y$, is an integer polynomial of degree at most $d_{\max}=R+S-2$. For a consecutive fiber starting at $x_0$, the integer Newton recurrence for any polynomial of degree at most $d_{\max}$ is

$$
f(x_0+d_{\max}+1)=
\sum_{i=0}^{d_{\max}}(-1)^{d_{\max}-i}
{d_{\max}+1\choose i}\,f(x_0+i).
$$

Iterating expresses every later point's **entire ordinary-jet column** as an integer combination of the first $d_{\max}+1$ points. Therefore retaining $\min\{|F_y|,R+S-1\}$ consecutive nodes per horizontal fiber preserves the **entire integral column image**, for arbitrary $D,R,S,J$ and any finite support with contiguous horizontal fibers. This is a classical finite-difference proof, not new asymptotic machinery.

Independent exact HNF controls with $R=3,S=J=2,\rho=5$:
- $D=1$: 81 nodes -> 38 nodes, same image.
- $D=3$: 43 -> 20, same image.
- $D=19$: 21 -> 12, same image.
- $D=26$: 11 -> 4, same image.
Also $D=3,R=4,S=J=2$: 43 -> 25, same image. Exact one-step recurrence was checked on every trimmed horizontal fiber.

**Production negative control.** At the explicit endpoint $D=450^4=41,006,250,000$ with current $R=D/4,\ S=R/25,\ \rho=(13/25)(450)^3=47,385,000$, the *longest possible* horizontal fiber has only $2\rho+1=94,770,001$ nodes, whereas the Newton window needs $R+S-1=10,661,624,999$—over 112 times as many. The simple construction therefore trims **nothing** at that floor. The same scaling ($R=\Theta(D)$ versus $\rho=\Theta(D^{3/4})$) warns against expecting it to help asymptotically without a sharper use of the available ordinary derivatives.

## What survives and what is not established

**Surviving [P-paper]:** a unimodular integer translation action, covariant parity pinching, rational analytic same-determinant frame bounds, a typed finite arithmetic boundary quotient, and a Newton finite-difference image-preserving support theorem. **Reproduced [M]:** bounded D-image failures, integer boundary quotient factors, a gauge-control measurement, and five small Newton-HNF checks. **Retired [R]:** universal sufficiency of the fixed six-point shape; any suggestion that the coarse Newton cap by itself cuts production samples. **Open [H]:** an integral-image support theorem with an effective size $O(RS/J)$ or similar, using the *actual* ordinary Z-jets and controlling all Smith obstructions and analytic upper cost. A naive transfer of univariate Hermite derivative interpolation is not permitted: $\partial_x=\partial_Z+\partial_W$, whereas this repository exposes only $\partial_Z$ jets holding $W$ fixed.

The next discriminating experiment should compare original ordinary jets against equal-compute derivative-degree and modular-rank controls, not import a changed jet convention or an inverse-Gram-optimized basis. No improved field discriminant, Lean compilation, global holonomy, or new complexity conclusion follows from Phase146.

**Execution:** install SymPy 1.14 and run python3 research/reverse_determinant/phase146_translation_newton.py from the repository root. Its source-compatibility check is explicit. Source-matched GitHub CI should be cited **only once the exact-head run has completed**; full data are integers/rationals, displayed natural logarithms are approximate.
