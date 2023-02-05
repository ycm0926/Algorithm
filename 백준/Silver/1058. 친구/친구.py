import sys
input = sys.stdin.readline
INF = int(1e9)

N = int(input())
graph = [[INF]*(N) for i in range(N)]
res = []
# 자신으로 가는 비용 0으로 초기화
for a in range(N):
    for b in range(N):
        if a==b:
            graph[a][b] = 0

# 간선 정보 입력
for i in range(N):
    a = input()
    for j in range(len(a)):
        if a[j] == 'Y':
            graph[i][j] = 1

# 점화식
for k in range(N):
    for a in range(N):
        for b in range(N):
            graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])

# 결과
for i in range(N):
    cnt = 0
    for j in range(N):
        # 2랑 같거나 작고, 자기 자신이 아니면 카운트
        if graph[i][j] <= 2 and graph[i][j] != 0:
            cnt += 1
    res.append(cnt)
print(max(res))