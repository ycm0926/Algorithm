import sys

pig = []
pig = [list(map(int, input().split())) for _ in range(int(input()))]
for i in range(len(pig)):
    cnt = 1
    for j in range(len(pig)):
        if pig[i][0] < pig[j][0] and pig[i][1] < pig[j][1]:
            cnt += 1
    print(cnt, end=' ')
