import sys
import math
from collections import deque
input = sys.stdin.readline

N, L, R = map(int,input().split())
graph = []

for i in range(N):
    graph.append(list(map(int,input().split())))

dx = [0,1,-1,0]
dy = [1,0,0,-1]

def bfs(i,j):
    global peoples

    visited[i][j] = True
    peoples = graph[i][j]
    union = [[i,j]]
    q = deque([(i,j)])

    while q:
        x,y = q.popleft()
        
        for i in range(4):
            nx = dx[i]+x
            ny = dy[i]+y

            # 그래프 범위 안이고 방문하지 않았다면
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                # 차이가 L이상 R이하라면
                if L <= abs(graph[x][y] - graph[nx][ny]) <= R:
                    peoples += graph[nx][ny]                        # 총 인원수 증가
                    visited[nx][ny] = True                          # 방문처리
                    union.append([nx,ny])                           # 해당 국가 좌표 추가
                    q.append([nx,ny])                               # q 추가 반복

    # 연합 국가 인원 수 변경
    for x,y in union:                                               
        graph[x][y] = math.floor(peoples/len(union))

    return len(union)

ans = 0                                 

while 1:
    ans += 1                                # 일수 증가
    check = False                           # 인구이동 했는지 체크
    visited = [[False]*N for i in range(N)] # 방문 체크
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                if bfs(i,j) > 1:            # 연합 국가 수가 2개 이상이라면 인구이동 했다고 체크
                    check = True
    if not check:                           # 이동하지 않았다면 그만.
        break
            
print(ans-1)                                # 마지막 이동하지 않은 날 빼주기