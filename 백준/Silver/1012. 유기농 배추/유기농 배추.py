import sys
input = sys.stdin.readline
sys.setrecursionlimit(int(1e9))
for _ in range(int(input())):
    M, N, K = map(int, input().split())

    graph = [[0 for _ in range(M)] for _ in range(N)]   # 밭 생성
    for i in range(K):                                  # 밭 배추 위치로 초기화
        a, b = map(int,input().split())
        graph[b][a] = 1

    cnt = 0
    def dfs(x,y):                                       # 1의 값들을 0으로 초기화를 위한 dfs 함수
        if x < 0 or x >= N or y < 0 or y >= M:          # 그래프 범위 벗어날 경우 리턴 (N과 M 위치 유의)
            return
        if graph[x][y] == 1:                            # 그래프값이 1일 경우
            graph[x][y] = 0                             # 0으로 방문 처리
            dfs(x,y+1)
            dfs(x,y-1)
            dfs(x+1,y)
            dfs(x-1,y)

    for i in range(N):
        for j in range(M):
            if graph[i][j] == 1:                        # graph[i][j] == 1일 경우 dfs시작
                dfs(i,j)
                cnt +=1
    print(cnt)