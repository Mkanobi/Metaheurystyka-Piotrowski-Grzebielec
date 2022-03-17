import tsplib95
#EUC_2D
problem = tsplib95.load('problems/br17.atsp')

def target_function_euc_2d(problem, path):
    solution=0
    for i in range(1,len(path)):
        solution += problem.get_weight(path[i-1],path[i])
    return solution

print(target_function_euc_2d(problem, [1,2,3]))