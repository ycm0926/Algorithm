def solution(num):
    return ('Even' if num%2 == 0 else 'Odd')

'''
# 다른사람 풀이

def evenOrOdd(num):
    # num의 첫번째 비트가 1이면 비트 연산을 통해 1을 반환
    # 리스트를 변수 초기화를 하지 않고 리스트 자체에 인덱싱
    return ["Even", "Odd"][num & 1] 
    
TIL/회고
- 비트 연산으로 홀짝 출력과 리스트를 바로 인덱싱 하는 방법은 새로웠다.
'''