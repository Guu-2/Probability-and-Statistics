#KQ ------
#1771 432 261
#6912 
#720
#2598960 -54912

def cross(A , B):
    return {a + b for a in A for b in B}

urn = cross('M' , '1234') | cross('P' , '123') | cross('C' , '12' ) | cross('L' , '1')

import itertools

from math import *

liste = []
for i in urn:
    liste.append(i)
    
# print(liste)
    

sol_3 = (list(itertools.permutations(liste , 10)))

# print(sol_3)

list_kq = []

for i in sol_3:
    str = ''
    for j in i:
        # Phần số 
        # print(j[1])
        # Phần chữ
        str+= j[0]
    
    # print(s)
    if 'MMMM' in str and 'PPP' in str and 'CC' in str:
        list_kq.append(i)
        
    
len_kq = len(list_kq)
    
print("a) different arrangements possible is : ") 

print(len_kq)

print("b) Print these arrangements : \n") 

print(list_kq)
        
        



