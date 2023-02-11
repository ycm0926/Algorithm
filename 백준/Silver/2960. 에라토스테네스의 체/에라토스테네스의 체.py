N, K = map(int,input().split())

era = [False]*2 + [True]*(N-1)
pr = []
cnt = 0

for i in range(2, N+1):                 # 2부터 n까지의 모든 수를 확인하며
    if era[i]:                          # i가 소수인 경우 (남은 수인 경우)
        for j in range(i, N+1,i):       # i부터 모든 배수를 지우기
            if era[j]:                  # j가 False인 경우만 카운트
                cnt += 1
                if cnt == K:
                    print(j)
                    exit()
            era[j] = False