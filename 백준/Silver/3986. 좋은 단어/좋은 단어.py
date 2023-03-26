import sys
input = sys.stdin.readline

cnt = 0

for i in range(int(input())):
    tmp = []
    for j in input().rstrip():
        if not tmp:
            tmp.append(j)
        elif tmp[-1] == j:
            tmp.pop()
        else:
            tmp.append(j)
    if not tmp:
        cnt += 1
print(cnt)