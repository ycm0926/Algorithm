import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
res = []
max_target = 0
graph = [list(map(int,input().split())) for i in range(n)]          # 지역 높이 입력

for i in graph:                                                     # 모든 지역 중 가장 높은 지역
    max_target = max(i)

dx = [-1,1,0,0]                                                     # 좌표 이동 구현
dy = [0,0,-1,1]

def bfs(x,y):                       
    q = deque([(x,y)])
    visited[x][y] = True                                            # 방문 체크

    while q:
        x,y = q.popleft()                                           # 좌표 이동

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= n:              # 맵 이탈 방지
                continue    
            if not visited[nx][ny]:                                 # 방문한 적이 없다면 체크
                visited[nx][ny] = True
                if graph[nx][ny] > k:                               # 방문 체크 후, 침수 높이 보다 크다면 반복
                    q.append((nx,ny))

for k in range(max_target):                                         # 0부터 가장 높은 지역까지 탐색
    cnt = 0
    visited = [[False] * n for i in range(n)]                       # 방문 체크
    for i in range(n):
        for j in range(n):
            if not visited[i][j] and graph[i][j] > k:               # 방문한적이 없고, 침수 되지 않는다면 탐색 시작
                bfs(i,j)
                cnt += 1                                            # 인접 지역 카운트
    res.append(cnt)

print(max(res))