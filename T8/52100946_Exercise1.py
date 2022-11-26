import pandas as pd

import math

data = pd.read_csv('iris.csv' , delimiter = ',')

print(data.head(5))


def count(data):
    return len(data)

def mean(data):
    return sum(data)/count(data)

def std(data):
    sum = 0
    for i in range(0, len(data)):
        sum = sum + (data[i] - mean(data))**2
    
    return (sum/count(data))**(1/2)
        
def min(data):
    min = data[0]
    for i in range(0, len(data)):
        if(data[i] < min):
            min = data[i]
    return min

def max(data):
    max = data[0]
    for i  in range(0, len(data)):
        if(data[i] > max):
            max = data[i]
    return max

def Frame(A):
    return  [count(A) ,mean(A) , std(A) , min(A) , max(A) ]

A = data['sepal.length']

B = data['sepal.width']

C = data['petal.length']

D = data['petal.width']

df = pd.DataFrame({'sepal.length': Frame(A) ,'sepal.width' : Frame(B) , 'petal.length' : Frame(C) , 'petal.width' : Frame(D)})


df = df.rename(index = {0 : 'count' , 1 : 'mean' , 2 :'std' , 3:'min' , 4:'max'})

print(df)

