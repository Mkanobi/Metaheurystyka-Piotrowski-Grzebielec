import math
# import tsplib95
import numpy
from goal_function import goal_function
import nn_pathfinder as nnpf

def k_random(problem, k):
    rozw = math.inf
    path = []
    arr = list(problem.get_nodes())
    for _ in range(k):
        numpy.random.shuffle(arr)
        if (rozw > goal_function(problem,arr)):
            rozw = goal_function(problem,arr)
            path = arr
    return path, rozw

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
    return path, goal_function(prob,path)

def extended_nearest_neighbour(prob):
    nodes = prob.get_nodes()
    solution = math.inf
    path = []
    for i in nodes:
        path_contender, contender = nearest_neighbour(prob,i)
        if contender < solution:
            path = path_contender
            solution = contender
    return path,solution

def two_opt(prob):
    curr = nnpf.pathfinder(prob)
    goal = goal_function(prob, curr)
    while True:
        candidate = curr
        for i in range(len(curr) - 1):
            for j in range(i + 1, len(curr) - 1):
                contender = curr
                nnpf.invert(contender, i, j)
                if goal_function(prob, contender) < goal:
                    candidate = contender
                    goal = goal_function(prob, candidate)
        if curr != candidate:
            curr = candidate
        else:
            break
    return curr, goal