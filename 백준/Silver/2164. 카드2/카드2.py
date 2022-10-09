n = int(input())

card = [i+1 for i in range(n)]
while len(card) > 1: # 입력값이 1이 이상시 반복
    if len(card) % 2: # 카드수가 홀수면
        arr = [card[-1]] # 마지막 카드 보관
        arr.extend(card[1::2]) # 마지칵 카드 뒤로 짝수 카드들 넣어줌
        card = arr # card 갱신
    else: # 카드수가 짝수면 홀수 카드 제거
        card = card[1::2]

print(card[0])
