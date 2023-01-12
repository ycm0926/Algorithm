import sys
input = sys.stdin.readline

N = int(input())
w = [int(input()) for i in range(N)]

if N <= 2:
    print(sum(w))
else:
    dp = [0] * (N+4)
    dp[0] = w[0]
    dp[1] = w[0]+w[1]

    for i in range(2,N):
        dp[i] = max(w[i]+dp[i-2],w[i]+w[i-1]+dp[i-3],w[i]+w[i-1]+dp[i-4])
    print(max(dp))