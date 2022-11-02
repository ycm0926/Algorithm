import sys

input = sys.stdin.readline
a = []
for i in range(10):
    a.append(int(input()))
    if sum(a) == 100:
        print(100)
        break
    elif sum(a) > 100:
        b = sum(a)
        a.pop()
        c = sum(a)
        if b - 100 <= 100 - c:
            print(b)
            break
        else:
            print(c)
            break
    elif i == 9:
        print(sum(a))
