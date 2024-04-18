def solution(topping):
    answer = 0
    a, b = dict(), dict()

    for i in topping:
        if i not in b:
            b[i] = 1
        else:
            b[i] += 1

    for i in range(len(topping)):
        b[topping[i]] -= 1
        if b[topping[i]] == 0:
            del b[topping[i]]

        if topping[i] not in a:
            a[topping[i]] = 1
        else:
            a[topping[i]] += 1

        if len(a) == len(b):
            answer += 1

    return answer
