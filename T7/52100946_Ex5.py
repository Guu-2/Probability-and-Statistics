import random

from fractions import Fraction

def P(event , space):
    return Fraction((event & space) , (space))
from itertools import product

import itertools

def check_straight(s):
    lista = []
    listb = []
    event = 0
    for i in s:
        lista.append(i[0])
    #     print(i)
    # print(lista)
    
    for i in lista:
        if(i == 'J'):
            i = 11
        if(i =='Q'):
            i = 12
        if(i == 'K'):
            i = 13
        listb.append(int(i))
    #     print(i)

    # print(listb)
    listb.sort()
    # listb = [1 , 2 , 3 , 4 , 5]
    cnt = 0
    for i in range(0 , len(listb) -1):
        u = listb[i+1] - listb[i]
        if(u == 1):
            cnt +=1;
        
    if(cnt == 4):
        event = 9999
    
    return event
    
def Practical_probability(n):
    sol = 0
    event = 0
    for i in range(n):
        attribute  =[]
        listb= []
        index1 = random.randint(0 , 51)
        attribute.append(Cards[index1][0])
        index2 = random.randint(0 , 50)
        attribute.append(Cards[index2][0])
        index3 = random.randint(0 , 49)
        attribute.append(Cards[index3][0])
        index4 = random.randint(0 , 48)
        attribute.append(Cards[index4][0])
        index5 = random.randint(0 , 47)
        attribute.append(Cards[index5][0])
        # print(attribute)
        

        
        for i in attribute:
            if(i == 'J'):
                i = 11
            if(i =='Q'):
                i = 12
            if(i == 'K'):
                i = 13
            listb.append(int(i))
        listb.sort()
        # listb = [1 , 2 , 3 , 4 , 5]
        cnt = 0
        for i in range(0 , len(listb) -1):
            u = listb[i+1] - listb[i]
            if(u == 1):
                cnt +=1;
            
        if(cnt == 4):
            event +=1
    
    return P(event, n)
             


Ranks = { 1, 2 , 3 , 4 , 5 ,6 , 7 , 8 , 9 , 10 ,'J' , 'Q' , 'K'}

Suilts = {'S' , 'C' , 'D' , 'H'}

Cards = list(product(Ranks , Suilts))



Ex5 = list(itertools.combinations(Cards , 5))

omega = itertools.combinations(Cards , 5)



Theorical = { s for s in Ex5 if check_straight(s) == 9999}

print("\n\nEX5")

print("a) Theorical probability : " +str(P(len(Theorical) , len(Ex5))))

print("d) Practical_probability : " +str(Practical_probability(30000)))

# print(Ex5.pop())


# n  = 0
# for i in a:
#     print(i[0])
#     n+=1
#     for j in i:
#         print(j)

#     if(n ==10):
#         break;



# list = [1 , 2 , 3 , 4 , 5]

# a  = len(list)

# for i in range(0 , len(list) -1):
#     print(list[i + 1] - list[i])


# print(check_straight(s))

# U4 = combos(a , 5)

# print(len(U4))


# print(len(a))


# list = [1 , 2 , 7 , 4 , 3 , ord('J')]



# list.sort()

# print(list)
