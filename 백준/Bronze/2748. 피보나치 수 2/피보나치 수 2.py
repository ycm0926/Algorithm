# 나의 풀이

n = int(input())
dp = [0,1]
for i in range(2,n+1): # 바텀 업 반복문
    dp.append(dp[i-1]+dp[i-2])
print(dp[n])

'''
# 다른 사람 풀이

def fibonacci(n, f_dict): # 탑 다운 재귀
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif f_dict.get(n):
        return f_dict[n]

    f_dict[n] = fibonacci(n - 1, f_dict) + fibonacci(n - 2, f_dict)

    return f_dict[n]


N, f_dict = int(input()), {}
print(fibonacci(N, f_dict))

# 다른 사람 풀이2

cur, next = 0, 1
for _ in range(int(input())):
	cur, next = next, next + cur
print(cur)

TIL/회고
- 다른 사람 풀이들도 비슷했다. 피보나치 -> 기본적인 DP구현
- 풀이 2는 값 하나만 구할 때엔 좋은 코드인 것 같다.
'''