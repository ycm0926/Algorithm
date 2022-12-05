import sys
if __name__ == '__main__':
    N, M = map(int, input().split())
    numbers = list(map(int,input().split()))
    for i in range(1, N):
        numbers[i] = numbers[i] + numbers[i-1]

    for _ in range(M):
        start, end = map(int, sys.stdin.readline().split())
        if start == 1:
            print(numbers[end-1])
        else:
            print(numbers[end-1]-numbers[start-2])