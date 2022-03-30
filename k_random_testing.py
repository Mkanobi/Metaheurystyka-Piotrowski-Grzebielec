from algorithms import k_random
import statistics as stat
import sys

def tester_k_random(number_of_tries_for_each_k, ktab, problem):
    results = [0 for _ in range(len(ktab))]
    tmp = [[0 for _ in range(number_of_tries_for_each_k)] for _ in range(len(ktab))]

    for m in range(len(ktab)):
        print(ktab[m], end=" ")
        sys.stdout.flush()
        for j in range(number_of_tries_for_each_k):
            tmp[m][j] = k_random(problem,ktab[m])

        for l in range(len(ktab)):
            results[l] = stat.mean(tmp[l])
    return results