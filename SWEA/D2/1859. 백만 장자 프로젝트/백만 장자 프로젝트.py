T = int(input())

for tc in range(1, T+1):

    N = int(input())
    price = list(map(int, input().split()))

    cnt = 0
    last_day = price[-1]
    for i in range(N-2, -1, -1):

        if last_day > price[i]: # 뒤부터 보기
            cnt += last_day - price[i]
        else:
            last_day = price[i]

    print(f"#{tc}", cnt)