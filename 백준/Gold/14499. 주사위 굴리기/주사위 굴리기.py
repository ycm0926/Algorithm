N, M, x, y, K = map(int,input().split())

arr = [list(map(int,input().split())) for i in range(N)]
lst = list(map(int, input().split()))

n1=n2=n3=n4=n5=n6=0 # 초기 주사위

di, dj = [0, 0, 0, -1, 1], [0, 1, -1, 0, 0] #동서 북남
alst = []
# 명령 이동 후 처리
for dr in lst:
    # [1] 이동 후 범위 체크 후 처리
    ni, nj = x+di[dr], y+dj[dr]

    if 0<=ni<N and 0<=nj<M:
        # [2] 주사위 면 굴리기 (키포인트)
        if dr==1:   # 동
            n1,n3,n4,n6 = n4,n1,n6,n3
        elif dr==2: # 서
            n1,n3,n4,n6 = n3,n6,n1,n4
        elif dr==3: # 북
            n1,n2,n5,n6 = n5,n1,n6,n2
        else:       # 남
            n1,n2,n5,n6 = n2,n6,n1,n5

        # [3] 이동한 바닥판이 0인지 여부에 따라 처리
        if arr[ni][nj] == 0:
            arr[ni][nj] = n6
        else:
            n6, arr[ni][nj] = arr[ni][nj], 0
        alst.append(n1) # 윗면의 값을 ans list에 저장
        x, y = ni, nj # 이동처리
if alst:
    print(*alst, sep='\n')
