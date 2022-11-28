import sys
input = sys.stdin.readline
N, M = map(int,input().split())
res = {}
for _ in range(N):
    a,b = input().strip().split()
    res[a] = b
for i in range(M):
    print(res[input().strip()])
