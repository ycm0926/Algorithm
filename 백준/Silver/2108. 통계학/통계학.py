import sys

array = []
input = sys.stdin.readline
n = int(input())
for _ in range(n):
    array.append(int(input()))
# 1
print(round(sum(array)/len(array)))
# 2
array.sort()
print(array[len(array)//2])
# 3
dic = {}
max_dic = []
for i in array:
    if i not in dic:
        dic[i] = 1
    else:
        dic[i] = dic[i]+1
for k, v in dic.items():
    if v == max(dic.values()):
        max_dic.append(k)
if len(max_dic) >= 2:
    print(max_dic[1])
else:
    print(max_dic[0])
# 4
print(array[-1]-array[0])
