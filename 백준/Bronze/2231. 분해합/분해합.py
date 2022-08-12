import sys

# 보통 브루트 포스의 문제의 범위는 1,000,000으로 주어지는 경우가 많다.
N = int(sys.stdin.readline().strip())
for i in range(1, N+1):
    arr = list(map(int, str(i)))  # str 변환하여 숫자를 하나씩 분리하여 int 리스트에 넣음
    result = i + sum(arr)  # arr 값들을 더하고 i를 더함
    if result == N:  # 결과가 N과 같으면 출력 후 멈춤
        print(i)
        break
else:  # 생성자가 없는 경우
    print(0)
    