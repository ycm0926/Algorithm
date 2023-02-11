def solution(s):
    answer = ''
    s = s.lower().split(' ')
    for i in range(len(s)):
        answer += s[i][:1].upper() + s[i][1:] + ' '

    return answer[:-1]