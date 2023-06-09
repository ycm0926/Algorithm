import heapq
import sys

input = sys.stdin.readline
heap = []
for i in range(int(input())):
    tmp = int(input())

    if tmp:
        heapq.heappush(heap, (abs(tmp),tmp))
    elif heap and not tmp:
        a = heapq.heappop(heap)
        if a[1] < 1:
            print(a[1])
        else:
            print(a[0])
    elif not heap and not tmp:
        print(0)
