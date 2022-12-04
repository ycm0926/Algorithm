import sys

dp = [0] * 101      # 메모이제이션 101까지 dp테이블 할당
dp[0] = 0
dp[1] = 1
dp[2] = 1
dp[3] = 1
dp[4] = 2
dp[5] = 2
for i in range(int(input())):
    N = int(input())
    for i in range(6, 101):
        dp[i] = dp[i-1]+dp[i-5]       # 점화식
    print(dp[N])


'''
TIL/회고
- 오랜만에 금방 풀린 dp 문제
'''