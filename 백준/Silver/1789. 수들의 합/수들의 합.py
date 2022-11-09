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
n = int(input())
arr = []
total = 0
i = 1
while 1:
    total += i
    if total == n:
        print(len(arr)+1)
        break
    elif total > n:
        total -= 2*i-1
        arr.pop()
        continue
    arr.append(i)
    i += 1
