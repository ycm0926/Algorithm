# 0 -- 1 0
# 1 -- 0 1
# 2 -- 1 1
# 3 -- 1 2
# 4 -- 2 3
# 5 -- 3 5
# 6 -- 5 8
import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    dp = [[1, 0], [0, 1]]
    if n < 2:
        print(*dp[n])
    else:
        for j in range(2,n+1):
            dp.append([dp[j-1][0]+dp[j-2][0],dp[j-1][1]+dp[j-2][1]])
        print(*dp[n])
