def dfs(n, sm, tlst):
    global ans

    # 가지치기
    if sm+(4-n)*mx <= ans:
        return

    if n==4:
        ans = max(ans, sm)
        return

    for ci, cj in tlst: # 도형의 모든 위치에서 네방향
        for di, dj in ((-1,0),(1,0),(0,-1),(0,1)):
            ni, nj = ci+di, cj+dj

            # 범위내 미방문이면 다음단계로
            if 0 <= ni < N and 0 <= nj < M and v[ni][nj]==0:
                v[ni][nj]=1
                dfs(n+1, sm+graph[ni][nj], tlst+[(ni,nj)])
                v[ni][nj]=0

N, M = map(int,input().split())
graph = [list(map(int,input().split())) for i in range(N)]
v = [[0]*M for _ in range(N)]
ans = 0
mx = max(map(max,graph))


for i in range(N):
    for j in range(M):
        v[i][j] = 1
        dfs(1, graph[i][j], [(i,j)])

print(ans)