import sys
input = sys.stdin.readline

INF = int(1e9)
N = int(input())
graph = [list(map(int,input().split())) for i in range(N)]

# 점화식
for k in range(N):
    for a in range(N):
        for b in range(N):
            if graph[a][k] and graph[k][b]:
                graph[a][b] = 1

# 정답 출력
for i in graph:
    print(*i)