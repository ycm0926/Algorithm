def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

def solution(n, computers):
    parent = [i for i in range(n)]
    
    for i in range(n):
        for j in range(i+1, n):
            if computers[i][j] == 1:
                union_parent(parent, i, j)
    
    networks = set()
    for i in range(n):
        networks.add(find_parent(parent, i))
    
    return len(networks)
