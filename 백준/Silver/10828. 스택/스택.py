import sys

array = []
for _ in range(int(input())):
    i = sys.stdin.readline().split()
    if i[0] == 'push':
        array.append(i[1])
    elif i[0] == 'pop':
        if array:
            print(array.pop())
        else:
            print(-1)
    elif i[0] == 'size':
        print(len(array))
    elif i[0] == 'empty':
        if array:
            print(0)
        else:
            print(1)
    elif i[0] == 'top':
        if array:
            print(array[-1])
        else:
            print(-1)
