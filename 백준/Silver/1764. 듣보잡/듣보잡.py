import sys
input = sys.stdin.readline

N, M = map(int,input().split())
d = set()
b = set()
for _ in range(N):
    d.add(input().strip())
for _ in range(M):
    b.add(input().strip())
intersection = list(d & b)
print(len(intersection))
for i in sorted(intersection):
    print(i)