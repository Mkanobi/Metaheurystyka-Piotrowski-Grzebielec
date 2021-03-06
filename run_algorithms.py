import tsplib95
import time
import argparse
import math

from algorithms2 import extended_nearest_neighbour, k_random, nearest_neighbour, two_opt
from problem_render import problem_render_asymmetrical, problem_render_euclidean, problem_render_symmetrical
from tabu_simple import tabu_search
from tabu_timed import tabu_search as tabu_time
from ants import ant_colony
from tourney_ants import ant_colony as tourney
from elite_ants import ant_colony as elite
from elite_ants_timed import ant_colony as timed
from elite_ants_timed_randomized import ant_colony as elite_timed_randomized

if __name__ == '__main__':
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

    result = [math.inf for _ in range(11)]
    exec_time = [0.0 for _ in range(11)]

    # start = time.time()
    # tmp = k_random(problem,1000)
    # result[0] = tmp[1]
    # end = time.time()
    # exec_time[0] = end - start
    # print("Obliczono k-random...")

    start = time.time()
    tmp1 = nearest_neighbour(problem,1)
    result[1] = tmp1[1]
    end = time.time()
    exec_time[1] = end - start
    print("Obliczono nn...")

    # start = time.time()
    # result[2] = extended_nearest_neighbour(problem)[1]
    # end = time.time()
    # exec_time[2] = end - start
    # print("Obliczono enn...")

    start = time.time()
    result[3] = two_opt(problem)[1]
    end = time.time()
    exec_time[3] = end - start
    print("Obliczono two_opt...")

    # start = time.time()
    # result[4] = tabu_search(problem,tmp1[0],'swap',7,3,100,10)[1]
    # end = time.time()
    # exec_time[4] = end - start
    # print("Obliczono tabu_search...")

    exe = tabu_time(problem,tmp1[0],'swap',7,3,5,10)
    result[5] = exe[1]
    exec_time[5] = exe[2]
    print("Obliczono tabu_time...")

    # start = time.time()
    # result[6] = ant_colony(problem, 40, 20, 4, 1, 3, 0.1)[1]
    # end = time.time()
    # exec_time[6] = end - start
    # print('Obliczono ACO...')
    #
    # start = time.time()
    # result[7] = tourney(problem, 40, 20, 4, 1, 3, 0.1, 7)[1]
    # end = time.time()
    # exec_time[7] = end - start
    # print('Obliczono Tourney...')
    #
    # start = time.time()
    # result[8] = elite(problem, 40, 20, 4, 1, 3, 0.1, 0.2)[1]
    # end = time.time()
    # exec_time[8] = end - start
    # print('Obliczono Elite...')
    #
    # exe = timed(problem, 5, 20, 4, 1, 3, 0.1, 0.2)
    # result[9] = exe[1]
    # exec_time[9] = exe[2]
    # print('Obliczono Timed...\n')

    exe = elite_timed_randomized(problem, 5, 20, 4, 1, 3, 0.1, 0, 0)
    result[10] = exe[1]
    exec_time[10] = exe[2]
    print('Obliczono Timed, elite, randomized...\n')

    best = min(result)


    # print('Rozwiazanie 1000-Random: ' + str(result[0]))
    # print('PRD 1000-Random: ' + "{:.2%}".format( (result[0]-best)/best) )
    # print('Czas 1000-Random: ' + str(exec_time[0]) + ' s\n')

    print('Rozwiazanie Nearest Nieghbour: ' + str(result[1]))
    print('PRD Nearest Nieghbour: ' + "{:.2%}".format( (result[1]-best)/best))
    print('Czas Nearest Nieghbour: ' + str(exec_time[1]) + ' s\n')

    # print('Rozwiazanie Extended Nearest Nieghbour: ' + str(result[2]))
    # print('PRD Extended Nearest Nieghbour: ' + "{:.2%}".format( (result[2]-best)/best))
    # print('Czas Extended Nearest Nieghbour: ' + str(exec_time[2]) + ' s\n')

    print('Rozwiazanie 2-OPT: ' + str(result[3]))
    print('PRD 2-OPT: ' + "{:.2%}".format( (result[3]-best)/best))
    print('Czas 2-OPT: ' + str(exec_time[3]) + ' s\n')

    # print('Rozwiazanie tabu: ' + str(result[4]))
    # print('PRD tabu: ' + "{:.2%}".format( (result[4]-best)/best))
    # print('Czas tabu: ' + str(exec_time[4]) + ' s\n')

    print('Rozwiazanie tabu_time: ' + str(result[5]))
    print('PRD tabu_time: ' + "{:.2%}".format( (result[5]-best)/best))
    print('Czas tabu_time: ' + str(exec_time[5]) + ' s\n')

    # print('Rozwiazanie ACO: ' + str(result[6]))
    # print('PRD ACO: ' + "{:.2%}".format( (result[6]-best)/best))
    # print('Czas ACO: ' + str(exec_time[6]) + ' s\n')
    #
    # print('Rozwiazanie Tourney: ' + str(result[7]))
    # print('PRD Tourney: ' + "{:.2%}".format( (result[7]-best)/best))
    # print('Czas Tourney: ' + str(exec_time[7]) + ' s\n')
    #
    # print('Rozwiazanie Elite: ' + str(result[8]))
    # print('PRD Elite: ' + "{:.2%}".format( (result[8]-best)/best))
    # print('Czas Elite: ' + str(exec_time[8]) + ' s\n')
    #
    # print('Rozwiazanie Timed: ' + str(result[9]))
    # print('PRD Timed: ' + "{:.2%}".format( (result[9]-best)/best))
    # print('Czas Timed: ' + str(exec_time[9]) + ' s\n')

    print('Rozwiazanie Elite Timed Randomized: ' + str(result[10]))
    print('PRD Timed: ' + "{:.2%}".format( (result[10]-best)/best))
    print('Czas Timed: ' + str(exec_time[10]) + ' s\n')
