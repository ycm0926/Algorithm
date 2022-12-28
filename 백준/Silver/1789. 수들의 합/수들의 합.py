S = int(input())
res = 0
if S == 1:
    print(1)
else:
    for i in range(1,S+1):
        res += i
        if res > S:
            print(i-1)
            break
