import tsplib95
from algorithms2 import extended_nearest_neighbour, k_random, nearest_neighbour, two_opt
from problem_render import problem_render_asymmetrical, problem_render_euclidean, problem_render_symmetrical
from tabu_timed import tabu_search as tabu_search
from elite_ants import ant_colony as ant_colony
import statistics as stat
import math
import matplotlib.pyplot as plt
import matplotlib
import time
import sys
# import numpy

#TODO: prd w zależności od rozmiaru kolonii, prd w zależności od współczynnika elityzmu, prd w zależności od ACS-rand, czas dzialania w zależności od liczby procesów
if __name__ == '__main__':
    problem = sys.argv[1]
    dim = tsplib95.load(problem).dimension
    solution = int(sys.argv[2])
    constraint = 5
    colony_size = dim//2
    alpha = 1
    beta = 3
    rho = 0.1


    def quality_by_time_tester(x,solution, k=100,):
        results_prd = [[0.0 for _ in range(len(x))] for _ in range(4)]
        results_val = [[0.0 for _ in range(len(x))] for _ in range(4)]
        lst = [0 for _ in range(4)]
        tmp_prd = [[0.0 for _ in range(k)] for _ in range(4)]
        #tmp_val = [[0.0 for _ in range(k)] for _ in range(4)]


        for i in range(len(x)):
            print(i)
            for j in range(k):
                print(str(x[i]) + ", " + str(j))
                #problem1 = tsplib95.parse(problem_render_euclidean('problem testowy',x[i],0,500))
                #problem1 = tsplib95.parse(problem_render_asymmetrical('problem testowy',x[i],0,500))
                #problem1 = tsplib95.parse(problem_render_symmetrical('problem testowy',x[i],0,500))
                problem1 = tsplib95.load(problem)

                start = time.time()
                #tmp_start = k_random(problem1,10)
                end = time.time()
                if (end-start > x[i]):
                    print("krandom time exceeded!")
                    return
                #lst[0] = tabu_search(problem1,tmp_start[0],'swap',10,5,x[i] - (end-start),10)
                start = time.time()
                ant_colony(problem1, constraint,colony_size, x[i],  alpha, beta, rho, 0)
                end = time.time()
                lst[1] = end-start
                print("czas " + str(end-start))
                #lst[2] = ant_colony(problem1, time_constraint, x[i], thread_count, alpha, beta, rho, 2, 1)

                #lst[3] = ant_colony(problem1, time_constraint, x[i], thread_count, alpha, beta, rho, 2, 0)
                
                for l in range(0,4):
                    tmp_prd[l][j] = lst[l]
    #                print(str(j) + " " + str(tmp_prd[l][j]))
    #                tmp_val[l][j] = lst[l][1]
            
            for l in range(0,4):
                results_prd[l][i] = stat.mean(tmp_prd[l])
                results_val[l][i] = stat.median(tmp_prd[l])
            #print(results_val[1][i])
            #print(results_val[2][i])
            #print(results_val[3][i])
            
        return results_prd, results_val



    x = [i for i in range(1, 11, 1)]

    problem_count = 1
    sarting_k_random =1
    results = quality_by_time_tester(x,solution,problem_count)
    fig, (ax1, ax2) = plt.subplots(1, 2)
    fig.suptitle('Problem ' + problem + ', solution = ' + str(solution) + '\n' + "Liczba iteracji: " + str(constraint) + ", alpha = " + str(alpha) + ", beta = " + str(beta) + ", rho = " + str(rho))
    #ax1.plot(x, results[0][0], "-r", label="tabu_search")
    ax1.plot(x, results[0][1], "-b", label="ant colony")
    #ax1.plot(x, results[0][2], "-g", label="ant colony + ACS ppb")
    #ax1.plot(x, results[0][3], "-m", label="ant colony + Elitism")
    ax1.set_title("Wykres średniego czasu rozwiązań w zależności od liczby wątków\n " + "średnia z " + str(problem_count) + " prób")
    ax1.set(xlabel="liczba wątków",ylabel="czas [s]")
    ax1.legend(loc="upper left")
    ax1.grid()
    #ax1.show()

    ax2.set_title("Wykres mediany czasu rozwiązań w zależności od liczby wątków\n średnia z " + str(problem_count) + " prób ") #+ problem_type + " dla każdej wielkości problemu)")

    #ax2.plot(x, results[1][0], "-r", label="tabu_search")
    ax2.plot(x, results[1][1], "-b", label="ant colony")
    #ax2.plot(x, results[1][2], "-g", label="ant colony + ACS ppb")
    #ax2.plot(x, results[1][3], "-m", label="ant colony + Elitism")
    ax2.set(xlabel="liczba wątków", ylabel="czas [s]")
    ax2.legend(loc="upper left")
    ax2.grid()

    
    #manager = plt.get_current_fig_manager()
    #manager.resize(*manager.window.maxsize())
    figure = plt.gcf()
    figure.set_size_inches(16, 9) # set figure's size manually to your full screen (32x18)
    #print(matplotlib.get_backend())
    #plt.show()
    plt.savefig(sys.argv[3], bbox_inches='tight')

    #plt.show()