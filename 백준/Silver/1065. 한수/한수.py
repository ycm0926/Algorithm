n = int(input())
dum, cnt, res = 0, 0, 0
for i in range(1,n+1):
    if len(str(i)) == 1 or len(str(i)) == 2:    # 길이가 1 or 2면 한수이므로, 바로 res += 1
        res += 1
    else:
        dum = list(map(int,str(i)))             # 숫자를 떼서 리스트를 만듦
        cnt = dum[0] - dum[1]                   # 첫 등차수열 값
        for j in range(1,len(dum)-1):           # 두 번째 값부터 등차수열만큼 증가하는지 비교
            if cnt == dum[j] - dum[j+1]:
                res += 1
print(res)