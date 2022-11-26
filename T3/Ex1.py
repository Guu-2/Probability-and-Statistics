from fractions import Fraction

def P(event , space):
    return Fraction(len(event & space) , len(space))

S = {'BB' , 'BG' , 'GB' , 'GG'}

B = {s for s in S if 'B' in s}

A_B = {s for s in B if s.count('B') == 2}

P_B = P(B , S)
 
P_A_B = P(A_B , S) 

P_A_with_B = P_A_B/P_B

print(P_A_with_B)




import itertools

Cats = {'M' , 'F'}





n = len(Cats)

k = 3

s = n**k

S = ('MMM' , 'MMF' , 'MFM' , 'MFF' , 'FMM' , 'FMF' , 'FFM' , 'FFF')

 

def cross(A , B):
    return {a + b for a in A for b in B}


urn = cross('A' ,'MF') | cross('B' ,'MF') | cross('C' ,'MF')

print(urn)

import itertools

def combos(item , n):
    return {''.join(combo) for combo in itertools.combinations(item , n)}

U6 = combos(urn , 3)

# print((U6))
# a = 13
# b = 27

S = {s for s in U6 if s.count('A') == 1 and s.count('B') == 1 and s.count('C') ==1 }
# print(len(a & b))

# print(S)

print("a)\n")
print('S = ' + str(S))

print("b)\n")
print('len(S) = ' + str(len(S)))

print("c)\n")
B = {i for i in S if i.count('F') >= 1}
#print(B)
print('B = ' + str(B))

print("d)\n")
A = {i for i in S if i.count('F') == 3}
print('A = ' + str((A)))


print("e)\n")

B = {i for i in S if i.count('F') >= 1}

B_A = {i for i in B if i.count('F') == 3}

P_B = P( B , S)

P_B_A = P( B_A , S)



KQ =  P_B_A / P_B
 
print('A_B = ' + str((KQ)))



from itertools import product

Cats = ['A' , 'B' , 'C']

#############################################

S = list(itertools.product([0 , 1] , repeat = 3))

# print(S)
U =[]
max = len(Cats)
j = 0
for i in S:
    for j in range(0 , max):
        U.append((Cats[j],i[j]))


# X = []
# for i in S:
#     s =''
#     for j in i:

#         if(j == 1 ):
#             j = 'M'
#         if(j == 0):
#             j = 'F'
#         s += str(j)
#     X.append(s)

print(U)


