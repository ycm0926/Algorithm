def solution(elements):
    answer = set()
    for i in range(len(elements)):
        tmp = elements[i]
        answer.add(elements[i])

        for j in range(i+1,len(elements)+i):
            tmp += elements[j%len(elements)]
            answer.add(tmp)
            
    return len(answer)