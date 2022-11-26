import itertools

from numpy import choose

E = { 'a' , 'b' , 'c' , 'd'}

k = 3


n = len(E)

choose_k = list(itertools.combinations(E , k))

print("%i - combinations of %s " %(k , E))
 
print(choose_k)
 
for i in choose_k:
    print(i)

print("Number of combinations = %i!/(%i!(%i - %i)!) = %i" %(n , k , n , k  , len(choose_k)))