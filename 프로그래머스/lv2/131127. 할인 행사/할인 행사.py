import copy
def solution(want, number, discount):
    answer = 0
    tmp = dict(zip(want,number))
    
    for i in range(len(discount)-9):
        cnt = copy.copy(tmp)
        for j in discount[i:i+10]:
            if j in cnt:
                cnt[j] -= 1
        for v in cnt.values():
            if v > 0:
                break
        else:
            answer += 1
    return answer