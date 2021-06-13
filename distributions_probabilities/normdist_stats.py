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


def percentile(x, mu, sigma):
    '''
    This function calculates the probability of a random sample
    being less than or equal to x
    '''
    return scipy.stats.norm(mu, sigma).cdf(x)


def probability(x, mu, sigma):
    '''
    This function calculates the probability of a random sample
    being equal to or near to x
    '''
    return scipy.stats.norm(mu, sigma).pdf(x)


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

    mu_f = 77
    sig_f = 5
    x_f = 83

    mu_c = (mu_f - 32) * (5/9)
    sig_c = 5/9 * 5
    x_c = (x_f - 32) * (5/9)

    perc_f = (1- percentile(x_f, mu_f, sig_f)) * 100
    perc_c = (1 - percentile(x_c, mu_c, sig_c)) * 100

    prob_f = (probability(x_f, mu_f, sig_f)) * 100
    prob_c = (5/9) * (probability(x_c, mu_c, sig_c)) * 100

    print(f'probability F: {prob_f.round(2)}\nprobability C: {prob_c.round(2)}')
    print('\n')
    print(f'percentile F: {perc_f.round(2)}\npercentile C: {perc_c.round(2)}')