import numpy as np
from scipy.stats import t
'''
Two sets of observations are "paired" if each observation in one set
has a special correspondence or connection with exactly one observation
in the other data set.

Using the difference between the paired observations is a common and
useful way to analyze paired data.

Then use the exact same t_dist method in a one sample method, on the
differences column mean (x-bar) and standard error (s/sqrt(n))
'''

# Amazon vs Bookstore example
# Bookstore - Amazon price for every book give us...
# h_0 that prices for amazon are equal to bookstore
# h_a that procies are different between the two

x_bar_diff = 3.58 # mean of sample
s_diff = 13.42 # standard deviation of sample
n_diff = 68 # books
SE = s_diff / np.sqrt(n_diff)
df = n_diff - 1
expected_value = 0 # zero because h_nought equals is no differnce

t_score = (x_bar_diff - expected_value) / SE
p_value = t.sf(abs(t_score), df=df) * 2
confidence_95 = t.interval(.95, df=df, loc=x_bar_diff, scale=SE)

print(round(t_score, 2), round(p_value, 2), confidence_95)