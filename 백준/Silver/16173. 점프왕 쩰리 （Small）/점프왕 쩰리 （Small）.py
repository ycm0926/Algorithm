import sys
from collections import deque

input = sys.stdin.readline
n = int(input())
graph = [list(map(int,input().split()))for i in range(n)]
visited = [[False]*n for i in range(n)]

def bfs(x,y):
    q = deque()
    q.append((x,y))
    visited[x][y] = True
    while q:
        x, y = q.popleft()
        nx = x + graph[x][y]
        ny = y + graph[x][y]
        if (nx == n - 1 and y == n - 1) or (x == n - 1 and ny == n - 1):
            return 'HaruHaru'
        if 0 <= nx < n and 0 <= y < n:
            if not visited[nx][y]:
                q.append((nx,y))
                visited[nx][y] = True
        if 0 <= x < n and 0 <= ny < n:
            if not visited[x][ny]:
                q.append((x,ny))
                visited[x][ny] = True
    return 'Hing'
print(bfs(0,0))