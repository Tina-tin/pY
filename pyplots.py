import matplotlib.pyplot as plt
import numpy as np

x = list(np.arange(-1,2, 0.0002))


def func(num):
    # function n^2 + 3n + 5
    return [n*n + 3*n + 5 for n in num]


plt.plot(func(x))
plt.ylabel('Values')
plt.xlabel('Arguments')
plt.show()