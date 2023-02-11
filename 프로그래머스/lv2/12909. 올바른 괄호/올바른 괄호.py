def solution(s):
    answer = []
    for i in range(len(s)):
        answer.append(s[i])
        if len(answer) >= 2 and answer[-1] == ')' and answer[-2] == '(':
            del answer[-2:]

    if answer:
        return False
    else:
        return True