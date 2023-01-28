def solution(board, moves):
    answer = []
    cnt = 0
    l_board = len(board[0])
    for m in moves:                                                 # 크레인 이동 시작
        if board[-1][m - 1] == 0:                                   # 인형이 없는 경우 중단
            continue
        for l in range(l_board):                                    # 인형뽑기 기계 탐색
            if board[l][m-1] != 0:                                  # 0이 아닌 숫자를 만나면 바구니에 넣기
                answer.append(board[l][m-1])
                board[l][m-1] = 0                                   # 인형 자리 0으로 교체

                if len(answer) > 1 and answer[-1] == answer[-2]:    # 바구니 위의 인형이 같다면 제거 하고 카운트
                    answer.pop()
                    answer.pop()
                    cnt += 2

                break
    return cnt