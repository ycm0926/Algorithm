for tc in range(1, 11):
    input()
    graph = [list(map(int, input().split())) for _ in range(100)]
    res = 0
    for i in range(100):
        check = False
        for j in range(100):
            if graph[j][i] == 1:
                check = True
            if check == True and graph[j][i] == 2: # 1을 발견하고 2를 발견 시
                res += 1
                check = False
    print(f'#{tc} {res}')
    