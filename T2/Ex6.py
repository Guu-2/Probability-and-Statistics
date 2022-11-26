from itertools import product

import itertools


Ranks = { 1, 2 , 3 , 4 , 5 ,6 , 7 , 8 , 9 , 10 ,'J' , 'Q' , 'K'}

Suilts = {'Bích' , 'Chuồn' , 'Rô' , 'Cơ'}

Cards = list(product(Ranks , Suilts))

#print((Cards))

n = 5

Ex6 = list(itertools.combinations(Cards , n))
sol_6 = []

        
    
#print(len(sol_6))
import random

# # def simulator_poker1(n):

#     for i in Ex6:
#         count  =  0
#         for j in i:
#             if(j[1] == 'Cơ'):
#                 count += 1 
#         if(count == 5):
#             sol_6.append(i)
#     return len(sol_6)

def simulator_poker1(n):

    sol = 0
    for i in range(n):
    
        index1 = random.randint(0 , 51)
        index2 = random.randint(0 , 50)
        index3 = random.randint(0 , 49)
        index4 = random.randint(0 , 48)
        index5 = random.randint(0 , 47)
        #print(index)
        if Cards[index1][1] == Cards[index2][1] == Cards[index3][1] == Cards[index4][1] == Cards[index5][1]== 'Cơ':
            sol +=1
    return sol / n
        

print('== EX6 ==')

#print(simulator_poker1(100))

print(simulator_poker1(100000))
