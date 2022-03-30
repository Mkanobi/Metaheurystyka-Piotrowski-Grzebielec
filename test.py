import tsplib95
import time
from algorithms import extended_nearest_neighbour, k_random, nearest_neighbour, two_opt
from problem_render import problem_render_euclidean
import statistics as stat


def tester(x, k=100):
    results = [[0.0 for _ in range(len(x))] for _ in range(4)]
    tmp = [[0.0 for _ in range(k)] for _ in range(4)]

    for i in range(len(x)):
        for j in range(k):
            problem1 = tsplib95.parse(problem_render_euclidean('problem testowy',x[i],0,500))
            
            start = time.time()
            k_random(problem1,100)
            end = time.time()
            tmp[0][j] = end - start

            start = time.time()
            nearest_neighbour(problem1,1)
            end = time.time()
            tmp[1][j] = end - start


            start = time.time()
            extended_nearest_neighbour(problem1)
            end = time.time()
            tmp[2][j] = end - start

            start = time.time()
            two_opt(problem1)
            end = time.time()
            tmp[3][j] = end - start

        
        for l in range(4):
            results[l][i] = stat.mean(tmp[l])
        
    return results