arr = [[0 for i in range(101)] for j in range(101)]
count = 0

for i in range(4):
    x, y, w, h = map(int, input().split())

    for row in range(x, w):
        for cal in range(y, h):
            arr[row][cal] = 1

for row in arr:
    count += sum(row)
print(count)