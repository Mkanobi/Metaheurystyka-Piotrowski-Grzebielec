import matplotlib.pyplot as plt
from quality_testing import tester
import numpy

x = [i for i in range(10, 61, 1)]
npx = numpy.array(x)
problem_count = 100
problem_type = "EUC_2D"
results = tester(x, problem_count, problem_type)

# print(numpy.array(results))

# plt.subplot(1, 2, 1)
fig, ((p, pn),(pn2, pn3)) = plt.subplots(2,2)

fig.suptitle("Średni czas działania algorytmów w zależności od DIMENSION (z " + str(problem_count) + " generowanych problemów " + problem_type + " dla każdego DIMENSION)")

p.plot(x, results[0], "-r", label="100-random")
p.plot(x, results[1], "-g", label="near")
p.plot(x, results[2], "-b", label="ex near")
p.plot(x, results[3], "-m", label="2-opt")
p.set(xlabel="DIMENISON problemu", ylabel="Czas działania w sekundach")

p.legend(loc="upper left")
p.grid()

pn.plot(x, [ results[0][i]/x[i] for i in range(len(x)) ], "-r", label="100-random / n")
pn.plot(x, [ results[1][i]/x[i] for i in range(len(x)) ], "-g", label="near / n")
pn.plot(x, [ results[2][i]/x[i] for i in range(len(x)) ], "-b", label="ex near / n")
pn.plot(x, [ results[3][i]/x[i] for i in range(len(x)) ], "-m", label="2-opt / n")
pn.set(xlabel="DIMENISON problemu", ylabel="Czas działania w sekundach / n")

pn.legend(loc="upper left")
pn.grid()

pn2.plot(x, [ results[0][i]/(x[i]*x[i]) for i in range(len(x)) ], "-r", label="100-random / n^2")
pn2.plot(x, [ results[1][i]/(x[i]*x[i]) for i in range(len(x)) ], "-g", label="near / n^2")
pn2.plot(x, [ results[2][i]/(x[i]*x[i]) for i in range(len(x)) ], "-b", label="ex near / n^2")
pn2.plot(x, [ results[3][i]/(x[i]*x[i]) for i in range(len(x)) ], "-m", label="2-opt / n^2")
pn2.set(xlabel="DIMENISON problemu", ylabel="Czas działania w sekundach / n^2")

pn2.legend(loc="upper left")
pn2.grid()

pn3.plot(x, [ results[0][i]/(x[i]*x[i]*x[i]) for i in range(len(x)) ], "-r", label="100-random / n^3")
pn3.plot(x, [ results[1][i]/(x[i]*x[i]*x[i]) for i in range(len(x)) ], "-g", label="near / n^3")
pn3.plot(x, [ results[2][i]/(x[i]*x[i]*x[i]) for i in range(len(x)) ], "-b", label="ex near / n^3")
pn3.plot(x, [ results[3][i]/(x[i]*x[i]*x[i]) for i in range(len(x)) ], "-m", label="2-opt / n^3")
pn3.set(xlabel="DIMENISON problemu", ylabel="Czas działania w sekundach / n^3")

pn3.legend(loc="upper left")
pn3.grid()



# plt.subplot(1, 2, 2)
# plt.plot(x, results[0], "-r", label="100-random")
# plt.plot(x, results[1], "-g", label="near")
# plt.plot(npx, (npx / 300) ** 2, "-c", label="square")
# plt.legend(loc="upper left")
# plt.grid()

plt.show()