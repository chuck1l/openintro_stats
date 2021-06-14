import matplotlib.pyplot as plt
plt.style.use('ggplot')
import numpy as np
import scipy.stats as stats
import math


fig, axs = plt.subplots(2)
fig.suptitle('Normal and T-Distributions')

mu = 0
variance = 1
sigma = math.sqrt(variance)

x = np.linspace(mu - 3*sigma, mu + 3*sigma, 100)
axs[0].plot(x, stats.norm.pdf(x, mu, sigma))
axs[0].set_title('Normal Distribution');

# Plotting the t-distribution 
n = 20
df = n - 1
x_t = np.linspace(
    stats.t.ppf(0.01, df),
    stats.t.ppf(0.99, df), 100
)
axs[1].plot(x_t, stats.t.pdf(x_t, df=df))
axs[1].set_title('t-Distribution');
plt.tight_layout()
plt.show()