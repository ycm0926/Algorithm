def solution(today, terms, privacies):
    answer = []
    terms = {i[0]:int(i[2:]) for i in terms}            # terms 딕셔너리
    
    for i, p in enumerate(privacies):                   
        date, kind = p.split(" ")                       # 개인정보 수집일자와 약관 종류 분리
        y, m, d = date.split(".")                       # 개인정보 수집일자 년, 월, 일 분리
        y = int(y) + (int(m)+terms[kind]-1)//12         # 년도 계산
                                                        # 
        m = (int(m)+terms[kind])%12 or 12               # 달 계산
        date = ".".join([f"{y}", f"{m:02}", d])         # 개인정보 수집일자 변경
        
        if today >= date:
            answer.append(i+1)
    
    return answer