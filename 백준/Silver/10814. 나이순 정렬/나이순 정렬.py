import sys

arr = []
for _ in range(int(input())):
    arr.append(sys.stdin.readline().split())
arr.sort(key=lambda x: (int(x[0])))
for i in range(len(arr)):
    print(' '.join(arr[i]))