import tsplib95
from algorithms2 import extended_nearest_neighbour, k_random, nearest_neighbour, two_opt
from goal_function import goal_function
from problem_render import problem_render_asymmetrical, problem_render_euclidean, problem_render_symmetrical
from tabu_simple import tabu_search as tabu_alt
import statistics as stat
import math
import matplotlib.pyplot as plt
import time
import sys
# import numpy

iterations = 100
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

#             start = time.time()
            lst[0] = k_random(problem1,100)
#             end = time.time()
#             tmp_time[0][j] = end - start

#             start = time.time()
            #lst[1] = nearest_neighbour(problem1,1)
#             end = time.time()
#             tmp_time[1][j] = end - start
            
#             start = time.time()
            #lst[2] = extended_nearest_neighbour(problem1)
#             end = time.time()
#             tmp_time[2][j] = end - start

            start = time.time()
            lst[3] = tabu_alt(problem1,lst[0][0],'swap',7,alt_length,iterations,alt_limit)
            end = time.time()
            tmp_time[3][j] = end - start
            if (lst[3][1] != goal_function(problem1,lst[3][0])):
                print("Blad swap!")
                return 1

            start = time.time()            
            lst[4] = tabu_alt(problem1,lst[0][0],'insert',7,alt_length,iterations,alt_limit)
            end = time.time()
            if (lst[4][1] != goal_function(problem1,lst[4][0])):
                print("Blad insert!: " + str(goal_function(problem1,lst[4][0])) + ", " + str(lst[4][1]))
                return 1
            tmp_time[4][j] = end - start

            start = time.time()            
            lst[5] = tabu_alt(problem1,lst[0][0],'invert',7,alt_length,iterations,alt_limit)
            end = time.time()
            if (lst[5][1] != goal_function(problem1,lst[5][0])):
                print("Blad invert!" + str(goal_function(problem1,lst[5][0])) + ", " + str(lst[5][1]))
                return 1
            tmp_time[5][j] = end - start

            #lst[5] = tabu_noalt(problem1,lst[0][0],'swap',7,50)

            for l in range(3,6):
                results_time[l][i] = stat.mean(tmp_time[l])
                        
            solution = math.inf
            #print(str(lst[3][1]) + " " + str(lst[4][1]) + " " + str(lst[5][1]))
            for z in range (3,6):
                if (solution > lst[z][1]):
                    solution = lst[z][1]
            
            for l in range(3,6):
                tmp[l][j] = abs(lst[l][1] - solution) / solution
        
        for l in range(3,6):
            results[l][i] = stat.mean(tmp[l])
        
    return results, results_time



x = [i for i in range(20, 31, 1)]
problem_count = 20
results = quality_tester(x,problem_count)
problem_type = "EUC_2D"
fig, (ax1, ax2) = plt.subplots(1, 2)
fig.suptitle('tabu z list?? nawrot??w (rozmiar nawrot??w + ' + str(alt_length) + ', limit nawrot??w ' + str(alt_limit) + ', rozw. startowe - 100-random, ??rednia z 20 pr??b, limit ' + str(iterations) + ' iteracji, wielko???? tabu: 7)')
#ax1.plot(x, results[0], "-o", label="100-random")
# ax1.plot(x, results[0][1], "-g", label="near")
# ax1.plot(x, results[0][2], "-b", label="ex near")
ax1.plot(x, results[0][3], "-m", label="tabu swap")
#ax1.plot(x, results[5], "-r", label="tabu bez listy nawrot??w")
ax1.plot(x, results[0][4], "-r", label="tabu insert")
ax1.plot(x, results[0][5], "-g", label="tabu invert")
ax1.set_title("Wykres ??rednich jako??ci rozwi??za?? w zale??no??ci od wielko??ci problemu\n " + problem_type + ", ??rednia z " + str(problem_count) + " pr??b")
ax1.set(xlabel="Wielko???? problemu",ylabel="??redni b????d")
ax1.legend(loc="upper left")
ax1.grid()
#ax1.show()

ax2.set_title("??redni czas dzia??ania algorytm??w w zale??no??ci od wielko??ci problemu\n (??rednia z " + str(problem_count) + " generowanych problem??w " + problem_type + " dla ka??dej wielko??ci problemu)")

#ax2.plot(x, results[0], "-o", label="100-random")
# ax2.plot(x, results[1][1], "-g", label="near")
# ax2.plot(x, results[1][2], "-b", label="ex near")
ax2.plot(x, results[1][3], "-m", label="tabu swap")
ax2.plot(x, results[1][4], "-r", label="tabu insert")
ax2.plot(x, results[1][5], "-g", label="tabu invert")
ax2.set(xlabel="Wielko???? problemu", ylabel="Czas dzia??ania w sekundach")
ax2.legend(loc="upper left")
ax2.grid()

plt.show()