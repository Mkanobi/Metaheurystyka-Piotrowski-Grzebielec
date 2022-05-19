from goal_function import goal_function as goal
from random import choices, randrange
from threading import Thread
import math

# TODO
# boolean list of visited

def ant_walk(weights: list, pheromones: list, starting_city: int, alpha: int, beta: int, Q: int, added: list, result: list) -> None:
    """
    weights: 2D list of edge weights
    pheromones: 2D list of pheromones deposit
    starting_city: The city from which the ant begins it's walk
    alpha: Influence control over pheromones
    beta: Influence control over distance
    Q: The ants pheromone stack
    added, result: Return lists for threads operations
    """
    dim = len(weights)
    path = [starting_city]
    path_len = 0

    # The main part of the ant walk, creating the path
    for itr in range(dim-1):
        city = path[-1]
        ppb = [pow(pheromones[city][k], alpha) * pow(1 / weights[city][k], beta) if k not in path else 0.0 for k in range(dim)]
        tmp = sum(ppb)
        ppb = [x / tmp for x in ppb]
        choice = choices(range(dim), ppb)[0]
        path_len += weights[city][choice]
        path.append(choice)
    path_len += weights[path[-1]][starting_city]

    # Pheromones update
    delta = Q / path_len
    for idx in range(dim):
        added[idx][(idx+1) % dim].append(delta)

    result.append([path, path_len])


def ant_colony(problem, iterations: int, colony_size: int, alpha: int, beta: int, rho: int, Q: int = 100) -> list:
    result = [[], math.inf]
    cities = list(problem.get_nodes())
    dim = len(cities)
    weights = [[problem.get_weight(i, j) for j in cities] for i in cities]
    pheromones = [[0.0 for _ in range(dim)] for _ in range(dim)]

    for itr in range(iterations):
        added = [[[] for _ in range(dim)] for _ in range(dim)]
        threads = []
        paths = []
        for idx in range(colony_size):
            starting_city = randrange(dim)
            threads.append(Thread(
                target=ant_walk,
                arguments=[weights, pheromones, starting_city, alpha, beta, Q, added, paths]))
        for t in threads: t.run()
        for t in threads: t.join()

        for i in range(dim):
            for j in range(dim):
                pheromones[i][j] *= i-rho
                pheromones[i][j] += sum(added[i][j])

        for path in paths:
            if path[1] < result[1]: result = path

    return result
