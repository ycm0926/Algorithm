import sys
input = sys.stdin.readline

tc = int(input())
def dfs(n):
    global cnt
    visited[n] = True
    cnt += 1
    for i in graph[n]:
        if not visited[i]:
            dfs(i)
for i in range(tc):
    n, m = map(int, input().split())
    graph = [[]*(m+1) for i in range(n+1)]
    visited = [False] * (n+1)
    cnt = 0
    for i in range(m):
        a, b = map(int,input().split())
        graph[a].append(b)
        graph[b].append(a)
    dfs(1)
    print(cnt-1)
