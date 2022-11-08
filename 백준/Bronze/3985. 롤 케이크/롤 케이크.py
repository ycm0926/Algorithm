import sys

input = sys.stdin.readline
l = int(input())
n = int(input())
predict_1, predict_2 = [], []
total_1, total_2 = [], []

def compare(list, max):
    ans = []
    for a, b in list:
        if a == max:  # max와 같은 값들을 넣어줌
            ans.append(b)
    ans.sort()  # 가장 큰 차이를 보내는 값들을 정렬
    return ans[0]  # 가장 많은 양을 가지면서 빠른 방청객

for i in range(1, n+1):
    p, k = map(int, input().split())
    predict_1.append([k-p, i])
    total_3 = []
    for j in range(p, k+1):
        if j not in total_2:
            total_2.append(j)
            total_3.append(j)
    total_1.append([len(total_3), i])

max_p = max(predict_1)[0]  # 예측 가장 큰 차이를 가지는 값
max_t = max(total_1)[0] # 실제 가장 큰 값을 가지는 값

print(compare(predict_1, max_p))
print(compare(total_1, max_t))
