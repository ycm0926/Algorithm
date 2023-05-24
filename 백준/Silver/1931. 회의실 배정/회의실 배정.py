N = int(input())
ans = 1
room = sorted([list(map(int,input().split())) for _ in range(N)], key = lambda x: (x[1], x[0]))
L = len(room)
s, e = room[0][0], room[0][1]

for i in range(1, L):
    if room[i][0] >= e:
        ans += 1
        e = room[i][1]
print(ans)
