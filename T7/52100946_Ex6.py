
E = { 0  , 1 , 2 , 3 , 4 , 5}

import itertools

a = list(itertools.permutations(E , 3))

b = list(itertools.permutations(E , 4))
print("\na) : \n" + str(a))

def pairwise(e):
    event = 0

    if e[0] != e[1] != e[2] != e[3]:
        
        event = 9999;
    return event
       
B = { s for s in b if pairwise(s) == 9999}

print("\nb) : \n" + str(B))



