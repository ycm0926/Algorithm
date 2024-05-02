T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    a, b = map(int,input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    if len(a) > len(b):
        a, b = b, a
    ans = 0

    for i in range(len(b)-len(a)+1):
        tmp = 0
        for j in range(len(a)):
            tmp += a[j]*b[j+i]
        ans = max(ans,tmp)

    print(f"#{test_case} {ans}")