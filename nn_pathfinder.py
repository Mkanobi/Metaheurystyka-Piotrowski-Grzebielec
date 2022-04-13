import math
from goal_function import goal_function as gf

def pathfinder_core(prob, start):
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
    return path

def pathfinder(prob):
    nodes = prob.get_nodes()
    solution = math.inf
    for i in nodes:
        contender = pathfinder_core(prob, i)
        if gf(prob, contender) < solution:
            solution = gf(prob, contender)
            path = contender
    return path

def invert(path, i, j):
    while i < j:
        path[i], path[j] = path[j], path[i]
        i += 1;
        j -= 1;