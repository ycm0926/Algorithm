def solution(ingredient):
    answer = 0
    jungsangsu = []

    for i in ingredient:
        jungsangsu.append(i)

        if jungsangsu[-4:] == [1, 2, 3, 1]:
            del jungsangsu[-4:]
            answer += 1

    return answer