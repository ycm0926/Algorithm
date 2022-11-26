N = int(input())
M = int(input())
graph = [[] for i in range(N+1)]
visited = [False] * (N+1)
cnt = 0

def dfs(v):
    global cnt
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            cnt += 1
            dfs(i)

for _ in range(M):
    a, b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
dfs(1)
print(cnt)