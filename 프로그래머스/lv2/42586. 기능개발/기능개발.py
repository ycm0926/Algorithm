import math
def solution(progresses, speeds):
    answer = []
    days = []
    for p,s in zip(progresses, speeds):
        days.append(math.ceil((100-p)/s))
    
    day = 0
    
    for i in range(1,len(days)):
        if days[i] > days[day]:
            answer.append(i-day)
            day = i
            
    answer.append(len(days)-day)
    
    return answer