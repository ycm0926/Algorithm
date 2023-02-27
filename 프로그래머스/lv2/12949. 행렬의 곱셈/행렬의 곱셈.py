def solution(arr1, arr2):
    answer = []

    for i in range(len(arr1)):
        tmp1 = []
        for j in range(len(arr2[0])):
            tmp2 = []
            for k in range(len(arr2)):
                tmp2.append(arr1[i][k]*arr2[k][j])
            tmp1.append(sum(tmp2))
        answer.append(tmp1)
        
    return answer




