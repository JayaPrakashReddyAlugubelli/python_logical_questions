# input  s = 'abc'
#  output :
#  abc
# acb
# bac
# bca
# cab
# cba


import itertools

# Original string
s = 'abc'

# Generate all permutations
permutations = itertools.permutations(s)



# Print each permutation
for p in permutations:
    print(''.join(p))
