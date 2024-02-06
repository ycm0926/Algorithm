import sys
from collections import deque

N, K = map(int,input().split())
balt = deque(map(int ,input().split()))
ans = 0
cnt = 0
robot = deque([False]*N)

while 1:
    ans += 1

    #1. 벨트, 로봇 회전 + 로봇 내림
    balt.rotate(1)
    robot.rotate(1)
    robot[N-1] = False
    robot[0] = False

    #2. 먼저 올라간 로봇부터 처리
    for i in range(N-2, 0, -1):

        #2-1 이동하려는 칸 로봇 없고, 내구도 1이상
        if robot[i] == True and robot[i+1] == False and balt[i+1] > 0:
            robot[i], robot[i+1] = False, True
            balt[i+1] -= 1

            # 0이 되는 개수 
            if balt[i+1] == 0:
                cnt += 1

    #3. 로봇을 올릴 수 있으면 올림
    if balt[0] > 0 and robot[0] == False:
        robot[0] = True
        balt[0] -= 1

        # 0이 되는 개수 
        if balt[0] == 0:
            cnt += 1

    # 0인 내구도 개수 >= k 종료
    if cnt >= K:
        print(ans)
        break