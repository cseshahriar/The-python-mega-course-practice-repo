""" Itertools: product, permutation, combinations, accumulate, groupby, 
    and infinite iterators
"""
from itertools import product, permutations

""" product """
a = [1, 2]
b = [3, 4]
product_data = product(a, b)
print(list(product_data))


""" permutation """
c = [1, 2, 3]
perm = permutations(c)
print(list(perm))
