import tsplib95
import time

from algorithms import extended_nearest_neighbour, k_random, nearest_neighbour, two_opt
from problem_render import problem_render_euclidean
from tabu_search import tabu_search
from nn_pathfinder import pathfinder_core
from goal_function import goal_function
problem1 = tsplib95.parse(problem_render_euclidean('problem testowy',100,0,100))


x = pathfinder_core(problem1,1)
print('NN: ' + str(goal_function(problem1,x)))
y,z = tabu_search(problem1,pathfinder_core(problem1,1),'swap',5,10)
start = time.time()
print('Rozwiazanie tabu: ' + str(z))
end = time.time()
print('Czas tabu: ' + str(end - start) + ' s')