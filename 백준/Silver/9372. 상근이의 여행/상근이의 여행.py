import sys


input = sys.stdin.readline
tc = int(input())

for i in range(tc):
    N, M = map(int,input().split())
    graph = [[] * (N+1) for i in range(N+1)]
    visited = [False] * (N+1)
    cnt = 0
    for i in range(M):
        a, b = map(int,input().split())
        graph[a].append(b)
        graph[b].append(a)

    print(N-1)