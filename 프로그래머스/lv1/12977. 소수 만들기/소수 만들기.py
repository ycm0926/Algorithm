from itertools import combinations

def solution(nums):

    lis = list(map(sum,combinations(nums,3)))
    cnt = 0
    for i in lis:
        for j in range(2,int(i**0.5)+1):
            if not i%j:
                break
        else:
            cnt += 1

    return cnt