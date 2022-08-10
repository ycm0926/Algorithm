while True:
    arr = list(map(int, input().split()))
    arr.sort()
    if sum(arr) == 0: # 0,0,0 입력시 종료
        break
    elif (arr[0]**2 + arr[1]**2) == arr[2]**2:  # x와 y를 각각 제곱하여 더하여 y와 같을경우 직각삼각형
        print("right")
    else:
        print("wrong")