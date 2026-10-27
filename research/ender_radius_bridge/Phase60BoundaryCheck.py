"""One preregistered per-form boundary check; no class number is computed."""
import json
import math
import sys
from fractions import Fraction as Q

def factors(n):
    answer = []
    d = 2
    while d*d <= n:
        e = 0
        while n % d == 0:
            n //= d
            e += 1
        if e:
            answer.append([d,e])
        d += 1
    if n > 1:
        answer.append([n,1])
    return answer

def isprime(n):
    return n >= 2 and all(n % d for d in range(2, math.isqrt(n)+1))

def scan(a,b,c,t):
    D = 4*a*c-b*b
    X = math.isqrt((4*c*t)//D)
    Y = math.isqrt((4*a*t)//D)
    prime_points = []
    all_points = []
    for x in range(-X,X+1):
        for y in range(-Y,Y+1):
            value = a*x*x+b*x*y+c*y*y
            if value <= t:
                all_points.append([x,y,value])
            if 3 <= value <= t and value % 2 and isprime(value):
                prime_points.append([x,y,value])
    return {"form":[a,b,c],"D":D,"t":t,"coordinate_bounds":{"X":X,"Y":Y},
            "bound_justification":"4aQ=(2ax+by)^2+D*y^2;4cQ=(2cy+bx)^2+D*x^2",
            "prime_representations":prime_points,"all_points_Q_le_t":all_points}

a,b,c,t,p = 3,1,1001,3,3
D = 4*a*c-b*b
fac = factors(D)
residue = (-D) % p
witnesses = [x for x in range(p) if x*x % p == residue]
guards = {"positive":a>0 and D>0,"primitive":math.gcd(math.gcd(a,abs(b)),c)==1,
          "reduced":-a < b <= a <= c and not (a==c and b<0),
          "D_mod4":D % 4 == 3,"squarefree":all(e==1 for _,e in fac),
          "odd_prime":isprime(p) and p>2,"unramified":D % p != 0,
          "nonzero_square":residue != 0 and bool(witnesses),
          "rational_enclosure_guards":D>100**2 and a*t==9}
output={"python":sys.version.split()[0],"fixed_case":[a,b,c,t,p],"D":D,
        "D_factorization":fac,"guards":guards,"square_residue":residue,"square_witnesses":witnesses,
        "class_number":"NOT_COMPUTED","aggregate_split_bound":"NOT_TESTED",
        "h_le_2_cutoff":"NOT_REFUTED_BY_THIS_TEST","h1_result":"UNCHANGED"}
if not all(guards.values()):
    output["status"]="INCONCLUSIVE_GUARD_FAILURE"
    print(json.dumps(output,indent=2))
    raise SystemExit(2)
case=scan(a,b,c,t)
control=scan(1,1,3003,t)
assert case["D"]==control["D"]==12011
assert case["prime_representations"]==[[-1,0,3],[1,0,3]]
assert control["prime_representations"]==[]
# For this fixed case U=(6*pi+12)/sqrt(D)+1 <36/100+1=34/25.
upper=Q(36,100)+1
count=len(case["prime_representations"])
assert upper==Q(34,25)<count
output.update(status="PER_FORM_ESTIMATE_VIOLATED",case=case,principal_control=control,
              candidate_expression="2*pi*t/sqrt(D)+4*sqrt(a*t/D)+1",
              rigorous_upper_exclusive=str(upper),actual_prime_representation_count=count,
              enclosure_basis="pi<4;D>100^2;a*t=9;all comparisons exact",
              interpretation="Counterexample to the suggested per-form estimate only; no aggregate or higher-class-number conclusion.")
print(json.dumps(output,indent=2))
