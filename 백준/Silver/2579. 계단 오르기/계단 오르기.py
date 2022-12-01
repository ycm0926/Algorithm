import sys
N = int(input())
li = list(map(int,sys.stdin.read().splitlines()))
if len(li) <= 2:        # 계단 개수가 2보다 작으면 모두 더해서 출력
    print(sum(li))
    exit()
d = [0] * N
d[0] = li[0]        # 첫 계단 점수 초기화
d[1] = d[0]+li[1]       # 두 번째 계단 합산 점수 초기화
d[2] = max(li[2]+li[1],li[2]+li[0])     # 세 번째 계단 합산 점수 초기화

for i in range(3,N):       # 바텀 업 (반복문)
    # max(현재의 점수 + 이전 점수 + 3칸전 합산 점수, 현재의 점수 2칸전 합산 점수)
    d[i] = max(li[i] + li[i - 1] + d[i-3], li[i] + d[i - 2])

print(d[-1])
'''
TIL/회고
- 이코테 책을 다시 복습하고 보니 이코테의 개미 전사와 비슷한 문제다.
- 개미 전사에서 살짝 변형되었지만 푸는데 오래 걸렸다....
'''