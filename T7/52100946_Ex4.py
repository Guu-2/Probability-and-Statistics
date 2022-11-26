import itertools
import random
from fractions import Fraction

def P(event , space):
    return Fraction(len(event & space) , len(space))

def combos(item , n):
    return {' '.join(combo) for combo in itertools.combinations(item , n)}
def cross(A , B):
    return {a + b for a in A for b in B}

urn = cross('W' , '12') | cross('B' ,'123') | cross('R' ,'1234')

print("a) " +str(urn))


U3 = combos(urn , 3)

print("\n\nb) " +str(U3))


white1blue1red1 = {s for s in U3 if s.count('R') == 1 and s.count('B') == 1 and s.count('W') == 1}

print("\n\nc) " +str(white1blue1red1))


P = P(white1blue1red1 , U3)

print("\n\nd)" +str(P))