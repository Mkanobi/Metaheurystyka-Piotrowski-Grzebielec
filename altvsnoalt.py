import tsplib95
from algorithms2 import extended_nearest_neighbour, k_random, nearest_neighbour, two_opt
from problem_render import problem_render_euclidean
from tabu_simple import tabu_search as tabu_alt
from tabu_noalt import tabu_search as tabu_noalt
import statistics as stat
import math
import matplotlib.pyplot as plt
# import numpy

def quality_tester(x, k=100):
    results = [[0.0 for _ in range(len(x))] for _ in range(6)]
    tmp = [[0.0 for _ in range(k)] for _ in range(6)]
    lst = [[[],0] for _ in range(6)]

    for i in range(len(x)):
        print(i)
        for j in range(k):
            problem1 = tsplib95.parse(problem_render_euclidean('problem testowy',x[i],0,500))
            print(len(lst[0][0]))
            lst[0] = k_random(problem1,100)
            #lst[1] = nearest_neighbour(problem1,1)
            #lst[2] = extended_nearest_neighbour(problem1)
            #lst[3] = two_opt(problem1)
            lst[4] = tabu_noalt(problem1,lst[0][0],'swap',7,100)
            lst[5] = tabu_alt(problem1,lst[0][0],'swap',7,5,100,10)
            
            solution = math.inf

            for k in range (4,6):
                if (solution > lst[k][1]):
                    solution = lst[k][1]
            
            for l in range(4,6):
                tmp[l][j] = abs(lst[l][1] - solution) / solution
        
        for l in range(4,6):
            results[l][i] = stat.mean(tmp[l])
        
    return results



x = [i for i in range(20, 31, 1)]
results = quality_tester(x,10)

#plt.plot(x, results[0], "-r", label="100-random")
#plt.plot(x, results[1], "-g", label="near")
#plt.plot(x, results[2], "-b", label="ex near")
#plt.plot(x, results[3], "-m", label="2-opt")
plt.plot(x, results[4], "-r", label="tabu bez listy nawrotów")
plt.plot(x, results[5], "-g", label="tabu z listą nawrotów (rozmiar 5, limit 10)")
plt.title("Wykres średnich jakości rozwiązań tabu w zależności od wielkości problemu, rozw. startowe - 100-random, średnia ze 100 prób, limit 100 iteracji, wielkość tabu: 7")
plt.xlabel("Wielkość problemu")
plt.ylabel("Średni błąd")
plt.legend(loc="upper left")
plt.grid()
plt.show()