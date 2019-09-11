import matplotlib.pyplot as plt
import numpy as np
import math

x = np.array(range(0, 10))
#x = np.linspace(-100, 100)
y = [np.log(x) / np.log(5), np.power(x, 0.1), np.power(x, 0.5), x, x * np.power(np.log2(x), 3), np.power(x, 3)]#, np.power(4, x)]
labels = ['log5(x)', 'x^0.1', 'sqrt(x)', 'x', 'x(log2(x))^3', 'x^3', '4^x', 'x!']
[plt.plot(x, y[i], label=labels[i]) for i in range(len(y))]
plt.legend()
plt.show()