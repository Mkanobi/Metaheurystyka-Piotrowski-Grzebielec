from neighborlib import invert, swap, insert, reverse_insert
from goal_function import goal_function as goal
import math
# from progressBar import printProgressBar

# problem: problem do rozwiązania
# solution: rozwiązanie startowe w formacie listy
# N: typ sąsiędztwa
# length: długość pamięci tabu
# k: liczba iteracji
def tabu_search(problem, solution, neighbor_type, length, k):
    if neighbor_type == 'invert':
        nfunc = invert
        nfunc2 = invert
    elif neighbor_type == 'swap':
        nfunc = swap
        nfunc2 = swap
    else:
        nfunc = insert
        nfunc2 = reverse_insert
    
    tabu = [[] for _ in range(length)]
    alt = [[] for _ in range(length)]
    ptr = [0, 0]
    result = solution
    result_goal = goal(problem, solution)
    
    
    for _ in range(k):
        tmp_solution = []
#         printProgressBar(z, k, length=130)
        best = math.inf
        for i in range(len(solution)):
            for j in range(i+1, len(solution)):
                tmp = solution
                nfunc(tmp, i, j)
                if tmp not in tabu:
                    v = goal(problem, tmp)
                    if v < best:
                        best = v
                        if tmp_solution != []:
                            alt[ptr[1]] = tmp_solution
                            ptr[1] = (ptr[1] + 1) % length
                        tmp_solution = tmp[:]
                nfunc2(tmp, i, j)
                
        if best < result_goal:
            result = tmp_solution
            result_goal = best
        tabu[ptr[0]] = solution
        ptr[0] = (ptr[0] + 1) % length
        
        if best == math.inf:
            solution = alt[ptr[1]]
    
#     printProgressBar(100, 100, length=130)
    return result, result_goal
