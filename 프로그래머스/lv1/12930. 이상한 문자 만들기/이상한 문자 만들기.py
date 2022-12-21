def solution(s):
    res = []
    cnt = 0
    for i in range(len(s)):
        if s[i] == " ":
            cnt = 0
            res.append(" ")
            continue
        if cnt % 2 == 0:
            res.append(s[i].upper())
        else:
            res.append(s[i].lower())
        cnt += 1
    return("".join(res))