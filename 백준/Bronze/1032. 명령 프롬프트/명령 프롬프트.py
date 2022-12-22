import sys

input = sys.stdin.readline
k = int(input())
res = list(input())
for i in range(k-1):
    for idx, j in enumerate(input()):       # 순서(idx)와 값(j)을 받음
        if res[idx] != j:                   # res[idx] 값과 j를 비교하여 다르면 '?'로 교체
            res[idx] = '?'
print(''.join(res))