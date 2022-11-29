import sys
from collections import deque

input = sys.stdin.readline
n = int(input())
graph = [list(map(int,input().split()))for i in range(n)]       # 입력 맵 생성
visited = [[False]*n for i in range(n)]     # 방문 테이블 생성
dx = [1,0]
dy = [0,1]
def bfs(x,y):
    q = deque()
    q.append((x,y))
    visited[x][y] = True
    while q:
        x, y = q.popleft()
        for i in range(2):
            nx = x + dx[i] * graph[x][y]        # 곱셈으로 방향 컨트롤
            ny = y + dy[i] * graph[x][y]
            if nx == n - 1 and ny == n - 1:        # 목표 지점 도착 시 출력
                return 'HaruHaru'
            if 0 <= nx < n and 0 <= ny < n:      # x를 graph값 만큼 이동
                if not visited[nx][ny]:      # 방문하지 않았을 시
                    q.append((nx,ny))        # q에 추가
                    visited[nx][ny] = True       # 방문 처리
    return 'Hing'       # 목표지점 도착하지 못할 시 출력
print(bfs(0,0))

'''
TIL/회고
- 오른쪽이나 아래로 갔을 경우 중복된 지역 발생, 방문 처리 안 할 시 -> 메모리 초과 발생
- 방문 처리를 하여 중복된 경우 패스
- 와..곱셈으로 방향 컨트롤은 다른 코드를 보고 수정했다.
'''