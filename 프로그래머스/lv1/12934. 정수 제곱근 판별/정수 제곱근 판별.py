import math
def solution(n):
    x = int(math.sqrt(n)) # n 제곱근 x 초기화
    if n == x**2: # n 의 제곱근이 있다면
        return (x+1)**2
    
    else :
        return -1

'''
# 다른사람 풀이

def solution(n):
    # return A and B or C
    # A가 참이면 B가 선택되며 or시 and결과 B가 참이기 때문에 바로 B리턴
    # A가 거짓이면 A가 선택되며 or시 and결과 A가 거짓이기 때문에 바로 '-1'리턴 
    return n == int(n**.5)**2 and int(n**.5+1)**2 or '-1'
    
TIL/회고
- 파이썬 bool타입의 특징을 이용한 풀이
- 기억이 잘 안 나서 다시 복습했지만 사용을 좀 해보면 안 까먹을 거 같다.
'''