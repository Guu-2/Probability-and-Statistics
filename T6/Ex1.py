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





def plot_pmf_normal(mu , sigma):
    '''Plot the probability mass function of Normal(mu , sigma)'''
    X = generator_data(mu - 4*sigma , mu + 4*sigma , 1000)
    P_normal =[pmf_normal(x, mu , sigma) for x in X ]
    plt.plot(X, P_normal ,'-')
    plt.title('PMF of Normal(%.2f , %.2f)' %(mu , sigma))
    plt.xlabel('X')
    plt.ylabel('P')
    plt.show()
# plot_pmf_normal(0 , 1.5)

def plot_cdf_normal(mu , sigma):
    '''Plot the cumulative distribution function of Normal(mu , sigma)'''
    X = generator_data(mu - 4*sigma , mu + 4*sigma , 1000)
    P_normal =[cdf_normal(x, mu , sigma) for x in X ]
    plt.plot(X, P_normal ,'r-')
    plt.title('CDF of Normal(%.2f , %.2f)' %(mu , sigma))
    plt.xlabel('X')
    plt.ylabel('P')
    plt.show()
    
print("a)")
plot_cdf_normal(0 , 1.5)

