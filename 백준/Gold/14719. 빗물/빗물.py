import sys
from collections import deque
input = sys.stdin.readline

H, W = map(int, input().split())
graph = [[0] * W for i in range(H)]
H_li = list(map(int, input().split()))
total = 0

dx = [-1,0,1,0]
dy = [0,1,0,-1]

for i in range(H):
    for j in range(W):
        if H_li[j] != 0:
            graph[i][j] = 1
            H_li[j] -= 1


def bfs(x,y):
    cnt = 1
    graph[x][y] = -1
    q = deque([(x,y)])

    while q:
        x, y = q.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= H or ny < 0 or ny >= W:
                continue

            elif graph[nx][ny] == 0 and graph[nx][:ny].count(1) and graph[nx][ny:].count(1):
                graph[nx][ny] = -1
                cnt += 1
                q.append((nx,ny))
    return cnt

for i in range(H):
    for j in range(W):
        if graph[i][j] == 0 and graph[i][:j].count(1) and graph[i][j:].count(1):
            total += bfs(i,j)
print(total)