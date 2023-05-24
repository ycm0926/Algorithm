def dfs(x, y, n):
    global ans

    if n == 1:
        ans += str(graph[x][y])
        return
    tmp = graph[x][y]

    for i in range(x, x+n):
        for j in range(y, y+n):
            if tmp != graph[i][j]:
                n = n//2
                ans += '('
                dfs(x,y,n)
                dfs(x,y+n,n)
                dfs(x+n,y,n)
                dfs(x+n,y+n,n)
                ans += ')'

                return

    ans += str(graph[x][y])

N = int(input())
ans = ""
graph = [list(map(int,input())) for i in range(N)]
dfs(0,0,N)
print(ans)