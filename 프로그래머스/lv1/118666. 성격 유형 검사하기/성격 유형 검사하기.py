def solution(survey, choices):
    answer = ''

    li = {1:3, 2:2, 3:1, 4:0, 5:1, 6:2, 7:3}
    cnt = {'R':0, 'T':0, 'C':0, 'F':0, 'J':0, 'M':0, 'A':0, 'N':0}

    for s,c in zip(survey,choices):
        if c == 4:
            continue
        elif c >= 5:
            cnt[s[1]] += li[c]
        else:
            cnt[s[0]] += li[c]
    
    if cnt['R'] >= cnt['T']:
        answer += 'R'
    else:
        answer += 'T'
    
    if cnt['C'] >= cnt['F']:
        answer += 'C'
    else:
        answer += 'F'
    if cnt['J'] >= cnt['M']:
        answer += 'J'
    else:
        answer += 'M'
    if cnt['A'] >= cnt['N']:
        answer += 'A'
    else:
        answer += 'N'

    return answer