def dfs(v):
    global ans
    visited[v] = True
    for i in g[v]:
        if not visited[i]:
            dfs(i)

n = int(input())
m = int(input())

g = [[] for i in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    g[a].append(b)
    g[b].append(a)


visited = [False] * (n+1)
dfs(1)
visited[1] = False
print(visited.count(True))
