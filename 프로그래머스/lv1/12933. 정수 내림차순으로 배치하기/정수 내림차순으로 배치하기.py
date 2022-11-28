# 나의 풀이

def solution(n):
    answer = list(str(n))
    answer.sort(reverse=True)
    return int(''.join(answer))

'''
# 다른사람 풀이

    return int("".join(sorted(list(str(n)), reverse=True)));

TIL/회고
- sort는 리턴이 없어 바로 print나 return시none이 출력된다.
- return에 int를 넣으면 될까 했는데 이렇게도 된다.
- 다른 사람 풀이도 비슷하다. sorted로 바로 반환해 준다.
'''