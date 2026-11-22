#!/usr/bin/env python3
"""Source-typed ordinary fourth-jet discrete translation identity at p=3.

For S=4 so k<=3, let z_t=z+3t. For all legal Frobenius-normalized
source rows, j3(z_t)-j3(z_0)=t*sum_{u=0}^2 j0(z_u) mod3.
This is a paper theorem from D^3=2*d/dq for q=(Z^3-W)/3, not a new
determinant valuation. The S=5,k=4 counterexample is deliberately retained.
"""
from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/"phase386"))
from source_jet_histogram import production_row_jet

def check(D,stop):
    total=0
    for x in range(3):
        for y in range(9):
            locations=[(x+3*t,y) for t in range(3)]
            for r in range(stop):
                for s in range(4):
                    jets=[production_row_jet(D,3,r,s,4,4,z)
                          for z in locations]
                    sum0=[sum(v[0][c] for v in jets)%3 for c in (0,1)]
                    for t in (1,2):
                        assert all((jets[t][3][c]-jets[0][3][c]-t*sum0[c])%3==0
                                   for c in (0,1)),(D,x,y,r,s,t)
                        total+=1
    return total

def main():
    for D in (19,43,283,403,412,7):
        assert D%3==1
        stop=100 if D==403 else 38
        count=check(D,stop)
        print("PASS discrete translation D",D,"r rows",stop,
              "source comparisons",count)
    # S=5 admits k=4, for which the degree<=3 argument is FALSE:
    z=[(3*t,0) for t in range(3)]
    jets=[production_row_jet(403,3,12,0,5,4,a) for a in z]
    sum0=sum(v[0][0] for v in jets)%3
    assert (jets[1][3][0]-jets[0][3][0])%3!=sum0
    # Non-inert p3 cannot silently inherit the integral quotient.
    try:
        production_row_jet(2,3,3,0,4,4,(0,1))
    except AssertionError:
        pass
    else:raise AssertionError("non-inert negative control failed")
    print("PASS S=5/k4 and non-inert hostile controls")

if __name__=="__main__":main()
