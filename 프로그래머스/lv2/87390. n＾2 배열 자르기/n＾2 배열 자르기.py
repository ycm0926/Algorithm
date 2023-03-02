def solution(n, left, right):
    answer = []
    for i in range(left,right+1):
        q,r = divmod(i,n)           # 몫과 나머지 구하기
        if q<r:                     # 큰값 q로 초기화
            q,r = r,q  
        answer.append(q+1)
    return answer