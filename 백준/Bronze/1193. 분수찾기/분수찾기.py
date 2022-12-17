X = int(input())

line = 1                    # line 생성
while X > line:             # X의 위치를 찾기 위한 반복 (X가 대각선 line보다 작아지면 중단)
    X -= line               # line에서 몇 번째에 위치하는지
    line += 1               # 몇 번째 line에 위치하는지
if line % 2 == 0:           # line이 짝수일 경우
    a = X
    b = line - X + 1
else:                       # line이 홀수일 경우
    a = line - X + 1
    b = X

print(a, '/', b, sep='')