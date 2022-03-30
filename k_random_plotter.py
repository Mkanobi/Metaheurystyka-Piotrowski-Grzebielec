import matplotlib.pyplot as plt
from k_random_testing import tester_k_random
import numpy

x = [i for i in range(1, 101, 1)]
npx = numpy.array(x)
results = tester_k_random(100,x)

# print(numpy.array(results))

# plt.subplot(1, 2, 1)
plt.plot(x, results, "-r", label="k-random")
# plt.plot(npx, [numpy.nan for _ in range(5)], "-c", label="square")
plt.legend(loc="upper left")
plt.title("Wykres dla problemu o wielkosci 100 w zależności od k dla k-random")
plt.grid()


plt.show()