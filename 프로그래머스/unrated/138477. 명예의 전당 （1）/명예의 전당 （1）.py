def solution(k, score):
    ans = []
    temple = []
    for i in score:
        if len(temple) < k:     # k일 까지 전당에 추가
            temple.append(i)
        elif temple[0] < i:     # 만일 전당의 제일 작은 값보다 새로운 score값이 크다면 교체
            temple[0] = i
        temple = sorted(temple)
        ans.append(temple[0])
    return ans
