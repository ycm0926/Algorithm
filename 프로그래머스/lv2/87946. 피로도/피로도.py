from itertools import permutations as p

def solution(k, dungeons):
    answer = 0
    for i in p(range(len(dungeons))):
        cnt = 0
        tmp = k
        for j in i:
            if tmp >= dungeons[j][0]:
                tmp -= dungeons[j][1]
                cnt += 1
                if tmp < 1:
                    break
        answer = max(cnt,answer)
    return answer
        
    
        
            

