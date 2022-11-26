import itertools

def cross(A , B):
    return {a + b for a in A for b in B}

gender = cross('B' , '123456') | cross('G' , '123456789')

liste = []
for i in gender:
    liste.append(i)
    
# print(liste)
    
k = 5


sol_4 = list(itertools.combinations(liste , k))

# print(sol_4)


list_kq = []
for i in sol_4:
    b = 0
    g = 0
    
    for j in i:
        if j[0] == 'B':
            b += 1     
        else:
            g += 1
    if b == 3 and g == 2:
        list_kq.append(i)
        
print('Different selections can the com-mittee consist of 3 men and 2 women is ' +str(len(list_kq)))

print('Print these selections to screen : \n')

print(list_kq)

        
   
    
        





