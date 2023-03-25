def solution(n, t, m, p):
    change = {10 : 'A', 11 : 'B', 12 : 'C', 13 : 'D', 14 : 'E', 15 : 'F'}
    answer = '01'
    num = 2
    
    while len(answer) < t*m:            # 미리 구할 숫자의 갯수 * 임에 참가하는 인원 ex) 4*2
        nums = ""                       # 진수변환 값 담기위한 변수
        idx = num                       # 다음 숫자 초기화
        
        while idx > 0:                  # 진수 변환
            q,r = divmod(idx,n)
            idx = q
            if r in change:
                nums += str(change[r])
            else:
                nums += str(r)
                
        nums = nums[::-1]               # 진수 뒤집기
        num += 1                        # 숫자 증가
        answer += nums
        
    return answer[p-1:t*m:m]