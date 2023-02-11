def solution(s):
    answer = ''
    a = sorted(list(map(int,s.split())))
    answer += str(a[0])+' '+str(a[-1])
    return answer