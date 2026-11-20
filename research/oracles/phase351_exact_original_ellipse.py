#!/usr/bin/env python3
"""Phase351: exact finite integer-ellipse endpoints b=298..307 only.

Original Tuned source: D=b^4, R=D//4, S=R//25,
thinRadius=ceil((11/25)*fourthRoot(D)^3).
The original Qthin is {(x,y) in Z^2: x*x+D*y*y<=thinRadius^2}.
Count it by exact vertical integer slices; never enumerate billions
of samples, use a floating circle area, or change the original source.

This is a BOUNDED experimental study, not a theorem for every D>=b^4.
The separately evaluated numerical lower/upper functions use exactly
the Phase348/347 scalar formulas, but their existence as original
Gram bounds below 307^4 is NOT proved by this script.
"""
from math import isqrt
from decimal import Decimal, localcontext
import json

def ceil_div(a, b):
    return -(-a // b)

def exact_ellipse_count(d, radius):
    y_max = isqrt(radius * radius // d)
    count = 0
    for y in range(-y_max, y_max + 1):
        remainder = radius * radius - d * y * y
        assert remainder >= 0
        count += 2 * isqrt(remainder) + 1
    return count, y_max

def scalar_gap(d, r):
    with localcontext() as ctx:
        ctx.prec = 65
        v = Decimal
        d, r = v(d), v(r)
        lower = (v(999997)/v(1000000))*d.ln() - v(57193)/v(10000)
        lower += v(2).ln()/4
        lower += v(4659)/v(625000)-v(16895455)/(v(625000)*d)
        lower += v(6931)/v(1000000)-v(2)/r
        lower += v(873747)/v(250000000)-v(40)/r
        upper = (v(4)/v(5))*d.ln()-v(1923)/v(2000)
        return lower - upper

def report():
    rows=[]
    for b in range(298, 308):
        d=b**4
        r=d//4
        s=r//25
        thin=ceil_div(11*b**3, 25)
        padded=ceil_div(13*b**3, 25)
        n,y_max=exact_ellipse_count(d,thin)
        needed=2*(r-1)+(s-1)
        gap=scalar_gap(d,r)
        rows.append({
            "b":b,"D":d,"R":r,"S":s,"thin_radius":thin,
            "padded_radius":padded,"max_abs_y":y_max,
            "original_Qthin_card":n,"required_interpolation":needed,
            "exact_count_surplus":n-needed,
            "conservative_cell_guard":(32593*b>=10000000),
            "phase343_scalar_lower_minus_upper_diagnostic":str(gap),
            "direct_count_pass_at_this_D":n>needed,
            "scalar_formulas_separated_at_this_D":gap>0
        })
        assert n>needed
    assert rows[-2]["b"]==306 and not rows[-2]["conservative_cell_guard"]
    assert rows[-1]["conservative_cell_guard"]
    assert not rows[3]["scalar_formulas_separated_at_this_D"]  # b=301
    assert rows[4]["scalar_formulas_separated_at_this_D"]      # b=302
    return rows

if __name__=="__main__":
    rows=report()
    print(json.dumps({
      "evidence":"bounded exact integer sample-count and high-precision scalar diagnostic",
      "not_proved":"uniform b>=302 or all D>=302^4, positive Gram, source-aligned analytic upper/lower below 307^4, field bound",
      "cases":rows
    },indent=2))
