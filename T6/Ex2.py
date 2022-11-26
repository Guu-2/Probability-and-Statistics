import matplotlib.pyplot as plt

import math

def generator_data(a,b , size):
    n = (b -a ) / (size -1)
    result = []
    s= a
    while(s < b):
        result.append(s)
        s = s + n
    '''khi cộng n lần cuối cùng bị dư nên chỉ lấy đến b'''
    if len(result) < size:
        result.append(b)
    return result


x = generator_data(9 , 12, 100)

def pmf_normal(x , mu, sigma):
    return (1.0 / sigma*math.sqrt(2*math.pi))*math.e**((-1.0/2)*((x - mu)/sigma)**2)
    
def cdf_normal(x , mu , sigma):
    return (1.0/2) * (1 + math.erf((x - mu)/(sigma*2**(1/2))))



print("b) " + str(pmf_normal(8.5 , 10 , 1)))
