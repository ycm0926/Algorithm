N, M = map(int,input().split())

words = set()
ans = 0
for i in range(N):
    words.add(input())

for i in range(M):
    if input() in words:
        ans += 1
print(ans)