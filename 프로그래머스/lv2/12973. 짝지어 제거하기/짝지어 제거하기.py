def solution(s):
    answer = [s[0]]
    for i in s[1:]:             
        if answer and answer[-1] == i:
            answer.pop()
        else:
            answer.append(i)
    if answer:
        return 0
    else:
        return 1