import math
import tsplib95
import numpy
from goal_function import goal_function

def k_random(problem, k):
    rozw = math.inf
    arr = list(problem.get_nodes())
    for i in range(k):
        numpy.random.shuffle(arr)
        rozw = min(rozw,goal_function(problem,arr))
    return rozw

def nearest_neighbour(prob, start):
    path = [start]
    while len(path) < prob.dimension:
        closest_city = -1
        closest_dist = math.inf
        cities = prob.get_nodes()
        for i in cities:
            if i not in path and prob.get_weight(path[len(path) - 1], i) < closest_dist:
                closest_city = i
                closest_dist = prob.get_weight(path[len(path) - 1], i)
        path.append(closest_city)
    return goal_function(prob, path)

def extended_nearest_neighbour(prob):
    nodes = prob.get_nodes()
    solution = math.inf
    for i in nodes:
        contender = nearest_neighbour(prob,i)
        if contender < solution:
            solution = contender
    return solution