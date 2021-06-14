import scipy.stats as stats
import seaborn as sns

'''
ANOVA uses a single hypothesis test to check whether the means across
many groups are equal.

3 Conditions on the data:
(1) The observations are independent within and across groups
(2) The data within each group are normal
(3) The variability across the groups is about equal


'''
# data in columns
sns.boxplot(data=df[[col1, col2, col3]])
fvalue, pvalue = stats.f_oneway(df[col1], df[col2], df[col3])
print(fvalue, pvalue)