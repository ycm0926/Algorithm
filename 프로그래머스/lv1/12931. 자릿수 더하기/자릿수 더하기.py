def solution(n):
    ans = 0
    answer = list(str(n)) # n 값을 str 형태로 list 만듬
    for i in map(int, answer): # map을 통해 하나씩 int로 변경후 계속 더해준다.
        ans += i
    
    return ans

'''
# 다른사람 풀이

def sum_digit(number):
    return sum(map(int,str(number)))

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print("결과 : {}".format(sum_digit(123)));

TIL/회고
- 한줄이면 ez하게 풀리는 문제
'''