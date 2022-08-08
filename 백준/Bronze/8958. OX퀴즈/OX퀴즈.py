A = int(input())

for _ in range(A):
    n = input()
    cnt = 0
    ans = 0
    for i in n:
        if i == 'O':
            cnt += 1
            ans += cnt
        else :
            cnt = 0
    print(ans)