import sys
import math

input = sys.stdin.readline

N, M = map(int,input().split())

jewel = [int(input()) for i in range(M)]
start = 1
end = max(jewel)

while (start <= end):
    cnt = 0
    total = 0
    mid = (start+end)//2

    for i in jewel:
        cnt += math.ceil(i/mid)

    if cnt > N:
        start = mid + 1
    else:
        end = mid - 1

print(end+1)