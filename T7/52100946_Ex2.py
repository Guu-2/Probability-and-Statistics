import itertools
import random
from fractions import Fraction

def P(event , space):
    return Fraction(len(event & space) , len(space))

def combos(item , n):
    return {' '.join(combo) for combo in itertools.combinations(item , n)}
def cross(A , B):
    return {a + b for a in A for b in B}

urn_ori = cross('B' , '12') | cross('W' ,'12345') | cross('R' ,'123')

urn_list = []
for i in urn_ori:
    urn_list.append(i)
    
    
print(urn_list)



Ex2 = combos(urn_ori , 3)
# urn_list1 = []
# for i in Ex2:
#     urn_list1.append(i)

    
# set = {1 , 2 , 3, 4}

# print(urn_list1)

# print(card1)
# print(urn)
# urn.discard(urn_list[card1])


# def same_color(n):
#     limit = 0
#     event = 0
#     for i in Ex2:
#         print(i)
#         limit+=1
#         for s in i:
#             if(s.count('R') == 3 or s.count('W') == 3 or s.count('B') ==3):
#                 event+=1
            
#         if(limit == n):
#             break;
    
#     return P(event , n)
    
    
    
# print(same_color(1000))
    

Ex2a = {s for s in Ex2 if s.count('R') == 3 or s.count('W') == 3 or s.count('B') ==3}

Ex2b = {s for s in Ex2 if s.count('R') == 1 and s.count('W') == 1 or s.count('B') ==1}

Ex2c = {s for s in Ex2 if s.count('R') == 2 or s.count('W') == 2 or s.count('B') == 2}

Ex2d = {s for s in Ex2 if s.count('R') == 2 or s.count('W') == 1}

Ex2e = {s for s in Ex2 if s.count('W') == 3}


print("n = " , len(Ex2))
print("a) " + str(P(Ex2a , Ex2)))
print("b) " + str(P(Ex2b , Ex2)))
print("c) " + str(P(Ex2c , Ex2)))
print("d) " + str(P(Ex2d , Ex2)))
print("e) " + str(P(Ex2e , Ex2)))

        
        