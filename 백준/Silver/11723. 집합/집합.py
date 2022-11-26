import sys

input = sys.stdin.readline
res = []

for _ in range(int(input())):
    M = input().split()
    if not M[0] == 'all' and not M[0] == 'empty':
        m = int(M[1])
    if M[0] == 'add':
        if m not in res:
            res.append(m)
    elif M[0] == 'remove':
        if m in res:
            res.remove(m)
    elif M[0] == 'check':
        if m in res:
            print(1)
        else:
            print(0)
    elif M[0] == 'toggle':
        if m in res:
            res.remove(m)
        else:
            res.append(m)
    elif M[0] == 'all':
        res = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21]
    elif M[0] == 'empty':
        res = []

'''
TIL/회고
- 순서대로 구현하면서 all과 empty은 추가적인 작업
- all은 for반복문 대신 리스트 바로 초기화
'''