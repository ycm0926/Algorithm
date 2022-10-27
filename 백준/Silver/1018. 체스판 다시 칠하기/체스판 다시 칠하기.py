import sys

input = sys.stdin.readline
n, m = map(int, input().split())

array = [list(input()) for _ in range(n)]
ans = []

# 시작지점
for i in range(n-7):
    for j in range(m-7):
        B_cnt = 0
        W_cnt = 0
        for a in range(i, i+8):
            for b in range(j, j+8):
                # 홀수자리 짝수자리 구별
                if (a+b)%2==0:
                    if array[a][b] == 'B':
                        B_cnt += 1
                    elif array[a][b] == 'W':
                        W_cnt += 1

                else:
                    if array[a][b] == 'B':
                        W_cnt += 1
                    elif array[a][b] == 'W':
                        B_cnt += 1

        ans.append(min(W_cnt,B_cnt))
print(min(ans))
