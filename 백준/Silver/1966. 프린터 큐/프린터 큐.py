import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, m = map(int, input().split())
    q = list(map(int, input().split()))
    q = [[idx, value] for idx, value in enumerate(q)]  # index와 값 분리
    cnt = 0
    while 1:
        if q[0][1] == max(q, key=lambda x: x[1])[1]:  # 값으로 정렬한 값이 첫번째에 있는지 확인
            cnt += 1  # 몇 번째에 출력이 되는지 확인을 위함
            if q[0][0] == m:
                print(cnt)
                break
            else:
                q.pop(0)
        else:
            q.append(q.pop(0))