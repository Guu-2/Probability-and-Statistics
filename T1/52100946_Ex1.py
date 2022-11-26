#60 chữ số ko trùng

# A = {1 , 2 , 3 ,  4 , 5}

import itertools

from numpy import choose

E = { 1 , 2 , 3 , 4 , 5}

k = 3

n = len(E)

choose_k = list(itertools.permutations(E , k))

print("%i - permutations of %s " %(k , E))
 
for i in choose_k:
    print(i)

print("Number of combinations = %i!/(%i!(%i - %i)!) = %i" %(n , k , n , k  , len(choose_k)))

