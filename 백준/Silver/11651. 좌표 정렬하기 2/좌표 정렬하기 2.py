import sys
for i in sorted([list(map(int,sys.stdin.readline().split())) for i in range(int(input()))],key=lambda x: (x[1],x[0])):
    print(*i)