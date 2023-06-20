from collections import deque

N = int(input())
graph = [input() for i in range(N)]
v = [[False]*N for i in range(N)]
ans = [0,0]
dx = [1,-1,0,0]
dy = [0,0,-1,1]

def dfs(x,y):
   q = deque([(x,y)])
   v[x][y] = True

   while q:
      x, y = q.popleft()

      for i in range(4):
         nx = x + dx[i]
         ny = y + dy[i]

         if 0 <= nx < N and 0 <= ny < N and not v[nx][ny]:
            if graph[x][y] == 'R' and graph[nx][ny] == 'G' or graph[x][y] == 'G' and graph[nx][ny] == 'R' or graph[x][y] == graph[nx][ny]:
               v[nx][ny] = True
               q.append((nx,ny))
            elif graph[x][y] == 'B' and graph[nx][ny] == 'B':
               v[nx][ny] = True
               q.append((nx,ny))

def dfs2(x,y):
   q = deque([(x,y)])
   v[x][y] = True

   while q:
      x, y = q.popleft()

      for i in range(4):
         nx = x + dx[i]
         ny = y + dy[i]

         if 0 <= nx < N and 0 <= ny < N and not v[nx][ny]:
            if graph[x][y] == graph[nx][ny]:
               v[nx][ny] = True
               q.append((nx,ny))


for i in range(N):
   for j in range(N):
      if not v[i][j]:
         dfs(i,j)
         ans[1] += 1

v = [[False]*N for i in range(N)]

for i in range(N):
   for j in range(N):
      if not v[i][j]:
         dfs2(i,j)
         ans[0] += 1
print(f'{ans[0]} {ans[1]}')