def solution(today, terms, privacies):
    answer = []
    today = int(today.replace('.',''))                          # today값 int로 변경
    terms_dict = {}                                             # 약관 유효기간 딕셔너리
    
    for i in terms:                     
        a,b = i.split()
        terms_dict[a] = int(b)
    
    for i in range(len(privacies)):
        temp = 0
        a,b = privacies[i].split()                              # 개인정보의 수집 일자와 약관 종류 분리
        c = int(a[5:7])+terms_dict[b]                           # 개인정보의 달에 유효기간 달을 더해준다.
        
        q,r = divmod(c, 12)                                     # divmod로 12의 몫과 나머지를 구한다. 년도가 바뀌는지 확인을 위함.
        
        if q != 0 and r == 0:                                   # c의 값이 12인 경우 (1,0)이 아닌 (0,12)로 교체
            q -= 1
            r = 12

        if r < 10:                                              # 나머지가 10보다 작다면 0을 붙여 자리를 맞춘다.
            r = '0'+str(r)
        else: 
            r = str(r)

        if q == 0:                                              # 몫이 0인 경우, 년도가 바뀌지 않는다. -> 개인정보의 달 값만 바꿔서 비교
            a_int = int((a[:5]+r+a[7:]).replace('.',''))        # 슬라이싱과 repalce를 통해 개인정보 int 값을 만든다.
            
            if a_int <= today:                                  # 유효기간 지났다면 파기
                answer.append(i+1)
        
        else:                                                   # 몫이 0이 아닌경우, 년도가 바뀐다.
            year = str(int(a[:4])+q)                            # 년도 변경
            a_int = int((year+r+a[7:]).replace('.',''))
            if a_int <= today:
                answer.append(i+1)

    return answer