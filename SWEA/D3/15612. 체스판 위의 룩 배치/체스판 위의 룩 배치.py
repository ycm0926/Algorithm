for tc in range(1,int(input())+1):
    chess = [input() for _ in range(8)]
    l_chess = len(chess)
    check_r = []
    cnt1 = False
    cnt2 = False
    for i in range(l_chess):
        check_c = 0
        for j in range(l_chess):
            if chess[i][j] == 'O' and check_c == 0:
                check_r.append(j)
                check_c += 1
            elif chess[i][j] == 'O' and check_c >= 1:
                check_c += 1
                break
        if check_c != 1: # 한 행에 1가 아닐 시
            print(f'#{tc} no')
            cnt2 = True
            break
    if cnt2 == False: # 한 행에 1개 씩 있을 시 열 검사
        for k in check_r:
            if check_r.count(k) != 1:
                cnt1 = True
                break
        if cnt1 == False:
            print(f'#{tc} yes')
        else:
            print(f'#{tc} no')
            
'''
T = int(input())

for test_case in range(1, T + 1):
    col = [0 for i in range(8)]
    state = 0
    sum = 0
    for i in range(8):
        st = input()
        if st.count('O') == 1:
            if col[st.index('O')] == 0:
                col[st.index('O')] = 1

    if col.count(1) == 8:
        print(f'#{test_case} yes')
    else:
        print(f'#{test_case} no')
'''