# 나의 풀이 (python3 276ms)
import sys
input = sys.stdin.readline
N, M = map(int,input().split())
res = {}  # 딕셔너리 선언
for _ in range(N):
    a,b = input().strip().split()  # a,b로 키,값 받음
    res[a] = b
for i in range(M):
    print(res[input().strip()]) # 입력돤 a의 value 출력

'''
TIL/회고
- 바로 딕셔너로 생각이 났던 문제다.
- 다른 풀이도 크게 다르지는 않다.
'''