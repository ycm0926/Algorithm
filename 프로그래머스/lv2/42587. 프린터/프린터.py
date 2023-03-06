from collections import deque
def solution(priorities, location):
    answer = 0
    tmp = deque([[i,idx] for idx, i in enumerate(priorities)])

    while 1:
        if tmp[0][0] == max(tmp)[0] and tmp[0][1] == location:
            return answer + 1
        elif tmp[0][0] == max(tmp)[0]:
            answer += 1
            tmp.popleft()
        else:
            tmp.append(tmp.popleft())
            
    