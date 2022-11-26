import matplotlib.pyplot as plt
import math



print('Binomial distribution')

def pmf_binom(k , n , p):
    return (math.factorial(n) / (math.factorial(k) * math.factorial(n - k)) ) * p**k *( 1- p)**(n - k)


print("a) " + str(pmf_binom(2 , 5 , 0.1)))




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
    
plot_pmf_binom(5 , 0.1)