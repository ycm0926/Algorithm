# 범위 천만 넘음 이진탐색
# 개수 확인 -> 계수정렬
import sys

# 카드 개수 n 입력받기
_ = int(input())
# 카드 값 테이블
array = [0] * 20000001

# 카드 개수 기록
for i in sys.stdin.readline().split():
    array[int(i)] += 1

# 확인 개수 m 입력받기
_ = int(input())

# 확인 카드 번호 리스트
x = list(map(int, sys.stdin.readline().split()))

# 찾는 카드 개수 하나씩 확인
for i in x:
    # 해당 카드 존재하는지 확인
    print(array[i], end=' ')

