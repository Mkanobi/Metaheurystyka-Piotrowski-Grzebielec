from neighborlib import invert, swap, insert, reverse_insert
from goal_function import goal_function as goal
import math
from progressBar import printProgressBar

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
#     alt = [[] for _ in range(length)]
    ptr = 0
    result = solution
    result_goal = goal(problem, solution)
    
    for z in range(k):
        #print('tabu iteracja' +str(z))
        N = []
        best = math.inf
        for i in range(len(solution)):
            for j in range(i+1, len(solution)):
                tmp = solution
                nfunc(tmp, i, j)
                if tmp not in tabu:
                    v = goal(problem, tmp)
                    if v < best:
                        best = v
                        solution = tmp
                nfunc2(tmp, i, j)
                
        
            
               
        if best < result_goal:
            result = solution
            result_goal = best
        tabu[ptr] = solution
        ptr = (ptr + 1) % length
    
    return result, result_goal