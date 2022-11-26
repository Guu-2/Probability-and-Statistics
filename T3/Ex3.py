import random

from itertools import product

import itertools

from fractions import Fraction



def P(event , space):
    return Fraction(len(event & space) , len(space))


Ranks = { 1, 2 , 3 , 4 , 5 ,6 , 7 , 8 , 9 , 10 ,'J' , 'Q' , 'K'}

Suilts = {'S' , 'C' , 'D' , 'H'}

Cards = list(product(Ranks , Suilts))

print(Cards)

def combos(item , n):
    return {''.join(combo) for combo in itertools.combinations(item , n)}


# print(combos(Ranks , 2))

# print(len(Cards))


# print(len(U))

        
U = {i for i in Cards}
# print(U)
a = []
for i in U:
    a.append(str(i[0]) +''+ str(i[1]))
    

print("a) " + str(a))

U = {i for i in a}

print(len(U))

def b():

    S = []
    
    sol = 0
    for i in range(1):
        count = 1
        index1 = random.randint(0 , 51)
        S.append(a[index1])
        
        index2 = random.randint(0 , 50)
        S.append(a[index2])
        
        index3 = random.randint(0 , 49)
        S.append(a[index3])
        
    return S


print("b) " + str(b()))


def cauc():
    kqc = []
    cnt =0

    S = b()
    for j in S:

        if(j[0] == 'K'):
            cnt+=1
    if(cnt == 2 or cnt == 1):
        kqc.append(S)
    
    return kqc
                
    # return kqc

## lấy 1 cái để tính xác suất
Z = []
def kqc():
    for i in range(0 , 100):
        X = cauc()
        for j in X:
            Z = { g for g in j}

            val = P(Z , U)
            
    print("c) " + str(Z))
    return val
    






def caud():
    kqc = []
    cnt =0

    S = b()
    for j in S:

        if(j[0] == 'K'):
            cnt+=1
    if(cnt >= 1):
        kqc.append(S)

    return kqc
                


## lấy 1 cái để tính xác suất
def kqd():
    for i in range(0 , 100):
        X = caud()
        for j in X:
            Z = { g for g in j}
            val = P(Z , U)
    print("d) " + str(Z))
    return val
    

print("e) P(A1) = " + str(kqc()) + " P(A2) = " + str(kqd()))

# kqd = []
# def caud(n):
#     for  i in range(0 , n):
#         b()
#         A = { v for v in S if v.count('K') >= 1}
#         for j in A:
#             kqd.append(str(j[0]) + '' + str(j[1]))
#     return kqd
        

# cauc(10)
# A1  = kqc
# print(A1)




# caud(10)
# A2 = kqd
# print(A2)


# A = [ i for i in U]
# print(A)
# print('== EX7 ==')

# #print(simulator_poker1(100))

# print(b(1))




# omega = list(itertools.permutations(a , 3))


# print(len(omega))


# print(len(omega))

# for i in S:
    