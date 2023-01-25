def solution(numbers, hand):
    col = [[1,4,7,'*'],[2,5,8,0],[3,6,9,'#']]
    row = [[1,2,3],[4,5,6],[7,8,9],['*',0,'#']]
    col_mid = [2,5,8,0]
    if hand == "right":                                                      #
        hand = 'R'
    if hand == "left":
        hand = 'L'
    answer = ''
    L_H = '*'
    R_H = '#'

    for i in numbers:
        if L_H == i:                                                # 전과 같은 번호가 들어오는 경우
            answer += 'L'
        elif R_H == i:                                              # 전과 같은 번호가 들어오는 경우
            answer += 'R'
        elif i == 1 or i == 4 or i == 7:                            # 1, 4, 7이 들어오는 경우
            answer += 'L'
            L_H = i
        elif i == 3 or i == 6 or i == 9:                            # 3, 6, 9가 들어오는 경우
            answer += 'R'
            R_H = i
        else:
            for j in col:                                           # 2, 5, 8, 0이 들어오는 경우
                if i in j:                                          # col에 i의 index를 middle_cnt에 넣어준다.
                    middle_cnt = j.index(i)
                if L_H in j:                                        # col의 요소 j에 L_H가 있다면 L_H의 index를 L_cnt에 넣어준다.
                    L_cnt = j.index(L_H)
                if R_H in j:                                        # col의 요소 j에 R_H가 있다면 R_H의 index를 R_cnt에 넣어준다.
                    R_cnt = j.index(R_H)

            if L_H in col_mid and R_H not in col_mid:               # 왼손이 가운데 키패드에 있을 경우
                for k in row:
                    if L_H in k:
                        if col_mid.index(i) > col_mid.index(L_H):
                            L_cnt += 1
                        else:
                            L_cnt -= 1

            if R_H in col_mid and L_H not in col_mid:               # 오른손이 가운데 키패드에 있을 경우
                for k in row:
                    if R_H in k:
                        if col_mid.index(i) > col_mid.index(R_H):
                            R_cnt += 1
                        else:
                            R_cnt -= 1

            a = abs(middle_cnt-L_cnt)                               # 거리계산
            b = abs(middle_cnt-R_cnt)

            if a == b:                                              # 거리가 같을 때
                answer += hand
                if hand == 'L':
                    L_H = i
                else:
                    R_H = i

            elif a > b:                                             # 오른손이 가까울 때
                answer += 'R'
                R_H = i

            else:                                                   # 왼손이 가까울 때
                answer += 'L'
                L_H = i
    return answer