import sys
n = int(input())
input = sys.stdin.readline
graph = [list(map(int,input().split())) for i in range(n)]
res = [0,0]
visited = 0
def dfs(x,y,n):
    visited = graph[x][y]               # 비교할 첫 번째 값 초기화


    for i in range(x,x+n):              # 반복문을 통해 종이 확인
        for j in range(y,y+n):
            if graph[i][j] != visited:  # 비교하는 값이 첫 번째 값과 다르다면
                n //= 2                 # n을 절반으로 나눈다.
                dfs(x,y,n)              # 4개로 분할 정복
                dfs(x+n,y,n)
                dfs(x,y+n,n)
                dfs(x+n,y+n,n)
                return
    res[visited] += 1                   # 비교하는 값이 모두 같다면 그 값에 +1
    return

dfs(0,0,n)
for i in res:
    print(i)