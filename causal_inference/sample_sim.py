from os import confstr
import pandas as pd
import numpy as np
import random
import matplotlib.pyplot as plt
plt.style.use('ggplot')
import scipy.stats

pop_size = 250000000
s_prop = int(pop_size * .88)
n_prop = int(pop_size * .12)
support_list = ['support'] * s_prop
not_list = ['not'] * n_prop

possible_entries = support_list + not_list
random.shuffle(possible_entries)

p = possible_entries.count('support')/pop_size

# Sample from the population 1000 times
# random.sample without replacement
# random.choices with replacement
n = 1000
sampled_entries = random.sample(possible_entries, n)
p_hat = sampled_entries.count('support')/n

error = p - p_hat

'''
Central Limit Therom: When observations are independent and the sample
size is sufficiently large, the sample proportion (p_hat) will tend to
follow a normal distribution with the following mean and standard error

mu_phat = p
SE_phat = sqrt(p * (1-p) / n)

Considered sufficiently large if:
n * p >= 10 and
n * (1-p) >= 10
"success-failure condition"

'''

# run the sampling test 10,000 times to see a distribution of sample
# proportion
n_trials = 10000
results = []
for i in range(10000):
    sample_loop = random.sample(possible_entries, 1000)
    p_hat_loop = sample_loop.count('support')/1000
    results.append(p_hat_loop)

plt.hist(results, bins=15)
#plt.show()

# CONFIDENCE INTERVALS (Constructing 95%)
'''
Standard Error represents Standard Deviation of the point estimate (p_hat)
Central Limit Therom gives us a normal distribution (meeting conditions)

95% represents ~1.96 Standard Deviations (or SE) of the mean.

point estimate = +/- 1.96 x SE sqrt((p * (1-p)) / n)
'''

# Calculate the z-score for a desired confidence interval, standard normdist
def z_score_conf(conf_int):
    '''
    this function generates the z-score (standard deviations of mean)

    Parameters: desired confidence interval

    Returns: z-score
    '''
    mu = 0
    sigma = 1
    tail = (1 - conf_int) / 2
    x = scipy.stats.norm(mu, sigma).ppf(tail)

    return abs((x-mu)/sigma)

# We are 95% confident that the population proportion (or mean) lives within
phat = sum(results) / len(results)
se = np.sqrt((phat * (1-phat))/n)
con_int = z_score_conf(.95)

print(round(con_int, 2))

upper_95 = phat + con_int * se
lower_95 = phat - con_int * se

print(f'\
    p hat: {round(phat, 2)}\n\
    SE_hat: {round(se, 2)}\n\
    Upper CI: {round(upper_95, 2)}\n\
    Lower CI: {round(lower_95, 2)}\
    '
)

breakpoint()
print('stopping here')