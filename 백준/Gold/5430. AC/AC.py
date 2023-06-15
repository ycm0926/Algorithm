from collections import deque

# R은 배열에 있는 수의 순서를 뒤집는 함수이고,
# D는 첫 번째 수를 버리는 함수이다.
# 배열이 비어있는데 D를 사용한 경우에는 에러가 발생한다.

for test_case in range(int(input())):
    f = input()
    n = input()
    flag = False

    if n != '0':
        f_list = deque(input()[1:-1].split(','))
    else:
        input()
        f_list = []

    for i in f:
        if i == 'R':
            if flag:
                flag = False
            else:
                flag = True
        elif i == 'D' and f_list:
            if not flag:
                f_list.popleft()
            else:
                f_list.pop()
        else:
            print('error')
            break
    else:
        f_list = list(f_list)
        if flag:
            f_list.reverse()
            print(f"[{','.join(f_list)}]")
        else:
            print(f"[{','.join(f_list)}]")
