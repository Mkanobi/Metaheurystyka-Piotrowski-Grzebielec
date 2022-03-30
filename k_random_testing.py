import tsplib95
import time
from algorithms import k_random
from problem_render import problem_render_euclidean
import statistics as stat
import numpy

def tester_k_random(k, x):
    results = [0 for _ in range(len(x))]
    tmp = [[0 for _ in range(k)] for _ in range(len(x))]

    for m in range(len(x)):
        for j in range(k):
            problem1 = tsplib95.parse(problem_render_euclidean('problem testowy',100,0,500))
            tmp[m][j] = k_random(problem1,x[m])
            
        for l in range(len(x)):
            results[l] = stat.mean(tmp[l])
    return results