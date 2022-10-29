N = int(input())
arr = [[0] * 101 for j in range(101)]

for i in range(N):
    x, y = map(int, input().split())

    for row in range(x, x+10):
        for cal in range(y, y+10):
            arr[row][cal] = 1
count = 0
for row in arr:
    count += row.count(1)
print(count)