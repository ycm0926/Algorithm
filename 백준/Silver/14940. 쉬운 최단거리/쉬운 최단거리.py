import sys
from collections import deque

def dfs(x,y):
    v[x][y] = True
    graph[x][y] = 0
    q = deque([(x,y)])

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and not v[nx][ny] and graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                v[nx][ny] = True
                q.append((nx,ny))

input = sys.stdin.readline
n, m = map(int,input().split())
v = [[False]*m for i in range(n)]
graph = [list(map(int, input().split())) for i in range(n)]
X, Y = -1, -1

for i in range(n):
    for j in range(m):
        if graph[i][j] == 2:
            X, Y = i, j
            break
    if X != -1:
        break

dx = [0,1,0,-1]
dy = [1,0,-1,0]

dfs(X,Y)

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1 and not v[i][j]:
            graph[i][j] = -1

for i in range(n):
    for j in range(m):
        print(graph[i][j], end =' ')
    print()