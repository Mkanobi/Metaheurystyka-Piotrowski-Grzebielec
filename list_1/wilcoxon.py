import scipy.stats as sp
import numpy as np
from wilcoxon_prepper import quality_tester

lst = np.array(quality_tester(100))

print()

res, pval = sp.wilcoxon(lst[0], lst[1])
print("100-random vs Near")
print(pval)

print()

res, pval = sp.wilcoxon(lst[1], lst[2])
print("Near vs Ext")
print(pval)

print()

res, pval = sp.wilcoxon(lst[2], lst[3])
print("Ext vs 2-OPT")
print(pval)

print()

res, pval = sp.wilcoxon(lst[0], lst[2])
print("100-random vs Ext")
print(pval)
print()

res, pval = sp.wilcoxon(lst[1], lst[2])
print("100-random vs 2-OPT")
print(pval)
print()

res, pval = sp.wilcoxon(lst[1], lst[2])
print("Near vs 2-OPT")
print(pval)