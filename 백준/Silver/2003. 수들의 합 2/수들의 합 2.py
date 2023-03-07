import sys

input = sys.stdin.readline
N, M = map(int,input().split())
lis = list(map(int,input().split()))
cnt, interval_sum, end = 0, 0, 0

# start 차례대로 증가 시키며 반복
for start in range(N):
    
    # end를 가능한 만큼 이동시키기
    while interval_sum < M and end < N:
        interval_sum += lis[end]
        end += 1

    # 부분합이 M일 때 카운트 증가
    if interval_sum == M:
        cnt += 1

    interval_sum -= lis[start]
print(cnt)