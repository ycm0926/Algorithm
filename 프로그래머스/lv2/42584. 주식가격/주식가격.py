def solution(prices):
    answer = []
    for i in range(len(prices)-1):
        tmp = 0
        for j in range(i+1,len(prices)):
            tmp += 1
            if prices[i] > prices[j]:
                answer.append(tmp)
                break
        else:
            answer.append(tmp)
    answer.append(0)
    return answer