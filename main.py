from sympy.utilities.iterables import multiset_permutations
import numpy as np

a = np.array([0,1,2,3,4,5])
b = []

for p in multiset_permutations(a, size=5):
    if p[0] != 0 and sum(p)%3 == 0:
        b.append(p)

print(len(b))