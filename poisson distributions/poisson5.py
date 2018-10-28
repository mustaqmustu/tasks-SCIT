import numpy as np
a=np.random.poisson(5,1000)
print(a)
#gives you poison distribution of lam=5 and size =1000
import matplotlib.pyplot as plt
count,bons,ignored=plt.hist(a,14,density = True)
plt.show()
#gives you the histogram of above poisson distribution
