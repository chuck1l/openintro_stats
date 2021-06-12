import scipy.stats

# cdf is the probability that random sample X is less than or equal to x
# pdf is the probability that random sample X is near x in the distribution
# ppf is the percent point function or inverse of cdf

def z_score(x, mu, sigma):
    '''
    This function calculates the z-score, or how many 
    standard deviations x lies from the mean of a
    normal distribution
    '''
    return (x-mu)/sigma

def probability(x, mu, sigma):
    '''
    This function calculates the probability of a random sample
    being less than or equal to x
    '''
    return scipy.stats.norm(mu, sigma).cdf(x)

def x_from_z(z_score, mu, sigma):
    '''
    This fucntion calculates the value in the normal distribution
    from the z-score, or at a specified number of deviations from
    the mean.
    '''
    return z_score * sigma + mu

def x_from_probability(pval, mu, sigma):
    '''
    This function calculates value of x from a specified 
    probability, or the inverse of cdf. What value is at the 
    percentile..
    '''
    return scipy.stats.norm(mu, sigma).ppf(pval)


def z_from_probability(pval, mu, sigma):
    x = x_from_probability(pval, mu, sigma)
    return z_score(x, mu, sigma)



if __name__ == '__main__':

    print(z_from_probability(.68, 1100, 200))
    print(z_from_probability(.95, 1100, 200))
    print(z_from_probability(.997, 1100, 200))
  