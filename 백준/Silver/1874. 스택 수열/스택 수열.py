import sys

input = sys.stdin.readline
n = int(input())

ans1 = []
ans2 = []
num_in = [int(input()) for _ in range(n)]
num_li = [i for i in range(1, n+1)]
num_li.sort(reverse=True)

i = 0
while i != n:
    if num_in[i] not in ans1:
        ans1.append(num_li.pop())
        ans2.append('+')
    if num_in[i] in ans1:
        if num_in[i] == ans1[-1]:
            ans1.pop()
            ans2.append('-')
        else:
            print('NO')
            exit()
        i += 1

for j in ans2:
    print(j)
