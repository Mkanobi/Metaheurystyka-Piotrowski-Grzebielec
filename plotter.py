import matplotlib.pyplot as plt
from test import tester
import numpy

x = [i for i in range(10, 31, 5)]
npx = numpy.array(x)
results = tester(x, 100)

# print(numpy.array(results))

# plt.subplot(1, 2, 1)
plt.plot(x, results[0], "-r", label="100-random")
plt.plot(x, results[1], "-g", label="near")
plt.plot(x, results[2], "-b", label="ex near")
plt.plot(x, results[3], "-m", label="2-opt")
# plt.plot(npx, [numpy.nan for _ in range(5)], "-c", label="square")
plt.legend(loc="upper left")
plt.grid()

# plt.subplot(1, 2, 2)
# plt.plot(x, results[0], "-r", label="100-random")
# plt.plot(x, results[1], "-g", label="near")
# plt.plot(npx, (npx / 300) ** 2, "-c", label="square")
# plt.legend(loc="upper left")
# plt.grid()

plt.show()