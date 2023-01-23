import sys

input = sys.stdin.readline
N, K = map(int,input().split())
characters = [int(input()) for i in range(N)]
start = min(characters)                         # start값은 가장 작은값부터
end =  start+K                                  # end는 가장 작은 값에서 K를 더한 값
while start <= end:
    mid = (start+end)//2
    cnt = 0

    for i in characters:                        # 레벨이 mid보다 작다면 차이 만큼 카운트
        if i < mid:
            cnt += mid-i

    if cnt <= K:                                # 카운트 한 값이 K보다 작거나 같다면 start 이동
        start = mid + 1
    else:
        end = mid - 1

print(end)