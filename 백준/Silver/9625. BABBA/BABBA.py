K = int(input())
dp = [0] * (K+1)
dp[1] = [0, 1]
if K < 2:
    print(*dp[K])
else:
    for i in range(2,K+1):
        dp[i] = [dp[i-1][1],sum(dp[i-1])]

    print(*dp[K])