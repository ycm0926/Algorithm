import sys
input = sys.stdin.readline

N, K = map(int,input().split())
coins = []
cnt = 0
for _ in range(N):
    coins.append(int(input()))
coins.reverse()
for i in coins:
    if K//i != 0:
        cnt += K//i
        K = K%i
print(cnt)