def solution(ingredient):
    answer = 0
    jungsangsu = []

    for i in ingredient:
        jungsangsu.append(i)

        if len(jungsangsu) >=4 and jungsangsu[-1] == 1 and jungsangsu[-2] == 3 and jungsangsu[-3] == 2 and jungsangsu[-4] == 1:
            del jungsangsu[-4:]
            answer += 1

    return answer