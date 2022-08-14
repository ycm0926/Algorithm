n, m = map(int, input().split())
card = list(map(int, input().split()))
max_card = 0

for i in range(n):  # 3중 for 문을 이용하여 더해줌
    for j in range(i+1, n):
        for k in range(j+1, n):
            if card[i] + card[j] + card[k] <= m:
                max_card = max(max_card, card[i] + card[j] + card[k])
            else:
                continue

print(max_card)
