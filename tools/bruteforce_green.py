"""Control 2: verify Green's three determinant facts exactly on small instances.
Elements of Z[sqrt(-D)] as pairs (a,b) = a + b*sqrt(-D). Gram entry <u,v> = sum tr(u_k * conj(v_k)),
tr((a1+b1 w)(a2-b2 w)) = 2(a1 a2 + D b1 b2) for w=sqrt(-D)."""
import sys, math, itertools, subprocess
sys.path.insert(0, 'tools')
from green_h1 import F_exact
from sympy import primerange, legendre_symbol

def mul(u, v, D): return (u[0]*v[0] - D*u[1]*v[1], u[0]*v[1] + u[1]*v[0])
def pw(u, e, D):
    r = (1, 0)
    for _ in range(e): r = mul(r, u, D)
    return r
def falling(r, j):
    out = 1
    for i in range(j): out *= (r - i)
    return out

def rows(R, S, J, N, D):
    pts = [((x, y), (x, -y)) for x in range(N) for y in range(N)]
    V = []
    for r in range(R):
        for s in range(S):
            row = []
            for (z, zp) in pts:
                for j in range(J):
                    if j > r: row.append((0, 0)); continue
                    c = falling(r, j)
                    t = mul(pw(z, r - j, D), pw(zp, s, D), D)
                    row.append((c * t[0], c * t[1]))
            V.append(row)
    return V

def gram(V, D):
    return [[sum(2*(a[0]*b[0] + D*a[1]*b[1]) for a, b in zip(u, v)) for v in V] for u in V]

def det_gp(M):
    s = "matdet([" + ";".join(",".join(map(str, r)) for r in M) + "])"
    return int(subprocess.run(["gp", "-q", "-D", "colors=no", "-s", "512M"], input=s, capture_output=True, text=True).stdout.strip())

def vp(n, p):
    k = 0
    while n % p == 0: n //= p; k += 1
    return k

def main():
  fails = 0
  for D in [7, 11, 19, 23, 31, 43, 47]:
      for (R, S, J) in [(3, 2, 3), (4, 2, 3), (5, 2, 4), (6, 3, 4), (7, 2, 5), (8, 2, 6)]:
          N = J
          while N > 1 and N*N*J > 2*R*S + J*(R+S) and (N-1) <= J: N -= 1
          N += 1
          if not (J >= N and N*N*J > 2*R*S + J*(R+S)): continue
          G = gram(rows(R, S, J, N, D), D)
          det = det_gp(G)
          B2 = (N-1)**2 * (1 + D)
          hada = math.prod(G[i][i] for i in range(len(G)))
          ok1 = det > 0
          ok2 = det <= hada
          ok3 = True; inert = []
          for p in primerange(3, R + 1):
              if D % p and legendre_symbol((-D) % p, p) == -1:
                  inert.append(p)
                  if vp(det, p) < 2 * F_exact(p, R, S): ok3 = False
          good = ok1 and ok2 and ok3
          fails += not good
          print(f"D={D:3d} R={R} S={S} J={J} N={N}: det>0 {ok1}  det<=Hadamard {ok2}  v_p>=2F {ok3} inert={inert}" + ("" if good else "  <-- FAIL"))
  print("FAILURES:", fails)


if __name__ == "__main__":
    main()