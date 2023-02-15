def solution(s):
    answer = []
    for i in s:
        answer.append(i)
        if len(answer) > 1 and answer[-1] == answer[-2]:
            del answer[-2:]
    if answer:
        return 0
    else:
        return 1