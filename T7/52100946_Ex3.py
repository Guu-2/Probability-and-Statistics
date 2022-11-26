from itertools import product

import itertools
from fractions import Fraction
def P(event , space):
    return (Fraction((event & space) , (space)))

Ranks = { 1, 2 , 3 , 4 , 5 ,6 , 7 , 8 , 9 , 10 ,'J' , 'Q' , 'K'}

Suilts = {'Bích' , 'Chuồn' , 'Rô' , 'Cơ'}

Cards = list(product(Ranks , Suilts))

# a = list(itertools.combinations(Cards , 5))

# print(a)
import random

def same_suit(n):

    sol = 0

    for i in range(n):
        attribute  =[]
        index1 = random.randint(0 , 51)
        attribute.append(Cards[index1][1])
        index2 = random.randint(0 , 50)
        attribute.append(Cards[index2][1])
        index3 = random.randint(0 , 49)
        attribute.append(Cards[index3][1])
        index4 = random.randint(0 , 48)
        attribute.append(Cards[index4][1])
        # print(attribute)
        if attribute.count('Cơ') == 4 or attribute.count('Rô') == 4 or attribute.count('Chuồn') == 4 or attribute.count('Bích') == 4:
            sol +=1
    return P(sol , n)
        
print("a) " +str(same_suit(10000)))

def different_suit(n):
    
    sol = 0
    for i in range(n):
        attribute  =[]
        index1 = random.randint(0 , 51)
        attribute.append(Cards[index1][1])
        index2 = random.randint(0 , 50)
        attribute.append(Cards[index2][1])
        index3 = random.randint(0 , 49)
        attribute.append(Cards[index3][1])
        index4 = random.randint(0 , 48)
        attribute.append(Cards[index4][1])
        # print(attribute)
        if attribute.count('Cơ') == 1 and attribute.count('Rô') ==1 and attribute.count('Chuồn') == 1 and attribute.count('Bích') == 1:
            sol +=1
    return P(sol , n)


print("b) "+ str(different_suit(10000)))

def same_color(n):
    sol = 0
    for i in range(n):
        attribute  =[]
        index1 = random.randint(0 , 51)
        attribute.append(Cards[index1][1])
        index2 = random.randint(0 , 50)
        attribute.append(Cards[index2][1])
        index3 = random.randint(0 , 49)
        attribute.append(Cards[index3][1])
        index4 = random.randint(0 , 48)
        attribute.append(Cards[index4][1])
        # print(attribute)
        if (attribute.count('Cơ') + attribute.count('Rô') == 4) or (attribute.count('Chuồn') + attribute.count('Bích') == 4):
            sol +=1
    return P(sol , n)


print("c) " +str(same_color(10000)))


def same_value(n):
    sol = 0
    for i in range(n):
        attribute  =[]
        index1 = random.randint(0 , 51)
        attribute.append(Cards[index1][0])
        index2 = random.randint(0 , 50)
        attribute.append(Cards[index2][0])
        index3 = random.randint(0 , 49)
        attribute.append(Cards[index3][0])
        index4 = random.randint(0 , 48)
        attribute.append(Cards[index4][0])
        # print(attribute)
        if Cards[index1][0] == Cards[index2][0] == Cards[index3][0] == Cards[index4][0]:
            sol +=1
    return P(sol , n)


print("d) " +str(same_value(300000)))

def number_type(n):

    event = 0
    s=0
    for i in range(n):
        attribute  =[]
        sol = 0
        index1 = random.randint(0 , 51)
        attribute.append(Cards[index1][0])
        index2 = random.randint(0 , 50)
        attribute.append(Cards[index2][0])
        index3 = random.randint(0 , 49)
        attribute.append(Cards[index3][0])
        index4 = random.randint(0 , 48)
        attribute.append(Cards[index4][0])

        for i in attribute:
            if(str(i).isdigit()==True):
                sol +=1
        
        if(sol == 4):
            event+=1

                
            
    return P(event , n)

print("e) "+ str(number_type(10000)))

def faces_type(n):
    
    event = 0
    s=0
    for i in range(n):
        attribute  =[]
        sol = 0
        index1 = random.randint(0 , 51)
        attribute.append(Cards[index1][0])
        index2 = random.randint(0 , 50)
        attribute.append(Cards[index2][0])
        index3 = random.randint(0 , 49)
        attribute.append(Cards[index3][0])
        index4 = random.randint(0 , 48)
        attribute.append(Cards[index4][0])

        for i in attribute:
            if(str(i).isdigit()==False):
                sol +=1
        
        if(sol == 4):
            event+=1

                
            
    return P(event , n)

print("e) "+ str(faces_type(10000)))


