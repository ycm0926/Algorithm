from collections import deque

n = int(input())
g = [list(map(int,input())) for _ in range(n)]

cnt = 0
num = []

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

# def bfs(x, y):
#     global cnt
#     q = deque()
#     q.append((x, y))
#     g[x][y] = 0
#     cnt += 1
#
#     while q:
#         x, y = q.popleft()
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
#             if nx < 0 or nx >= n or ny < 0 or ny >= n:
#                 continue
#             if g[nx][ny] == 1:
#                 g[nx][ny] = 0
#                 q.append((nx,ny))
#                 cnt += 1
#     return cnt

# for i in range(n):
#     for j in range(n):
#         if g[i][j] == 1:
#             num.append(bfs(i,j))
#             cnt = 0

def dfs(x, y):
    global cnt
    if x < 0 or x >= n or y < 0 or y >= n:
        return False

    if g[x][y] == 1:
        cnt += 1
        g[x][y] = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            dfs(nx, ny)
        return True

for i in range(n):
    for j in range(n):
        if dfs(i,j) == True:
            num.append(cnt)
            cnt = 0

num.sort()
print(len(num))
for i in num:
    print(i)