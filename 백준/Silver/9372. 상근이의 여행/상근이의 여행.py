import sys

input = sys.stdin.readline

for i in range(int(input())):
    N, M = map(int,input().split())
    for i in range(M):
        input()

    print(N-1)