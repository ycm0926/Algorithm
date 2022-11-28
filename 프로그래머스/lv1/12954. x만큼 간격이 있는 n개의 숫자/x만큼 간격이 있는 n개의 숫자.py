# 나의 풀이

def solution(x, n):
    if x > 0:
        return [i for i in range(x, n*x+1, x)]
    elif x == 0:
        return [0]*n
    else:
        return [i for i in range(x, n*x-1, x)]
    
'''
# 다른사람 풀이

def number_generator(x, n):
    # 함수를 완성하세요
    return [i * x + x for i in range(n)]
print(number_generator(2, 5))

TIL/회고
- X가 0일 때 처리 때문에 오래 걸렸다.
- 다른 사람 풀이처럼 조금만 생각을 달리 했으면  쉬웠을 텐데 하..ㅠ
'''