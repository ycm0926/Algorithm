import sys

input = sys.stdin.readline

N, M = map(int,input().split())

arr = []
a = []
arr = [list(input().split()) for i in range(N)]

for i in range(N):
    for j in range(M):
        if arr[i][j] == '1':
            if a:
                print(abs(i-a[0])+abs(j-a[1]))
                exit()
            a = [i,j]