n = int(input())
schedule = [list(map(int, input().split())) for _ in range(n)]
dp = [0] * (n + 1)  # DP 테이블 초기화

# 뒤에서부터 거꾸로 탐색하면서 DP를 채워나간다.
for i in range(n - 1, -1, -1):
    if i + schedule[i][0] <= n:  # 현재 상담이 가능한 경우
        dp[i] = max(schedule[i][1] + dp[i + schedule[i][0]], dp[i + 1])
    else:  # 현재 상담이 퇴사 전까지 불가능한 경우
        dp[i] = dp[i + 1]

print(dp[0])  # 최대 이익 출력
