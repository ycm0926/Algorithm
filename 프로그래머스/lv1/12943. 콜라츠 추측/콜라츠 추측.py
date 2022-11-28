# 나의 풀이

def solution(num):
    answer = 0
    while num != 1:  # 1이 아니면 반복
        if num % 2 == 0:  # 1-1 케이스 
            num /= 2
        else:
            num = num*3+1  # 1-2 케이스
        answer += 1
        if answer == 500:  # 2 케이스
            return -1
    return answer

'''
# 다른 사람 풀이

def collatz(num):
    for i in range(500):
        num = num / 2 if num % 2 == 0 else num*3 + 1
        if num == 1:
            return i + 1
    return -1
    
TIL/회고
- 다른 사람 풀이는 A if 조건 else B로 축약한 풀이
- A if 조건 else B if 조건 else C도 가능
'''