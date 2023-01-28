import sys
from collections import deque

input = sys.stdin.readline
n = int(input())
graph = [list(map(int,input().split()))for i in range(n)]       # 입력 맵 생성
visited = [[False]*n for i in range(n)]                         # 방문 테이블 생성

def bfs(x,y):
    q = deque()
    q.append((x,y))
    visited[x][y] = True
    while q:
        x, y = q.popleft()
        nx = x + graph[x][y]
        ny = y + graph[x][y]
        if (nx == n - 1 and y == n - 1) or (x == n - 1 and ny == n - 1):        # 목표 지점 도착 시 출력
            return 'HaruHaru'
        if 0 <= nx < n:                     # 오른쪽 이동 범위 확인
            if not visited[nx][y]:          # 방문하지 않았을 시 q에 추가
                q.append((nx,y))
                visited[nx][y] = True
        if 0 <= ny < n:                     # 아래 이동 범위 확인
            if not visited[x][ny]:          # 방문하지 않았을 시 q에 추가
                q.append((x,ny))
                visited[x][ny] = True
    return 'Hing'                           # 목표지점 도착하지 못할 시 출력
print(bfs(0,0))