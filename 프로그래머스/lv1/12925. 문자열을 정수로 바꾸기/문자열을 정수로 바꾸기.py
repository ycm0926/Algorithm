# 나의 풀이
def solution(s):
    li = []
    for i in s:
        for j in i:
            if j == '"':
                continue
            elif j == '-':
                li.append(j)
            else:
                li.append(j)

    li = ''.join(li)
    return int(li)

'''
# 다른사람 풀이
def solution(str):
    a = int(str)
    return a

TIL/회고

- int리스트는 join 불가하다.
- 다른사람 풀이 파이썬은 정수형으로 바꿀 때 자동으로 -,+는 변환을 해준다.
'''