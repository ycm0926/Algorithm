import sys

input = sys.stdin.readline
N, M = map(int, input().split())
N_l = list(map(int, input().split()))
start = max(N_l)
end = sum(N_l)

while start <= end:
    cnt = 0
    total = 0
    mid = (start + end) // 2

    for i in N_l:
        if total + i > mid:
            cnt += 1
            total = 0
        total += i
    if total:
        cnt += 1
    if cnt <= M:                         # 개수가 부족한 경우 더 자르기(왼쪽 부분 탐색)
        end = mid - 1
    else:                               # 개수가 충분한 경우 덜 자르기(오른쪽 부분 탐색)
        start = mid + 1

print(end+1)