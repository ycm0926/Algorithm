from collections import deque

def solution(food):
    q = deque(['0'])
    for i in range(len(food)-1,0,-1):       # 리스트 -1부터 값을 가져온다
        if food[i] > 1:                     # 값이 1 초과인 경우
            for _ in range(food[i]//2):     # 데큐 양쪽에 넣어준다
                q.append(str(i))
                q.appendleft(str(i))
    return ''.join(list(q))