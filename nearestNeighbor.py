import math
import tsplib95


def target_function_euc_2d(problem, path):
    solution = 0
    for i in range(1, len(path)):
        solution += problem.get_weight(path[i - 1], path[i])
    return solution


def nearestNeighbor(prob, start):
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
    return target_function_euc_2d(prob, path)


problem = tsplib95.load('problems/br17.atsp')
print(nearestNeighbor(problem, 1))
