mu, sigma = 0, 0.1 # mean and standard deviation
import numpy as np
s = np.random.normal(mu, sigma, 1000)
print(s)
#gives you normal distribution 
import matplotlib.pyplot as plt
count, bins, ignored = plt.hist(s, 30, density=True)
plt.plot(bins, 1/(sigma * np.sqrt(2 * np.pi)) *
                np.exp( - (bins - mu)**2 / (2 * sigma**2) ),
         linewidth=2, color='r')
plt.show()
#gives you histogram of above normal distribution
