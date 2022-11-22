def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:
            answer += i
            
    return answer
'''
# 다른사람 풀이

def sumDivisor(num):
    return sum([i for i in range(1,num+1) if num%i==0])

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(sumDivisor(12))

TIL/회고
- 1레벨이라 기본적인 쉬운문제
- 다른 사람의 풀이를 보아도 거이 비슷하다.
'''