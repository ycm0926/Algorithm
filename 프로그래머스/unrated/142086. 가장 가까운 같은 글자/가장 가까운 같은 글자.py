def solution(s):
    temp = []
    ans = []

    for i in range(len(s)):
        if s[i] not in temp:
            ans.append(-1)
        else:
            idx = 1
            for j in temp[::-1]:
                if s[i] == j:
                    ans.append(idx)
                    break
                idx += 1
        temp.append(s[i])

    return ans