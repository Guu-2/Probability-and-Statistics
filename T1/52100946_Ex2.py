#KQ ------
#1771 432 261
#6912 
#720
#2598960 -54912



def cross(A , B):
    return {a + b for a in A for b in B}

urn = cross('W' , '12345678') | cross('B' , '123456') | cross('R' , '123456789')


# print(len(urn))


import itertools

k =3

U3 = list(itertools.combinations(urn , k))

len_U3 = len(U3)

#Solution for a

n = len(urn)

# print("U3 - combinations of %s " %(k))

print("\na) Number of combinations = %i!/(%i!(%i - %i)!) = %i" %(n , k , n , k  , len_U3))

# print('a)-> ' + str(len(U3)))


#Solution for b

White = list(itertools.combinations(cross('W' , '12345678') , 1 ))

Black = list(itertools.combinations(cross('B' , '123456') , 1))

Red = list(itertools.combinations(cross('R' , '123456789') , 1))

# b = 0
# for i in U3:
#     if i[0][0] != i[1][0] and i[0][0] != i[2][0] and i[1][0] != i[2][0]:
#         b +=1


b = len(White) * len(Black)* len(Red)



print("\nb) Enumerate all possible cases of three balls of different colors is :  " + str(b))


# for u in U3:
#     print(u)


# #Solution for c

U3 = list(itertools.permutations(urn , k))

num = 0
# set = {None ,}
for s in U3:
    if s[0][0] == 'W' and s[1][0] =='R':
        # set.add(s)
        num+=1
        
print('c) Enumerate all possible cases of the first ball being white and the second ball red : ' +str(num))
# num =0
    