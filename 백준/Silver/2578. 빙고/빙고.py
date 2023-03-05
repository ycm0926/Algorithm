import sys

input = sys.stdin.readline
bingo = [list(map(int,input().split())) for _ in range(5)]
sol = [list(map(int,input().split())) for _ in range(5)]

b_cnt = 0  # 빙고 최소 개수 카운트 12 이상이 되면 그 때부터 check 시작
total = 0
def check():
    # 빙고 개수 카운트 
    cnt = 0 

    # 가로 빙고 확인
    for i in range(5):
        if sum(bingo[i]) == 0:
            cnt +=1
            if cnt >= 3:
                print(total)
                exit()

    # 세로 빙고 확인
    for i in range(5):
        for j in range(5):
            if bingo[j][i] != 0:
                break
        else:
            cnt += 1
            if cnt >= 3:
                print(total)
                exit()


    # 왼 대각 빙고 확인
    for i in range(5):
        if bingo[i][i] != 0:
            break
    else:
        cnt += 1
        if cnt >= 3:
            print(total)
            exit()
    
    # 오 대각 빙고 확인
    for i in range(5):
        if bingo[i][4-i] != 0:
            break
    else:
        cnt += 1
        if cnt >= 3:
            print(total)
            exit()


for a in sol:
    for b in a:
        for c in range(5):
            for d in range(5): 
                if b == bingo[c][d]:
                    bingo[c][d] = 0
                    total += 1
                    b_cnt += 1
                    if b_cnt >= 12:
                        check()