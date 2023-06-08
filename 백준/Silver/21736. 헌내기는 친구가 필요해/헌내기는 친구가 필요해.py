import sys
sys.setrecursionlimit(10**9)

def dfs(x,y):
    global ans

    if x < 0 or x >= N or y < 0 or y >= M:
        return

    if not v[x][y] and campus[x][y] != 'X':
        v[x][y] = True

        if campus[x][y] == 'P':
            ans += 1

        dfs(x-1,y)
        dfs(x,y-1)
        dfs(x+1,y)
        dfs(x,y+1)


N, M = map(int, input().split())
campus = [input() for i in range(N)]
v = [[False]*M for i in range(N)]
X, Y = 0, 0
ans = 0

for i in range(N):
    for j in range(M):
        if campus[i][j] == 'I':
            X, Y = i, j
            break
    if X and Y != 0:
        break

dfs(X, Y)
print('TT' if ans == 0 else ans)