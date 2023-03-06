from math import floor
def solution(str1, str2):
    str1, str2 = str1.upper(), str2.upper() # 문자열 전부 대문자로 변경
    l_str1, l_str2 = [], []                 # 두 글자씩 끊은 문자열 집합들
    i_cnt, s_cnt = 0, 0                     # 다중교집합, 다중합집합 
        
    for i in range(len(str1)):
        if str1[i:i+2].isalpha() and len(str1[i:i+2]) == 2:
            l_str1.append(str1[i:i+2])
        
    for i in range(len(str2)):
        if str2[i:i+2].isalpha() and len(str2[i:i+2]) == 2:
            l_str2.append(str2[i:i+2])
            
    if not l_str1 and not l_str2:                               # 집합 A와 집합 B가 모두 공집합일 경우
        return 65536
    elif (not l_str1 and l_str2) or (l_str1 and not l_str2):    # 공집합은 없지만 합집합은 존재할 경우
        return 0
    else:
        tmp = set(set(l_str1)|set(l_str2))                      # 집합 A와 집합 B의 합집합
        for i in tmp:                                           # 다중교집합, 다중합집합 진행
            # 다중교집합
            if i in l_str1 and i in l_str2:
                i_cnt += min(l_str1.count(i),l_str2.count(i))

            # 다중합집합        
            if i in tmp:
                s_cnt += max(l_str1.count(i),l_str2.count(i))     
                
        return floor(i_cnt/s_cnt*65536)
    
    
