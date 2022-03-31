import tsplib95
from algorithms import extended_nearest_neighbour, k_random, nearest_neighbour, two_opt
from problem_render import problem_render_euclidean
import statistics as stat
# import numpy

def quality_tester(x, k=100):
    results = [[0.0 for _ in range(len(x))] for _ in range(4)]
    tmp = [[0.0 for _ in range(k)] for _ in range(4)]
    lst = [0 for _ in range(4)]

    for i in range(len(x)):
        for j in range(k):
            problem1 = tsplib95.parse(problem_render_euclidean('problem testowy',x[i],0,500))
            
            lst[0] = k_random(problem1,100)
            lst[1] = nearest_neighbour(problem1,1)
            lst[2] = extended_nearest_neighbour(problem1)
            lst[3] = two_opt(problem1)
            
            solution = min(lst)
            
            for l in range(4):
                tmp[l][j] = abs(lst[l] - solution) / solution
        
        for l in range(4):
            results[l][i] = stat.mean(tmp[l])
        
    return results