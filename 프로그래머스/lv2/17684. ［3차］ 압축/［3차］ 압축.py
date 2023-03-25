def solution(msg):
    LZW = {'A':1, 'B':2, 'C':3, 'D':4, 'E':5, 'F':6, 'G':7, 'H':8, 'I':9, 'J':10, 'K':11, 'L':12, 'M':13,
           'N':14, 'O':15, 'P':16, 'Q':17, 'R':18, 'S':19, 'T':20, 'U':21, 'V':22, 'W':23, 'X':24, 'Y':25, 'Z':26}
    answer = []
    idx = 27
    tmp = msg[0]
    for i in msg[1:]:                       
        if tmp in LZW:                      # LZW 사전에 있는지 확인
            tmp += i
        else:                               # 없다면 사전 추가, answer 추가, idx 업데이트, tmp 업데이트
            LZW[tmp] = idx
            idx += 1
            answer.append(LZW[tmp[:-1]])
            tmp = tmp[-1]+i
            
    if tmp:                                 # tmp 값이 남기 때문에 마지막으로 처리
        if tmp in LZW:                      # tmp 값이 LZW에 있다면 
            answer.append(LZW[tmp])
        else:                               # 없다면 마지막 부분 분리해서 answer에 추가
            answer.append(LZW[tmp[:-1]])
            answer.append(LZW[tmp[-1]])
    return answer