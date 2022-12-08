_ = input()
s = set(map(int,input().split()))
_ = int(input())
lis = list(map(int,input().split()))
for i in lis:
    if i in s:     # 상근이가 카드를 가지고 있는지 체크
        print(1, end=' ')
    else:
        print(0, end=' ')