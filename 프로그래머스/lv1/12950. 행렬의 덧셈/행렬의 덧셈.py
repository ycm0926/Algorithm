def solution(arr1, arr2):
    res = []
    for a,b in zip(arr1,arr2):
        res.append([x+y for x,y in zip(a, b)])
    return res