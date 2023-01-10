import sys

input = sys.stdin.readline

K, M = map(int,input().split())
LAN = [int(input()) for i in range(K)]
start = 1
end = max(LAN)
while start <= end:
    total = 0
    mid = (start+end)//2                # 자를 랜선 길이 지정

    for i in LAN:
        total += i//mid                 # 자른 랜선 수

    if total < M:                       # 랜선의 개수가 부족한 경우 더 짧게 자르기(왼쪽 탐색)
        end = mid - 1

    else:                               # 랜선의 개수가 충분한 경우 덜 자르기(오른쪽 탐색)
        start = mid + 1
print(end)