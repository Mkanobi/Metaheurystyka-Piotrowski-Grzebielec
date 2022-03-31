import tsplib95
from algorithms import extended_nearest_neighbour, k_random, nearest_neighbour, two_opt
from problem_render import problem_render_euclidean
import statistics as stat
# import numpy

def quality_tester(k=100):
    tmp = [[0 for _ in range(k)] for _ in range(4)]

    for j in range(k):
        print(j)
        problem1 = tsplib95.parse(problem_render_euclidean('problem testowy',40,0,1000000000000000000))
        
        tmp[0][j] = k_random(problem1,100)
        tmp[1][j] = nearest_neighbour(problem1,1)
        tmp[2][j] = extended_nearest_neighbour(problem1)
        tmp[3][j] = two_opt(problem1)
        
    return tmp
