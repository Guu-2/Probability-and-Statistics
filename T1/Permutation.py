import itertools

E = {'a' , 'b' , 'c' , 'd'}

k = 3 

n = len(E)

permute_k = list(itertools.permutations(E , k))

print("%i -permuatation of %s  "%(k , E))

print(permute_k)

for i in permute_k:

  print(i)

print("size = " , "%i!/(%i - %i)! = " %(n , n , k) , len(permute_k))
