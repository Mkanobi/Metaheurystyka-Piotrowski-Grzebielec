from neighborlib import invert, swap, insert
from goal_function import goal_function as goal
import copy
import math

# problem: problem do rozwiązania
# solution: rozwiązanie startowe w formacie listy
# N: typ sąsiędztwa
# length: długość pamięci tabu
# k: liczba iteracji
def tabu_search(problem, solution, neighbor_type='invert', length, k):
    if neighbor_type == 'invert':
        nfunc = invert
    elif neighbor_type == 'swap':
        nfunc = swap
    else:
        nfunc = insert
    
    tabu = [[] for _ in range(length)]
    ptr = 0
    result = solution
    result_goal = goal(problem, solution)
    
    for _ in range(k):
        N = []
        for i in range(len(solution)):
            for j in range(i+1, len(solution)):
                tmp = solution.copy()
                nfunc(tmp, i, j)
                N.append(tmp)
                
        best = math.inf
        for contender in N:
            if contender not in tabu:
                tmp = goal(problem, contender)
                if tmp < best:
                    best = tmp
                    solution = contender
               
        if best < result_goal:
            result = solution
            result_goal = best
        tabu[ptr] = solution
        ptr = (ptr + 1) % length
    
    return result, result_goal