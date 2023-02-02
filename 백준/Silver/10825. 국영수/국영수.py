import sys

input = sys.stdin.readline
res = []
for i in range(int(input())):
    이름, 국어, 영어, 수학 = input().split()
    국어 = int(국어)
    영어 = int(영어)
    수학 = int(수학)
    res.append([국어,영어,수학,이름])

for i in sorted(res, key=lambda x: (-x[0],x[1],-x[2],x[3])):
    print(i[-1])