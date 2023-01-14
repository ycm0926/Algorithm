def solution(t, p):
    ans = 0
    idx1 = 0
    idx2 = len(p)
    while 1:
        if idx2 > len(t):                # idx2가 t의 길이보다 커지면 종료
            break

        if int(t[idx1:idx2]) <= int(p):  # 슬라이싱한 t의 수가 p보다 작다면 카운트
            ans += 1
        idx1 += 1                        # 슬라이싱 좌표 이동
        idx2 += 1
    return ans