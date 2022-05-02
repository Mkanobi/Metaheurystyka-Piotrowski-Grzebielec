import tsplib95

def goal_function(problem, path):
    solution = 0
    for i in range(1, len(path)):
        solution += problem.get_weight(path[i - 1], path[i])
    solution += problem.get_weight(path[len(path)-1], path[0])
    return solution
def path_len(problem,i, j):
    return problem.get_weight(i, j)