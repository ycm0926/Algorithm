import sys

while True:
    arr = list(map(int, sys.stdin.readline().rstrip()))
    arr2 = list(reversed(arr))
    if sum(arr) == 0:
        break
    elif arr == arr2:
        print('yes')
    else:
        print('no')
