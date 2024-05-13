T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    times = list(map(int, input().split()))
    ans = ""
    # 60분이 넘어가는 경우
    # 12시가 넘어가는 경우

    m = times[1] + times[3]
    h = times[0] + times[2]

    if m >= 60:
        h += 1
        m -= 60

    if h >= 12:
        h -= 12

    print(f"#{test_case} {h} {m}")
