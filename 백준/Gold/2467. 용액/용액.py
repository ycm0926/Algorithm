import sys
input = sys.stdin.readline

n = int(input())
solutions = list(map(int,input().split()))

INF = int(1e10)
min_slo = INF
end = n - 1

for i in range(n-1):                                # 첫 번째 값 i 이후의 값을 start로 시작
    start = i + 1

    while start <= end:
        mid = (start+end)//2
        sol = solutions[i] + solutions[mid]         # i와 mid 값을 더해서 비교

        if abs(sol) < min_slo:
            min_slo = abs(sol)
            idx1, idx2 = i, mid

        if sol < 0:
            start = mid + 1
        else:
            end = mid - 1

print(solutions[idx1],solutions[idx2])