import sys

input = sys.stdin.readline

for tc in range(3):
    res = list(map(int,input().split()))
    if res.count(0) == 1:
        print('A')
    elif res.count(0) == 2:
        print('B')
    elif res.count(0) == 3:
        print('C')
    elif res.count(0) == 4:
        print('D')
    else:
        print('E')
