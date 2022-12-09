n = int(input())

dp = [0] * 1001     # dp 테이블 설정
dp[1] = 1
dp[2] = 3
for i in range(3,1001):
    dp[i] = dp[i-1] + dp[i-2]*2     # 점화식

print(dp[n]%10007)