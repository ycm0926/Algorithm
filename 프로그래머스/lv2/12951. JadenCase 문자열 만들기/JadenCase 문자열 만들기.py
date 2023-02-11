def solution(s):
    jc = s.split(' ')

    for i in range(len(jc)):
        jc[i] = jc[i].capitalize()

    return ' '.join(jc)