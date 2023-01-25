def solution(numbers, hand):
    col = [[1,4,7,'*'],[2,5,8,0],[3,6,9,'#']]
    row = [[1,2,3],[4,5,6],[7,8,9],['*',0,'#']]
    col_mid = [2,5,8,0]
    if hand == "right":
        hand = 'R'
    if hand == "left":
        hand = 'L'
    answer = ''
    L_H = '*'
    R_H = '#'

    for i in numbers:

        if L_H == i:
            answer += 'L'
        elif R_H == i:
            answer += 'R'
        elif i == 1 or i == 4 or i == 7:
            answer += 'L'
            L_H = i
        elif i == 3 or i == 6 or i == 9:
            answer += 'R'
            R_H = i
        else:
            for j in col:
                if i in j:
                    middle_cnt = j.index(i)
                if L_H in j:
                    L_cnt = j.index(L_H)
                if R_H in j:
                    R_cnt = j.index(R_H)

            if L_H in col_mid and R_H not in col_mid:
                for k in row:
                    if L_H in k:
                        if col_mid.index(i) > col_mid.index(L_H):
                            L_cnt += 1
                        else:
                            L_cnt -= 1

            if R_H in col_mid and L_H not in col_mid:
                for k in row:
                    if R_H in k:
                        if col_mid.index(i) > col_mid.index(R_H):
                            R_cnt += 1
                        else:
                            R_cnt -= 1

            a = abs(middle_cnt-L_cnt)
            b = abs(middle_cnt-R_cnt)

            if a == b:
                answer += hand
                if hand == 'L':
                    L_H = i
                else:
                    R_H = i

            elif a > b:
                answer += 'R'
                R_H = i

            else:
                answer += 'L'
                L_H = i
    return answer