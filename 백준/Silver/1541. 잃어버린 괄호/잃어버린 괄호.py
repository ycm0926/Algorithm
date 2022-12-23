arr = input().split('-')        # '-' 기준으로 나눈다
s = 0
for i in arr[0].split('+'):     # arr 첫 번째 값에 '+'가 있다면
    s += int(i)                 # 값들을 서로 더해줘서 첫 번째 값을 얻는다.
for i in arr[1:]:               # 두번째 값 부터 시작
    for j in i.split('+'):      # i에 '+'가 있다면 j로 하나씩 받아서 첫 번째 값 s에 모두 빼준다.
        s -= int(j)
print(s)
