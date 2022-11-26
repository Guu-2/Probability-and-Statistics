import matplotlib.pyplot as plt
import math

print('Bernoulli distribution')


def pmf_bernoulli(p , x):
    return p**x * (1 - p)**(1 - x)


def plot_pmf_bernoulli(p):
    '''Plot the probability mass function of bernoulli(P)'''
    X = [ 0 , 1]
    P_bernoulli = [pmf_bernoulli(p, x) for x in X]
    plt.plot(X , P_bernoulli , 'o')
    
    plt.title('PMF of Berboulli(p = %.2f)' % p)
    plt.xlabel('Value')
    plt.ylabel('Probability')
    plt.show()
    
plot_pmf_bernoulli(0.5)

print('Binomial distribution')

def pmf_binom(k , n , p):
    return (math.factorial(n) / (math.factorial(k) * math.factorial(n - k)) ) * p**k *( 1- p)**(n - k)

def plot_pmf_binom(n , p):
    '''Plot the probability mass function of Binom(n , p)'''
    K = list(range(0 , n + 1))
    P_binom = [pmf_binom(k , n , p) for k in K]
    plt.plot(K , P_binom , '-o')
    axes = plt.gca()
    axes.set_xlim([0 , n])
    axes.set_ylim ([0 , 1.1 *max(P_binom)])
    plt.title('PMF of Bin(%i , %.2f)' %(n , p))
    plt.xlabel('Numer k of successes')
    plt.ylabel('Probability of k successes')
    plt.show()
    
plot_pmf_binom(15 , 0.5)

print('Poisson distribution')

def pmf_poisson(k , lam):
    return (lam**k * math.e**(-lam)) /(math.factorial(k))


def plot_pmf_poisson(n, lam):
    '''Plot the probability mass function of Poisson( n , lambda)'''
    K = list(range(0 , n + 1))
    P_poisson = [pmf_poisson(k , lam) for k in K]
    plt.plot(K , P_poisson , '-o')
    plt.title('PMF of Poisson(%i)' %lam)
    plt.xlabel('Number of Events')
    plt.ylabel('Probability of Number of Events')
    plt.show()
    
plot_pmf_poisson(25 , 5)

print('Geometric distribution')

def pmf_geo( p , x):
    return p*(1 - p)**(x - 1) 

def plot_pmf_geo(p , n):
    '''Plot the probability mass function of Geometric'''
    K = list(range(0 , n + 1))
    # print(K)
    P_geo = [pmf_geo( p , k) for k in K]
    plt.plot(K ,P_geo , '-o')
    plt.title('PMF of Geometric(%i)' %p)
    plt.xlabel('Probability')
    plt.ylabel('n')
    plt.show()
    
plot_pmf_geo(0.3 , 10)