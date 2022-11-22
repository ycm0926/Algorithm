def solution(arr):
    return (sum(arr)/len(arr)) # 리스트 값들을 더한 후 길이 만큼 나눠준다

'''
# 다른사람 풀이

from functools import reduce
def solution(n):
    # reduce 초기값이 없다면 lambda를 통해 list 에서 두 개의 값을 가져와 더한 후 결과를 x에 저장하고 다시 list에서 y값을 가져와 x에 계속 더해 준다.
    return(reduce(lambda x, y : x + y, list) / len(list)) 

TIL/회고
- 문제는 쉽게 풀렸으며, reduce 함수의 사용법을 처음 알게됐다.
'''
