import matplotlib.pyplot as plt
import math


print('Geometric distribution')

def pmf_geo( p , x):
    return p*(1 - p)**(x - 1) 



print("a) " +str(pmf_geo(0.4 , 3)))

def plot_pmf_geo(p , n):
    '''Plot the probability mass function of Geometric'''
    K = list(range(1 , n + 1))
    # print(K)
    P_geo = [pmf_geo( p , k) for k in K]
    plt.plot(K ,P_geo , '-o')
    plt.title('PMF of Geometric(%.2f)' %p)
    plt.xlabel('Probability')
    plt.ylabel('n')
    plt.show()
    
plot_pmf_geo(0.4 , 10)