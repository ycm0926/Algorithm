from copy import deepcopy as dc
def solution(want, number, discount):
    answer = 0
    tmp = dict(zip(want,number))
    diff = len(discount)-9
    
    for i in range(diff):
        cnt = dc(tmp)
        for j in discount[i:i+10]:
            if j in cnt:
                cnt[j] -= 1
        for v in cnt.values():
            if v > 0:
                break
        else:
            answer += 1
    return answer