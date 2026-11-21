#!/usr/bin/env python3
"""Finite Gauss/character crosscheck for all 62 fundamental negative D with |D|<=199.

This deliberately reuses and cites Phase378's independently implemented
(two algorithmic routes) enumeration. No Heegner classification is imported.
"""
import importlib.util
from pathlib import Path

source = Path(__file__).resolve().parents[1] / 'phase378' / 'tao_zero_free_1024.py'
assert source.exists(), f'missing pinned Phase378 source {source}'
spec=importlib.util.spec_from_file_location('phase378_finite',str(source))
mod=importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)
sieve=mod.squarefree_sieve(199)
fundamental=[d for d in range(1,200) if mod.is_fundamental(-d,sieve)]
assert len(fundamental)==62, ('unexpected fundamental count',len(fundamental))
forms=[]; characters=[]
for d in fundamental:
 h1=mod.count_reduced_primitive_forms(-d)
 h2=mod.class_number_from_character(-d)
 assert h1==h2,('class-number discrepancy',d,h1,h2)
 if h1==1:forms.append(d)
 if h2==1:characters.append(d)
expected=[3,4,7,8,11,19,43,67,163]
assert forms==characters==expected
print('PASS: 62 negative fundamental discriminants <=199, two class-number algorithms agree')
print('The nine absolute class-number-one discriminants:',forms)
