
from fractions import Fraction

def P(event , space):
    return Fraction(len(event & space) , len(space))

def cross(A , B):
    return {a + b for a in A for b in B}

urn = cross('W' , '12345678') | cross('B' ,'123456') | cross('R' ,'123456789')

#print(urn)

import itertools

def combos(item , n):
    return {' '.join(combo) for combo in itertools.combinations(item , n)}

U6 = combos(urn , 6)

b2w2r2 = {s for s in U6 if s.count('B') == 2 and s.count('W') == 2 and s.count('R') == 2}


print('== EX8 ==')

print(P(b2w2r2 , U6))





