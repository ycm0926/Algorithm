import sys

cnt = [0] * 10001

for _ in range(int(sys.stdin.readline())):
    cnt[int(sys.stdin.readline())] += 1

for i in range(10001):  # 리스트에 기록된 정렬 점보 확인
    for _ in range(cnt[i]):
        print(i)