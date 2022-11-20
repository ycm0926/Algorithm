N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
A.sort()
B.sort(reverse=True)
res = 0
for i in range(N):
    res += A[i]*B[i]
print(res)
'''
TIL/회고
- 문제를 최대한 분석해서 쉽게 풀어보자.
'''