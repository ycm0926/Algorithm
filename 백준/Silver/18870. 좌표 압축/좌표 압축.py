import sys

input = sys.stdin.readline
input()
arr = list(map(int, input().split()))
dic = {}
for i,v in enumerate(sorted(set(arr))):
    dic[v] = i
for i in range(len(arr)):
    arr[i] = dic[arr[i]]
print(*arr)