import random
x = [random.randint(1 , 6 ) for i in range(8000)]

X = set(x)

# print(x)
# print(X)

P = [x.count(i)/len(x) for i in X]

print(P)