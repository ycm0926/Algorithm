import sys

input = sys.stdin.readline
N, K = map(int,input().split())
characters = [int(input()) for i in range(N)]
start = min(characters)
end =  1000000001
while start <= end:
    mid = (start+end)//2
    cnt = 0

    for i in characters:
        if i < mid:
            cnt += mid-i

    if cnt <= K:
        start = mid + 1
    else:
        end = mid - 1

print(end)