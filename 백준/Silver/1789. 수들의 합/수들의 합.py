'''
11
1 1 i=1
3 1,2 i=2
6 1,2,3 i=3
10 1,2,3,4 i=4
15 1,2,3,4,5 i=5
10 1,2,3,4 i=5
6 1,2,3 i=5
11 1,2,3,4,5 i=5
'''
S = int(input())
total = 0
i = 0

while 1:
    i += 1
    total += i
    if total + i+1 > S:
        print(i)
        break
