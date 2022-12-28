# 300초 60초 10초

T = int(input())
lis = [0,0,0]
if T%10 != 0:
    print(-1)
else:
    lis[0] += T//300
    T %= 300
    lis[1] += T//60
    T %= 60
    lis[2] += T//10
    T %= 10
    print(*lis)