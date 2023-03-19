def solution(genres, plays):
    rank1 = {}
    rank2 = {}
    answer = []

    for i,(g,p) in enumerate(zip(genres,plays)):                                # rank1은 가장 많이 재생된 장르 찾기, rank2는 고유 번호와 재생 횟수
        if g in rank1:
            rank1[g] += p
            rank2[g].append([p,i])
        else:
            rank1[g] = p
            rank2[g] = [[p,i]]
    rank1 = sorted(rank1.items(), key=lambda x: x[1], reverse=True)             # 속한 노래가 많이 재생된 장르를 먼저 정렬
    
    for i in rank1:
        tmp = sorted(rank2[i[0]], key=lambda x: (x[0], -x[1]), reverse=True)    # 장르 내에서 많이 재생된 노래를 먼저 정렬
        if len(tmp) > 1:                                                                
            answer.append(tmp[0][1])                                            # 고유 번호가 낮은 노래를 먼저 수록합니다.
            answer.append(tmp[1][1])
        else:
            answer.append(tmp[0][1])
    return answer    