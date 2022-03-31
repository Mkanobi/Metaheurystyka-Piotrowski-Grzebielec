import scipy.stats as sp
from wilcoxon_prepper import quality_tester

lst = quality_tester(500)

res, pval = sp.wilcoxon(lst[0], lst[1])
print("100-random vs Near")
print(res)
print(pval)

res, pval = sp.wilcoxon(lst[1], lst[2])
print("Near vs Ext")
print(res)
print(pval)

res, pval = sp.wilcoxon(lst[2], lst[3])
print("Ext vs 2-OPT")
print(res)
print(pval)

res, pval = sp.wilcoxon(lst[0], lst[2])
print("100-random vs Ext")
print(res)
print(pval)

# res, pval = sp.wilcoxon(lst[0], lst[1])
# print(res)
# print(pval)