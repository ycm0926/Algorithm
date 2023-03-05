import sys
sys.setrecursionlimit(100000)

input = sys.stdin.readline
M, N, K = map(int,input().split())
graph = [[0] * N for i in range(M)]
res = 0
res2 = []

def dfs(x,y):
    global tmp

    # 사각형 범위 넘어가면 리턴
    if x <= -1 or x >= M or y <= -1 or y >= N: 
        return

    # graph 값이 0이라면 1로 초기화 하고 재귀
    if graph[x][y] == 0:
        graph[x][y] = 1
        tmp += 1

        dfs(x+1,y)
        dfs(x-1,y)
        dfs(x,y-1)
        dfs(x,y+1)


for i in range(K):
    a, b, c, d = map(int,input().split())
    for i in range(b, d):
        for j in range(a, c):
            graph[i][j] = 1

for i in range(M):
    for j in range(N):
        if graph[i][j] == 0:
            tmp = 0
            dfs(i,j)
            res += 1
            res2.append(tmp)
            tmp = 0

print(res)
print(*sorted(res2))


# [[0, 0, 0, 0, 1, 1, 0],
#  [0, 1, 0, 0, 1, 1, 0], 
#  [1, 1, 1, 1, 0, 0, 0],
#  [1, 1, 1, 1, 0, 0, 0],
#  [0, 1, 0, 0, 0, 0, 0]]