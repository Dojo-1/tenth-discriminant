"""Phase390: independent high-precision Decimal scalar sign check.

The scalar expressions are transcribed from Phase355Scalar302.lean,
but this is NOT the Lean rational-log certificate; Decimal.ln() is
a numerical consistency check only. Requires CPython >=3.11.
"""
from decimal import Decimal,localcontext

def scalar_difference(t):
    if not isinstance(t,int) or t<1:raise ValueError("positive integer fourth root required")
    with localcontext() as ctx:
        ctx.prec=75
        z=lambda x:Decimal(x)
        D=t**4;R=D//4
        d=z(D);r=z(R);ld=d.ln();l2=z(2).ln()
        lower=(z(999997)/1000000*ld-z(57193)/10000+l2/4
               +z(4659)/625000-z(16895455)/(625000*d)
               +z(6931)/1000000-z(2)/r
               +z(873747)/250000000-z(40)/r)
        upper=z(4)/5*ld-z(1923)/2000
        return {"t":t,"D":D,"R":R,
                "lower_minus_upper":str(lower-upper),
                "status":"DECIMAL_DIAGNOSTIC_NOT_ANALYTIC_CERTIFICATE"}

if __name__=="__main__":
    for t in (300,301,302,303):
        print(scalar_difference(t))
