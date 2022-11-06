# d0 = 1, 0
# d1 = 0, 1
# d2 = 1, 1
# d3 = 1, 2
# d4 = 2. 3
# d5 = 3, 5
# d6 = 5, 8
import sys

input = sys.stdin.readline
t = int(input())

for i in range(t):
    n = int(input())
    d = [] * n
    d.append([1, 0])
    d.append([0, 1])
    d.append([1, 1])
    if n >= 3:
        for i in range(3,n+1):
            d.append([d[i-1][0] + d[i-2][0], d[i-1][1] + d[i-2][1]])
        print(*d[n])
    else:
        print(*d[n])
