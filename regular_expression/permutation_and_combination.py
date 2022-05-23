# https://www.geeksforgeeks.org/python-itertools-permutations/
# https://www.geeksforgeeks.org/permutation-and-combination-in-python/

from itertools import permutations
from itertools import combinations

a = "ABCD"

p = permutations(a)
for i in list(p):
    print(i)

comb = combinations(a, 2)
for j in list(comb):
    print(j)
