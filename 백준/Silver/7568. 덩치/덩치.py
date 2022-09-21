import sys

arr = [list(map(int, sys.stdin.readline().split())) for _ in range(int(input()))]
for i in range(len(arr)):
    cnt = 1
    for j in range(len(arr)):
        if arr[i][0] < arr[j][0] and arr[i][1] < arr[j][1]:
            cnt += 1
    print(cnt, end=' ')
    