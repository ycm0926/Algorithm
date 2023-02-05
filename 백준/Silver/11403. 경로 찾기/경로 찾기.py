import sys
input = sys.stdin.readline

INF = int(1e9)
N = int(input())
graph = [list(map(int,input().split())) for i in range(N)]

# 자기자신 초기화
for i in range(N):
    for j in range(N):
        if graph[i][j] == 0:
            graph[i][j] = INF

# 점화식
for k in range(N):
    for a in range(N):
        for b in range(N):
            graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])

# 정답 그래프 생성
for i in range(N):
    for j in range(N):
        if graph[i][j] == INF:
            graph[i][j] = 0
        else:
            graph[i][j] = 1

# 정답 그래프 출력
for i in graph:
    for j in i:
        print(j, end=' ')
    print()