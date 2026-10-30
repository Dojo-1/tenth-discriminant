"""Sealed rational arithmetic only; does not verify analytic premises."""
from fractions import Fraction as F
from pathlib import Path
import json
import sys

checks=[
 ('ceiling_absorption',F('0.521')*450**3-F('0.52')*450**3-1,'positive'),
 ('inner_radius',F('0.495')**2*F('3.14')-F('0.76'),'positive'),
 ('chosen_radius_guard',F('0.52')-F('1.001')*F('0.495')-F(10,450),'positive'),
 ('upper_count',4-(4*F('0.521')**2+2*F('0.521')/450+2*F('0.521')/450**3+F(1,450**4)),'positive'),
 ('centered_rounding',F(1,2)+F(1,2*5**2)-F(13,25),'zero'),
 ('derivative_gain',F(13,20)-(F(13,25)+F(1,8)),'nonnegative'),
 ('scale_saving',16*F('0.99')*F('0.43')/676-F(1,100),'positive'),
 ('normalized_constant',F('0.65')+F('0.04')*F('4.11')-F('0.00025')-F('0.001')-F('0.813'),'positive'),
 ('published_endpoint',F('0.199997')*F('24.5813')-F('4.916'),'positive'),
 ('coarse_endpoint',F('0.199997')*F('24.58')-F('4.916'),'negative'),
]
assert len(checks)==10
records=[]
for name,value,relation in checks:
 passed={'positive':value>0,'negative':value<0,'nonnegative':value>=0,'zero':value==0}[relation]
 records.append({'name':name,'numerator':value.numerator,'denominator':value.denominator,'relation':relation,'passed':passed})
 assert passed,(name,value,relation)
Path(sys.argv[1]).write_text(json.dumps({'checks':records,'scope':'Rational arithmetic only;no analytic premise or new cutoff verified'},indent=2)+'\n',encoding='utf-8')
print('PASS: all10 fixed rational checks; analytic premises remain separate; no endpoint search.')
