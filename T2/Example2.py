import itertools

def combos(item , n):
    return {' '.join(combo) for combo in itertools.combinations(item , n)}
def cross(A , B):
    return {a + b for a in A for b in B}

urn = cross('W' , '12345678') | cross('B' ,'123456') | cross('R' ,'123456789')

print(urn)

U6 = combos(urn , 6)

print((U6))

import random

print(random.sample(U6 , 10))

# all 6 ball red

red6 = {s for s in U6 if s.count('R') == 6}

# P(red6, U6)

