import sys

input = sys.stdin.readline

W, H, X, Y, P = map(int,input().split())
cnt = 0

for i in range(P):
    x, y = map(int,input().split())

    # 직사각형에 있는 경우
    if X <= x <= X+W and Y <= y <= Y+H:
        cnt += 1
    
    # 왼 타원에 있는 경우
    elif ((x-X)**2+(y-(Y+H//2))**2)**0.5 <= H//2:
        cnt += 1

    # 오 타원에 있는 경우
    elif ((x-(W+X))**2+(y-(Y+H//2))**2)**0.5 <= H//2:
        cnt += 1

print(cnt)