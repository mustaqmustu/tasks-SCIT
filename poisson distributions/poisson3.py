import numpy as np
a=np.random.poisson(3,1000)
print(a)
#gives you thye poisson distribution with lam=3 and size=1000
import matplotlib.pyplot as plt
count,bons,ignored=plt.hist(a,14,density = True)
plt.show()
#gives you histogram of above poisson distribution
