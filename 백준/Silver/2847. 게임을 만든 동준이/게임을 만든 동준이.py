import sys
input = sys.stdin.readline
n = int(input())
level = [int(input()) for _ in range(n)]
level.reverse()
ans = 0

for i in range(n - 1):
    while 1:
        if level[i] > level[i+1]:
            break
        else:
            level[i+1] -= 1
            ans +=1
print(ans)
