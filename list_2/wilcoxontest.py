import tsplib95
import scipy.stats as sp
import numpy as np
from tabu_simple import tabu_search
from algorithms2 import extended_nearest_neighbour, k_random, nearest_neighbour, two_opt
from problem_render import problem_render_euclidean, problem_render_symmetrical, problem_render_asymmetrical
tabu_size = 7
alt_length = 5
alt_limit = 5
iterations = 50
dimension = 20
def quality_tester(k=100,dim=50):
    tmp = [ [ [[],0] for _ in range(k)] for _ in range(3)]
    for j in range(k):
        print(j)
        #problem1 = tsplib95.parse(problem_render_symmetrical('problem testowy',dimension,0,1000000))
        problem1 = tsplib95.parse(problem_render_euclidean('problem testowy',dimension,0,1000000))
        krand = k_random(problem1,100)
        tmp[0][j] = tabu_search(problem1,krand[0],'insert',tabu_size,alt_length,iterations,alt_limit)[1]
        tmp[1][j] = tabu_search(problem1,krand[0],'swap',tabu_size,alt_length,iterations,alt_limit)[1]
        tmp[2][j] = tabu_search(problem1,krand[0],'invert',tabu_size,alt_length,iterations,alt_limit)[1]
        
    return tmp



alfa = 0.05
lst = np.array(quality_tester(50,dimension))
print('Rodzaj problemu: EUC 2D, Rozmiar problemu: ' + str(dimension))
print('Tabu size: ' + str(tabu_size) +', alt_length: ' + str(alt_length) + ', iteracje: ' + str(iterations) + ', limit nawrotów: ' + str(alt_limit))
print("Hipoteza: średnie PRD algorytmów tabu jest takie samo, Test Wilcoxona, alfa=" + str(alfa) + ":")

res, pval = sp.wilcoxon(lst[0], lst[1])
print("p-value dla tabu-insert / tabu-swap: " + str(pval))
if (pval < 0.05):
    print("Hipoteza odrzucona!")
else:
    print("Hipoteza przyjęta - średnie prd insert, swap są takie same.")

print()

res, pval = sp.wilcoxon(lst[1], lst[2])
print("p-value dla tabu-swap / tabu-invert: " + str(pval))
if (pval < 0.05):
    print("Hipoteza odrzucona!")
else:
    print("Hipoteza przyjęta - średnie prd invert, swap są takie same.")

print()

res, pval = sp.wilcoxon(lst[0], lst[2])
print("p-value dla tabu-insert / tabu-invert: " + str(pval))
if (pval < 0.05):
    print("Hipoteza odrzucona!")
else:
    print("Hipoteza przyjęta - średnie prd insert, invert są takie same.")