import sys
from collections import deque
input = sys.stdin.readline
N, M, V = map(int,input().split())

graph = [[]*(N+1) for i in range(N+1)]  # 그래프 생성

v = [False] * (N+1)                     # 방문 체크를 위한 리스트

for i in range(M):                      # 그래프에 정점들을 넣어줌
    a,b = map(int,input().split())
    graph[a].append(b)                  # 양방향이므로 양쪽을 넣어준다.
    graph[b].append(a)

for i in range(1, N+1):                 # 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문
    graph[i].sort()
def dfs(n):                             # dfs 탐색
    v[n] = True
    print(n, end=' ')
    for i in graph[n]:
        if not v[i]:
            dfs(i)

dfs(V)
print()
v = [False] * (N + 1)                   # bfs를 위한 새로운 방문 리스트

def bfs(n):                             # bfs 탐색
    q = deque([n])
    v[n] = True
    while q:
        n = q.popleft()
        print(n, end=' ')
        for i in graph[n]:
            if not v[i]:
                v[i] = True
                q.append(i)
bfs(V)