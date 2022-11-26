import random

def simulator_dice3(n):
    count  =  0
    for i in range(n):
        dice1 = random.randint(1 , 6)
        dice2 = random.randint(1 , 6)
        if dice1 == dice2:
            count += 1
    #print(count)
    return count/n
     
     
print('== EX3 ==')
print(simulator_dice3(100))   
print(simulator_dice3(1000))
