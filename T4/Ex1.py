import numpy as np
import random
import itertools

x = np.random.choice([0  , 1 , 2 , 3 ,4  ,5] , 3650 , p =[0.1 , 0.2 , 0.3 , 0.2 , 0.15 , 0.05])

X = set(x)


print("a) " + str(X))
Xb = []
for i in X:
    Xb.append(i)
    
print(Xb)
P_D_F = []
for i in Xb:
    cnt = 0
    # print(i)
    for j in x:
        if(j == i):
            cnt+=1
            
    P_D_F.append(cnt / len(x))
   
print("b) " + str(P_D_F))

EX  =0
for i in X:
    EX = EX + (i * P_D_F[i - 1])
    

VarX = 0

for i in X:
    VarX = VarX + (i - EX )*(i - EX)*P_D_F[i - 1]
    
import math

SD = math.sqrt(VarX)



print("c) \n Expectation = " + str(EX)  + "\n" + " Variance = "  + str(VarX) +" \n Standard Deviation = "+ str(SD))

FX = sum(P_D_F[3:])

print("d) " + str(FX))

