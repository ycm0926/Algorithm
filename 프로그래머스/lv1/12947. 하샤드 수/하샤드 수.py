# 나의 풀이
def solution(x):
    res = sum(map(int,str(x))) # int형을 str로 변환하여 하나씩 int로 변환하여 sum
    if x % res == 0:
        return True
    else:
        return False

'''
# 다른사람 풀이
def Harshad(n):
    return n % sum([int(c) for c in str(n)]) == 0

TIL/회고

- 다른사람 풀이 boolean 이용해서 더 간결한 코드
'''
