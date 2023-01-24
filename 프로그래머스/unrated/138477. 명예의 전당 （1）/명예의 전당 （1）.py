def solution(k, score):

    q = []

    answer = []
    for s in score:

        q.append(s)
        if (len(q) > k):        # 전당에 수가 k보다 많다면
            q.remove(min(q))    # 제일 작은 값 삭제
        answer.append(min(q))  

    return answer