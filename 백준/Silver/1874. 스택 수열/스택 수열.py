import sys

input = sys.stdin.readline
n = int(input())

stack = []
ans = []
num_in = [int(input()) for _ in range(n)]
num_li = [i for i in range(1, n+1)]
num_li.sort(reverse=True)

i = 0
while i != n:
    try:
        if num_in[i] not in stack:
            stack.append(num_li.pop())
            ans.append('+')
        if num_in[i] in stack:
            stack.pop()
            ans.append('-')
            i += 1
    except:
        print('NO')
        exit()

for j in ans:
    print(j)
