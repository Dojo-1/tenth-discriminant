#!/usr/bin/env python3
"""E13: original ordinary Z jets transported through U=Z,V=W-Z.

D_Z at fixed W = D_U - D_V, not the tangential D_U on a horizontal fiber.
"""
import sympy as s
U,V,Z,W=s.symbols('U V Z W')
def transported(F,j):
    return s.expand(sum(s.binomial(j,k)*(-1)**k *
        s.diff(F,U,j-k,V,k) for k in range(j+1)))
tests=0
for r in range(8):
    for degreeW in range(6):
        new=U**r*(U+V)**degreeW
        original=Z**r*W**degreeW
        for j in range(6):
            left=s.expand(s.diff(original,Z,j).subs({Z:U,W:U+V}))
            right=transported(new,j)
            assert s.expand(left-right)==0
            tests+=1
assert transported(U*(U+V),1)==U+V
assert s.diff(U*(U+V),U)!=U+V
print('PASS',tests,'source-preserving moving-frame jet identities.')
print('False control: tangential d/dU changes the original source derivative.')
