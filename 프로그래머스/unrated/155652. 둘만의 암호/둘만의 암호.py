def solution(s, skip, index):
    answer = ""
    skip_ord = [i-97 for i in list(map(ord, skip))]     # skip 값 변환
    for i in s:                                         # 문자열 s에서 하나씩 가져온다.
        i_o = ord(i)-97                                 # i_o의 범위는 0~25  
        cnt = 0                                         # 이동 카운트 변수
        while cnt != index:                             # cnt가 index와 같을 때까지 반복
            i_o = i_o+1                                 # i_o를 i_o+1로 초기화 -> 알파벳 하나씩 이동
            if i_o >= 26:                               # i_o가 26을 넘는다면 %연산으로 0~25범위로
                i_o %= 26
            if i_o not in skip_ord:                     # i_o가 skip에 없다면 cnt 증가
                cnt += 1

        answer += chr(i_o+97)                           # 알파벳으로 변환

    return answer