import scipy.stats

# cdf is the probability that random sample X is less than or equal to x
# pdf is the probability that random sample X is near x in the distribution
# ppf is the percent point function or inverse of cdf

def z_score(x, mu, sigma):
    return (x-mu)/sigma

def p_value(x, mu, sigma):
    return scipy.stats.norm(mu, sigma).cdf(x)

def x_from_z(z_score, mu, sigma):
    return z_score * sigma + mu

def x_from_pval(pval, mu, sigma):
    return scipy.stats.norm(mu, sigma).ppf(pval)



if __name__ == '__main__':

    mu = 1100
    sigma = 200
    x = 1500 
    print(z_score(x, mu, sigma))
    print(p_value(x, mu, sigma))
    print(x_from_z(z_score(x, mu, sigma), mu, sigma))
    print(x_from_pval(p_value(x, mu, sigma),mu, sigma))