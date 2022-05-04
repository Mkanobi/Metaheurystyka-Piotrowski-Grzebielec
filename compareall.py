import tsplib95
from algorithms2 import extended_nearest_neighbour, k_random, nearest_neighbour, two_opt
from problem_render import problem_render_asymmetrical, problem_render_euclidean, problem_render_symmetrical
from tabu_simple import tabu_search as tabu_alt
from tabu_noalt import tabu_search as tabu_noalt
import statistics as stat
import math
import matplotlib.pyplot as plt
import time
# import numpy
iterations = 300
alt_length = 5
alt_limit = 5
def quality_tester(x, k=100):
    results = [[0.0 for _ in range(len(x))] for _ in range(6)]
    tmp = [[0.0 for _ in range(k)] for _ in range(6)]
    lst = [[[],0] for _ in range(6)]

    results_time = [[0.0 for _ in range(len(x))] for _ in range(6)]
    tmp_time = [[0.0 for _ in range(k)] for _ in range(6)]

    for i in range(len(x)):
        print(i)
        for j in range(k):
            print(str(i) + ", " + str(j))
            problem1 = tsplib95.parse(problem_render_euclidean('problem testowy',x[i],0,500))
            #problem1 = tsplib95.parse(problem_render_asymmetrical('problem testowy',x[i],0,500))
            #problem1 = tsplib95.parse(problem_render_symmetrical('problem testowy',x[i],0,500))
            #print(len(lst[0][0]))

            start = time.time()
            lst[0] = k_random(problem1,100)
            end = time.time()
            tmp_time[0][j] = end - start

            start = time.time()
            lst[1] = nearest_neighbour(problem1,1)
            end = time.time()
            tmp_time[1][j] = end - start
            
            start = time.time()
            lst[2] = extended_nearest_neighbour(problem1)
            end = time.time()
            tmp_time[2][j] = end - start

            start = time.time()
            lst[3] = two_opt(problem1)
            end = time.time()
            tmp_time[3][j] = end - start

            start = time.time()            
            lst[4] = tabu_alt(problem1,lst[0][0],'swap',7,alt_length,iterations,alt_limit)
            end = time.time()
            tmp_time[4][j] = end - start

            start = time.time()            
            lst[5] = tabu_alt(problem1,lst[1][0],'swap',7,alt_length,iterations,alt_limit)
            end = time.time()
            tmp_time[5][j] = end - start

            #lst[5] = tabu_noalt(problem1,lst[0][0],'swap',7,50)

            for l in range(6):
                results_time[l][i] = stat.mean(tmp_time[l])
                        
            solution = math.inf

            for z in range (0,6):
                if (solution > lst[z][1]):
                    solution = lst[z][1]
            
            for l in range(0,6):
                tmp[l][j] = abs(lst[l][1] - solution) / solution
        
        for l in range(0,6):
            results[l][i] = stat.mean(tmp[l])
        
    return results, results_time



x = [i for i in range(20, 31, 1)]
problem_count = 20
results = quality_tester(x,problem_count)
problem_type = "EUC_2D"
fig, (ax1, ax2) = plt.subplots(1, 2)
fig.suptitle('tabu z listą nawrotów (rozmiar nawrotów + ' + str(alt_length) + ', limit nawrotów ' + str(alt_limit) + ', rozw. startowe - 100-random, średnia z 20 prób, limit ' + str(iterations) + ' iteracji, wielkość tabu: 7, sąsiedztwo: swap)')
#ax1.plot(x, results[0], "-o", label="100-random")
ax1.plot(x, results[0][1], "-g", label="near")
ax1.plot(x, results[0][2], "-b", label="ex near")
ax1.plot(x, results[0][3], "-m", label="2-opt")
#ax1.plot(x, results[5], "-r", label="tabu bez listy nawrotów")
ax1.plot(x, results[0][4], "-r", label="tabu 100-random")
ax1.plot(x, results[0][5], "-k", label="tabu nearest-neighbour")
ax1.set_title("Wykres średnich jakości rozwiązań w zależności od wielkości problemu\n " + problem_type + ", średnia z " + str(problem_count) + " prób")
ax1.set(xlabel="Wielkość problemu",ylabel="Średni błąd")
ax1.legend(loc="upper left")
ax1.grid()
#ax1.show()

ax2.set_title("Średni czas działania algorytmów w zależności od wielkości problemu\n (średnia z " + str(problem_count) + " generowanych problemów " + problem_type + " dla każdej wielkości problemu)")

#ax2.plot(x, results[0], "-o", label="100-random")
ax2.plot(x, results[1][1], "-g", label="near")
ax2.plot(x, results[1][2], "-b", label="ex near")
ax2.plot(x, results[1][3], "-m", label="2-opt")
ax2.plot(x, results[1][4], "-r", label="tabu 100-random")
ax2.plot(x, results[1][5], "-k", label="tabu nearest-neighbour")
ax2.set(xlabel="DIMENISON problemu", ylabel="Czas działania w sekundach")
ax2.legend(loc="upper left")
ax2.grid()

plt.show()