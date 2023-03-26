import sys
input = sys.stdin.readline

cnt = 0

for i in range(int(input())):
    tmp = []
    for j in input().rstrip():
        if not tmp or tmp[-1] != j:
            tmp.append(j)
        else:
            tmp.pop()
    if not tmp:
        cnt += 1
print(cnt)