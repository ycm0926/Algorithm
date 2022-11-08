import sys

input = sys.stdin.readline
l = int(input())
n = int(input())
predict_1 = []
predict_2 = []
total_1 = []
total_2 = []
for i in range(1, n+1):
    p, k = map(int, input().split())
    predict_1.append([k-p, i])
    total_3 = []
    for j in range(p, k+1):
        if j not in total_2:
            total_2.append(j)
            total_3.append(j)
    total_1.append([len(total_3), i])

# 1번 많이 받는 것을 예측 하는 방청객
max_p = max(predict_1)[0]  # 예측 가장 큰 차이를 가지는 값
for a, b in predict_1:  # 방청객의 길이 값들 중
    if a == max_p:  # max_l과 같은 값들을 넣어줌
        predict_2.append(b)
predict_2.sort()  # 가장 큰 차이를 보내는 값들을 정렬
print(predict_2[0])  # 가장 많은 양을 가지면서 빠른 방청객

total_3 = []
# 2번 실제 많이 받는 방청객
max_t = max(total_1)[0] # 실제 가장 큰 값을 가지는 값
for a, b in total_1:
    if a == max_t:
        total_3.append(b)
total_3.sort()
print(total_3[0])
