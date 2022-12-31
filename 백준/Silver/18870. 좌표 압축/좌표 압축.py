import sys
input = sys.stdin.readline

input()
arr = list(map(int, input().split()))
s = sorted(set(arr))
dic = {s[i]:i for i in range(len(s))}
for i in arr:
    print(dic[i], end=' ')