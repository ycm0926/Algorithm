import sys

input = sys.stdin.readline
T = int(input())
for i in range(T):
    cnt = 0
    N, M = map(int,input().split())
    A = list(map(int,input().split()))
    B = sorted(map(int,input().split()))

    for i in A:
        s, e = 0, M-1
        while s <= e:
            
            mid = (s+e)//2
    
            if i > B[mid]:
                s = mid+1
            else:
                e = mid-1
        cnt += s
    print(cnt)