import random

from fractions import Fraction

def P(event , space):
    return (Fraction((event & space) , (space)))

n =1000

def both_dice_same(n):
    event = 0
    for i in range(n):
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        if(dice1 == dice2):
            event+=1;
            
    return P(event, n);


print("a) " +str(both_dice_same(n)))

def both_dice_different(n):
    event = 0
    for i in range(n):
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        if(dice1 != dice2):
            event+=1;
            
    return P(event, n);
    
print("b) " +str(both_dice_different(n)))
    
def both_dice_even(n):
    event = 0
    for i in range(n):
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        if(dice1 % 2 == 0 and dice2 %2 == 0):
            event+=1;
            
    return P(event, n);
        
print("c) " +str(both_dice_even(n)))

def both_dice_odd(n):
    event = 0
    for i in range(n):
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        if(dice1 %2 != 0 and  dice2%2 != 0):
            event+=1;
            
    return P(event, n);

print("d) " +str(both_dice_odd(n)))


def one_odd_one_even(n):
    event = 0
    for i in range(n):
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        if((dice1 %2 != 0 and  dice2%2 == 0) or(dice1 %2 == 0 and  dice2%2 != 0)):
            event+=1;
            
    return P(event, n);

print("e) " +str(one_odd_one_even(n)))



def value_is_six(n):
    event = 0
    for i in range(n):
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        if(dice1 ==6 and  dice2 ==6):
            event+=1;
            
    return P(event, n);
      

print("f) " +str(value_is_six(n)))

def value_greater_than_10(n):
    event = 0
    for i in range(n):
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        if(dice1 + dice2 > 10):
            event+=1;
            
    return P(event, n);


print("g) " +str(value_greater_than_10(n)))

