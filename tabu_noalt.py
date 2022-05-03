from neighborlib import invert, swap, insert, reverse_insert
from goal_function import goal_function as goal
from goal_function import path_len
import math
import time
def generate_goal_tab(problem,goal_val,solution,neighbor_type):
    tab = [[0 for i in range(len(solution))] for j in range(len(solution))]
    if (neighbor_type == 'swap'):
        for i in range(len(solution)):
            for j in range(i+1, len(solution)):
                tab[i][j] = goal_val
                
                if(j-i == 1):
                    previ = solution[(i-1)%len(solution)]
                    tab[i][j] -= path_len(problem,previ,solution[i])
                    tab[i][j] += path_len(problem,previ,solution[j])

                    nextj = solution[(j+1)%len(solution)]
                    tab[i][j] -= path_len(problem,solution[j],nextj)
                    tab[i][j] += path_len(problem,solution[i],nextj)
                    tab[i][j] += - path_len(problem,solution[i],solution[j]) + path_len(problem,solution[j],solution[i])
                elif (j-i == len(solution)-1):
                    prevj = solution[(j-1)%len(solution)]
                    tab[i][j] -= path_len(problem,prevj,solution[j])
                    tab[i][j] += path_len(problem,prevj,solution[i])

                    nexti = solution[(i+1)%len(solution)]
                    tab[i][j] -= path_len(problem,solution[i],nexti)
                    tab[i][j] += path_len(problem,solution[j],nexti)
                    tab[i][j] -= - path_len(problem,solution[i],solution[j]) + path_len(problem,solution[j],solution[i])
                else:

                    previ = solution[(i-1)%len(solution)]
                    tab[i][j] -= path_len(problem,previ,solution[i])
                    tab[i][j] += path_len(problem,previ,solution[j])

                    nextj = solution[(j+1)%len(solution)]
                    tab[i][j] -= path_len(problem,solution[j],nextj)
                    tab[i][j] += path_len(problem,solution[i],nextj)

                    prevj = solution[(j-1)%len(solution)]
                    tab[i][j] -= path_len(problem,prevj,solution[j])
                    tab[i][j] += path_len(problem,prevj,solution[i])

                    nexti = solution[(i+1)%len(solution)]
                    tab[i][j] -= path_len(problem,solution[i],nexti)
                    tab[i][j] += path_len(problem,solution[j],nexti)

                #swap(solution,i,j)
                #if (tab[i][j] != goal(problem,solution)):
                #    print("Blad! " +str(i) + ", " + str(j) + ", " + str(tab[i][j]) + ", " + str(goal(problem,solution)))
                #swap(solution,i,j)
    if (neighbor_type == 'invert'):
        for i in range(len(solution)):
            tab[i][i] = goal_val
            for j in range(i+1, len(solution)):
                if (i == 0 and j == len(solution)-1):
                    tab[i][j] = tab[i][j-1]
                else: 
                    tab[i][j] = tab[i][j-1] 
                    tab[i][j] += - path_len(problem,solution[(i-1)%len(solution)],solution[(j-1)%len(solution)]) + path_len(problem,solution[(i-1)%len(solution)],solution[j])
                    tab[i][j] += path_len(problem,solution[j],solution[(j-1)%len(solution)]) - path_len(problem,solution[i],solution[j])
                    tab[i][j] += - path_len(problem,solution[j],solution[(j+1)%len(solution)]) + path_len(problem,solution[i],solution[(j+1)%len(solution)])

                #invert(solution,i,j)
                #if (tab[i][j] != goal(problem,solution)):
                #    print("Blad! " +str(i) + ", " + str(j) + ", " + str(tab[i][j]) + ", " + str(goal(problem,solution)))
                #invert(solution,i,j)
    if (neighbor_type == 'insert'):
        for i in range(len(solution)):
            for j in range(i+1, len(solution)):
                tab[i][j] = goal_val
                if (j-i != len(solution)-1):
                    tab[i][j] += path_len(problem,solution[i],solution[(j+1)%len(solution)]) - path_len(problem,solution[j],solution[(j+1)%len(solution)])
                    tab[i][j] += path_len(problem,solution[(i-1)%len(solution)],solution[(i+1)%len(solution)]) - path_len(problem,solution[(i-1)%len(solution)],solution[i])
                    tab[i][j] += path_len(problem,solution[j],solution[i]) - path_len(problem,solution[i],solution[(i+1)%len(solution)])
                    insert(solution,i,j)
                #if (tab[i][j] != goal(problem,solution)):
                #    print("Blad! " +str(i) + ", " + str(j) + ", " + str(tab[i][j]) + ", " + str(goal(problem,solution)))
                #reverse_insert(solution,i,j)
    return tab          

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
    print("Startowe rozw tabu: " + str(result_goal))
    
    for _ in range(k):
        flag = False
        best = math.inf
        goal_tab = generate_goal_tab(problem,goal(problem,solution),solution,neighbor_type)
        for i in range(len(solution)):
            for j in range(i+1, len(solution)):
                guard = True
                nfunc(solution, i, j)
                if t_arr[i][j] == 0 or goal_tab[i][j] > result_goal:
                    start = time.time()
                    cnt += 1
                    #v = goal(problem, solution)
                    v = goal_tab[i][j]
                    end = time.time()
                    exec_time += (end - start)
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
    
    #print(exec_time)
    #print(cnt)
    return result, result_goal
