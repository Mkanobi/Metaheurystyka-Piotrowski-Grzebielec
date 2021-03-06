import tsplib95
from algorithms2 import extended_nearest_neighbour, k_random, nearest_neighbour, two_opt
from problem_render import problem_render_asymmetrical, problem_render_euclidean, problem_render_symmetrical
from tabu_simple import tabu_search as tabu_alt
from tabu_noalt import tabu_search as tabu_noalt
import statistics as stat
import math
import matplotlib.pyplot as plt
import time
import sys
# import numpy

def quality_tester(x, k, alt_length, itr):
    print(x)
    print(alt_length)
    print(itr)
    results = [[0.0 for _ in range(len(x))] for _ in range(6)]
    tmp = [[0.0 for _ in range(k)] for _ in range(6)]
    lst = [[[],0] for _ in range(6)]

    results_time = [[0.0 for _ in range(len(x))] for _ in range(6)]
    tmp_time = [[0.0 for _ in range(k)] for _ in range(6)]

    for i in range(len(x)):
        print(i)
        for j in range(k):
            print(str(i) + ", " + str(j))
            #problem1 = tsplib95.parse(problem_render_euclidean('problem testowy',x[i],0,500))
            problem1 = tsplib95.parse(problem_render_asymmetrical('problem testowy',20,0,500))
            #problem1 = tsplib95.parse(problem_render_symmetrical('problem testowy',x[i],0,500))

            lst[0] = k_random(problem1,100)
            lst[1] = nearest_neighbour(problem1,1)
            lst[2] = extended_nearest_neighbour(problem1)

            start = time.time()
            lst[3] = two_opt(problem1)
            end = time.time()
            tmp_time[3][j] = end - start

            start = time.time()            
            lst[4] = tabu_alt(problem1,lst[0][0],'swap',7,alt_length,itr,x[i])
            end = time.time()
            tmp_time[4][j] = end - start

            start = time.time()            
            lst[5] = tabu_alt(problem1,lst[1][0],'swap',7,alt_length,itr,x[i])
            end = time.time()
            tmp_time[5][j] = end - start
            
            solution = math.inf

            for z in range (6):
                if (solution > lst[z][1]):
                    solution = lst[z][1]
            
            for l in range(6):
                tmp[l][j] = abs(lst[l][1] - solution) / solution

        for l in range(6):
            results_time[l][i] = stat.mean(tmp_time[l])
        
        for l in range(6):
            results[l][i] = stat.mean(tmp[l])
        
    return results[4]

lim = [i for i in range(5, 11)]
problem_count = 20

for itr in range(20, 201, 20):
    plt.figure()
    plt.imshow(
        [quality_tester(lim, 15, length, itr) for length in range(5, 9)],
        extent=[0, 1, 5, 9],
        aspect='auto',
        origin='lower')
    plt.colorbar()
    plt.ylabel('T_max')
    plt.xlabel('itr = {}'.format(itr))
    plt.savefig('quality_{}.png'.format(itr))
    plt.close()



# results = quality_tester(x,problem_count)
# problem_type = "ATSP"
# fig, (ax1, ax2) = plt.subplots(1, 2)
# fig.suptitle('tabu z list?? nawrot??w (rozmiar nawrot??w + ' + str(alt_length) + ', limit nawrot??w ' + str(alt_limit) + ', rozw. startowe - 100-random, ??rednia z 20 pr??b, limit ' + str(iterations) + ' iteracji, wielko???? tabu: 7, s??siedztwo: swap)')
# #ax1.plot(x, results[0], "-o", label="100-random")
# # ax1.plot(x, results[0][1], "-g", label="near")
# # ax1.plot(x, results[0][2], "-b", label="ex near")
# ax1.plot(x, results[0][3], "-m", label="2-opt")
# #ax1.plot(x, results[5], "-r", label="tabu bez listy nawrot??w")
# ax1.plot(x, results[0][4], "-r", label="tabu 100-random")
# ax1.plot(x, results[0][5], "-k", label="tabu nearest-neighbour")
# ax1.set_title("Wykres ??rednich jako??ci rozwi??za?? w zale??no??ci od wielko??ci problemu\n " + problem_type + ", ??rednia z " + str(problem_count) + " pr??b")
# ax1.set(xlabel="Wielko???? problemu",ylabel="??redni b????d")
# ax1.legend(loc="upper left")
# ax1.grid()
# #ax1.show()
# 
# ax2.set_title("??redni czas dzia??ania algorytm??w w zale??no??ci od wielko??ci problemu\n (??rednia z " + str(problem_count) + " generowanych problem??w " + problem_type + " dla ka??dej wielko??ci problemu)")
# 
# #ax2.plot(x, results[0], "-o", label="100-random")
# # ax2.plot(x, results[1][1], "-g", label="near")
# # ax2.plot(x, results[1][2], "-b", label="ex near")
# ax2.plot(x, results[1][3], "-m", label="2-opt")
# ax2.plot(x, results[1][4], "-r", label="tabu 100-random")
# ax2.plot(x, results[1][5], "-k", label="tabu nearest-neighbour")
# ax2.set(xlabel="DIMENISON problemu", ylabel="Czas dzia??ania w sekundach")
# ax2.legend(loc="upper left")
# ax2.grid()
# 
# plt.show()
