import random
from itertools import product

import itertools


Ranks = { 1, 2 , 3 , 4 , 5 ,6 , 7 , 8 , 9 , 10 ,'J' , 'Q' , 'K'}

Suilts = {'Bích' , 'Chuồn' , 'Rô' , 'Cơ'}

Cards = list(product(Ranks , Suilts))

def simulator_poker2(n):
    
    sol = 0
    for i in range(n):
        count = 1
    
        index1 = random.randint(0 , 51)
        index2 = random.randint(0 , 50)
        index3 = random.randint(0 , 49)
        index4 = random.randint(0 , 48)

        #print(index)
        if Cards[index2][1] != Cards[index1][1]:

            count+=1
        if Cards[index3][1] != Cards[index1][1] and Cards[index3][1] != Cards[index2][1]:

            count+=1
        if Cards[index4][1] != Cards[index1][1] and Cards[index4][1] != Cards[index2][1] and Cards[index4][1] != Cards[index3][1]:

            count+=1
        if(count == 4):
            sol+=1
            
    return sol / n
        

print('== EX7 ==')

#print(simulator_poker1(100))

print(simulator_poker2(10000))
