import sys
input = sys.stdin.readline

n = int(input())
chickens = list(map(int,input().split()))
k = n//int(input())                                     # n//k 개씩 끊어서 저장하는 규칙 있음
                                                        # 8//2 -> 1 5 2 4, 2 9 7 3
res = []
def div(chickens,n):
    if n <= 2:
        return sorted(chickens)
    else:
        n //= 2
        res = div(chickens[:n],n) + div(chickens[n:],n)

        if n == k:
            print(*res)

        return sorted(res)
div(chickens,n)
#           1 5 2 4 2 9 7 3                     -> N=8, k=1 div(chickens[:4],4) + div(chickens[4:],4)
#   1 5 2 4,                2 9 7 3             -> N=4, k=2 div(chickens[:2],2) + div(chickens[2:],2)
# 1 2,      4 5,        2 3,        9 7         -> N=2, k=4 (n <= 2 return sorted(chickens)) * 4번 실행  -> 4개 씩 짝지어 return
#   1 2 4 5,                2 3 7 9             -> N=4, k=2 if 4 == 4 (k = n//int(input())              -> pront(*res)