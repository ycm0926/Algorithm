import sys
input = sys.stdin.readline
for i in range(int(input())):
    k = list(map(int,input().split()))
    ave = sum(k[1:])/k[0]
    cnt = 0
    for j in k[1:]:
        if j > ave:
            cnt += 1
    print(f"{cnt/(len(k[1:]))*100:.3f}%")