for test_case in range(int(input())):
    l = int(input())

    MBTI = list(map(str,input().split()))
    ans = int(1e9)

    '''
        비둘기집 원리
        비둘기가 n마리, 비둘기집이 m개 있을 때
        n이 m보다 크면 적어도 하나의 집에는 비둘기가 2마리 이상 들어간다는 원리
        즉, 인원이 17명 이상이면 2명의 같은 MBTI 33명이면 3명이므로 최소 거리는 0  
    '''

    if l > 32:
        print(0)
        continue

    for i in range(l):
        for j in range(l):
            for k in range(l):
                tmp = 0
                if i == j or j == k or k == i:
                    continue

                for m in range(4):

                    if MBTI[i][m] != MBTI[j][m]:
                        tmp += 1
                    if MBTI[j][m] != MBTI[k][m]:
                        tmp += 1
                    if MBTI[i][m] != MBTI[k][m]:
                        tmp += 1

                ans = min(tmp,ans)
    print(ans)