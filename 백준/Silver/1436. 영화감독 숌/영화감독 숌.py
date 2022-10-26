n = int(input())

cnt = 0
num = 0
while 1:
    num += 1
    if "666" in str(num):
        cnt +=1
    if cnt == n:
        break
print(num)
