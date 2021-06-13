from scipy.stats import chisquare

'''
CHI-SQUARED:
We are to evaluate whether there is convincing evidence that a set of
observed counts in k categories are unusually different from what might
be expected under a null hypothesis.

expected counts are based on the null hypothesis.

The conditions:
Independence: Each case that contributes a count to the table must be
              independent of all other cases in the table
Sample size: Each expected count is at least 5

The test statistic below follows a chi-square distribution with 
k - 1 degrees of freedom
O = the observed value
E = the expected value

X2 = (O1 - E1)**2 / E1 + (O2 - E2)**2 / E2 + ..... + (On - En)**2 / En

The p-value in this test statistic is found by looking at the upper tail
of this chi-square distribution. We consider the upper tail because larger
values of X2 would provide greater evidence against the null hypothesis
'''
observed_list = [717, 369, 155, 69, 28, 14, 10]
observed_list2 = [500, 600, 130, 100, 200, 45, 15]
expected_list = [743, 338, 154, 70, 32, 14, 12]

result_1 = chisquare(f_obs=observed_list, f_exp=expected_list) 

result_2 = chisquare(f_obs=observed_list2, f_exp=expected_list)

print(f'Observation I: {result_1}\n')
print(f'Observation II: {result_2}')