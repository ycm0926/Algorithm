def solution(answers):
    first = [5 if i%5==0 else i%5 for i in range(1,len(answers)+1)] # first 리스트 만들기
    second = []
    third = []

    cnt = 1
    for i in range(len(answers)):                                   # second 리스트 만들기
        if i % 2 == 0:                                              # index가 짝수면 2를 추가
            second.append(2)
        else:                                                       # index가 홀수면 cnt를 추가
            second.append(cnt)
            cnt += 1                                                # cnt에 1 더해줌
            if cnt == 2:                                            # cnt가 2면 1더해 3을 만듦
                cnt += 1
            if cnt == 6:                                            # cnt가 6이면 1로 초기화
                cnt = 1

    cnt = 3
    for i in range(len(answers)):                                   # third 리스트 만들기
        third.append(cnt)                                           # third에 cnt 추가
        if len(third) % 2 == 0:                                     # 길이가 짝수고
            if cnt == 3:                                            # cnt가 3이면 1로 초기화
                cnt = 1
            elif cnt == 5:                                          # cnt가 5면 3으로 초기화
                cnt = 3
            else:                                                   # cnt가 3,5아니라면 cnt += 1
                cnt += 1                                            # 만약 third[-1] == 2라면 cnt 4로 초기화
                if third[-1] == 2:
                    cnt = 4

    lis = [0,0,0]
    ans = []
    for i in range(len(answers)):                                   # 수포자 각자 정답 개수 카운트
        if answers[i] == first[i]:
            lis[0] +=1
        if answers[i] == second[i]:
            lis[1] +=1
        if answers[i] == third[i]:
            lis[2] +=1

    for i in range(len(lis)):                                       # 최대 값과 같은 값의 index를 ans에 추가
        if max(lis) == lis[i]:
            ans.append(i+1)
    return ans


# 무식해 보여도 사실은 최고의 방법일 때가 있지요.
# 가능한 모든 상황을 조사해 문제를 풀어보세요.
