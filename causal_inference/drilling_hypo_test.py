import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt
plt.style.use('ggplot')
import scipy.stats

'''
Does data provide strong evidence that the proportion of college
graduates who don't have an opinion on offshore drilling differs
from non-college graduates.

The Data:
            College Grad
            YES  |  NO  | 
Don't know| 104     131   
      Know| 334     258   
     total| 438     389

h_0 there is no difference between college and non-college opinions
n_a there is a difference in opinion amoung the two groups   
'''
n_c = 438
n_nc = 389
p_c = 104 / 438
p_nc = 131 / 389

p_pooled = (104 + 131) / (438 + 389)
p_d = p_c - p_nc
# Calculate the standard error for this dataset
se_temp_c = p_pooled * (1-p_pooled) / n_c
se_temp_nc = p_pooled * (1-p_pooled) / n_nc
se = np.sqrt(se_temp_c + se_temp_nc)

# Compute the test statistic, and graph the image
Z = (p_d - 0) / se # zero in this case becuase null is no difference
x_axis = np.arange(0.15, 0.45, 0.001)
upper = p_pooled + Z * se
lower = p_pooled - Z * se
pos_upper = np.linspace(upper, .45, 10)
pos_lower = np.linspace(lower, .15, 10)
plt.plot(x_axis, scipy.stats.norm.pdf(x_axis, p_pooled, se))
plt.vlines(upper, 0, 1, colors='darkblue')
plt.vlines(lower, 0, 1, colors='darkblue')
plt.show()

p_value = scipy.stats.norm.sf(abs(Z))*2

print(f'Part I - Z Score: {Z}, P-Value: {p_value}') # results is 0.00157 reject the null in favor of the alternative

# PII Those who support drilling
'''
The Data:
            College Grad
            YES  |  NO  | 
   support| 154     132   
     other| 284     257   
     total| 438     389

h_0 there is no difference between college and non-college opinions
n_a there is a difference in opinion amoung the two groups
'''
n_c = 438
n_nc = 389
p_c = 154/438
p_nc = 132/389
p_pooled = (132+154)/(n_c+n_nc)

p_d = p_c - p_nc
se_temp_c = p_pooled * (1-p_pooled) / n_c
se_temp_nc = p_pooled * (1-p_pooled) / n_nc
se = np.sqrt(se_temp_c+se_temp_nc)
Z = (p_d - 0) / se
p_value = scipy.stats.norm.sf(abs(Z)) * 2
print(f'Part II - Z Score: {Z}, P-Value: {p_value}') # 0.71 Fail to reject the null

# Plot the axis
x_axis = np.arange(0.15, .45, 0.001)
upper = p_pooled + Z * se
lower = p_pooled - Z * se
pos_upper = np.linspace(upper, .15, 10)
pos_lower = np.linspace(lower, .45, 10)
plt.plot(x_axis, scipy.stats.norm.pdf(x_axis, p_pooled, se))
plt.vlines(upper, 0, 1, colors='darkblue')
plt.vlines(lower, 0, 1, colors='darkblue')
plt.show()

