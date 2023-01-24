def solution(k, m, score):
    answer = 0
    score = sorted(score,reverse=True)
    for i in range(0,len(score),m):
        box = score[i:i+m]
        if len(box) == m:               # 포장이 됐다면 (최저 사과 점수) x (한 상자에 담긴 사과 개수)
            answer += box[-1]*m

    return answer
