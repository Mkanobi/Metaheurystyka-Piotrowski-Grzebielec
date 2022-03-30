import tsplib95
import time

from algorithms import extended_nearest_neighbour, k_random, nearest_neighbour
from problem_render import problem_render_euclidean

problem1 = tsplib95.parse(problem_render_euclidean('problem testowy',100,0,500))

start = time.time()
print('Rozwiazanie 100-Random: ' + str(k_random(problem1,100)))
end = time.time()
print('Czas 100-Random: ' + str(end - start) + ' s')

start = time.time()
print('Rozwiazanie Nearest Neigbour: ' + str(nearest_neighbour(problem1,1)))
end = time.time()
print('Czas Nearest Nieghbour: ' + str(end - start) + 's')

start = time.time()
print('Rozwiazanie Extended Nearest Neigbour: ' + str(extended_nearest_neighbour(problem1)))
end = time.time()
print('Czas Extended Nearest Nieghbour: ' + str(end - start) + 's')