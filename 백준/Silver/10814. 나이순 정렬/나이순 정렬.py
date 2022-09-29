import sys

t = int(input())

arr = []
for _ in range(t):
    arr.append(sys.stdin.readline().split())
arr.sort(key=lambda x: (int(x[0])))
for i in range(t):
    print(' '.join(arr[i]))