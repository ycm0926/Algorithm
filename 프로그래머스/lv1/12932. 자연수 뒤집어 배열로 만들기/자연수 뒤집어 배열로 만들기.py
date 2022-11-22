def solution(n):
    # int형 리스트로 만든 후 뒤집고 다시 리트로 만들어 출력
    return list(reversed(list(map(int,str(n)))))

'''
# 다른사람 풀이

def digit_reverse(n):
    return list(map(int, reversed(str(n))))
    
TIL/회고
- 처음 str로 받을때 뒤집으면 되는구나... 
'''