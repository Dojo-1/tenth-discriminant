"""Independent NumPy enumeration for the Phase269 bounded inert-prime sieve.

No class number computation, no fundamental-discriminant filter.
Every acceptance test is a necessary condition for h(-d)=1 at d>163.
"""
import numpy as np

LIMIT=322**4
first=[3,5,7,11,13,17,19]
rest=[23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101,103,107,109]
expected=[1717429,829089,401173,195269,95237,46513,22527,10809,5138,
          2469,1199,589,284,133,74,29,16,9,6,2,0]
W=8
for p in first:
    W*=p
wheel=np.arange(3,W,8,dtype=np.int64)
for p in first:
    sq={(x*x)%p for x in range(p)}
    allowed=np.array([r for r in range(p) if ((-r)%p) not in sq],dtype=np.int64)
    wheel=wheel[np.isin(wheel%p,allowed)]
assert W==38798760 and wheel.size==12960

# Different enumeration order from the C++ implementation.
base=np.arange(LIMIT//W+1,dtype=np.int64)*W
nums=(wheel[:,None]+base[None,:]).ravel()
nums=nums[(nums>163)&(nums<LIMIT)]
assert nums.size==3590972
print("initial", nums.size)
for i,p in enumerate(rest):
    sq={(x*x)%p for x in range(p)}
    allowed=np.array([r for r in range(p) if ((-r)%p) not in sq],dtype=np.int64)
    nums=nums[(nums<=4*p)|np.isin(nums%p,allowed)]
    print(p, nums.size)
    assert nums.size==expected[i]
    if p==107:
        assert sorted(nums.tolist())==[585811843,1764959683]
assert nums.size==0
assert (1*1+163)%41==0 and not (4*41<163)
assert (41*41+585811843)%109==0
assert (6*6+1764959683)%109==0
print("PASS")
