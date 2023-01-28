import sys

input = sys.stdin.readline
def dfs(x,y):

    visited[x][y] = True

    if y+1 < M and graph[x][y] == '-' and graph[x][y+1] == '-':     # `-`이고 다음이 `-`일 경우 재귀
        dfs(x,y+1)
    elif x+1 < N and graph[x][y] == '|' and graph[x+1][y] == '|':   # `|`이고 다음이 `|`일 경우 재귀
        dfs(x+1,y)

N, M = map(int,input().split())
graph = [input() for i in range(N)]
visited = [[False]*M for i in range(N)]
total = 0

for i in range(N):
    for j in range(M):
        if visited[i][j] == False:
            dfs(i,j)
            total += 1
print(total)