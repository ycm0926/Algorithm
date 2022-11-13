# 끝점을 기준
n = input()
for i in range(len(n)):print(n[i]) if i % 10 == 9 else print(n[i], end='')
'''
# 시작점을 기준
for i in range(len(n)):
    if i % 10 == 0:
        j = i + 10
        print(n[i:j])
'''