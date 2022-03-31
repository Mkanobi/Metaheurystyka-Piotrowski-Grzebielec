import tsplib95
from algorithms import extended_nearest_neighbour, k_random, nearest_neighbour, two_opt
from problem_render import problem_render_euclidean, problem_render_symmetrical, problem_render_asymmetrical
import statistics as stat
import time
# import numpy

# Print iterations progress
def printProgressBar (iteration, total, prefix = 'Progress:', suffix = 'Complete', decimals = 1, length = 50, fill = '█', printEnd = "\r"):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
        printEnd    - Optional  : end character (e.g. "\r", "\r\n") (Str)
    """
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print(f'\r{prefix} |{bar}| {percent}% {suffix}', end = printEnd)
    # Print New Line on Complete
    if iteration == total: 
        print()

def quality_tester(k=100):
    tmp = [[0 for _ in range(k)] for _ in range(4)]

    printProgressBar(0, k)
    for j in range(k):
        problem1 = tsplib95.parse(problem_render_asymmetrical('problem testowy',50,0,1000000000000000000))
        
        tmp[0][j] = k_random(problem1,100)
        tmp[1][j] = nearest_neighbour(problem1,1)
        tmp[2][j] = extended_nearest_neighbour(problem1)
        tmp[3][j] = two_opt(problem1)
        
        printProgressBar(j + 1, k)
        
    return tmp
