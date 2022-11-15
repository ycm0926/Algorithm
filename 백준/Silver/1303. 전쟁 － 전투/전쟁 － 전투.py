import copy

m, n = map(int,input().split())
graph_w = [list(input()) for _ in range(n)]
graph_b = copy.deepcopy(graph_w)
cnt_w = cnt_b = 0
sm_w = sm_b = 0

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

def dfs_w(x,y):
    global cnt_w, cnt_b

    if x < 0 or x >= n or y < 0 or y >= m:
        return

    if graph_w[x][y] == 'W':
        graph_w[x][y] = 0
        cnt_w += 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            dfs_w(nx,ny)

def dfs_b(x,y):
    global cnt_w, cnt_b

    if x < 0 or x >= n or y < 0 or y >= m:
        return
    elif graph_w[x][y] == 'B':
        graph_w[x][y] = 1
        cnt_b += 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            dfs_b(nx,ny)

for i in range(n):
    for j in range(m):
        if graph_w[i][j] == 'W':
            dfs_w(i,j)
            sm_w += cnt_w ** 2
            cnt_w = 0
        elif graph_b[i][j] == 'B':
            dfs_b(i,j)
            sm_b += cnt_b ** 2
            cnt_b = 0
print(sm_w,sm_b)