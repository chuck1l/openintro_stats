import math

'''
The bionomial distribution is used to describe the number of successes
in a fixed number of trials.

k success in n trials = n!/(k! * (n-k)!) * p**k * (1-p)**(n-k)

Mean (mu) = n * p
Variance (sigma squared) = n * p * (1-p)
Standard Dev (sigma) = np.sqrt(n * p * (1-p))

Four conditions for binomial to check:
(1) The trials are independent.
(2) The number of trials, n, is fixed.
(3) Each trial outcome can be classified as a success or failure. 
(4) The probability of a success, p, is the same for each trial.
'''


def binom_probability(n, k, p):
    '''
    This function will return the probability that the count of
    overservations will be deemed successful in n trials, with
    the specified probability. 

    Parameters: 
        n = number of independent trials
        k = number of successes
        p = pobability of success

    Returns:
        The probability of k successes in n trials
    '''
    n_factorial = math.prod(range(1, n+1))
    if k == 0:
        k_factorial = 1
    else:
        k_factorial = math.prod(range(1, k+1))

    n_minus_k_fact = math.prod(range(1, (n-k)+1))
    n_choose_k = n_factorial/(k_factorial*n_minus_k_fact)

    return n_choose_k * p**(k) * (1-p)**(n-k)
    


if __name__ == '__main__':

    print(binom_probability(8, 3, .3))
    print(binom_probability(8, 5, .7))
