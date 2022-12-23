d = [0]*21
d[0] = 0
d[1] = 1
d[2] = 1
for i in range(3,21):
    d[i] = d[i-1]+d[i-2]
print(d[int(input())])