# 0 -- 1 0
# 1 -- 0 1
# 2 -- 1 1
# 3 -- 1 2
# 4 -- 2 3
# 5 -- 3 5
# 6 -- 5 8
import sys

input = sys.stdin.readline
dp = [[0] * 2] * 41     # dp 선언
dp[0] = [1, 0]
dp[1] = [0, 1]

for j in range(2, 41):      # dp 테이블 초기화
    dp[j] = [dp[j - 1][0] + dp[j - 2][0], dp[j - 1][1] + dp[j - 2][1]]
for _ in range(int(input())):       # 결과 출력
    n = int(input())
    print(*dp[n])

'''
TIL/회고
- 어지러운 DP.. 바텀 업으로 DP테이블 모두 초기화
- 처음 풀이는 DP 테이블을 for문 안에 넣어서 시간과 메모리 낭비가 컸었다.
- DP 테이블은 밖에서 선언해 주고 구현해서 메모 제이 션 제대로 사용하자.
'''