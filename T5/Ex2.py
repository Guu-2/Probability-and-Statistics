import matplotlib.pyplot as plt
import math

print('Poisson distribution')

def pmf_poisson(k , lam):
    return (lam**k * math.e**(-lam)) /(math.factorial(k))

print("a) " +str(pmf_poisson( 2, 3)))


def plot_pmf_poisson(n, lam):
    '''Plot the probability mass function of Poisson( n , lambda)'''
    K = list(range(1 , n + 1))
    print(K)
    P_poisson = [pmf_poisson(k , lam) for k in K]
    plt.plot(K , P_poisson , '-o')
    plt.title('PMF of Poisson(%i)' %lam)
    plt.xlabel('Number of Events')
    plt.ylabel('Probability of Number of Events')
    plt.show()
    
plot_pmf_poisson(5 , 3) 


