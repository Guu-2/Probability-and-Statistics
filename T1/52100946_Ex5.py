import itertools


def cross(A , B):
    return {a + b for a in A for b in B}




A = cross('S' , '1234567890JQK') | cross('C' , '1234567890JQK') | cross('D' , '1234567890JQK') | cross('H' , '1234567890JQK')


# print((list_s))



poker_5 = list(itertools.combinations(A , 5))

len_poker_5 = len(poker_5)

print('a) Solution for a : ' + str(len_poker_5))


def check_three_of_a_kind(arr):
    # không dùng list đc 
    check = {}
    for i in arr:
        check[i] = arr.count(i)
    if len(check) == 3 and 3 in check.values():
        return True
    
    

list_kq = []
for i in poker_5:
    ar = []
    for j in i:
        ar.append(j[1])
    if(check_three_of_a_kind(ar) == True):
        list_kq.append(i)


len_three_of_a_kind = len(list_kq)

print('b) number variable len_three_of_a_kind is : ' + str(len_three_of_a_kind) )
        







        

