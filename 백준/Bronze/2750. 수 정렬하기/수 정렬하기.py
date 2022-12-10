import sys
input = sys.stdin.readline
a = []
for i in range(int(input())):
    a.append(int(input()))
for i in sorted(a):
    print(i)