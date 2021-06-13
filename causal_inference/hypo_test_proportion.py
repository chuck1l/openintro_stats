

'''
Hypothesis Testing for proportions. When evaluating hypotheses for
proportions we will use the p-value method, and the evaluation method
will be slightly modified.

Seting a H_nought and H_alternative. Since we are attempting to either
fail to reject the null, or reject the null in favor of the alternative,
the sampling distribution is determined under the null proportion

p_0 is the sample proportion. So,

The conditions are:
Independence: The poll was based on a simple random sample

Success-failure: Based on the sample size of n
n * p_0 >= 10 and n * (1 - p_0) >= 10

The above is evaluating the null hypothesis estimate. This is a procedural
difference from the confidence interval method.

The p-value represents the probability of the observed p_hat, or p_hat 
that is more extreme, if the null hypothesis were true. Evaluating the 
"null distribution"

p-value is found by, finding the null distribution, and then find a tail
area in that distribution corresponding to our point estimate. The p-value
represents the probability of observing such an extreme sample proportion
by chance, if the null is true.

SE = sqrt(p_0 * (1-p_0) / n)

generate the z-score just as before: observation (x)

Z = (x - p_0) / SE

p_value = (scipy.stats.norm(p_0, SE).cdf(x)) x 2

times 2 because we are interested in two-tail test. 

compare p_value to alpha (traditionally 0.05)

We reject the null if the p_value is less than or equal to alpha

'''