for _ in range(int(input())):
    M, N, x, y = map(int, input().split())
    ans = 1
    while(x <= M*N):
        if x%N == y%N:
            print(x)
            ans = 0
            break
        x += M
    if ans:
        print(-1)

# (a-x)%M == 0
# (x+m-x)%M == 0