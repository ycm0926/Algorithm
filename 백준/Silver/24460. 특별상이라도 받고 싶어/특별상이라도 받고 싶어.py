import sys

N = int(input())

input = sys.stdin.readline
chair = [list(map(int, input().split())) for i in range(N)]
def div(row,col,n):
    if n == 1:
        return chair[row][col]

    else:
        n //= 2
        temp = [div(row, col, n),div(row + n, col, n),div(row, col + n, n),div(row + n, col + n, n)]

        return sorted(temp)[1]

print(div(0,0,N))