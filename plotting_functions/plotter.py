import matplotlib.pyplot as plt
from test import tester

x = [i for i in range(1, 101, 1)]
results = tester(x, 100)

plt.plot(x, results[0], "-r", label="100-random")
plt.plot(x, results[1], "-g", label="near")
plt.plot(x, results[2], "-b", label="ex near")
plt.plot(x, results[3], "-m", label="2-opt")
plt.legend(loc="upper left")
plt.grid()
plt.show()