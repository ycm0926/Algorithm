import sys

input = sys.stdin.readline
h, w = map(int,input().split())
memo = [input() for i in range(h)]
res = 0
for i in memo:
    cnt = 0
    for j in i:
        if j == '\\' or j == '/':
            cnt += 1
            res += 0.5
        if cnt%2 == 1 and j == '.':
            res += 1

print(int(res))