from neighborlib import invert, swap, insert, reverse_insert
from goal_function import goal_function as goal
from goal_function import path_len
import math
from time import time
from copy import copy

def generate_goal_tab(problem, goal_val, solution, neighbor_type):
    tab = [[0 for _ in range(len(solution))] for _ in range(len(solution))]
    
    if neighbor_type == 'swap':
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
def tabu_search(problem, solution, neighbor_type, length, k, limit):
    if neighbor_type == 'invert':
        nfunc = invert
        nfunc2 = invert
    elif neighbor_type == 'swap':
        nfunc = swap
        nfunc2 = swap
    else:
        nfunc = insert
        nfunc2 = reverse_insert
    
    exe = 0.0
    cnt = 0
    cnt3 = 0
    dim = problem.dimension
    tabu = [[-1, -1] for _ in range(length)]
    t_arr = [[0 for _ in range(dim)] for _ in range(dim)]
    alt = [[[], [], []] for _ in range(length)]
    ptr = [0, 0]
    ti, tj = 0, 0
    result = solution
    result_goal = goal(problem, solution)
#     print("Startowe rozw tabu: " + str(result_goal))
    
    for _ in range(k):
        best = math.inf
        start = time()
        goal_tab = generate_goal_tab(problem, goal(problem, solution), solution, neighbor_type)
        exe += time() - start
        
        for i in range(len(solution)):
            for j in range(i+1, len(solution)):
                nfunc(solution, i, j)
                if t_arr[i][j] == 0 or goal_tab[i][j] < result_goal:
                    #if t_arr[i][j] == 1 and goal_tab[i][j] < result_goal:
                    #    print("gool")
                    v = goal_tab[i][j]
                    if v < best:
                        best = v
                        ti, tj = i, j
                nfunc2(solution, i, j)
        
        #print("i: " + str(ti) + ", j: " + str(tj) + ", t_arr[i][j]: " + str(t_arr[ti][tj]) + ", result: " + str(result_goal))
        #print(alt[(ptr[1]-1)%length][2])
        #print("Indeksy: " + str(ti) + " " + str(tj))
        if alt[(ptr[1]-1)%length] != [[], [], []]:
            alt[(ptr[1]-1)%length][2][ti][tj]=1
            alt[(ptr[1]-1)%length][1][(ptr[0]-1)%length] = [ti,tj]
        if best == math.inf:
            used = ptr[1]
            if alt[ptr[1]] == [[], [], []]: used = 0 
            solution = alt[used][0]
            tabu = alt[used][1]
            t_arr = alt[used][2]
        else:
            nfunc(solution, ti, tj)
            t_arr[tabu[ptr[0]][0]][tabu[ptr[0]][1]] = 0
            t_arr[ti][tj] = 1
            tabu[ptr[0]] = [ti, tj]
            ptr[0] = (ptr[0] + 1) % length
        if best < result_goal:
            cnt = 0
            alt[ptr[1]][0] = copy(result)
            alt[ptr[1]][1] = copy(tabu)
            alt[ptr[1]][2] = copy(t_arr)
            ptr[1] = (ptr[1] + 1) % length
            result = solution[:]
            result_goal = best
        else:
            cnt += 1
            if cnt % limit == limit:
                #print("nawrot")
                cnt3 += 1
                used = ptr[1]
                if alt[ptr[1]] == [[], [], []]: used = 0
                solution = alt[used][0]
                tabu = alt[used][1]
                t_arr = alt[used][2]
            
#     print(exe)
    #print(cnt)
    print("Liczba nawrotow: " + str(cnt3))
    return result, result_goal

