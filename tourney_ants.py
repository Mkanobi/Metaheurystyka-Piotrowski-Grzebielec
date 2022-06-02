from goal_function import goal_function as goal
from random import sample, randrange, shuffle
from threading import Thread
import math

# from StackOverflow
def split(a, n):
    k, m = divmod(len(a), n)
    return (a[i*k+min(i, m):(i+1)*k+min(i+1, m)] for i in range(n))

def ant_walk_mult(weights: list, pheromones: list, starting_city: list, alpha: int, beta: int, tournament_size: int, added: list, result: list) -> None:
    for str_ct in starting_city:
        ant_walk(weights, pheromones, str_ct, alpha, beta, tournament_size, added, result)

def ant_walk(weights: list, pheromones: list, starting_city: int, alpha: int, beta: int, tournament_size: int, added: list, result: list) -> None:
    """
    weights: 2D list of edge weights
    pheromones: 2D list of pheromones deposit
    starting_city: The city from which the ant begins it's walk
    alpha: Influence control over pheromones
    beta: Influence control over distance
    tournament_size: Size of a single tournament
    Q: The ants pheromone stack
    added, result: Return lists for threads operations
    """
    dim = len(weights)
    path = [starting_city]
    path_len = 0

    # The main part of the ant walk, creating the path
    for itr in range(dim-1):
        city = path[-1]
        available_cities = [city for city in range(dim) if city not in path]
        tournament = sample(available_cities, min(tournament_size, len(available_cities)))
        ppb = [
            (pow(pheromones[city][k], alpha) * pow(1 / weights[city][k], beta) \
            if weights[city][k] != 0 else math.inf) \
            for k in tournament]
        zipped = zip(ppb, tournament)
        choice = max(zipped)[1]
        path_len += weights[city][choice]
        path.append(choice)
    path_len += weights[path[-1]][starting_city]

    # Pheromones update
    delta = 100 / path_len
    for idx in range(dim):
        added[path[idx]][path[(idx+1) % dim]].append(delta)

    result.append([path, path_len])

def ant_colony(problem, iterations: int, colony_size: int, t_cnt: int, alpha: int, beta: int, rho: int, tournament_size: int) -> list:
    result = [[], math.inf]
    cities = list(problem.get_nodes())
    dim = len(cities)
    colony_size = min(colony_size, dim)
    weights = [[problem.get_weight(i, j) for j in cities] for i in cities]
    pheromones = [[100.0 for _ in range(dim)] for _ in range(dim)]

    for itr in range(iterations):
        added = [[[] for _ in range(dim)] for _ in range(dim)]
        threads = []
        paths = []
        tmp = list(range(dim))
        shuffle(tmp)
        tmp = tmp[:colony_size]
        starting_points = list(split(tmp, t_cnt))
        for starting_city in starting_points:
            threads.append(Thread(
                target=ant_walk_mult,
                args=[weights, pheromones, starting_city, alpha, beta, tournament_size, added, paths]))
        for t in threads: t.start()
        for t in threads: t.join()

        for i in range(dim):
            for j in range(dim):
                pheromones[i][j] *= 1-rho
                pheromones[i][j] += sum(added[i][j])

        for path in paths:
            if path[1] < result[1]: result = path[:]

    return result
