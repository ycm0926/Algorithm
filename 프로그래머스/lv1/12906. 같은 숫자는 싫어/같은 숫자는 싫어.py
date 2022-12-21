def solution(arr):
    res = [arr[0]]          # arr의 첫 번째 값을 res에 넣어준다. 
    for i in arr[1:]:       # arr의 두 번째 값부터 받음
        if res[-1] != i:    # res의 마지막 값이 i와 다르다면 append해준다.
            res.append(i)
    return res