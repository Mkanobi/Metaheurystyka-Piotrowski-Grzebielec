import tsplib95
import time
import argparse
import math

from algorithms2 import extended_nearest_neighbour, k_random, nearest_neighbour, two_opt
from problem_render import problem_render_asymmetrical, problem_render_euclidean, problem_render_symmetrical
from tabu_simple import tabu_search
parser = argparse.ArgumentParser()

parser.add_argument('--type', type=str,
                    help='Typ problemu do wygenerowania (EUC_2D, ATSP_EXPLICIT, TSP_EXPLICIT)')
parser.add_argument('--dim', type=int,
                    help='Dimension problemu do wygenerowania')
parser.add_argument('--min', type=int,
                    help='Min value odległości/pozycji problemu do wygenerowania')
parser.add_argument('--max', type=int,
                    help='Max value odległości/pozycji problemu do wygenerowania')
parser.add_argument('--input', type=str,
                    help='Nazwa pliku do użycia jako input')
parser.add_argument('--output', type=str,
                    help='Nazwa pliku do użycia jako output wygenerowanego problemu')


type = "EUC_2D"
dim = 100
minimum = 0
maximum = 500
args = parser.parse_args()
if (args.type is not None):
    if (args.type != "EUC_2D" and args.type != "ATSP_EXPLICIT" and args.type != "TSP_EXPLICIT"):
        parser.error("Nieznany typ problemu do wygenerowania! (podaj EUC_2D, ATSP_EXPLICIT, TSP_EXPLICIT)")
    type = args.type
if (args.dim is not None):
    dim = args.dim
if (args.min is not None):
    minimum = args.min
if (args.max is not None):
    maximum = args.max

if (args.input is None):
    if (type == "EUC_2D"):
        problem = tsplib95.parse(problem_render_euclidean('problem testowy',dim,minimum,maximum))
    if (type == "TSP_EXPLICIT"):
        problem = tsplib95.parse(problem_render_symmetrical('problem testowy',dim,minimum,maximum))
    if (type == "ATSP_EXPLICIT"):
        problem = tsplib95.parse(problem_render_asymmetrical('problem testowy',dim,minimum,maximum))
else:
    problem = tsplib95.load(args.input)
    type = problem.type + "_" + problem.edge_weight_type
    dim = problem.dimension

if (args.output is not None):
    f = open(args.output, "a")
    f.write(problem.render())
    f.close()

print('Typ problemu: ' + type + ', ' + 'Rozmiar: ' + str(dim) + '\n')

result = [math.inf for _ in range(5)]
exec_time = [0.0 for _ in range(5)]

start = time.time()
tmp = k_random(problem,1000)
result[0] = tmp[1]
end = time.time()
exec_time[0] = end - start
print("Obliczono k-random...")

start = time.time()
tmp1 = nearest_neighbour(problem,1)
result[1] = tmp1[1]
end = time.time()
exec_time[1] = end - start
print("Obliczono nn...")

start = time.time()
result[2] = extended_nearest_neighbour(problem)[1]
end = time.time()
exec_time[2] = end - start
print("Obliczono enn...")

start = time.time()
result[3] = two_opt(problem)[1]
end = time.time()
exec_time[3] = end - start
print("Obliczono two_opt...")

start = time.time()
result[4] = tabu_search(problem,tmp1[0],'swap',7,3,200,20)[1]
end = time.time()
exec_time[4] = end - start
print("Obliczono tabu_search...\n")
   
best = min(result)


print('Rozwiazanie 1000-Random: ' + str(result[0]))
print('PRD 1000-Random: ' + "{:.2%}".format( (result[0]-best)/best) )
print('Czas 1000-Random: ' + str(exec_time[0]) + ' s\n')

print('Rozwiazanie Nearest Nieghbour: ' + str(result[1]))
print('PRD Nearest Nieghbour: ' + "{:.2%}".format( (result[1]-best)/best))
print('Czas Nearest Nieghbour: ' + str(exec_time[1]) + ' s\n')

print('Rozwiazanie Extended Nearest Nieghbour: ' + str(result[2]))
print('PRD Extended Nearest Nieghbour: ' + "{:.2%}".format( (result[2]-best)/best))
print('Czas Extended Nearest Nieghbour: ' + str(exec_time[2]) + ' s\n')

print('Rozwiazanie 2-OPT: ' + str(result[3]))
print('PRD Extended 2-OPT: ' + "{:.2%}".format( (result[3]-best)/best))
print('Czas Extended 2-OPT: ' + str(exec_time[3]) + ' s\n')

print('Rozwiazanie tabu: ' + str(result[4]))
print('PRD Extended tabu: ' + "{:.2%}".format( (result[4]-best)/best))
print('Czas Extended tabu: ' + str(exec_time[4]) + ' s\n')
