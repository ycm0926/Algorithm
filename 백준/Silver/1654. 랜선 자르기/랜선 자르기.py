import sys

input = sys.stdin.readline
k, n = map(int, input().split())

k_list = [int(input()) for _ in range(k)]
start, end = 1, max(k_list)

while (start <= end):
    total = 0
    mid = (start+end)//2
    for x in k_list:
        total += x//mid
    # 전선이 부족한 경우 왼쪽 탐색
    if total < n:
        end = mid-1
    # 오른쪽 탐색
    else:
        start = mid+1

print(end)
