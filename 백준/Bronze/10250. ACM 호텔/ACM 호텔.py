# 예제 입력과 출력에 규칙힌트 존재

import sys

t = int(input())

for _ in range(t):
    h, w, n = map(int, sys.stdin.readline().split())
    num = n // h+1
    floor = n % h
    if n % h == 0:  # h의 배수이면
        num = n//h
        floor = h
    print(f'{floor*100+num}')