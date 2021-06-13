import pandas as pd
import numpy as np
import math
import scipy.stats

'''
Applying  confidence intervals and hypothesis tests to differences
in population proportions p1 - p2

Still must meet the indepence, but for both sample groups

The success-failure condition must also be met for both groups
(minimum of ten observations for both conditions within both groups)

New standard error calculation

SE = sqrt( (p_t * (1 - p_t) / n_t) + (p_c * (1 - p_c) / n_c) )

'''
# Example with treatment and control group
# Treatment 14 success, 40 failures
# Control 11 successes, 50 failures (notice all have greater than 10)

p_t = 14/40
p_c = 11/50
# P difference between treatment and control
p_d = p_t - p_c

temp_se_t = p_t * (1-p_t) / 40
temp_se_c = p_c * (1-p_c) / 50
SE = np.sqrt(temp_se_t + temp_se_c)

# 90% Confidence interval z-score = 1.65 so:
upper = p_d + 1.65 * SE
lower = p_d - 1.65 * SE

'''
In this example, we are 90% confident that the treatment had a delta of 
-2.7% to 28.7% percentage point impact on success rate for patients similar
to the ones in this study.

Because 0% is contained in the interval, we don't have enough information
to say if the treatment helps or harms the patients
'''

# EXAMPLE ONE MAMMOGRAM
'''
Hypothesis testing with the difference of probability is 0 because
As it pertains to the null distribution, not the results
h_0 = .5 (p_t - p_c = 0, or equivalently p_t = p_c)

Group 1 = women received regular mammograms
Control = women received regualr non-mammogram exams

                Death From Breast Cancer
                   Yes         No           Total
    Mammograms|   500          44,425       44,925
       Control|   505          44,405       44,910
        Totals|   1,005        88,830       89,835

h_0 : Mammograms are equally as effective as non-mammagrams (p = .5)
h_a : Mammograms are not equally as effective
'''
# in this case p_t and p_c are equal so we must use p_pooled
p_pooled = (500 + 505) / (44925 + 44910)
p_t = 500/44925
p_c = 505/44910

# point estimate (differnce in breast cancer death rates)
p_d = p_t - p_c

se_t_temp = p_pooled * (1-p_pooled) / 44925
se_c_temp = p_pooled * (1-p_pooled) / 44910
SE = np.sqrt(se_t_temp + se_c_temp)

# compute the test statistic Z and graph the picture
Z = (p_d - 0) / SE

p_value = scipy.stats.norm.sf(abs(Z)) * 2 # two tailed test!!!

print(Z, p_d, SE, p_value)