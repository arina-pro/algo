import matplotlib.pyplot as plt
import numpy as np
import math

x = np.array(range(10))
y1 = x * np.power(2, x)
y2 = np.power(x, 3)
plt.subplot(411)
plt.plot(x, y1, label='x * 2^x')
plt.plot(x, y2, label='x^3')
plt.legend()

x = np.array(range(100))
y3 = 3 * x + 5
y4 = x
plt.subplot(412)
plt.plot(x, y3, label='3x + 5')
plt.plot(x, y4, label='x')
plt.legend()

y5 = 10 * np.log2(x)
y6 = np.power(np.log2(x), 2)
plt.subplot(413)
plt.plot(x, y5, label='10log2(x)')
plt.plot(x, y6, label='(log2(x))^2')
plt.legend()

x = np.array(range(10))
y7 = np.power(x, 2) / (np.log(x) / np.log(3))
y8 = x * np.power(np.log2(x), 2)
plt.subplot(414)
plt.plot(x, y7, label='x^2 / log3(x)')
plt.plot(x, y8, label='x(log2(x))^2')
plt.legend()

plt.show()