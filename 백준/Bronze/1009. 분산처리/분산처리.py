import sys

input = sys.stdin.readline

for i in range(int(input())):
    a, b = map(int, input().split())
    aa = a % 10
    if aa == 0:
        print(10)
    elif aa in [1,5,6]:
        print(aa)
    elif aa in [4,9]:
        bb = b % 2
        if bb == 0:
            print(aa**2%10)
        else:
            print(aa)
    else:
        bb=b%4
        if bb == 0:
            print(aa**4%10)
        else:
            print(aa**bb%10)
# 1, 2, 3, 4 -> 0
# 2, 4, 8, 16,   32
# 3, 9, 27, 81,   243
# 1 = 1
# 2 = 2,4,6,8
# 3 = 3,9,7,1
# 4 = 4,6
# 5 = 5
# 6 = 6
# 7 = 7,9,3,1
# 8 = 8,4,2,6
# 9 = 9,1
# 10 = 0