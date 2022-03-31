import matplotlib.pyplot as plt
from algorithms import extended_nearest_neighbour, nearest_neighbour, two_opt
from k_random_testing import tester_k_random
from problem_render import problem_render_asymmetrical, problem_render_euclidean, problem_render_symmetrical
import tsplib95

x = [i for i in range(1, 501, 1)]
problem_size = 100
number_of_tries  = 10
problem_type = "EUC_2D"

if problem_type == "EUC_2D":
    problem1 = tsplib95.parse(problem_render_euclidean('problem testowy',problem_size,0,500))
elif problem_type == "TSP_EXPLICIT":
    problem1 = tsplib95.parse(problem_render_symmetrical('problem testowy',problem_size,0,500))
elif problem_type == "ATSP_EXPLICIT":
    problem1 = tsplib95.parse(problem_render_asymmetrical('problem testowy',problem_size,0,500))

two_solution = two_opt(problem1)
nearest_solution = nearest_neighbour(problem1,1)
nearest_extended_solution = extended_nearest_neighbour(problem1)
print(nearest_solution)
print(nearest_extended_solution)
print(two_solution)
y_2opt = [two_solution for i in range(len(x))]
y_nearest = [nearest_solution for i in range(len(x))]
y_extended_nearest = [nearest_extended_solution for i in range(len(x))]
results = tester_k_random(number_of_tries,x,problem1)


plt.plot(x, results, "-r", label="k-random")
plt.plot(x, y_nearest, "-g", label = "nearest neighbour")
plt.plot(x, y_extended_nearest, "-m", label = "extended nearest neighbour")
plt.plot(x, y_2opt, "-b", label = "2-opt")
plt.title("Wykres średnich z " + str(number_of_tries) + " rozwiązań k-random dla wygenerowanego problemu " + str(problem_type) + " o DIMENSION " + str(problem_size) + " w zależności od k")
plt.grid()
plt.xlabel("Wielkość k dla k-random")
plt.ylabel("Średnia długość ścieżki znalezionej przez k-random")
plt.legend(loc="upper right")
plt.show()