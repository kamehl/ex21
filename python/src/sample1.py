import matploitlib.pyplot as plt
import numpy as np

x = np.arange(0,100,0.5)

hz = 5.0

y = np.sin(2.0 * np.pi * (x * hz) / 100)

plt.plot(x,y)
plt.savefig('test.png')
