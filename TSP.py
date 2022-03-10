import random
import tsplib95


def problemRender(name, dim, rf, rb):
    prob = f'NAME: {name}\nTYPE: TSP\nDIMENSION: {dim}\nEDGE_WEIGHT_TYPE: EUC_2D\nNODE_COORD_SECTION:\n'
    for i in range(1, dim + 1):
        prob += f'{i} {random.randint(rf, rb)} {random.randint(rf, rb)}\n'
    return prob


problem = tsplib95.parse(problemRender('test', 8, 0, 100))
print(problem.render())
