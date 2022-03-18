import random
import tsplib95


def problem_render_euclidean(name, dim, rf, rb):
    prob = f'NAME: {name}\nTYPE: TSP\nDIMENSION: {dim}\nEDGE_WEIGHT_TYPE: EUC_2D\nNODE_COORD_SECTION:\n'
    for i in range(1, dim + 1):
        prob += f'{i} {random.randint(rf, rb)} {random.randint(rf, rb)}\n'
    return prob


def problem_render_symmetrical(name, dim, rf, rb):
    prob = f'NAME: {name}\nTYPE: TSP\nDIMENSION: {dim}\nEDGE_WEIGHT_TYPE: EXPLICIT\nEDGE_WEIGHT_FORMAT: UPPER_ROW\nDISPLAY_DATA_TYPE: NO_DISPLAY\nEDGE_WEIGHT_SECTION\n'
    for i in range(dim - 1, 0, -1):
        for j in range(0, i):
            prob += f'{random.randint(rf, rb)} '
        prob += '\n'
    return prob


def problem_render_asymmetrical(name, dim, rf, rb):
    prob = f'NAME: {name}\nTYPE: ATSP\nDIMENSION: {dim}\nEDGE_WEIGHT_TYPE: EXPLICIT\nEDGE_WEIGHT_FORMAT: FULL_MATRIX\nDISPLAY_DATA_TYPE: NO_DISPLAY\nEDGE_WEIGHT_SECTION\n'
    for i in range(0, dim):
        for j in range(0, dim):
            if i == j:
                prob += '9999'
            else:
                prob += f'{random.randint(rf, rb)}'
            prob += ' '
        prob += '\n'
    return prob
