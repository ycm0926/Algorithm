import sys

input = sys.stdin.readline
while 1:
    lst = list(map(int,input().strip()))
    lst2 = list(reversed(lst))
    if sum(lst) == 0:
        break
    elif lst == lst2:
        print('yes')
    else:
        print('no')
'''
import sys

input = sys.stdin.readline
while 1:
    lst = list(map(int, input().strip()))
    lst_l = len(lst)
    cnt = 0
    if lst[0] == 0 and lst_l == 1:
        break
    for i in range(lst_l):
        if lst[i] == lst[-i-1]:
            cnt += 1
            if cnt == lst_l//2:
                print('yes')
                break
        else:
            print('no')
            break
'''