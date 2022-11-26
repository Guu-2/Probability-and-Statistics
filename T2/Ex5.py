import random

def simulator_dice5(n):
    count  =  0
    for i in range(n):
        dice1 = random.randint(1 , 6)
        dice2 = random.randint(1 , 6)
        if dice1 + dice2 > 6:
            count += 1
    #print(count)
    return count/n
     
     
print('== EX5 ==')
print(simulator_dice5(100))   
print(simulator_dice5(1000))
