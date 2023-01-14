def solution(lottos, win_nums):

    find_lottos = 0
    cnt_zero = [i for i in lottos if i == 0]                    # zero 개수
    dict = {6:1, 5:2, 4:3, 3:4, 2:5, 1:6, 0:6}                  # 등수 dict
    for i in lottos:                                            # 같은 번호 찾기
        for j in win_nums:
            if i == j:
                find_lottos += 1

    return [dict[find_lottos+len(cnt_zero)],dict[find_lottos]]