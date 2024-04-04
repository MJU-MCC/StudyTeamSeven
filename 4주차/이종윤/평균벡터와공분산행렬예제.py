import numpy as np

x = np.array([[5.1,3.5,1.4,0.2], [4.9,3.0,1.4,0.2], [4.7,3.2,1.3,0.2], [4.6,3.1,1.5,0.2], [5.0,3.6,1.4,0.2], [5.4,3.9,1.7,0.4], [4.6,3.4,1.4,0.3], [5.0,3.4,1.5,0.2]])
print(x, '\n\n')

x_mean = x.mean(axis=0)
print(x_mean, '\n\n')

x_var = np.cov(x.T, ddof=0)
print(x_var)
