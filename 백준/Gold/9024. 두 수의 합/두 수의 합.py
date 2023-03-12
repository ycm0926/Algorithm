import sys
from collections import deque
input = sys.stdin.readline

for i in range(int(input())):
    N, K = map(int,input().split())
    S = sorted(list(map(int,input().split())))
    cnt, interval_sum = 0, 0
    s, e = 0, N-1
    tmp = []
    while s < e:
        interval_sum = S[s] + S[e]
        
        if interval_sum == K:
            cnt += 1
            s += 1
            e -= 1
        else:
            if interval_sum > K:
                e -= 1
            else:
                s += 1
            tmp.append(abs(K-interval_sum))

    if cnt:
        print(cnt)
    else:
        print(tmp.count(min(tmp)))