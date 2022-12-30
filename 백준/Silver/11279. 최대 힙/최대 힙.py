import heapq
import sys

input = sys.stdin.readline
res = []
for i in range(int(input())):
    x = int(input())
    if x != 0:
        heapq.heappush(res, -x)
    elif x == 0 and not res:
        print(0)
    else:
        print(-(heapq.heappop(res)))
