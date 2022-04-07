def invert(path, i, j):
    while i < j:
        path[i], path[j] = path[j], path[i]
        i += 1;
        j -= 1;
        
def swap(path, i, j):
    path[i], path[j] = path[j], path[i]
    
def insert(path, i, j):
    tmp = path[i]
    del path[i]
    path.insert(j, tmp)