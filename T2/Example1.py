from fractions import Fraction

def P(event , space):
    return Fraction(len(event & space) , len(space))

D = {1, 2, 3 , 4 , 5 , 6}

even = {2 , 4 , 6}

#print(P(even , D))


def cross(A , B):
    return {a + b for a in A for b in B}


urn = cross('W' , '12345678') | cross('B' ,'123456') | cross('R' ,'123456789')

#print(urn)

import itertools

def combos(item , n):
    return {' '.join(combo) for combo in itertools.combinations(item , n)}

U6 = combos(urn , 6)

print(len(U6))

import random

#print(random.sample(U6 , 10))

# all 6 ball red

red6 = {s for s in U6 if s.count('R') == 6}

print(P(red6, U6))

b3w2r1 = {s for s in U6 if s.count('B') == 3 and s.count('W') == 2 and s.count('R') == 1}

print(P(b3w2r1 , U6))

w4 = {s for s in U6 if s.count('W') == 4}

print(P(w4, U6))

import random

n = 100

count  = 0;

for simulations in range(n):
    tosses = random.randint(0 , 1)
    if(tosses == 1):
        count += 1
print(count/n)

import random

count = 0;

n = 10;

for i  in range(n):
    die1 = random.randint(1 , 6)
    die2 = random.randint(1 , 6)
    if( die1 == 1) and die2 ==6:
        count+=1

print(count/n)

from itertools import product

Ranks = {1 , 2 ,3  , 4, 5 , 6 , 7, 8 , 9 , 10 ,'J' , 'Q' , 'K'}

Suits = {'Cơ' , 'Rô' , 'Chuồn' , 'Bích'}

Cards = list(product(Ranks, Suits))

print(len(Cards))

print(Cards[:10])
 
def simulator_poker(n):
    count = 0;
    for i in range(n):
        index = random.randint(0 , 51)
        if Cards[index][1] == 'Cơ' or Cards[index][1] == 'Rô':
            count += 1
    return count/n


print(simulator_poker(10))

print(simulator_poker(100))

print(simulator_poker(1000))

print(simulator_poker(10000))

