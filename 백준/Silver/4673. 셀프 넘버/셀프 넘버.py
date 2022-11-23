# 나의 풀이 (616ms)
lst = []
for i in range(10000): 
    n_l = list(map(int, str(i))) # 입력 숫자를 숫자 리스트로 자리 분리
    lst.append(sum(n_l)+i) # 생성자 들을 전부 lst에 넣어준다.

for j in range(1,10000):
    if j not in lst: # lst에 없다면 i 출력
        print(j)
'''
# 다른사람 풀이 (56ms)

import sys

def d(n: int): # 생성자 값 만드는 함수
    return n + n//1000 + (n%1000)//100 + (n%100)//10 + n%10

dList = [0]*10000
for n in range(10000):
    try:
        dList[d(n)] = 1 # 함수를 돌면서 생성자 값이 있다면 dlist 자리에 1을 넣음 카운트 계수정렬 느낌
    except IndexError: # 생성자 값이 10000이 넘으면 무시
        continue

for d in range(10000):
    if dList[d]==0:
        print(d)

TIL/회고
- 다른사람 풀이 중에 정답을 전부 출력하는 방법이 제일 빠르긴 했다. 천잰데..?
- 개수 체크 또는 set 자료형을 사용하는 방법이 시간을 많이 단축 시킨다.
'''