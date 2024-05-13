T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    puzzle = [list(map(int, input().split())) for i in range(9)]
    ans = 1

    # 가로
    for i in puzzle:
        if len(set(i)) < 9:
            ans = 0
            print(f"#{test_case} 0")
            break
    if ans == 0:
        continue

    # 세로
    for i in range(9):
        tmp = set()
        for j in range(9):
            tmp.add(puzzle[j][i])

        if len(tmp) < 9:
            ans = 0
            print(f"#{test_case} 0")
            break

    if ans == 0:
        continue

    # 3*3
    for i in range(0,7,3):
        tmp = set()
        for j in range(0,7,3):
            tmp.update([puzzle[i][j], puzzle[i][j+1], puzzle[i][j+2]])
            tmp.update([puzzle[i+1][j], puzzle[i+1][j+1], puzzle[i+1][j+2]])
            tmp.update([puzzle[i+2][j], puzzle[i+2][j+1], puzzle[i+2][j+2]])
            if len(tmp) < 9:
                ans = 0
                print(f"#{test_case} 0")
                break
        if ans == 0:
            break

    if ans == 0:
        continue

    print(f"#{test_case} 1")
