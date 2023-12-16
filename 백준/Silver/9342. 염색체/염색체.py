T = int(input())

test = ['A', 'B', 'C', 'D', 'E', 'F']

for i in range(T):
    chro = input()

    if len(chro) < 3 or chro[0] not in test or chro[-1] not in test:
        print('Good')
        continue

    # 0번째가 A가 아니고 1부터 A가 나오는 경우
    if chro[0] != 'A':
        j = 1
        while j < len(chro)-2 and chro[j] == 'A':
            j += 1
        while j < len(chro)-1 and chro[j] == 'F':
            j += 1
        while j < len(chro) and chro[j] == 'C':
            j += 1

    # 0번째가 A가 나오는 경우
    elif chro[0] == 'A' :
        j = 0
        while j < len(chro)-2 and chro[j] == 'A':
            j += 1
        while j < len(chro)-1 and chro[j] == 'F':
            j += 1

        while j < len(chro) and chro[j] == 'C':
            j += 1

    if j == len(chro):
        print('Infected!')
    else:
        print('Good')