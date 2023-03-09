import sys

input = sys.stdin.readline
N = int(input())
M = int(input())
nums = sorted(map(int,input().split()))

cnt = 0
interval_sum = 0
s, e = 0, N-1

while s < e:
    interval_sum = nums[s] + nums[e]

    if interval_sum == M:
        cnt += 1
        s += 1
        e -= 1
    elif interval_sum > M:
        e -= 1
    else:
        s += 1

print(cnt)