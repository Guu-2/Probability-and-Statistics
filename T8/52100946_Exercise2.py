import pandas as pd

import math

data = pd.read_csv('population_csv.csv' , delimiter = ',')

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



data = data.set_index("Country Name")

c1 = data.loc["Arab World","Year"]

c2 = data.loc["Uruguay","Year"]

c3 = data.loc["Vanuatu","Year"]

c4 = data.loc["Vietnam","Year"]



df = pd.DataFrame({'Country Name': ["Arab World" ,"Uruguay" ,"Vanuatu" ,"Vietnam"] , 'Country Code':["ARB" , "URY" , "VUT" , "VNM"],
                   "Mean" : [mean(c1) , mean(c2) , mean(c3) , mean(c4)] , 
                   "Std" : [std(c1) , std(c2) , std(c3) , std(c4)],
                   "Min" : [min(c1) , min(c2) , min(c3) , min(c4)],
                   "Max" : [max(c1) , max(c2) , max(c3) , max(c4)]})

print(df)