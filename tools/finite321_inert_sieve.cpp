#include <cstdio>
#include <vector>
#include <cstdint>
#include <algorithm>

// Phase269: exact integer-only CRT sieve; no PARI, sympy, or class-number input.
// Hypothesis: for fundamental -d with h(-d)=1 and d>163, every prime p<d/4
// is inert. We reject a SUPerset of fundamental discriminants.
using u64 = unsigned long long;

int main() {
  const u64 LIMIT = 10617447681ULL; // 321^4, exclusive
  const int first[] = {3,5,7,11,13,17,19};
  const int rest[] = {
    23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101,103,107,109
  };
  const int W = 38798760; // 8*3*5*7*11*13*17*19

  std::vector<std::vector<unsigned char>> nonresidue(110);
  for (int p : first) {
    std::vector<bool> sq(p, false);
    for (int x=0; x<p; ++x) sq[(x*x)%p] = true;
    nonresidue[p].resize(p);
    for (int r=0; r<p; ++r)
      nonresidue[p][r] = (r!=0 && !sq[(p-r)%p]);
  }
  for (int p : rest) {
    std::vector<bool> sq(p, false);
    for (int x=0; x<p; ++x) sq[(x*x)%p] = true;
    nonresidue[p].resize(p);
    for (int r=0; r<p; ++r)
      nonresidue[p][r] = (r!=0 && !sq[(p-r)%p]);
  }

  int checkW = 8;
  for (int p:first) checkW *= p;
  if (checkW != W) return 2;

  std::vector<int> wheel;
  for (int r=3; r<W; r+=8) {
    bool ok=true;
    for (int p:first) if (!nonresidue[p][r%p]) { ok=false; break; }
    if (ok) wheel.push_back(r);
  }
  std::printf("wheel W=%d residues=%zu\n", W, wheel.size());

  u64 total=0, eliminated[21]={}, survivors=0;
  for (int r:wheel) {
    for (u64 d=r; d<LIMIT; d+=W) {
      if (d<=163) continue;
      ++total;
      bool ok=true;
      for (size_t i=0; i<21; ++i) {
        int p=rest[i];
        // Strict: inertness is required only for 4*p<d.
        if (static_cast<u64>(4*p)>=d) continue;
        if (!nonresidue[p][d%p]) {
          ++eliminated[i];
          ok=false;
          break;
        }
      }
      if (ok) {
        ++survivors;
        std::printf("unexpected survivor=%llu\n", d);
      }
    }
  }

  std::printf("wheel candidates 164 <= d < LIMIT: %llu\n", total);
  u64 left=total;
  const u64 expected[21] = {
    1696178,818872,396251,192895,94091,45960,22255,10671,5062,2437,
    1178,578,281,132,74,29,16,9,6,2,0
  };
  bool counts_ok=(wheel.size()==12960 && total==3546560 && survivors==0);
  for (int i=0; i<21; ++i) {
    left-=eliminated[i];
    std::printf("prime=%d remaining=%llu\n",rest[i],left);
    if (left!=expected[i]) counts_ok=false;
  }
  // Negative endpoint control: p=41 is NOT required at d=163.
  if (!(4*41>163 && (1*1+163)%41==0)) counts_ok=false;
  // The last two candidates each have an explicit square root at p=109.
  if (!(4*109<585811843 && (41*41LL+585811843LL)%109==0)) counts_ok=false;
  if (!(4*109<1764959683 && (6*6LL+1764959683LL)%109==0)) counts_ok=false;
  std::printf("survivors=%llu checks=%s\n",survivors,counts_ok?"PASS":"FAIL");
  return counts_ok?0:1;
}
