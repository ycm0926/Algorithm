def solution(dartResult):
    ans = []
    for i in range(len(dartResult)):
        idx1 = dartResult[i]
        idx2 = dartResult[i-1]
        if idx2 == '0' and dartResult[i-2] == '1':         # i-1,i-2 값이 10인 경우
            idx2 = 10
        if not idx1.isdigit():                             # 숫자가 아닌 경우
            if idx1 == 'S':
                ans.append(int(idx2))
            elif idx1 == 'D':
                ans.append(int(idx2)**2)
            elif idx1 == 'T':
                ans.append(int(idx2)**3)
            elif idx1 == '*':
                if len(ans) <2:
                    ans[0] *=2
                else:
                    ans[-1] *= 2
                    ans[-2] *= 2
            else:
                ans[-1] *= -1

    return sum(ans)