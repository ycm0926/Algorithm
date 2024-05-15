T = int(input())

for test_case in range(1, T + 1):

    print(f"#{test_case}")
    ans = ""
    for i in range(int(input())):
        a, b = input().split()
        b = int(b)
        ans += a*b

    for i in range(0,len(ans),10):
        print(ans[i:i+10])