import sys
input = sys.stdin.readline

N = int(input())
s = [int(input()) for i in range(N)]

if N <= 2:
    print(sum(s))
    exit(0)

dp = [0]*N
dp[0] = s[0]
dp[1] = dp[0]+s[1]
dp[2] = max(s[1]+s[2],s[0]+s[2])

for i in range(3,N):
    dp[i] = max(s[i]+s[i-1]+dp[i-3],s[i]+dp[i-2])
print(dp[-1])
# 1800 2l 커피 헤이즐넛맛 커피 맛있겠당