N, r, c = map(int, input().split())
n = 2**N

def dfs(r,c,start):
    global n
    if n == 1:                              # 최소 크기인 1x1에 도달한 경우 중단
        print(start)
    else:
        n //= 2
        if r < n and c < n:                 # 1사분면
            dfs(r, c, start)
        elif r < n and c >= n:              # 2사분면
            dfs(r, c-n, start+n**2)
        elif r >= n and c < n:              # 3사분면
            dfs(r-n, c, start+n**2*2)
        else:                               # 4사분면
            dfs(r-n, c-n, start+n**2*3)
dfs(r,c,0)