import tsplib95
from algorithms import extended_nearest_neighbour, k_random, nearest_neighbour, two_opt
from problem_render import problem_render_euclidean

def quality_tester(problem):
    lst = [0 for _ in range(4)]

    lst[0] = k_random(problem,100)
    lst[1] = nearest_neighbour(problem,1)
    lst[2] = extended_nearest_neighbour(problem)
    lst[3] = two_opt(problem)
        
    solution = min(lst)
        
    tmp[abs(lst[j] - solution) / solution for j in range(4)]
    
    print(f"100-random")