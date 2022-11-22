n = int(input())
m = n
i = 0
while True:
    # 각 자리를 %10과 //10 으로 분해하여 반복
    m = m % 10 * 10 + (m % 10 + m // 10) % 10
    i += 1
    if m == n:
        break
print(i)