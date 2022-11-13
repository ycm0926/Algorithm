import sys
input = sys.stdin.readline
m = []
for _ in range(int(input())):
    k = int(input())
    if k == 0:
        m.pop()
    else:
        m.append(k)
print(sum(m))
