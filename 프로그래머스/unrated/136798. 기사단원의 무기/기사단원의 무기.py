def solution(number, limit, power):
    answer = []
    for i in range(1,number+1):                 # 약수 범위
        cnt = 0                                 # 약수 개수
        for j in range(1, int(i **(1/2))+1):    # 약수의 절반까지 탐색
            if i%j == 0:                        # 약수라면 카운트
                cnt += 1
                if j != i//j:                   # 짝이 되는 약수가 중복 값 방지
                    cnt += 1
        if cnt > limit:
            cnt = power
        answer.append(cnt)
    return sum(answer)