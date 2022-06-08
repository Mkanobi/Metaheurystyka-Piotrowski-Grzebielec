"""
Ta funkcja teoretycznie działa
Wykorzystane procesy
Część paralelizacji została poświęcona
Brak profitu
"""



from goal_function import goal_function as goal
from random import choices, randrange, shuffle
from threading import Thread
from multiprocessing import Pool
import math

# from StackOverflow
def split(a, n):
    k, m = divmod(len(a), n)
    return (a[i*k+min(i, m):(i+1)*k+min(i+1, m)] for i in range(n))
#
# def ant_walk_mult(weights: list, pheromones: list, starting_city: list, alpha: int, beta: int, added: list, result: list) -> None:
#     for str_ct in starting_city:
#         ant_walk(weights, pheromones, str_ct, alpha, beta, added, result)

def ant_walk(arguments) -> None:
    """
    weights: 2D list of edge weights
    pheromones: 2D list of pheromones deposit
    starting_city: The city from which the ant begins it's walk
    alpha: Influence control over pheromones
    beta: Influence control over distance
    Q: The ants pheromone stack
    added, result: Return lists for threads operations
    """
    # print('xd')
    weights = arguments[0]
    pheromones = arguments[1]
    starting_city = arguments[2]
    alpha = arguments[3]
    beta = arguments[4]
    dim = len(weights)
    path = [starting_city]
    path_len = 0

    # The main part of the ant walk, creating the path
    for itr in range(dim-1):
        city = path[-1]
        ppb = [
            (pow(pheromones[city][k], alpha) * \
            pow(1 / weights[city][k], beta) if weights[city][k] != 0 else -1) if k not in path else 0.0 for k in range(dim)]
        if -1 not in ppb:
            tmp = sum(ppb)
            ppb = [x / tmp for x in ppb]
        else:
            ppb = [1 if x == -1 else 0 for x in ppb]
        choice = choices(range(dim), ppb)[0]
        path_len += weights[city][choice]
        path.append(choice)
    path_len += weights[path[-1]][starting_city]

    # Pheromones update
    # delta = 100 / path_len
    # for idx in range(dim):
    #     added[path[idx]][path[(idx+1) % dim]].append(delta)

    return [path, path_len]

def ant_colony(problem, iterations: int, colony_size: int, t_cnt: int, alpha: int, beta: int, rho: int) -> list:
    result = [[], math.inf]
    cities = list(problem.get_nodes())
    dim = len(cities)
    colony_size = min(colony_size, dim)
    weights = [[problem.get_weight(i, j) for j in cities] for i in cities]
    pheromones = [[100.0 for _ in range(dim)] for _ in range(dim)]

    for itr in range(iterations):
        threads = []
        tmp = list(range(dim))
        shuffle(tmp)
        tmp = tmp[:colony_size]
        arguments = [[weights, pheromones, i, alpha, beta] for i in tmp]
        # starting_points = list(split(tmp, t_cnt))
        # for starting_city in starting_points:
        #     threads.append(Process(
        #         target=ant_walk_mult,
        #         args=(weights, pheromones, starting_city, alpha, beta, added, paths)))
        # for t in threads: t.start()
        # for t in threads: t.join()
        with Pool(processes=t_cnt) as pool:
            paths = pool.map(ant_walk, arguments)

        for path in paths:
            delta = 100 / path[1]
            for idx in range(dim):
                pheromones[path[0][idx]][path[0][(idx+1) % dim]] += delta

        for i in range(dim):
            for j in range(dim):
                pheromones[i][j] *= 1-rho

        for path in paths:
            if path[1] < result[1]: result = path[:]

    return result
