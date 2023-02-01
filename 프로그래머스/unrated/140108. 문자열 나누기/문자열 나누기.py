def solution(s):
    cnt_1 = 1                                     # 시작 글자 개수
    cnt_2 = 0                                     # 다른 글자 개수
    start = s[0]                                    # 시작 글자
    temp = s[0]                                     # 문자열 모음

    ans = []

    for i in range(1,len(s)-1):
        temp += s[i]                                # 단어 추가
        if start == s[i]:                           # 단어가 시작 단어와 같다면 시작 글자 카운트 증가
            cnt_1 += 1
        if start != s[i] and cnt_1 > cnt_2:         # 단어가 시작 단어와 다르고, 시작 글자 개수가 크다면
            cnt_2 += 1                              # 다른 글자 카운트 증가
        if start != s[i] and cnt_1 <= cnt_2:        # 단어가 시작 단어와 다르고, 시작 글자 개수가 같거나 크다면
            ans.append(temp)                        # temp에 있는것들을 ans에 넣어준다.
            cnt_1 = 0                               # 시작 글자와 다른 글자 개수 초기화
            cnt_2 = 0
            start = s[i+1]                          # 시작 글자 변경 후, 반복
            temp = ""                               # 문자열 모음 초기화

    if temp:                                        # temp에 값이 남았다면, s[-1]과 함께 추가 
        ans.append(temp+s[-1])  
    else:                                           # 남지 않았다면, s[-1]만 추가
        ans.append(s[-1])    
        
    return len(ans)