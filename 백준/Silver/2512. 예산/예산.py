import sys

input = sys.stdin.readline

N = int(input())
moneys = list(map(int,input().split()))
n_b= int(input())

start = 1
end = max(moneys)
if sum(moneys) <= n_b:
    print(max(moneys))
    exit(0)
else:
    while start <= end:
        total = 0
        mid = (start+end)//2

        for i in moneys:
            if i > mid:
                total += mid
            else:
                total += i
        if total <= n_b:
            start = mid + 1
        else:
            end = mid - 1

print(end)