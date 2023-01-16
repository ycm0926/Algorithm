def solution(n, lost, reserve):
                                                
    lost, reserve = set(lost), set(reserve)     # set 자료형
    cross = lost & reserve                      # 교집합
    lost -= cross                                 
    reserve -= cross
                                                
    cnt = n-len(lost)                           # 최소한의 개수
                                                
    for i in lost:                              # 여벌의 체육복 확인
        if i-1 in reserve:
            reserve.remove(i-1)
            cnt +=1
        elif i+1 in reserve:
            reserve.remove(i+1)
            cnt +=1

    return cnt