import sys
input = sys.stdin.readline

INF = int(1e9)
N, M = map(int,input().split())
graph = [[INF]*(N+1) for i in range(N+1)]
res = []

# 자기자신 0 초기화
for a in range(1,N+1):
    for b in range(1, N+1):
        if a==b:
            graph[a][b] = 0

# 간선 초기화
for _ in range(M):
    a, b = map(int,input().split())
    graph[a][b] = 1
    graph[b][a] = 1

# 점화식
for k in range(1,N+1):
    for a in range(1,N+1):
        for b in range(1,N+1):
            graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])

# 케빈 베이컨의 수가 가장 작은 사람 출력
for i in range(1,N+1):
    cnt = 0
    for j in range(1,N+1):
        if graph[i][j] != INF and graph[i][j] != 0:
            cnt += graph[i][j]
    res.append(cnt)

print(res.index(min(res))+1)