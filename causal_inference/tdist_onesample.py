import numpy as np
from scipy.stats import t
'''
The standard error is dependent on the population standard deviation,
sigma. We rarely know sigma, so we estimate it. We use the t-distribution
to fix the problem of the imperfections behind estimating sigma.

Two Conditions Required for Modeling:
Independence: The sample observations must be independent

Normality: When the sample is small, observations must come from a
normally distributed population. Condition can relax based for larger
and larger sample sizes.

n < 30 : if the sample size is less than 30 and no clear outliers 
        exist, we assume the data come from normally distributed 
        population, nearly normal.

n >= 30: if the sample size is at least 30 and no extreme outliers
        exist, we assume the sampling distribution of x-bar is nearly
        normal. Even if the underlying distribution of observations is
        not.

SE = sigma / sqrt(n) (don't know sigma so s = sigma esimate). s
SE = s/sqrt(n) (s = standard deviation of the sample)

t-distribution is always centered at 0, and has one parameter, 
degrees of freedom (df). Which describes the exact shape of the 
bell-shaped t-distribution.

degrees of freedom (df) traditionally = n - 1

SE = s/sqrt(n)
df = n - 1

'''
# For 95% confidence
# 2.5% for upper
s = 2.3
n = 19
df = n - 1
se = s/np.sqrt(n)
# 95% confidence interval
conf_int = t.interval(alpha=.95, df=df, loc=4.4, scale=se)

# Runners problem 
'''
new average race time = 97.32
old average race time = 93.29
average race SE = 1.70 or s/sqrt(n)
n = 100
'''
t = (97.32 - 93.29)/1.70
p_value = t.sf(abs(t), df=99) * 2

# Finding p-value from T-score
# scipy.stats.t.sf(abs(), df) * 2 for two tailed
'''
(a) n=11,T =1.91
(b) n=17,T =−3.45
(c) n=7,T =0.83
(d) n=28,T =2.13
'''
a = t.sf(abs(1.91), df=10) * 2
b = t.sf(abs(-3.45), df=16) * 2
c = t.sf(abs(0.83), df=6) * 2
d = t.sf(abs(2.13), df=27) * 2
print(a, b, c, d)