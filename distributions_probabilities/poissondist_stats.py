import math
import numpy as np

'''
The Poisson distribution is often useful for estimating the number
of events in a large population over a unit of time.

The rate: The average number of occurances/events over the specified
unit of time. (typically denoted by lambda or mu)

Standard Deviation = sqrt(lambda)

P(ovserve k events) = (lambda**k * e**-lambda) / k!

The conditions for Poisson to check:
(1) The trials are independent.
(2) The population that generates the events is large
'''
def poisson_probability(mu, k):
    '''
    This function returns the poisson probability of event(s) occuring
    over a specified unit of time. The time in the rate (lambda) and 
    the specified unit of time must be on the same scale.

    Parameters:
        lambda = The rate
        k = The number of events we expect to observe
    
    Returns: 
        The probability of k number of events occuring with regard to 
        lambda
    '''
    if k == 0:
        k_factorial = 1
    else:
        k_factorial = math.prod(range(1, k+1))

    p = mu**k *  np.exp(-1 * mu) / k_factorial

    return p

if __name__ == '__main__':

    print(poisson_probability(75, 70))