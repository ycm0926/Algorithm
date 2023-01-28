import sys

input = sys.stdin.readline

N, M = map(int,input().split())
graph = [input() for i in range(N)]
total = 0
for i in range(N):
    check = False
    cnt = 0
    for j in graph[i]:
        if j == '-' and check:
            continue
        elif j == '-':
            cnt += 1
            check = True
            continue
        elif j == '|':
            total += cnt
            cnt = 0
            check = False
    total += cnt
for i in range(M):
    check = False
    cnt = 0
    for j in range(N):
        if graph[j][i] == '|' and check:
            continue
        elif graph[j][i] == '|':
            cnt += 1
            check = True
            continue
        elif graph[j][i] == '-':
            total += cnt
            cnt = 0
            check = False
    total += cnt
print(total)