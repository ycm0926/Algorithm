n = int(input())
dp = [0] * 10001
for i in range(1,n+1):
    cnt = 0
    for j in range(1, int(i**0.5)+1):
        if i % j == 0:
            cnt += 1
    dp[i] = dp[i-1] + cnt
print(dp[n])