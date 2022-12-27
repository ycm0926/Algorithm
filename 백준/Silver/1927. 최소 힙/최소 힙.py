import sys
import heapq
input = sys.stdin.readline
q = []
for i in range(int(input())):
    a = int(input())
    if a == 0:
        if not q:
            print(0)
            continue
        print(heapq.heappop(q))
    else:
        heapq.heappush(q, a)