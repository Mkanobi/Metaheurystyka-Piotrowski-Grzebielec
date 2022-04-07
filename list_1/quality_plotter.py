import matplotlib.pyplot as plt
from quality_test import quality_tester

x = [i for i in range(10, 21, 1)]
results = quality_tester(x)

plt.plot(x, results[0], "-r", label="100-random")
plt.plot(x, results[1], "-g", label="near")
plt.plot(x, results[2], "-b", label="ex near")
plt.plot(x, results[3], "-m", label="2-opt")
plt.title("Wykres średnich jakości rozwiązań w zależności od wielkości problemu")
plt.xlabel("Wielkość problemu")
plt.ylabel("Średni błąd")
plt.legend(loc="upper left")
plt.grid()
plt.show()