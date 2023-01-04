from collections import Counter

def solution(N, stages):
    user = len(stages)              # 사용자 수
    answer = [0] * (N+1)            # 실패율 리스트
    dummy = []                      # 실패율 0 리스트
    for i in range(1,N+1):
        k = stages.count(i)         # 스테이지 i번에서 실패한 사람 카운트
        if k == 0:                  # 모두가 통과 했다면 순번과 100을 넣어준다.
            answer[i] = (i,0)
            continue
        answer[i] = (i,k/user)      # 실패한 사람이 있다면 순번과 실패율을 answer에 넣어준다.
        user -= k                   # 전체 유저수에서 실패한 유저수를 빼준다.
    return [i[0] for i in sorted(answer[1:], key =  lambda x: -x[1])]