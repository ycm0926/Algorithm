import sys

input = sys.stdin.readline
for i in range(int(input())):
    cnt = 0
    N, M = map(int,input().split())
    A = sorted(map(int,input().split()))
    B = sorted(map(int,input().split()))
    idx, cnt = 0, 0

    for i in range(N):
        while idx < M:
            if A[i] > B[idx]:
                idx += 1
            else:
                break
        cnt += idx
    print(cnt)