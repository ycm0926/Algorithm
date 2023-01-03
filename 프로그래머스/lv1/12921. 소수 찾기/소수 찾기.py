def solution(n):
    res = 0
    for i in range(2,n+1):                      # 2부터 n까지 소수 찾기
        cnt = False                             # 소수 체크
        for j in range(2,int(i**0.5)+1):        # 제곱근 까지 순회
            if i % j == 0:
                cnt = True                      # 소수가 아니라면 True
                break
        if cnt == False:                        # False이면 소수이므로 res + 1
            res += 1
    return res