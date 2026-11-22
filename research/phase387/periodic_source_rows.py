#!/usr/bin/env python3
"""Exact controls for eventual periodicity of ordinary Frobenius-normalized
source jets modulo odd inert p. Paper proof is in PERIODIC_SOURCE_ROWS.md.
"""
from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/"phase386"))
from source_jet_histogram import production_row_jet

def test():
    S=J=4
    for D in (19,43,283,403,412):
        assert D%3==1 # -D nonsquare mod3
        count=0
        for x in range(9):
            for y in range(9):
                for s in range(S):
                    for r in range(13,76):
                        a=(x,y)
                        assert production_row_jet(D,3,r+24,s,S,J,a,1)==production_row_jet(D,3,r,s,S,J,a,1)
                        count+=1
        assert count==20412
        print("PASS period24 D",D,"source jet comparisons",count)
    D,p=3,5
    # The same algebraic theorem predicts L=p*(p^2-1)=120.
    for s in range(S):
        for r in range(p*(S-1-s)+J,29):
            for a in ((0,0),(1,0),(0,1),(2,3),(4,5),(24,24)):
                assert production_row_jet(D,p,r+120,s,S,J,a,1)==production_row_jet(D,p,r,s,S,J,a,1)
    print("PASS period120 for inert p5/D3 source")
    for length,r,s,a in ((8,13,0,(0,1)),(12,13,0,(1,1)),(16,13,0,(0,1))):
        assert production_row_jet(403,3,r+length,s,S,J,a,1)!=production_row_jet(403,3,r,s,S,J,a,1)
    print("PASS hostile shorter-period controls 8,12,16")

if __name__=="__main__":test()
