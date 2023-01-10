import sys

input = sys.stdin.readline

N, M = map(int,input().split())
h = list(map(int,input().split()))

start = 1
end = max(h)

while start <= end:
    total = 0
    mid = (start+end)//2

    for i in h:
        if i > mid:
            total += i-mid

    if total < M:
        end = mid - 1
    else:
        start = mid + 1

print(end)