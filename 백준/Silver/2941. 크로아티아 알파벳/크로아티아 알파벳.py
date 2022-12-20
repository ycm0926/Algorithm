dict = {'c=':1, 'c-':1, 'dz=':1, 'd-':1, 'lj':1, 'nj':1, 's=':1, 'z=':1}

cro = input()
cnt,i,j = 0,0,2
while i <= len(cro)-1:          # 반복문 중지 조건
    if cro[i:j] in dict:        # 문자열 슬라이싱으로 크로티아 알파벳 파악
        cnt += dict[cro[i:j]]
        i += 2
        j += 2
    elif cro[i:j+1] in dict:    # dz=일 경우
        cnt += dict[cro[i:j+1]]
        i += 3
        j += 3
    else:                       # dict안에 없는 경우
        cnt += 1
        i += 1
        j += 1

print(cnt)