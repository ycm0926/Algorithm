import sys

word = input()
w_len = len(word)
C = []
for i in range(1, w_len+1):
    for j in range(i, w_len+1):
        if i*j == w_len:
            C.append([i, j])

C.sort()
R = C[-1]
ans = [[_ for _ in range(R[0])] for _ in range(R[1])]

k = 0
for i in range(len(ans)):
    for j in range(len(ans[i])):
        ans[i][j] = word[k]
        k += 1
for i in range(len(ans[0])):
    for j in range(len(ans)):
        print(ans[j][i], end='')
