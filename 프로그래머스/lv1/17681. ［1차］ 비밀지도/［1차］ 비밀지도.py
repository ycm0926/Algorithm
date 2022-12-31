def solution(n, arr1, arr2):
    arr3 = []
    for a,b in zip(arr1,arr2):
        c = bin(a | b)[2:].replace('1','#').replace('0',' ')
        if len(c) != n:
            arr3.append(((n - len(c)) * ' ') + c)
        else:
            arr3.append(c)
    return arr3
