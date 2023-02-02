def solution(s, skip, index):
    answer = ""
    skip_ord = [i-97 for i in list(map(ord, skip))]     # skip 값 변환
    print(skip_ord)
    for i in s:
        i_o = ord(i)-97
        cnt = 0
        while cnt != index:
            i_o = i_o+1
            if i_o >= 26:
                i_o %= 26
            if i_o not in skip_ord:
                cnt += 1

        answer += chr(i_o+97)

    return answer