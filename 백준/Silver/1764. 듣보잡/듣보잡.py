# 나의 풀이 (128ms)

import sys
input = sys.stdin.readline

N, M = map(int,input().split())
d = set()        # 중복 없는 자료형 생성
b = set()
for _ in range(N):
    d.add(input().strip())
for _ in range(M):
    b.add(input().strip())
intersection = list(d & b)        # 교집합 생성
print(len(intersection))
for i in sorted(intersection):
    print(i)

'''
# 다른 사람 풀이 (python3 108ms)

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
names = set()
results = set()

for _ in range(N):                              # 중복 없으므로 set 자료형 활용
    names.add(input())

for _ in range(M):
    name = input()
    if name in names:                           # 앞 세트에 있으면 뒷 세트에 추가
        results.add(name)

print(len(results))
for result in sorted(results):                  # 뒷 세트 정렬 후 출력
    print(result.rstrip())
    

TIL/회고
- 아 쉬운 문제인데 쉽게 생각하는 게 어렵다.. 문제 분석이 부족한 걸까.. 파이썬을 까먹은 걸까 안 떠오른다 ㅠㅠ
'''