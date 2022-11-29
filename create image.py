import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt('DS0.txt', dtype = np.int32)
plt.figure(figsize=(9.6, 5.4))
plt.scatter(data[:, 1], data[:, 0])
plt.savefig("output.jpg")
