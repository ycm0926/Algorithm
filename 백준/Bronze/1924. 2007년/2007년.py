x, y = map(int, input().split())

dic = {0:'SUN', 1:'MON', 2:'TUE', 3:'WED', 4:'THU', 5:'FRI', 6:'SAT'}

'''
31 28 31 30 31 30 31 31
'''
cnt = 0
for i in range(1, x):
    if i == 4 or i == 6 or i == 9 or i == 11:
        cnt += 30
    elif i == 2:
        cnt += 28
    else:
        cnt += 31
cnt += y
if x == 1:
    print(dic[y % 7])
else:
    print(dic[cnt % 7])
