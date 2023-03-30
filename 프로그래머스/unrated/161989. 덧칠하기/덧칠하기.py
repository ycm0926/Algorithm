def solution(n, m, section):
    answer = 1
    s = section[0]+m-1
    
    if m == 1:
        return len(section)
    
    for i in section[1:]:
        if s < i:
            answer += 1
            s = i+m-1
    
    return answer