from neighborlib import invert, swap, insert, reverse_insert
from goal_function import path_len as goal_better
import math
import time

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
    
    cnt = 0
    exec_time = 0
    dim = problem.dimension
    tabu = [[-1, -1] for _ in range(length)]
    t_arr = [[0 for _ in range(dim)] for _ in range(dim)]
    alt = [[] for _ in range(length)]
    ptr = [0, 0]
    result = solution
    v = goal(problem, solution)
    result_goal = v
    
    for _ in range(k):
        flag = False
        best = math.inf
        for i in range(len(solution)):
            for j in range(i+1, len(solution)):
                guard = True
                if t_arr[i][j] == 0:
                    start = time.time()
                    cnt += 1
                    v = goal_better(problem, solution, v, i, j, neighbor_type)
                    end = time.time()
                    exec_time += (end - start)
                    nfunc(solution, i, j)
                    if v < best:
                        best = v
                        if flag:
                            guard = False
                            nfunc2(solution, i, j)
                            nfunc(solution, ti, tj)
                            alt[ptr[1]] = solution
                            nfunc2(solution, ti, tj)
                            ptr[1] = (ptr[1] + 1) % length
                        ti, tj = i, j
                        flag = True
                if guard: nfunc2(solution, i, j)
                
        if best == math.inf:
            solution = alt[ptr[1]]
        else:
            nfunc(solution, ti, tj)
            t_arr[tabu[ptr[0]][0]][tabu[ptr[0]][1]] = 0
            t_arr[ti][tj] = 1
            tabu[ptr[0]] = [ti, tj]
            ptr[0] = (ptr[0] + 1) % length
        if best < result_goal:
            result = solution[:]
            result_goal = best
    
    print(exec_time)
    print(cnt)
    return result, result_goal

