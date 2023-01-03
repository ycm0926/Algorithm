import sys
from collections import deque
INF = int(1e9)                                                          # 무한을 의미하는 값으로 10억을 설정
N, M = map(int,input().split())
graph = [[INF]*(N+1) for i in range(N+1)]

for a in range(1, N+1):                                                 # 자기 자신에서 자기 자신으로 가는 비용은 0으로 초기화
    for b in range(1, N+1):
        if a == b:
            graph[a][b] = 0

for _ in range(M):                                                      # A에서 B로 가는 비용은 1로 설정
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

for k in range(1, N+1):                                                 # 점화식에 따라 플로이드 워셜 알고리즘을 수행
    for a in range(1, N+1):
        for b in range(1, N+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

res = min(map(sum,graph))                                               # graph에서 가장 작은 값 초기화

for i in range(N+1):                                                    # graph에서 가장 작은 값 위치 출력
    if res == sum(graph[i]):
        print(i)
        break
