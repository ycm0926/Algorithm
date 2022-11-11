'''
1이 들어오면 다음 값 만큼 거리 증가
2가 들어오면 다음 값 만큼 거리 감소
스피드 == 거리
문제에 설명이 부족하다.
'''
t = int(input())

for i in range(1, t+1):
    tc = int(input())
    spd = 0
    dis = 0
    for j in range(tc):
        c = list(map(int, input().split()))

        if c[0] == 1:
            spd += c[1]
        elif c[0] == 2:
            spd -= c[1]
            if spd < 0:
                spd = 0

        dis += spd

    print(f'#{i} {dis}')
