import random
x = [random.randint(0 , 2) for i in range(10000)]

print("a) " +str(x))

X = set(x)

print("b) " + str(X))

P = [x.count(i)/len(x) for i in X]

print("c) "+str(P))

EX = 0

for i in X:
    EX+= (i * P[i - 1])

print(EX)

Varx = 0
for i in X:
    Varx+= (i - EX)*(i - EX)*P[i - 1]
print(Varx)

import math
SD = math.sqrt(Varx)

pol = 0
for i in X:

    if(i == 1):
        break;
    pol+=1
    
print("d) \n Expectation = " + str(EX)  + "\n" + " Variance = "  + str(Varx) +" \n Standard Deviation = "+ str(SD))
        
One_Head = sum(P[pol:])

print("e) " + str(One_Head))