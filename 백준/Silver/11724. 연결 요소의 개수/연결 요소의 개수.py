import sys
from collections import deque

input = sys.stdin.readline
N, M = map(int,input().split())
graph = [[]*(N+1)for i in range(N+1)]   # 그래프 생성
visited = [False] * (N+1)               # 방문 확인

for i in range(M):                      # 양방향 그래프 초기화
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

cnt = 0                                 # 연결 요소 개수 확인 변수
def bfs(n):
    global cnt
    if visited[n] == True:              # 방문을 한 적이 있다면 함수 종료
        return
    visited[n] = True
    q = deque([n])
    cnt += 1
    while q:
        n = q.popleft()
        for i in graph[n]:
            if not visited[i]:
                visited[i] = True
                q.append(i)

for i in range(1,N+1):                  # 모든 노드 확인
    bfs(i)
print(cnt)