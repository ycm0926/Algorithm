'''
A사 : 1리터당 P원의 돈을 내야 한다.
B사 : 기본 요금이 Q원이고, 월간 사용량이 R리터 이하인 경우
요금은 기본 요금만 청구된다. 하지만 R 리터보다 많은 양을
사용한 경우 초과량에 대해 1리터당 S원의 요금을 더 내야 한다.
종민이의 집에서 한 달간 사용하는 수도의 양이 W리터라고 할 때,
요금이 더 저렴한 회사를 골라 그 요금을 출력하는 프로그램을 작성하라.

for tc in range(1, int(input())+1):
    n = int(input())
    numbers = [0] *10
    i = 1
    while 0 in numbers:
        print(numbers)
        num = str(n*i)
        for j in range(len(num)):
            numbers[int(num[j])] += 1
        i += 1
    print(f'#{tc} {num}')

'''
t = int(input())
for i in range(1, t+1):
    n = int(input())
    case = n
    idx = 1
    ans = []
    while 1:
        case = n*idx
        word = list(map(str, str(case)))
        for j in word:
            if j not in ans:
                ans.append(j)
        if len(ans) == 10:
            print(f'#{i} {case}')
            break
        idx += 1

