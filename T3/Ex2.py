from fractions import Fraction

def P(event , space):
    return {Fraction(len(event & space) , len(space))}

S = [('Thanh', 'Nữ'), ('Hồng', 'Nữ'), ('Thương', 'Nữ'), 
     ('Đào', 'Nữ'), ('My', 'Nữ'), ('Yến', 'Nữ'), ('Hạnh', 'Nữ'),
     ('My', 'Nữ'), ('Vy', 'Nữ'), ('Tiên', 'Nữ'), ('Thanh', 'Nam'), 
     ('Thanh', 'Nam'), ('Bình', 'Nam'), ('Nhật', 'Nam'), 
     ('Hào', 'Nam'), ('Đạt', 'Nam'), ('Minh', 'Nam')]


print("a)\n")

#set tự động xóa trùng

A = [i for i in S if i[0] == 'Thanh']
print('A = ' + str(A))



print("b)\n")

B = [i for i in S if i[1] == 'Nữ']

print('B = ' + str(B))


print("c)\n")

A = [i for i in S if i[0] == 'Thanh']

A_B = [i for i in A if i[1] == 'Nữ']

print("A_B = " + str(A_B))

print("d)\n")

def numerator(A , S):
    
    cnt = 0;
    for i in A:
        # print(i)
        for j in S:
            # print(j)
            if i == j:
                cnt +=1;
                break;
    
    return cnt;


# print(len(S))


P_A = str(numerator(A , S)) + '/' + str(len(S))



P_B = str(numerator(B , S)) + '/' + str(len(S))


P_A_B = str(numerator(A_B , S)) + '/' + str(len(S))


print("P_A = " + str(P_A)+"\n"+ "P_B = " + str(P_B) + "\n" +  "P_A_B = " + str(P_A_B))


print("e)\n")

A = [i for i in S if i[1] == 'Nữ']

A_B = [i for i in A if i[0] == 'Thanh']

P_A_B = str(numerator(A_B , S)) + '/' + str(len(S))

print("Probability = " + str(P_A_B))

