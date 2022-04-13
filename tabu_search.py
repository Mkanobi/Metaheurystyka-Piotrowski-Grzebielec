from neighborlib import invert, swap, insert
from goal_function import goal_function as goal
import math
from progressBar import printProgressBar

# problem: problem do rozwiązania
# solution: rozwiązanie startowe w formacie listy
# N: typ sąsiędztwa
# length: długość pamięci tabu
# k: liczba iteracji
def tabu_search(problem, solution, length, k, neighbor_type='invert'):
    if neighbor_type == 'invert':
        nfunc = invert
    elif neighbor_type == 'swap':
        nfunc = swap
    else:
        nfunc = insert
    
    tabu = [[] for _ in range(length)]
#     alt = [[] for _ in range(length)]
    ptr = 0
    result = solution
    result_goal = goal(problem, solution)
    
    for it in range(k):
        printProgressBar(it+1, k)
        best = math.inf
        contender = list(solution)
        for i in range(len(solution)):
            for j in range(i+1, len(solution)):
                nfunc(contender, i, j)
                if contender not in tabu:
                    tmp = goal(problem, contender)
                    if tmp < best:
                        best = tmp
                        solution = list(contender)
                nfunc(contender, i, j)
               
        if best < result_goal:
            result = solution
            result_goal = best
        tabu[ptr] = solution
        ptr = (ptr + 1) % length
    
    return result, result_goal