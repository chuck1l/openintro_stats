import numpy as np

'''
If X is a random variable that takes value 1 with probability of success
p, and 0 probability of success 1-p - then X is a bernoulli random variable
with:

Mean(mu) = p
Standard Deviation(sigma) = sqrt(p * (1-p))

The geometric distribution is used to describe how many trials it takes to
observe a success.

The trials must be independent and identically distributed (don't affect each
other, and have equal probability of success)

Mean (mu) = 1/p
Variance (sigma squared) = (1-p)/p**2
Standard Dev. (sigma) = sqrt((1-p)/p**2)
'''


def standard_deviation(p):
    '''
    This funtion simply returns the standard deviation for 
    a Bernoulli distribution.
    '''
    return np.sqrt((1-p)/p**2)


def probability_success_on_n(p, n):
    '''
    This function returns the probability of success for n trials.
    '''
    return (1-p)**(n-1) * p


def a_success_within_n_trials(p, n):
    '''
    This function returns the probability of a single success within
    a number (n) of trails
    '''
    results = []

    for i in range(1, n+1):
        print(i)
        results.append(probability_success_on_n(p, i))

    return sum(results)


if __name__ == '__main__':

    print(probability_success_on_n(.125, 3))
    