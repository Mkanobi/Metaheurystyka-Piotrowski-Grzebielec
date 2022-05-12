from tabu_search import tabu_search
from problem_render import problem_render_euclidean as pre
from nn_pathfinder import pathfinder_core as pf
import tsplib95

problem = tsplib95.load('problems/br17.atsp')
path, result = tabu_search(problem, pf(problem, 1), 1000, 10000, 'swap')
print(result)