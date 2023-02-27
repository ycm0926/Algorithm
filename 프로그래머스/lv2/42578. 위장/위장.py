def solution(clothes):
    
    answer = 1
    Camouflage = {}
    
    for i in clothes:
        if i[1] in Camouflage:
            Camouflage[i[1]] += 1       # 옷 종류별 카운트
        else:
            Camouflage[i[1]] = 2        # 옷을 안 입는 경우 추가 +1
    
    for i in Camouflage.values():
        answer *= i
        
    return answer-1